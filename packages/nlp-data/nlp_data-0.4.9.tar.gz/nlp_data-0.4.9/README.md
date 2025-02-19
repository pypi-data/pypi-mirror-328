## 普强内部NLP数据存储分享工具


### 安装

<details>
<summary>pypi安装</summary>

```bash
# 安装基本功能
pip install nlp-data
# 安装全部功能
pip install nlp-data[all]
```
</details>

<details>
<summary>普强源安装</summary>

```bash
pip install nlp-data --upgrade -i http://192.168.130.5:5002/simple/ --trusted-host 192.168.130.5 --extra-index-url https://mirrors.aliyun.com/pypi/simple
```

</details>

### 使用
<details>
<summary><b>Store的使用</b></summary>

```python 
    # Store相当于是S3对象存储的一个Bucket的封装,每个数据类型对应一个Bucket
    from nlp_data import NLUDocStore
    # 查看文档
    NLUDocStore.list()
    # 获取文档
    docs = NLUDocStore.pull('xxx')
    # 推送文档
    NLUDocStore.push(docs=docs, name='xxx')
```
</details>

<details>
<summary><b>Doc的使用</b></summary>

  ```python
      # Doc是nlp-data的一个存储结构,可以用来存储该格式的数据,以及对数据进行一些操作
      # DocList是Doc的集合,可以用来存储多个Doc,相当于一个python List,有几本的append,extend等类方法, 但不同的DocList有特定的方法用来处理# 该数据类型
      # 以NLUDoc为例,该文档里面有domain,slots,intention等字段,可以用来存储NLU的结果
      from nlp_data import NLUDoc, NLUDocList
      # 创建一个NLUDoc
      doc = NLUDoc(text='添加明天上午跟张三开会的提醒')
      doc.set_domain('schedule_cmn')
      doc.set_intention('add_schedule')
      doc.set_slot(text='明天上午', label='date')     # 优化后，若槽值不存在文本中将不再自动生成索引
      doc.set_slot(text='跟张三开会', label='title')
      # 添加先验实体
      doc.set_prior_entity(text='张三', label='name')
      # 创建一个NLUDocList,并添加doc
      docs = NLUDocList()
      # 添加自定义tag，用于细分数据
      doc.add_tag("方言", "粤语")
      doc.add_tags({"方言": "粤语", "来源": "abnf"})
      # 删除tag
      doc.pop_tag("方言")
      
      docs.append(doc)
      # 从abnf句式输出文件中批量初始化
      docs = NLUDocList.from_abnf_output(output_dir='your/dir', domain='schedule_cmn')
      # 上传到bucket
      from nlp_data import NLUDocStore
      NLUDocStore.push(docs=docs, name='xxx')
  ```
</details>

<details>
<summary><b>Augmentor</b>的使用</summary>

  ```python
    # Augmentor是nlp-data的一个数据增强工具,可以用来对数据进行增强
    from nlp_data import GPTAugmentor, NLUDocStore, DialogueDocList, DialogueDoc
    # 创建一个Augmentor
    augmentor = GPTAugmentor(api_key='xxx')
    # 广东话或者四川话增强NLUDoc
    docs = NLUDocStore.pull('xxx')
    aug_docs = augmentor.augment_nlu_by_localism(docs, '广东话')
    # 根据主题和情景生成多轮对话
    dialogue_docs = augmentor.generate_dialogue_docs(theme='添加日程', situation='用户正在驾驶车辆与车机系统丰田进行语音交互')
    # 对多轮对话数据增强
    dialogue_docs = DialogueDocList()
    dialogue_docs.quick_add(theme='添加日程', situation='用户正在驾驶车辆与车机系统丰田进行交互', conversation=['你好,丰田', '在呢,有什么可以帮助你的', '我要添加一个明天上午跟张三开会的日程', '好的已为您添加成功'])
    aug_dialogue_docs = augmentor.augment_dialogue(dialogue_docs)
  ```
  </details>

