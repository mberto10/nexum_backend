---
tags:
  - ai coding
Type:
  - Documentation
Framework:
  - Agnostic
Phase:
  - Coding
Notes: Documentation from Pinecone Data
Model Optimised:
  - n.a.
---
# Pinecone Documentation - Data

````markdown
tent of the records](/guides/data/fetch-data).

## [​](\#delete-all-records-for-a-parent-document)  Delete all records for a parent document

To delete all records representing chunks of a single document, first list the record IDs based on their common ID prefix, and then [delete the records by ID](/guides/data/delete-data#delete-specific-records-by-id):

Python

JavaScript

Java

Go

curl

Copy

```python
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key='YOUR_API_KEY')

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/data/target-an-index
index = pc.Index(host="INDEX_HOST")

for ids in index.list(prefix='doc1#', namespace='example-namespace'):
  print(ids) # ['doc1#chunk1', 'doc1#chunk2', 'doc1#chunk3']
  index.delete(ids=ids, namespace=namespace)

```

## [​](\#work-with-multi-level-id-prefixes)  Work with multi-level ID prefixes

The examples above are based on a simple ID prefix ( `doc1#`), but it’s also possible to work with more complex, multi-level prefixes.

For example, let’s say you use the prefix pattern `doc#v#chunk` to differentiate between different versions of a document. If you wanted to delete all records for one version of a document, first list the record IDs based on the relevant `doc#v#` prefix and then [delete the records by ID](/guides/data/delete-data#delete-specific-records-by-id):

Python

JavaScript

Java

Go

curl

Copy

```python
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key='YOUR_API_KEY')

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/data/target-an-index
index = pc.Index(host="INDEX_HOST")

for ids in index.list(prefix='doc1#v1', namespace='example-namespace'):
    print(ids) # ['doc1#v1#chunk1', 'doc1#v1#chunk2', 'doc1#v1#chunk3']
    index.delete(ids=ids, namespace=namespace)

```

However, if you wanted to delete all records across all versions of a document, you would list the record IDs based on the `doc1#` part of the prefix that is common to all versions and then [delete the records by ID](/guides/data/delete-data#delete-specific-records-by-id):

Python

JavaScript

Java

Go

curl

Copy

```python
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key='YOUR_API_KEY')

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/data/target-an-index
index = pc.Index(host="INDEX_HOST")

for ids in index.list(prefix='doc1#', namespace='example-namespace'):
    print(ids) # ['doc1#v1#chunk1', 'doc1#v1#chunk2', 'doc1#v1#chunk3', 'doc1#v2#chunk1', 'doc1#v2#chunk2', 'doc1#v2#chunk3']
    index.delete(ids=ids, namespace=namespace)

```

## [​](\#rag-using-pod-based-indexes)  RAG using pod-based indexes

The `list` endpoint does not support pod-based indexes. Instead of using ID prefixes to reference parent documents, [use a metadata key-value pair](/guides/data/upsert-data#upsert-records-with-metadata). If you later need to delete the records, you can [pass a metadata filter expression to the `delete` endpoint](/guides/data/delete-data#delete-specific-records-by-metadata).

Was this page helpful?

YesNo

[Understanding metadata](/guides/data/understanding-metadata) [Understanding data freshness](/guides/data/data-freshness/understanding-data-freshness)

On this page

- [Use ID prefixes](#use-id-prefixes)
- [Use ID prefixes to reference parent documents](#use-id-prefixes-to-reference-parent-documents)
- [List all record IDs for a parent document](#list-all-record-ids-for-a-parent-document)
- [Delete all records for a parent document](#delete-all-records-for-a-parent-document)
- [Work with multi-level ID prefixes](#work-with-multi-level-id-prefixes)
- [RAG using pod-based indexes](#rag-using-pod-based-indexes)


[Pinecone Docs home page![logo](https://mintlify.s3.us-west-1.amazonaws.com/pinecone-2/logo/light.svg)](/)

2024-10 (latest)

Search or ask...

Search...

Navigation

Hybrid search and sparse vectors

Understanding hybrid search

[Guides](/guides/get-started/overview) [Reference](/reference/api/introduction) [Examples](/examples/notebooks) [Models](/models/overview) [Integrations](/integrations/overview) [Troubleshooting](/troubleshooting/contact-support) [Releases](/release-notes/2024)

Pinecone supports vectors with sparse and dense values, which allows you to perform hybrid search on your Pinecone index. Hybrid search combines semantic and keyword search in one query for more relevant results. Semantic search results for out-of-domain queries can be less relevant; [combining these with keyword search results can improve relevance](https://arxiv.org/abs/2210.11934). This topic describes how hybrid search with sparse-dense vectors works in Pinecone.

To see sparse-dense embeddings in action, see the [Ecommerce hybrid search example](https://github.com/pinecone-io/examples/blob/master/learn/search/hybrid-search/ecommerce-search/ecommerce-search.ipynb).

This feature is in [public preview](/release-notes/feature-availability).

## [​](\#hybrid-search-in-pinecone)  Hybrid search in Pinecone

In Pinecone, you perform hybrid search with **sparse-dense vectors**. Sparse-dense vectors combine [dense and sparse embeddings](https://www.pinecone.io/learn/dense-vector-embeddings-nlp/#dense-vs-sparse-vectors) as a single vector. Sparse and dense vectors represent different types of information and enable distinct kinds of search.

### [​](\#dense-vectors)  Dense vectors

The basic vector type in Pinecone is a [dense vector](https://www.pinecone.io/learn/dense-vector-embeddings-nlp/). Dense vectors enable semantic search. Semantic search returns the most similar results according to a specific distance metric even if no exact matches are present. This is possible because dense vectors generated by embedding models such as [`multilingual-e5-large`](/models/multilingual-e5-large) are numerical representations of semantic meaning.

### [​](\#sparse-vectors)  Sparse vectors

Sparse vectors have very large number of dimensions, where only a small proportion of values are non-zero. When used for keywords search, each sparse vector represents a document; the dimensions represent words from a dictionary, and the values represent the importance of these words in the document. Keyword search algorithms compute the relevance of text documents based on the number of keyword matches, their frequency, and other factors.

## [​](\#sparse-dense-workflow)  Sparse-dense workflow

Using sparse-dense vectors involves the following general steps:

1. [Create dense vectors](/guides/inference/generate-embeddings.mdx) using a dense embedding model.
2. [Create sparse vectors](/guides/data/encode-sparse-vectors) using a sparse embedding model.
3. [Create an index](/guides/indexes/create-an-index) with the `dotproduct` [metric](/guides/indexes/understanding-indexes#dotproduct).
4. [Upsert sparse-dense vectors to your index](/guides/data/upsert-sparse-dense-vectors).
5. [Search the index using sparse-dense vectors](/guides/data/query-sparse-dense-vectors).
6. Pinecone returns sparse-dense vectors.

## [​](\#considerations-for-serverless-indexes)  Considerations for serverless indexes

### [​](\#query-execution)  Query execution

The implementation of hybrid search is meaningfully different between pod-based and serverless indexes. If you switch from one to the other, you may experience a regression in accuracy.

When you query a serverless index, query planners choose clusters of records based on their similarity to the dense vector value in the query. Query executors then select records based on the similarity of both their dense and sparse vector values to the dense and sparse vector values in the query. Because the initial selection of clusters is based only on dense vector values, this process can affect accuracy in cases where records contain dense and sparse values that are from different data representations (e.g., image and text) or are otherwise not strongly correlated.

For more details about the execution of hybrid queries, see [Serverless architecture](/reference/architecture/serverless-architecture#query-executors).

### [​](\#sparse-retrieval-costs)  Sparse retrieval costs

Retrieving sparse vectors from a serverless index incurs additional RUs. See [Understanding cost](/guides/organizations/manage-cost/understanding-cost#serverless-indexes) for more details.

## [​](\#limitations)  Limitations

Pinecone sparse-dense vectors have the following limitations:

- Records with sparse vector values must also contain dense vector values.

- Sparse vector values can contain up to 1000 non-zero values and 4.2 billion dimensions.

- Only indexes using the [dotproduct distance metric](/guides/indexes/understanding-indexes#dotproduct) support querying sparse-dense vectors.

Upserting, updating, and fetching sparse-dense vectors in indexes with a different distance metric will succeed, but querying will return an error.

- Indexes created before February 22, 2023 do not support sparse vectors.


## [​](\#see-also)  See also

- [Create sparse vector embeddings](/guides/data/encode-sparse-vectors)
- [Upsert sparse-dense vectors](/guides/data/upsert-sparse-dense-vectors)
- [Query sparse-dense vectors](/guides/data/query-sparse-dense-vectors)
- [Ecommerce hybrid search example](https://github.com/pinecone-io/examples/blob/master/learn/search/hybrid-search/ecommerce-search/ecommerce-search.ipynb)

Was this page helpful?

YesNo

[Check data freshness](/guides/data/data-freshness/check-data-freshness) [Encode sparse vectors](/guides/data/encode-sparse-vectors)

On this page

- [Hybrid search in Pinecone](#hybrid-search-in-pinecone)
- [Dense vectors](#dense-vectors)
- [Sparse vectors](#sparse-vectors)
- [Sparse-dense workflow](#sparse-dense-workflow)
- [Considerations for serverless indexes](#considerations-for-serverless-indexes)
- [Query execution](#query-execution)
- [Sparse retrieval costs](#sparse-retrieval-costs)
- [Limitations](#limitations)
- [See also](#see-also)


````