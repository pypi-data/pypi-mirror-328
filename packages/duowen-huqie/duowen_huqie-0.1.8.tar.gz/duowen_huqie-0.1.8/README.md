# 自然语言处理工具包

```python
from duowen_huqie import NLP

nlp = NLP()

text = "Apache Spark 是一个用于大规模数据处理的统一分析引擎。它提供了 Java、Scala、Python 和 R 的高级 API，以及支持通用执行图的优化引擎。它还支持包括 Spark SQL 用于 SQL 和结构化数据处理、Spark 上的 pandas API 用于 pandas 工作负载、MLlib 用于机器学习、GraphX 用于图处理以及 Structured Streaming 用于增量计算和流处理的丰富高级工具集。"

# 粗切
print(nlp.content_cut(text))

# 细切
print(nlp.content_sm_cut(text))

# 新增词条
nlp.tok_add_word("分析引擎", 1000, "nr")

# 删除词条
nlp.tok_del_word("分析引擎")

# 更新词条
nlp.tok_update_word("分析引擎", 1000, "n")

# 词条查询权重
print(nlp.term_weight("大数据平台使用的什么数据引擎"))

query = "什么是混合召回？"

documents = ["混合召回是一种结合文本召回和向量召回的方法。",
             "文本召回通过关键词匹配实现，向量召回通过语义相似度实现。",
             "混合召回可以提高搜索的准确性和覆盖率。", ]

query_vector = [...]  # 向量需要外部计算
docs_vector = [[...], [...], [...]]  # 向量需要外部计算

# 文本相似度
print(nlp.text_similarity(question=query, docs=documents))

# 问句文本相似度(去除停词)
print(nlp.query_text_similarity(question=query, docs=documents))

# 混合相似度
print(nlp.hybrid_similarity(question=query, question_vector=query_vector, docs_vector=docs_vector, docs=documents))

# 问句混合相似度(去除停词)
print(
    nlp.query_hybrid_similarity(question=query, question_vector=query_vector, docs_vector=docs_vector, docs=documents))

# 向量相似度
print(nlp.vector_similarity(question_vector=query_vector, docs_vector=docs_vector))

```