<details>
<summary><b>S3的使用</b></summary>

  s3是基础的S3对象存储的封装,可以用来创建bucket,上传下载文件等
  ```python
    # 初始化
    s3 = S3Storage()
    # 列出所有bucket
    s3.list_buckets()
    # 创建bucket
    s3.create_bucket('test')
    # 列出bucket下所有文件
    s3.list_files('test')
    # 上传文件
    s3.upload_file(file_path='./test.txt', bucket_name='test')
    # 下载文件
    s3.download_file(object_name='./test.txt', bucket_name='test')
    # 删除文件
    s3.delete_file(bucket_name='test', file_name='test.txt')
    # 上传文件夹
    s3.upload_dir(bucket_name='test', dir='./tests')
    # 下载文件夹
    s3.download_dir(bucket_name='test', object_name='./tests', save_dir='./')
    # 删除文件夹
    s3.delete_dir(bucket_name='test', dir_name='tests')
    # 删除bucket
    s3.delete_bucket('test')
  ```
</details>


<details>
<summary><b>命令行</b></summary>

```bash
# 查看帮助
nlp-data --help
# 下载文件,当xxx为一个s3中的文件夹时,会下载该文件夹下所有文件
nlp-data download xxx.xxx --bucket xxx --save_path xxx
# 上传文件, 当xxx为一个文件夹时,会上传该文件夹下所有文件
nlp-data upload xxx --bucket xxx
# 删除文件, 当xxx为一个文件夹时,会删除该文件夹下所有文件
nlp-data delete xxx --bucket xxx
```
</details>

<details>
<summary><b>存储LLM会话数据</b></summary>

**[Dialog类说明和示例代码](Dialogue.md)**
</details>

<details>
<summary><b>多意图测试数据构建</b></summary>

```python 
from nlp_data import MultiIntentionDoc,MultiIntentionDocList
# 传入垂类bucket列表,方法内部自动从垂类bucket拉取必过/回归集,以及多意图自有数据.返回列表1[输入1,输入2],列表2[输入1的期望输出列表,输入2的期望输出列表]
multiDataSet = MultiIntentionDocList.genMultiDataset(['tmp-bucket'])
# 输入文本
multiDataSet[0][:3]  # ['帮忙APP分类中搜索爱趣听', '我要喺设置分类中搜索音量', '全部搜索一下bilibili']
# 期望输出
multiDataSet[1][:3]  # [['帮忙APP分类中搜索爱趣听'], ['我要喺设置分类中搜索音量'], ['全部搜索一下bilibili']]
```
</details>

### 示例

examples文件夹下有一些示例代码,可以参考,下面是翻译中文nlu文档然后保存英文nlu的示例

```python
python examples/translate_nlu.py --api_key xxx --doc_name schedule/train --save_name schedule/train --num_samples 5000
```
上述代码将nlu bucket里面的schedule/train文档翻译成英文,nlu-en bucket中


### 开发说明

1. 本项目使用poetry进行包管理,请确保已经安装poetry
2. 本项目使用d-project进行流程管理,请确保已经安装d-project

> 添加新数据结构

1. 先在document模块下创建自己的数据结构,需要继承docarray的BaseDoc,和DocList 分别实现自己的XXDoc和XXDocList  以及相关数据支持的功能函数
2. storage模块下创建自己的DocStore 需要继承 base里面的BaseDocStore  实现pull 和 push 类方法, 并写明bucket_name
3. 使用S3Storage 根据2中的bucket_name 创建bucket

> 发布

1. 修改pyproject.toml中的版本号
2. 修改project.yml版本号
3. 执行```project run publish```

### minio

nlp-data使用minio作为存储后端,目前部署在`192.168.130.5`服务器`/home/wangmengdi/work/minio`目录下,可以通过以下命令启动

```bash
bash run.sh
```


### 依赖安装
方言分析工具：
```
pip install canto-filter==1.0.4
```
大模型数据增广：
```
pip install openai==1.58.1
```
