from docarray import BaseDoc, DocList
from docarray.typing import ID
from typing import List, Dict, Any, Optional, Union, Literal, Tuple
from pathlib import Path
from pydantic import validator, constr, conint, validate_arguments, confloat
from tqdm import tqdm
from copy import deepcopy
from docarray.utils.filter import filter_docs
from random import randint, choices
from lightning_utilities.core.imports import RequirementCache
import re
import os
import cantofilter
from collections import Counter
from typing import List

import requests
import json
import pandas as pd


datsets_requirement = bool(RequirementCache('datasets'))
pandas_requirement = bool(RequirementCache('pandas'))

Label = constr(strip_whitespace=True, min_length=1)
Index = conint(ge=0, strict=True)
Score = confloat(ge=0, le=1, strict=True)

def get_ents(tags: List[str]) -> List[Tuple[int, int, str]]:
    """从序列标签中提取实体

    Args:
        tags (List[str]): 序列标签.

    Returns:
        List[Tuple[int, int, str]]: 实体列表.例如, [(2, 6, 'PER')]
    """
    entities = []
    entity = []
    for i, tag in enumerate(tags):
        if tag.startswith('B-'):
            if entity:
                entities.append(tuple(entity))
            label = tag.split('-')[1:]
            if isinstance(label, list):
                label = '-'.join(tag.split('-')[1:])
            entity = [i, i + 1, label]
        elif tag.startswith('I-'):
            if entity:
                label = tag.split('-')[1:]
                if isinstance(label, list):
                    label = '-'.join(tag.split('-')[1:])
                if entity[2] == label:
                    entity[1] = i + 1
        else:
            if entity:
                entities.append(tuple(entity))
            entity = []
    if len(entity) == 3:
        entities.append(tuple(entity))
    return entities


def assert_span_text_in_doc(doc_text: str, span_text: str, span_indices: List[Index]) -> None:
    """检查span的文本与标注的下标对应doc文本一致

    Args:
        doc_text (str): doc文本
        span_text (str): span文本
        span_indices (List[Index]): 在文档中的下标
    """
    try:
        text = ''.join([doc_text[i] for i in span_indices])
    except Exception as e:
        print(span_indices)
        print(len(span_indices))
        raise e
    # 如果实体文本存在则确保实体文本与下标对应文本一致,确保标注正确
    assert text == span_text, f'文本: <{span_text}> 与下标文本: <{text}> 不一致'

class Intention(BaseDoc):
    id: ID = None
    text: Label
    score: Optional[Score] = None
    semantic_intention: str = None
    orgi_intention: Optional[Label] = None
    
class Domain(BaseDoc):
    id: ID = None
    text: Label
    score: Optional[Score] = None
    semantic_domain: Optional[str] = None

class Slot(BaseDoc):
    value: str                    # 模型服务后处理的槽值结果
    rawValue: str                 # 模型服务的原始结果（模型直接结果）
    semantic_slot: Optional[str] = None     # 对应槽位的解释（注：语义资源平台没有对槽位做名称解释，此处填写只用来做名称标识）
    class Config:
        allow_population_from_keys = True  # 允许直接从字典创建对象

class Entity(BaseDoc):
    id: ID = None
    label: Label                                       # 槽位标签
    text: Optional[str] = None  # 语义资源级别的槽值 （0.4.9版本槽位数据开始使用新格式，此格式保留向下兼容其它版本）
    rawvalue_text: str          # 模型rawValue槽值
    semantic_text: Optional[str] = None                # 语义资源的槽值
    indices: Optional[List[Index]] = None              # 0.4.4开始将把槽位索引的硬性检测逻辑下除，方便填写
    score: Optional[Score] = None
    slot: Optional[Slot] = None

    
    def is_contiguous(self):
        """判断实体是否连续

        Returns:
            bool: 是否连续
        """
        return self.indices == list(range(self.indices[0], self.indices[-1] + 1))
    
    @validator('text')
    def validate_text(cls, v: str, values: dict):
        if v is not None:
            values['ori_text'] = v # 记录原始文本,以此修改下边列表
            return v.strip().replace('\n', '') # 左右没有空格并且有效字符不为0则返回原文
        else:
            return v
    
    @validator('indices')
    def validate_indices(cls, v: List[Index], values):
        v = sorted(v)
        if 'text' in values:
            if values['text']:
                assert len(values['ori_text']) == len(v), f'下标: <{v}>与原始文本: <{values["ori_text"]}>长度不符'
                start = values['ori_text'].index(values['text'])
                indices = v[start: start+len(values['text'])]
                del values['ori_text']
                return indices
            else:
                return v
        else:
            return v

    @validator('slot', pre=True, always=True)
    def validate_slot(cls, v):
        if isinstance(v, dict):
            return Slot(**v)
        return v
    
class Hicar(BaseDoc):
    use_hicar: bool = False
    app: Optional[Entity] = None
        

