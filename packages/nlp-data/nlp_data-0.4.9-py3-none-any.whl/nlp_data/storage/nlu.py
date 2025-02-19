from typing import Iterator
from ..document import NLUDocList, NLUDoc,MultiIntentionDoc,MultiIntentionDocList
from .base import BaseDocStore
from ..utils import check_pydantic_version
from docarray import DocList
import random


class NLUDocStore(BaseDocStore):
    
    bucket_name = 'nlu'
    
    @classmethod
    def pull(cls, name: str, show_progress: bool = True) -> NLUDocList:
        name = name.strip()
        docs = DocList[NLUDoc].pull(url=f's3://{cls.bucket_name}/{name}', show_progress=show_progress)
        return NLUDocList(docs)
    
    # @check_pydantic_version()    # 下除pydantic版本校验问题，即使版本装对了也无法进行校验；应对方法：readme/requirements统一pydantic版本
    @classmethod
    def push(cls, docs: NLUDocList, name: str, show_progress: bool = True, shuffle: bool = True) -> None:
        name = name.strip()
        if shuffle:
            random.shuffle(docs)
        _ = DocList[NLUDoc].push_stream(docs, url=f's3://{cls.bucket_name}/{name}', show_progress=show_progress)
        return

    @classmethod
    def pull_stream(cls, name: str, show_progress: bool = True) -> Iterator[NLUDoc]:
        name = name.strip()
        for doc in DocList[NLUDoc].pull_stream(url=f's3://{cls.bucket_name}/{name}', show_progress=show_progress):
            yield doc
    
            
class NLUDocStoreZH(NLUDocStore):
    
    bucket_name = 'nlu'
    
    
class NLUDocStoreEN(NLUDocStore):
    
    bucket_name = 'nlu-en'


class MultiIntentionDocStore(BaseDocStore):
    
    bucket_name = 'multi-intention-zh'
 
    @classmethod
    def pull(cls, name: str, show_progress: bool = True) -> MultiIntentionDocList:
        name = name.strip()
        # 创建MultiIntentionDoc实例的容器,用来存储拉取的docs
        docs = DocList[MultiIntentionDoc].pull(url=f's3://{cls.bucket_name}/{name}', show_progress=show_progress)
        return MultiIntentionDocList(docs) # 返回出来
    
    @classmethod
    @check_pydantic_version()
    def push(cls, docs: MultiIntentionDocList, name: str, show_progress: bool = True, shuffle: bool = True) -> None:
        name = name.strip()
        if shuffle:
            random.shuffle(docs)
            # 实例化一个MultiIntentionDoc容器用来接收待上传的MultiIntentionDocList
        _ = DocList[MultiIntentionDoc].push_stream(docs, url=f's3://{cls.bucket_name}/{name}', show_progress=show_progress)
        return

    @classmethod
    def pull_stream(cls, name: str, show_progress: bool = True) -> Iterator[MultiIntentionDoc]:
        name = name.strip()
        for doc in DocList[MultiIntentionDoc].pull_stream(url=f's3://{cls.bucket_name}/{name}', show_progress=show_progress):
            yield doc
    
class MultiIntentionDocStoreEN(MultiIntentionDocStore):
    
    bucket_name = 'multi-intention-en'