class NLUDoc(BaseDoc):
    text: str
    language: Optional[str] = None
    domain: Optional[Domain] = None
    intention: Optional[Intention] = None
    slots: DocList[Entity] = DocList[Entity]()
    abnf_output: Optional[str] = None
    screen: Optional[Literal["driver", "passenger"]] = None
    hicar: Optional[Hicar] = None
    prior_ents: DocList[Entity] = DocList[Entity]()
    tags: Dict[str, str] = {}
    
    @validator('text')
    def validate_text(cls, v: str, values: dict):
        return v.strip().replace('\n', '')
    
    @validator('hicar', always=True)
    def validate_hicar(cls, v: Optional[Hicar], values: dict):
        if v:
            if v.app:
                assert_span_text_in_doc(doc_text=values['text'], span_text=v.app.text, span_indices=v.app.indices)
            return v
        else:
            # 如果 text中包含在`手机上`, `手机上`, `用手机`等关键词,则默认为使用hicar
            if re.search(r'手机上|手机上|用手机|使用hicar|用hicar', values['text']):
                hicar = Hicar(use_hicar=True)
                return hicar
            else:
                return v
            
    @validator('screen', always=True)
    def validate_screen(cls, v: Optional[Literal["driver", "passenger"]], values: dict):
        if v is None:
            driver_res =  re.search(r'主驾屏|主驾驶屏幕|主驾驶屏|主驾屏幕|主驾', values['text'])
            passenger_res =  re.search(r'副驾屏|副驾驶屏幕|副驾视屏|副驾屏幕|副驾', values['text'])
            if driver_res and not passenger_res:
                return 'driver'
            elif passenger_res and not driver_res:
                return 'passenger'
            else:
                return v
        else:
            return v
            
    
    @validate_arguments
    def set_slot(self,
                 label: Label,
                 rawvalue_text: str,
                 semantic_text: str,
                 indices: Optional[List[Index]] = None, 
                 score: Optional[Score] = None,
                 # 旧的参数，保留是为了适配其他版本的nlp-data
                 text: Optional[str] = None,
                 ):
        
        # 开放检查字符串必须存在文本的限制；开放必须填入索引的问题（当模型rawvalue槽值不存在文本时）
        if rawvalue_text not in self.text:
            indices = None
            slot = Entity(label=label,
                          score=score,
                          rawvalue_text=rawvalue_text,
                          semantic_text=semantic_text,
                          text=text           # 向下兼容，此处是语义资源级别的槽值
                          )
            if self.slots is None:
                self.slots = DocList[Entity]()
            if slot not in self.slots:
                self.slots.append(slot)
        else:
            # 当槽值存在文本内，自动寻找索引
            _tmp_value = ""
            if rawvalue_text:
                _tmp_value = rawvalue_text
            
            if not indices:
                start = self.text.index(_tmp_value)
                end = start + len(_tmp_value)
                indices = list(range(start, end))
            slot = Entity(indices=indices, 
                          label=label,
                          score=score,
                          rawvalue_text=rawvalue_text,
                          semantic_text=semantic_text
                          )
            if self.slots is None:
                self.slots = DocList[Entity]()
            if slot not in self.slots:
                assert_span_text_in_doc(doc_text=self.text, span_text=_tmp_value, span_indices=indices)
                self.slots.append(slot)
            
    @validate_arguments
    def set_prior_ent(self, text: constr(strip_whitespace=True, min_length=1), label: Label, indices: Optional[List[Index]] = None, score: Optional[Score] = None):
        if not indices:
            start = self.text.index(text)
            end = start + len(text)
            indices = list(range(start, end))
        slot = Entity(text=text, indices=indices, label=label, score=score)
        if not hasattr(self, 'prior_ents'):
            self.prior_ents = DocList[Entity]()
        if slot not in self.prior_ents:
            assert_span_text_in_doc(doc_text=self.text, span_text=text, span_indices=indices)
            self.prior_ents.append(slot)
    
    @validate_arguments
    def set_domain(self, text: constr(strip_whitespace=True, min_length=1), semantic_domain: Optional[str] = None, score: Optional[Score] = None):
        self.domain = Domain(text=text, score=score, semantic_domain=semantic_domain)
    
    @validate_arguments
    def set_intention(self, text: constr(strip_whitespace=True, min_length=1), semantic_intention: Optional[str] = None, orig_intention: Optional[str] = None, score: Optional[Score] = None):
        self.intention = Intention(text=text, score=score, semantic_domain=semantic_intention, orig_intention=orig_intention)
        self.intention.semantic_intention = semantic_intention
        self.intention.orgi_intention = orig_intention
        
    @validate_arguments
    def set_screen(self, screen: Literal["driver", "passenger"]):
        self.screen = screen
        
    @validate_arguments
    def set_hicar(self, app: Optional[str] = None, indices: Optional[List[Index]] = None) -> None:
        if app:
            if not indices:
                start = self.text.index(app)
                end = start + len(app)
                indices = list(range(start, end))
            app_entity = Entity(text=app, indices=indices, label='app')
        else:
            app_entity = None
        hicar = Hicar(app=app_entity, use_hicar=True)
        self.hicar = hicar
    
    @classmethod
    def from_abnf_output_line(cls, 
                              line: constr(strip_whitespace=True, min_length=1), 
                              domain: Label, 
                              intention: Label,
                              lang: Literal['zh', 'en'] = 'zh') -> "NLUDoc":
        """根据abnf数据的一行数据初始化NLUDoc

        Args:
            domain (Label): 领域
            intention (Label): 意图
            line (constr, optional): . Defaults to True, min_length=1).

        Returns:
            NLUDoc: nlu文档.
        """
        # text = ''
        text = []
        spans = line.strip().split(' ')
        ents = []
        ent_spans = []
        for idx, span in enumerate(spans):
            if span.startswith('B-'):
                label = span[2:]
                for _span in spans[idx+1:]:
                    if _span.startswith('I-') and _span[2:] == label:
                        if ent_spans:
                            if lang == 'zh':
                                ent = ''.join(ent_spans)
                            if lang == 'en':
                                ent = ' '.join(ent_spans)
                            ents.append((label, ent))
                    if not _span.startswith('I-') and not _span.startswith('B-'):
                        ent_spans.append(_span)
            if not span.startswith('I-') and not span.startswith('B-'):
                text.append(span)
        if lang == 'zh':
            text = ''.join(text)
        if lang == 'en':
            text = ' '.join(text)
        doc = NLUDoc(text=text, domain=Domain(text=domain), intention=Intention(text=intention))
        for ent in ents:
            label = ent[0]
            ent_text = ent[1]
            doc.set_slot(text=ent_text, label=label)
        doc.abnf_output = line.strip()
        return doc
    
    def __hash__(self) -> int:
        return hash(self.text)
    
    def __eq__(self, __value: object) -> bool:
        return self.text == __value.text
    
    def __hasattr__(self, name: str):
        return name in self.__dict__
    
    def __getattr__(self, item: str):
        if item in self._docarray_fields().keys():
            if item in  self.__dict__:
                return self.__dict__[item]
            else:
                if item == 'prior_ents':
                    self.__dict__['prior_ents'] =  DocList[Entity]()
                    return self.__dict__[item]
        else:
            return super().__getattribute__(item)
        
        
class NLUExample(BaseDoc):
    """存放NLU文档对, 主要用于存放NLU文档对的评估结果
    """
    id: ID = None
    x: NLUDoc
    y: NLUDoc
    
    @validator('x')
    def validate_x(cls, value: NLUDoc, values: dict):
        """确保x与y的文本一致
        """
        y = values.get('y', None)
        if y:
            assert value.text == y.text, f'x文本: <{value.text}>与y文本: <{y.text}>不一致'
        return value
    
    @validator('y')
    def validate_y(cls, value: NLUDoc, values: dict):
        """确保x与y的文本一致
        """
        x = values.get('x', None)
        if x:
            assert value.text == x.text, f'y文本: <{value.text}>与x文本: <{x.text}>不一致'
        return value
    
    @property
    def is_intention_badcase(self):
        """判断x与y的意图是否不一致
        """
        if not self.y.intention:
            return False
        elif not self.x.intention:
            return True
        else:
            return self.x.intention.text != self.y.intention.text
    
    @property   
    def is_domain_badcase(self):
        """判断x与y的领域是否不一致
        """
        if not self.y.domain:
            return False
        elif not self.x.domain:
            return True
        else:
            return self.x.domain.text != self.y.domain.text
    
    @property 
    def is_slot_badcase(self):
        """判断x与y的槽位是否不一致
        """
        # 数量不等
        if len(self.y.slots) != len(self.x.slots):
            return True
        # slot的文本或者label不一致
        y_texts = [slot.text for slot in self.y.slots]
        x_texts = [slot.text for slot in self.x.slots]
        if sorted(y_texts) != sorted(x_texts):
            return True
        x_labels = [slot.label for slot in self.x.slots]
        y_labels = [slot.label for slot in self.y.slots]
        if sorted(x_labels) != sorted(y_labels):
            return True
        return False
    
    @property
    def is_badcase(self):
        """判断x与y是否不一致
        """
        return self.is_intention_badcase or self.is_domain_badcase or self.is_slot_badcase
    
        
        
class NLUDocList(DocList[NLUDoc]):
    
    @property
    def ent_labels(self):
        """获取所有实体标签
        """
        return list(set(self.traverse_flat('slots__label')))
    
    @classmethod
    def from_file(cls, file_path: Union[str, Path], domain: str) -> 'NLUDocList':
        """从文件中一行一行读取文本,并转换为NLUDocList

        Args:
            file_path (Union[str, Path]): 文件路径.
            
            domain (str): 领域名称.

        Returns:
            NLUDocList: NLU文档列表
        """
        file_path = Path(file_path)
        assert file_path.is_file(), f'文件: <{file_path}>不存在'
        docs = NLUDocList()
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in tqdm(lines):
                doc = NLUDoc(text=line)
                doc.set_domain(text=domain)
                docs.append(doc)
        return docs
    
    @classmethod
    def from_ner_dataset(cls, dataset_dir: Union[str, Path]) -> 'NLUDocList':
        """将NLUDocList.convert_slots_to_ner_dataset保存的数据集转换为NLUDocList

        Args:
            dataset_dir (Union[str, Path]): 数据集目录

        Raises:
            ImportError: datasets未安装

        Returns:
            NLUDocList: NLU文档列表
        """
        if not datsets_requirement:
            raise ImportError('datasets not installed, please install datasets first, pip install datasets')
        else:
            from datasets import load_from_disk, DatasetDict, Dataset
        
        def convert_to_nlu_doc(example: Dict[str, Any]) -> NLUDoc:
            text = example['text']
            doc = NLUDoc(text=text)
            for ent in example['ents']:
                doc.set_slot(text=ent['text'], label=ent['label'], indices=ent['indices'])
            return doc
        
        ds = load_from_disk(dataset_dir)
        if isinstance(ds, DatasetDict):
            docs = NLUDocList()
            for split in ['train', 'validation']:
                if split in ds:
                    for example in tqdm(ds[split]):
                        doc = convert_to_nlu_doc(example)
                        docs.append(doc)
                else:
                    print(f'{split}数据集不存在')
        if isinstance(ds, Dataset):
            docs = NLUDocList([convert_to_nlu_doc(example) for example in tqdm(ds)])
        return docs
                
    
    @classmethod
    def from_v1_ner_dataset(cls, file_path: Union[str, Path], end_char: str = '。', split_char: str = '\t') -> 'NLUDocList':
        """将旧版本的NER数据集转换为NLUDocList,需要文件如下格式:
        麻	O
        烦	O
        向	B-VERB
        大	I-VERB
        调	I-VERB
        提	B-ENTITY
        示	I-ENTITY
        的	I-ENTITY
        聲	I-ENTITY
        音	I-ENTITY
        。	O
        其中一行为一个token,并且以空格分割,最后一个为标签
        
        Args:
            file_path (Union[str, Path]): txt文件路径.
            end_char (str, optional): 一个doc文本的区分结束字符. Defaults to '。'.
            split_char (str, optional): 一行中token跟标签的差分字符. Defaults to '\t'.
        """
        def post_process(data: Tuple[List[str], List[str]]) -> NLUDoc:
            tokens, tags = data
            text = ''.join(tokens)
            doc = NLUDoc(text=text)
            ents = get_ents(tags=tags)
            for ent_start, ent_end, ent_label in ents:
                ent_text = text[ent_start:ent_end]
                doc.set_slot(text=ent_text, label=ent_label, indices=list(range(ent_start, ent_end)))
            return doc
        
        with open(file_path, 'r') as f:
            lines = f.readlines()
            lines = [line.strip('\n').split(split_char) for line in lines]
            
        end_token = end_char
        all_data = []
        tokens = []
        tags = []
        for line in tqdm(lines, desc='处理数据'):
            if len(line) == 2:
                token, tag = line
                if token == end_token:
                    all_data.append((tokens, tags))
                    tags = []
                    tokens = []
                else:
                    tokens.append(token)
                    tags.append(tag)

        docs = NLUDocList()
        for data in tqdm(all_data, desc='转换数据'):
            doc = post_process(data)
            docs.append(doc)
        return docs
    
    @classmethod
    def from_v1_ner_dataset_eng(cls, file_path: Union[str, Path], end_char: str = '.', split_char: str = '\t') -> 'NLUDocList':
        """将旧版本的英文NER数据集转换为NLUDocList,需要文件如下格式: 
        Args:
            file_path (Union[str, Path]): txt文件路径.
            end_char (str, optional): 一个doc文本的区分结束字符. Defaults to '.'.
            split_char (str, optional): 一行中token跟标签的差分字符. Defaults to '\t'.
        """
        
        def post_process_eng(data: Tuple[List[str], List[str]]) -> NLUDoc:
            tokens, tags = data
            text = ' '.join(tokens)
            doc = NLUDoc(text=text)
            ents = get_ents(tags=tags)
            for ent_start, ent_end, ent_label in ents:
                ent_text = ' '.join(tokens[ent_start:ent_end])
                doc.set_slot(text=ent_text, label=ent_label)
            return doc
        
        with open(file_path, 'r') as f:
            lines = f.readlines()
            lines = [line.strip('\n').split(split_char) for line in lines]
            
        end_token = end_char
        all_data = []
        tokens = []
        tags = []
        for line in tqdm(lines, desc='处理数据'):
            if len(line) == 2:
                token, tag = line
                if token == end_token:
                    all_data.append((tokens, tags))
                    tags = []
                    tokens = []
                else:
                    tokens.append(token)
                    tags.append(tag)

        docs = NLUDocList()
        for data in tqdm(all_data, desc='转换数据'):
            doc = post_process_eng(data)
            docs.append(doc)
        return docs
    
    @classmethod
    def from_abnf_output(cls, 
                         abnf_output_dir: str, 
                         domain: str,
                         add_space: bool = False) -> 'NLUDocList':
        """将abnf输出转换为NLU文档,并存放在NLUDocList中

        Args:
            abnf_output_dir (str): abnf输出目录
            domain (str): 领域名称

        Returns:
            NLUDocList: NLU文档列表

        """
        return convert_abnf_to_nlu_docs(output_dir=abnf_output_dir, domain=domain, add_space=add_space)
    
    @classmethod
    def from_abnf_output_24mm(cls,
                              domain: str,
                              intention_dict: dict,
                              language: Literal['zho', 'eng'] = "zho",
                              semantic_domain: str = "",
                              source: str = ""
                              ) -> 'NLUDocList':
        """将abnf输出转换为NLU文档,并存放在NLUDocList中
        Args:
            abnf_output_dir (str): abnf输出目录
            domain (str): 领域名称
        Returns:
            NLUDocList: NLU文档列表
        """
        
        doclist = NLUDocList()
    
        # 遍历意图字典，找到对应的文件
        for intent_id, intent_info in intention_dict.items():
            file_list = intent_info["file"]
            
            for filename in file_list:

                # 读取文件内容
                file_path = filename
                text_lines = read_txt(file_path)
                
                # 逐行处理成规范格式
                for line in text_lines:
                    # 判断中英文
                    if not language:
                        language = detect_language(line)
                    
                    # 复用工具类时的后处理
                    if language == "zho":
                        lang = "zh"
                    elif language == "eng":
                        lang = "en"
                    else:
                        lang = "zh"
                    
                    doc = NLUDoc.from_abnf_output_line(line=line, 
                                                        domain=domain, 
                                                        intention=intent_info["label"],
                                                        lang=lang
                                                        )
                    # 更改intention信息
                    doc.intention.id = intent_id
                    # 槽位信息已在abnf_output_line处理，跳过
                    _slot = {}
                    # 更改tag信息
                    tags = {
                        # 语义资源信息
                        "semantic_domain": semantic_domain,
                        "semantic_intention": intent_info["text"],
                        "source": source,
                        "desc": tags_desc_analyzer(text=line),
                        "intention": intent_info["label"]
                    }
                    doc.tags = tags
                    # 更改language信息
                    doc.language = language
                    
                    # slots = [
                    # Entity(text="早上好", indices=[0,1,2], label="name"),
                    # Entity(text="我不好", indices=[3,4,5], label="position")
                    # ] 
                    
                    # doc.slots = slots
                    
                    # 存入列表
                    doclist.append(doc)
        return doclist
                
    @classmethod
    def statistics_tags_docs(cls,
                        docs_list: DocList
                        ) -> None:
        # todo: 该功能目前仅是简单打印，待完善结构化输出
        # 统计domain数量和占比
        domain_counter = Counter([doc.domain.text for doc in docs_list if doc.domain])
        total_domains = len(domain_counter)
        domain_stats = {domain: {'count': count, 'ratio': count / len(docs_list)} for domain, count in domain_counter.items()}

        # 统计intention数量和占比
        intention_counter = Counter([doc.intention.text for doc in docs_list if doc.intention])
        total_intentions = len(intention_counter)
        intention_stats = {intention: {'count': count, 'ratio': count / len(docs_list)} for intention, count in intention_counter.items()}

        # 统计tags中的source和desc数量和占比
        source_counter = Counter([doc.tags.get("source", "") for doc in docs_list if "tags" in doc.__dict__ and "source" in doc.tags])
        desc_counter = Counter([doc.tags.get("desc", "") for doc in docs_list if "tags" in doc.__dict__ and "desc" in doc.tags])

        total_sources = len(source_counter)
        source_stats = {source: {'count': count, 'ratio': count / len(docs_list)} for source, count in source_counter.items()}
        total_descs = len(desc_counter)
        desc_stats = {desc: {'count': count, 'ratio': count / len(docs_list)} for desc, count in desc_counter.items()}

        # 统计slots数据结构中的槽位个数，槽位频率，槽位种类
        slot_labels = [slot.label for doc in docs_list for slot in doc.slots]
        slot_counter = Counter(slot_labels)
        total_slots = sum(slot_counter.values())
        slot_stats = {label: {'count': count, 'frequency': count / total_slots} for label, count in slot_counter.items()}

        # 打印统计结果
        print(f"Domain数据量统计（共{total_domains}个）")
        for domain, stats in domain_stats.items():
            print(f"{domain}:\t{stats['count']} 条\t数据占比 {stats['ratio']:.2%}")
        
        print(f"\nIntention数据量统计（共{total_intentions}个）")
        for intention, stats in intention_stats.items():
            print(f"{intention}:\t{stats['count']} 条\t数据占比 {stats['ratio']:.2%}")
        
        print(f"\n数据来源Source（共{total_sources}种）")
        for source, stats in source_stats.items():
            print(f"{source}:\t{stats['count']} 条\t数据占比 {stats['ratio']:.2%}")
        
        print(f"\n数据类型Desc统计")
        for desc, stats in desc_stats.items():
            print(f"{desc}:\t{stats['count']} 条\t数据占比 {stats['ratio']:.2%}")
        
        print(f"\n实体槽位Slot统计（共{total_slots}/{total_domains}条数据出现槽位）")
        for slot, stats in slot_stats.items():
            print(f"{slot}:\t{stats['count']} 个实体\t实体频率占比 {stats['frequency']:.2%}")

        return None
    
    @classmethod
    def statistics_docs(cls,
                        docs_list: DocList
                        ) -> None:
        
        # 1. 数据集基本信息
        total_docs = len(docs_list)
        print("数据集基本信息:")
        print(f"  - 数据集总数量: {total_docs}")
        
        # 2. 数据集domain信息
        domain_counts = Counter(doc.domain.text for doc in docs_list if doc.domain)
        try:
            domain_semantic_mapping = {doc.domain.text: doc.domain.semantic_domain for doc in docs_list if doc.domain and doc.domain.semantic_domain}
        except:
            domain_semantic_mapping = {doc.domain.text: doc.domain.text for doc in docs_list if doc.domain and doc.domain.text}
        print("Domain信息:")
        print(f"  - Domain种类个数: {len(domain_counts)}")
        for domain, count in domain_counts.items():
            semantic_domain = domain_semantic_mapping.get(domain, "未知")
            print(f"    - {domain} ({semantic_domain}): {count} ({count / total_docs * 100:.2f}%)")
        
        # 3. 数据集intention信息
        intention_counts = Counter(doc.intention.text for doc in docs_list if doc.intention)
        total_intentions = sum(intention_counts.values())
        try:
            intention_semantic_mapping = {doc.intention.text: doc.intention.semantic_intention for doc in docs_list if doc.intention and doc.intention.semantic_intention}
        except:
            intention_semantic_mapping = {doc.intention.text: doc.intention.text for doc in docs_list if doc.intention and doc.intention.text}
        print("Intention信息:")
        print(f"  - intention种类个数: {len(intention_counts)}")
        for intention, count in intention_counts.items():
            semantic_intention = intention_semantic_mapping.get(intention, "未知")
            print(f"    - {intention} ({semantic_intention}): {count} ({count / total_intentions * 100:.2f}%)")
        
        # 4. 数据集slots信息
        docs_with_slots = sum(1 for doc in docs_list if doc.slots)
        slot_counts = Counter(slot.label for doc in docs_list for slot in doc.slots if doc.slots)
        total_slots = sum(slot_counts.values())
        print("Slots信息:")
        print(f"  - slots种类个数: {len(slot_counts)}")
        for slot, count in slot_counts.items():
            print(f"    - {slot}: {count} ({count / total_slots * 100:.2f}%)")
        print(f"  - 语料中存在slots槽位的文本数量: {docs_with_slots} ({docs_with_slots / total_docs * 100:.2f}%)")
        
        return None
        
    
    def convert_intention_to_text_classification_dataset(self, 
                                                         save_path: Optional[str] = None,
                                                         train_ratio: float = 0.8,   
                                                         split_test: Optional[bool] = False,
                                                         add_labels: Optional[bool] = True):
        """将NLUDocList转换为文本分类数据集

        Args:
            train_ratio (float, optional): 训练集划分比率. Defaults to 0.8.
            save_path (Optional[str], optional): 数据集保存路径. Defaults to None.
            split_test (Optional[bool], optional): 是否划分测试集. Defaults to False.
            add_labels (Optional[bool], optional): 是否添加多标签列表. Defaults to True.

        Returns:
            Optional[DatasetDict]: 转换后的数据集, 如果save_path为None则返回划分后的数据集.
        """
        if not datsets_requirement:
            raise ImportError('datasets not installed, please install datasets first, pip install datasets')
        else:
            from datasets import Dataset, DatasetDict
        if not pandas_requirement:
            raise ImportError('pandas not installed, please install pandas first, pip install pandas')
        else:
            import pandas as pd
        data = {'text': self.text, 'label': self.traverse_flat('intention__text')}
        df = pd.DataFrame(data)
        train_df = df.groupby('label').sample(frac=train_ratio)
        if not split_test:
            val_df = df.drop(train_df.index)
            ds = DatasetDict({'train': Dataset.from_pandas(train_df, preserve_index=False), 'validation': Dataset.from_pandas(val_df, preserve_index=False)})
        else:
            val_ratio = (1 - train_ratio) / 2
            val_df = df.drop(train_df.index).groupby('label').sample(frac=val_ratio)
            test_df = df.drop(train_df.index).drop(val_df.index)
            ds = DatasetDict({'train': Dataset.from_pandas(train_df, preserve_index=False), 'validation': Dataset.from_pandas(val_df, preserve_index=False), 'test': Dataset.from_pandas(test_df, preserve_index=False)})
        if add_labels:
            ds = ds.map(lambda example: {'labels': [example['label']]})
        if save_path:
            ds.save_to_disk(save_path)
        else:
            return ds
        
    
    
    def convert_slots_to_ner_dataset(self, 
                                     save_path: Optional[str] = None,
                                     train_ratio: float = 0.8,  
                                     split_test: Optional[bool] = False):
        """将NLUDocList转换为NER数据集

        Args:
            train_ratio (float, optional): 训练集划分比率. Defaults to 0.8.
            save_path (Optional[str], optional): 数据集保存路径. Defaults to None.
            split_test (Optional[bool], optional): 是否划分测试集. Defaults to False.

        Returns:
            Optional[DatasetDict]: 转换后的数据集, 如果save_path为None则返回划分后的数据集.
        """
        if not datsets_requirement:
            raise ImportError('datasets not installed, please install datasets first, pip install datasets')
        else:
            from datasets import Dataset, DatasetDict
        if not pandas_requirement:
            raise ImportError('pandas not installed, please install pandas first, pip install pandas')
        else:
            import pandas as pd
        data = {'text': self.text, 
                'ents': [[ent.dict(exclude={"id"}) for ent in ent_ls] for ent_ls in self.slots],
                'prior_ents': [[ent.dict(exclude={"id"}) for ent in ent_ls] for ent_ls in self.prior_ents]}
        df = pd.DataFrame(data)
        train_df = df.sample(frac=train_ratio)
        if not split_test:
            val_df = df.drop(train_df.index)
            ds = DatasetDict({'train': Dataset.from_pandas(train_df, preserve_index=False), 'validation': Dataset.from_pandas(val_df, preserve_index=False)})
        else:
            val_ratio = (1 - train_ratio) / 2
            val_df = df.drop(train_df.index).sample(frac=val_ratio)
            test_df = df.drop(train_df.index).drop(val_df.index)
            ds = DatasetDict({'train': Dataset.from_pandas(train_df, preserve_index=False), 'validation': Dataset.from_pandas(val_df, preserve_index=False), 'test': Dataset.from_pandas(test_df, preserve_index=False)})
        if save_path:
            ds.save_to_disk(save_path)
        else:
            return ds
        
    def convert_intention_to_fasttext_dataset(self, save_path: str = 'train.txt', split_type: Literal['char', 'no_split'] = 'char'):
        """转换为fasttext的数据格式txt文件,文本将按照字符进行切分

        Args:
            save_path (str): 保存目录
        """
        with open(save_path, 'w') as f:
            for doc in self:
                if doc.intention:
                    if split_type == 'char':
                        f.write(f"__label__{doc.intention.text} {' '.join(list(doc.text))}" + "\n")
                    else:
                        f.write(f"__label__{doc.intention.text} {doc.text}" + "\n")
        
    def convert_to_llm_nlu_dataset(self, valid_ratio: float = 0.2, save_path: Optional[str] = None):
        """将NLUDocList转换为LLM的NLU数据集,用于训练基于LLM做NLU结果生成的模型.
        
        - 模板示例: 你需要为用户的输入做如下的任务: 1.选择一种领域类型.以下是所有领域类型:{"domain1", "domain2", "domain3"}. 2.选择一种意图类型,以下是所有意图类型:{"intention1", "intention2", "intention3"} 3. 抽取所有实体以及其对应的标签,以下是所有实体类型:{"entity1", "entity2", "entity3"}
        """
        if not datsets_requirement:
            raise ImportError('datasets not installed, please install datasets first, pip install datasets')
        else:
            from datasets import Dataset
        entity = set([ent.label for doc in self for ent in doc.slots])
        domain = set([doc.domain.text for doc in self if doc.domain])
        intention = set([doc.intention.text for doc in self if doc.intention])
        
        ## 获得一个真实模板
        for example in self:
            if len(example.slots) > 0:
                example_input = example.text
                example_response = {"domain":f"{example.domain.text}","intention":f"{example.intention.text}", "entity":[]}
                for ent in example.slots:
                    example_response['entity'].append({'text':ent.text, 'label':ent.label})
        
        ## 构建指令
        base_instruction = f'你需要为用户的输入做如下的任务: 1.选择一种领域类型.以下是所有领域类型:{domain}. 2.选择一种意图类型,以下是所有意图类型:{intention} 3. 抽取所有实体以及对应类型, 以下是所有实体类型{entity}.并将结果以字典格式返回.例如:用户输入:{example_input}.输出:{example_response}'
        data = {"instruction": [], "input": [], "response": []}
        for i in range(len(self)):
            data['instruction'].append(base_instruction)
            data['input'].append(self[i].text)
            response = {"domain":"","intention":"", "entity":[]}
            if self[i].domain:
                response['domain'] = self[i].domain.text
            if self[i].intention:
                response['intention'] = self[i].intention.text
            if len(self[i].slots) > 0:
                for slot in self[i].slots:
                    response['entity'].append({'text':slot.text, 'label':slot.label})
            data['response'].append(response)
        ds = Dataset.from_dict(data)
        dsd = ds.train_test_split(test_size=valid_ratio)
        dsd['validation'] = dsd.pop('test')
        if save_path:
            dsd.save_to_disk(save_path)
        else:
            return dsd
        
    def compute_acc(self):
        """根据NLUExample的is_badcase方法计算准确率
        """
        assert self.doc_type == NLUExample, "该方法只能用于NLUExample类型的DocList"
        return 1 - sum(self.traverse_flat('is_badcase')) / len(self)
    
    
    def up_sampling_by_intention(self):
        """根据意图类型数据上采样, 使得每个意图类型的数量一致
        """
        intention_ls = self.traverse_flat('intention__text')
        intention_count = {intention: intention_ls.count(intention) for intention in set(intention_ls)}
        max_count = max(intention_count.values())
        for intention in tqdm(intention_count):
            query = {'intention__text': {'$eq': intention}}
            intention_docs = filter_docs(self, query)
            if len(intention_docs) < max_count:
                for _ in range(max_count - len(intention_docs)):
                    idx = randint(0, len(intention_docs) - 1)
                    self.append(deepcopy(intention_docs[idx]))
        return self
    
    def sample_by_intention(self, n_sample: int) -> 'NLUDocList':
        """根据意图类型采样, 使得每个意图类型的数量一致
        """
        docs = NLUDocList()
        intention_labels = set(self.traverse_flat('intention__text'))
        samples_per_intention = n_sample // len(intention_labels)
        for intention in intention_labels:
            query = {'intention__text': {'$eq': intention}}
            intention_docs = filter_docs(self, query)
            sample_docs = choices(intention_docs, k=samples_per_intention)
            docs.extend(sample_docs)
        return docs
    
    def check_language(self) -> str:
        """检查文档的语言是否一致
        """
        lang = set(self.traverse_flat('language'))
        assert len(lang) == 1, f'文档的语言不一致: {lang}'
        return lang.pop()

    def set_language(self, lang: Literal['zh', 'en']):
        """设置文档的语言
        """
        for doc in self:
            doc.language = lang
    
    def filter_intention(self, intention: str) -> 'NLUDocList':
        """根据意图类型过滤文档
        """
        query = {'intention__text': {'$eq': intention}}
        return filter_docs(self, query)
    
    def filter_hicar(self, use_hicar: bool) -> 'NLUDocList':
        """根据是否使用hicar过滤文档
        """
        query = {'hicar__use_hicar': {'$eq': use_hicar}}
        return filter_docs(self, query)
    
    def filter_screen(self, screen: Literal['driver', 'passenger']) -> 'NLUDocList':
        """根据屏幕类型过滤文档
        """
        query = {'screen': {'$eq': screen}}
        return filter_docs(self, query)
    
    def filter_no_hicar_screen(self) -> 'NLUDocList':
        """过滤没有使用hicar的文档
        """
        query = {"$and": [{'$or': [{"hicar": {"$eq": None}}, {"hicar__use_hicar": {"$eq": False}}]}, {'screen': {'$eq': None}}]}
        return filter_docs(self, query)
    
class MultiIntentionDoc(BaseDoc):
    """多意图doc实例"""
    origin_input: str
    # expected_output: list[str]
    expected_output: List[str]


class MultiIntentionDocList(DocList[MultiIntentionDoc]):
    """多意图doc实例的容器列表及相关支撑方法"""

    def reqParser(self,text):
        url = "http://101.42.114.253:20000/rewrite"  # 多意图线上接口
        payload = json.dumps({"sessionId": "NLPer","text": text})
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        pred = response.json()['data']['texts']
        return pred
    
    def calculateEm(self,origin_inputs,expected_outputs,pred_list,res_file):
        """构建df,计算多意图预测em值，将结果写入指定路径"""
        res,percentage = pd.DataFrame(), ""
        res['输入'] = origin_inputs
        res['期望'] = expected_outputs
        res['输出'] = pred_list
        res['拆分是否正确'] = res.apply(lambda x: 'y' if x['期望'] == x['输出'] else 'f', axis=1)
        # print('多意图拆分em值')
        # print(res['拆分是否正确'].value_counts() / res.shape[0])
        res_tmp = res['拆分是否正确'].value_counts() / res.shape[0]
        for l,s in zip(res_tmp.index.tolist(),res_tmp.values):
            percentage += l+' '+str(round(s,3))+' '
        res = res[['输入', '期望', '输出', '拆分是否正确']]
        res.to_excel(res_file,index=False,sheet_name= percentage)
        print(f"多意图拆分结果已写入：{res_file}")
        return res

    @classmethod
    def predict(cls,docs,res_file):
        """调用多意图的接口测试，输出报告和精度"""
        pre = cls() 
        origin_inputs,expected_outputs,pred_list = [], [], []
        for doc in tqdm(docs):
            origin_inputs.append(doc.origin_input)
            expected_outputs.append(doc.expected_output)
            pred = pre.reqParser(doc.origin_input)
            pred_list.append(pred)
        res = pre.calculateEm(origin_inputs,expected_outputs,pred_list,res_file)
        return res
        
    
    @classmethod
    def mustcorrectTest(cls,domain_name,res_file):
        """从垂类bucket拉取必过集和回归集，输出多意图拆分结果"""
        from ..storage import NLUDocStore
        NLUDocStore.bucket_name = domain_name
        domain_file_list = NLUDocStore().list()
        # tests_file_list  后续垂类如果增加训练数据，这里可加文件名过滤，提取出测试数据,
        # 也可以根据文件名分别测试,作为不同sheet,合并在一个报告中
        origin_inputs,expected_outputs,pred_list = [], [], []
        mus = cls()
        for f in domain_file_list:
            if f.endswith("regression_set") or f.endswith('golden_set'):
                docs = NLUDocStore.pull(f)
                for doc in docs:
                    origin_inputs.append(doc.text)
                    expected_outputs.append([doc.text])
                    pred = mus.reqParser(doc.text)
                    pred_list.append(pred)
        res = mus.calculateEm(origin_inputs,expected_outputs,pred_list,res_file)
        return res
   
    def pullDomainData(self,bucket_name:str):
        """获取垂类数据中的必过和回归数据"""
        from ..storage import NLUDocStore
        NLUDocStore.bucket_name = bucket_name
        bucket_file_list = NLUDocStore.list()
        origin_inputs,expected_outputs = [],[]
        for f in bucket_file_list:
            if f.endswith("regression_set") or f.endswith('golden_set'):
                docs = NLUDocStore.pull(f)
                for doc in docs:
                    origin_inputs.append(doc.text)
                    expected_outputs.append([doc.text])
        return origin_inputs,expected_outputs
    
    def pullMUltiData(self):
        """获取多意图自有数据"""
        from ..storage import MultiIntentionDocStore
        bucket_file_list = MultiIntentionDocStore.list()
        origin_inputs,expected_outputs = [],[]
        for f in bucket_file_list:
            docs = MultiIntentionDocStore.pull(f)
            for doc in docs:
                origin_inputs.append(doc.origin_input)
                expected_outputs.append(doc.expected_output)
        return origin_inputs,expected_outputs

    @classmethod
    def genMultiDataset(cls,buckets:List[str]):
        """接收领域bucket列表,构建多意图所需数据(原始输入,期望输出列表)"""
        origin_inputs,expected_outputs = [],[]
        gen = cls()
        # 垂类必过/回归数据
        for bucket in buckets:
            origin_input,expected_output = gen.pullDomainData(bucket)
            origin_inputs += origin_input 
            expected_outputs += expected_output 
        # 多意图自有数据
        multi_input,multi_output = gen.pullMUltiData()
        origin_inputs += multi_input 
        expected_outputs += multi_output 

        return origin_inputs,expected_outputs





def convert_abnf_to_nlu_docs(output_dir: str, domain: str, error_pass: bool = True, add_space: bool = False) -> NLUDocList:
    """将abnf句式生成的数据转换NLUDoc并以DocList[NLUDoc]的形式返回
        
    注意:
    - 每个abnf输出文件的标题应该是对应的intention
    - 实体请以B-XXX, I-XXX的形式标注
    - 支持嵌套实体, 以B-XXX与之后遍历到的第一个I-XXX为实体

    参数:
    - output_dir (str): abnf输出文件夹
    - domain (str): 领域名称
    - error_pass (bool): 是否忽略错误, 默认为True
    - add_space (bool): 是否span之间添加空格, 主要用于英文, 默认为False.

    返回:
    - DocList: 转换后的NLUDocList
    """
    docs = NLUDocList()
    for f in Path(output_dir).iterdir():
        if f.is_file() and f.suffix == '.abnf_out':
            intention = f.stem
            with open(f, 'r') as f:
                lines = f.readlines()
                for line in tqdm(lines):
                    try:
                        if len(line.strip()) > 0:
                            text = ''
                            spans = line.strip().split(' ')
                            ents = []
                            for idx, span in enumerate(spans):
                                if span.startswith('B-'):
                                    label = span[2:]
                                    ent = ""
                                    for _span in spans[idx+1:]:
                                        if _span.startswith('I-') and _span[2:] == label:
                                            ents.append((label, ent.strip()))
                                        if not _span.startswith('I-') and not _span.startswith('B-'):
                                            ent += _span
                                            if add_space:
                                                ent += " "
                                                
                                if not span.startswith('I-') and not span.startswith('B-'):
                                    text += span
                                    if add_space:
                                        text += ' '
                            doc = NLUDoc(text=text, domain=Domain(text=domain), intention=Intention(text=intention))
                            for ent in ents:
                                label = ent[0]
                                ent_text = ent[1]
                                doc.set_slot(text=ent_text, label=label)
                            doc.abnf_output = line.strip()
                            docs.append(doc)   
                    except Exception as e:
                        print(f'转换错误: {e}')
                        pass
    return docs


def read_txt(file_path) -> List:
    with open(file_path, 'r', encoding='utf-8') as file:
        test_data = [line.strip() for line in file]
    return test_data


def tags_desc_analyzer(text: str) -> Dict:
    """ 标签处理器 """
    # todo: 更好的hicar、主副驾、声纹识别方式、识别四川话方言的方法
    
    # 判断是否为方言
    dialect_label = str(cantofilter.judge(text))
    if dialect_label == "cantonese" or dialect_label == "mixed":
        return "方言"
    
    # 判断desc为hicar
    available_hicar_list = ["在手机上", "在华为手机上"]
    for item in available_hicar_list:
        if item in text:
            return "hicar"
        
    # 判断desc为主副驾
    available_driver_list = ["主驾", "副驾", "主驾驶", "副驾驶"]
    for item in available_driver_list:
        if item in text:
            return "主副驾"
        
    # 判断是否为声纹
    pattern = r"给.*?打开|给.*?使用"
    # 使用re.search检查模式是否存在于句子中
    if re.search(pattern, text):
        return "声纹"

    return "核心句式"

def detect_language(sentence: str) -> Literal["zho", "eng"]:
    # 正则表达式匹配中文字符
    # fixme: 全角符号 可能判断有误
    chinese_pattern = re.compile(r'[\u4e00-\u9fff]+')
    if chinese_pattern.search(sentence):
        return "zho"
    else:
        return "eng"