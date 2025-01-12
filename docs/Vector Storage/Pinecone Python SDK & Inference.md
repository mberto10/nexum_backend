---
tags:
  - ai coding
Type:
  - Documentation
Framework:
  - Agnostic
Phase:
  - Coding
Notes: Documentation from Pinecone Inference and Python SDK
Model Optimised:
  - n.a.
Link: https://docs.pinecone.io/reference/python-sdk
---
# Pinecone Python SDK & Inference

````markdown

[Pinecone Docs home page![logo](https://mintlify.s3.us-west-1.amazonaws.com/pinecone-2/logo/light.svg)](/)

2024-10 (latest)

Search or ask...

Search...

Navigation

SDKs

Python SDK

[Guides](/guides/get-started/overview) [Reference](/reference/api/introduction) [Examples](/examples/notebooks) [Models](/models/overview) [Integrations](/integrations/overview) [Troubleshooting](/troubleshooting/contact-support) [Releases](/release-notes/2024)

There are two versions of the Python SDK:

- `pinecone[gRPC]`: Relies on gRPC for data operations and is more performant than `pinecone`.
- `pinecone`: Has a minimal set of dependencies and interacts with Pinecone via HTTP requests.

See the [Pinecone Python SDK\\
documentation](https://sdk.pinecone.io/python/pinecone.html)
for full installation instructions, usage examples, and reference information.

To make a feature request or report an issue, please [file an issue](https://github.com/pinecone-io/pinecone-java-client/issues).

## [​](\#install)  Install

To install the latest version of the [Python SDK](https://github.com/pinecone-io/pinecone-python-client), run the following command:

gRPC

HTTP

Copy

```Shell
pip install "pinecone[grpc]"

```

To install a specific version of the Python SDK, run the following command:

gRPC

HTTP

Copy

```Shell
pip install "pinecone[grpc]"==<version>

```

To check your SDK version, run the following command:

Copy

```Shell
pip show pinecone

```

To use the [Inference API](/guides/inference/understanding-inference), you must be on version 5.0.0 or later.

### [​](\#install-the-pinecone-assistant-python-plugin)  Install the Pinecone Assistant Python plugin

To interact with [Pinecone Assistant](/guides/assistant/understanding-assistant) using the [Python SDK](/reference/python-sdk), upgrade the client and install the `pinecone-plugin-assistant` package as follows:

HTTP

Copy

```shell
pip install --upgrade pinecone pinecone-plugin-assistant

```

## [​](\#upgrade)  Upgrade

If you already have the Python SDK, upgrade to the latest version as follows:

gRPC

HTTP

Copy

```Shell
pip install "pinecone[grpc]" --upgrade

```

## [​](\#initialize)  Initialize

Once installed, you can import the library and then use an [API key](/guides/projects/manage-api-keys) to initialize a client instance:

gRPC

HTTP

Copy

```Python
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

```

When [creating an index](/guides/indexes/create-an-index), import the `ServerlessSpec` or `PodSpec` class as well:

Serverless index

Pod-based index

Copy

```Python
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec

pc = Pinecone(api_key="YOUR_API_KEY")

pc.create_index(
  name="example-index",
  dimension=1536,
  metric="cosine",
  spec=ServerlessSpec(
    cloud="aws",
    region="us-east-1"
  )
)

```

## [​](\#proxy-configuration)  Proxy configuration

If your network setup requires you to interact with Pinecone through a proxy, you will need to pass additional configuration using optional keyword parameters:

- `proxy_url`: The location of your proxy. This could be an HTTP or HTTPS URL depending on your proxy setup.
- `proxy_headers`: Accepts a python dictionary which can be used to pass any custom headers required by your proxy. If your proxy is protected by authentication, use this parameter to pass basic authentication headers with a digest of your username and password. The `make_headers` utility from `urllib3` can be used to help construct the dictionary.
- `ssl_ca_certs`: By default, the client will perform SSL certificate verification using the CA bundle maintained by Mozilla in the [`certifi`](https://pypi.org/project/certifi/) package. If your proxy is using self-signed certicates, use this parameter to specify the path to the certificate (PEM format).
- `ssl_verify`: SSL verification is enabled by default, but it is disabled when set to `False`. It is not recommened to go into production with SSL verification disabled.

gRPC

HTTP

Copy

```python
from pinecone.grpc import PineconeGRPC as Pinecone
import urllib3 import make_headers

pc = Pinecone(
    api_key="YOUR_API_KEY",
    proxy_url='https://your-proxy.com',
    proxy_headers=make_headers(proxy_basic_auth='username:password'),
    ssl_ca_certs='path/to/cert-bundle.pem'
)

```

Was this page helpful?

YesNo

[Introduction](/reference/pinecone-sdks) [Node.js SDK](/reference/node-sdk)

On this page

- [Install](#install)
- [Install the Pinecone Assistant Python plugin](#install-the-pinecone-assistant-python-plugin)
- [Upgrade](#upgrade)
- [Initialize](#initialize)
- [Proxy configuration](#proxy-configuration)



[Pinecone Docs home page![logo](https://mintlify.s3.us-west-1.amazonaws.com/pinecone-2/logo/light.svg)](/)

2024-10 (latest)

Search or ask...

Search...

Navigation

Inference

Understanding Pinecone Inference

[Guides](/guides/get-started/overview) [Reference](/reference/api/introduction) [Examples](/examples/notebooks) [Models](/models/overview) [Integrations](/integrations/overview) [Troubleshooting](/troubleshooting/contact-support) [Releases](/release-notes/2024)

Pinecone Inference is a service that gives you access to [embedding](/guides/inference/understanding-inference#embedding-models) and [reranking](/guides/inference/understanding-inference#reranking-models) models hosted on Pinecone’s infrastructure.

Pinecone currently hosts models in the US only.

## [​](\#workflows)  Workflows

You can use Pinecone Inference as a [standalone](/guides/inference/understanding-inference#standalone-inference) service or [integrated](/guides/inference/understanding-inference#integrated-inference) with Pinecone’s database operations.

### [​](\#standalone-inference)  Standalone inference

When you use Pinecone Inference as a standalone service, you [generate embeddings](/guides/inference/generate-embeddings) and [rerank results](/guides/inference/rerank) as distinct steps from other database operations like [upsert](/guides/data/upsert-data) and [query](/guides/data/query-data).

1

Embed data

2

Create an index

3

Upsert embeddings

4

Embed queries

5

Search the index

6

Rerank results

### [​](\#integrated-inference)  Integrated inference

This feature is in [public preview](/release-notes/feature-availability).

When you use [integrated inference](/guides/inference/integrated-inference), embedding and reranking are integrated with database operations and do not require extra steps.

1

Create an index configured for a specific embedding model

2

Upsert data with integrated embedding

3

Search the index with integrated embedding and reranking

## [​](\#embedding-models)  Embedding models

The following embedding models are hosted by Pinecone and avaiable for [standalone](/guides/inference/understanding-inference#standalone-inference) or [integrated](/guides/inference/understanding-inference#integrated-inference) inference:

### [​](\#multilingual-e5-large)  multilingual-e5-large

[`multilingual-e5-large`](/models/multilingual-e5-large) is a high-performance dense embedding model trained on a mixture of multilingual datasets. It works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs).

**Details**

- Vector type: Dense
- Modality: Text
- Dimension: 1024
- Recommended similarity metric: Cosine
- Max input tokens per sequence: 507
- Max sequences per batch: 96

**Parameters**

The `multilingual-e5-large` model supports the following parameters:

| Parameter | Type | Required/Optional | Description | Default |
| --- | --- | --- | --- | --- |
| `input_type` | string | Required | The type of input data. Accepted values: `query` or `passage`. |  |
| `truncate` | string | Optional | How to handle inputs longer than those supported by the model. Accepted values: `END` or `NONE`.<br>`END` truncates the input sequence at the input token limit. `NONE` returns an error when the input exceeds the input token limit. | `END` |

**Rate limits**

Rate limits are defined at the project level and vary based on [pricing plan](https://www.pinecone.io/pricing/) and input type.

| Input type | Starter plan | Paid plans |
| --- | --- | --- |
| `passage` | 250k tokens per minute | 1M tokens per minute |
| `query` | 50k tokens per minute | 250k tokens per minute |
| Combined | 5M tokens per month | Unlimited tokens per month |

### [​](\#pinecone-sparse-english-v0)  pinecone-sparse-english-v0

This feature is in [public preview](/release-notes/feature-availability).

[`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0) is a sparse embedding model for converting text to [sparse vectors](/guides/get-started/glossary#sparse-vector) for keyword or hybrid semantic/keyword search. Built on the innovations of the [DeepImpact architecture](https://arxiv.org/pdf/2104.12016), the model directly estimates the lexical importance of tokens by leveraging their context, unlike traditional retrieval models like BM25, which rely solely on term frequency.

**Details**

- Vector type: Sparse
- Modality: Text
- Recommended similarity metric: Dotproduct
- Max input tokens per sequence: 512
- Max sequences per batch: 96

**Parameters**

The `pinecone-sparse-english-v0` model supports the following parameters:

| Parameter | Type | Required/Optional | Description | Default |
| --- | --- | --- | --- | --- |
| `input_type` | string | Required | The type of input data. Accepted values: `query` or `passage`. |  |
| `truncate` | string | Optional | How to handle inputs longer than those supported by the model. Accepted values: `END` or `NONE`.<br>`END` truncates the input sequence at the input token limit. `NONE` returns an error when the input exceeds the input token limit. | `END` |
| `return_tokens` | boolean | Optional | Whether to return the string tokens. | `False` |

**Rate limits**

Rate limits are defined at the project level and vary based on [pricing plan](https://www.pinecone.io/pricing/).

| Limit type | Starter plan | Paid plans |
| --- | --- | --- |
| Tokens per minute | 250K | 1M |
| Tokens per month | Unlimited | Unlimited |

## [​](\#reranking-models)  Reranking models

The following reranking models are hosted by Pinecone and available for [standalone](/guides/inference/understanding-inference#standalone-inference) or [integrated](/guides/inference/understanding-inference#integrated-inference) inference:

### [​](\#bge-reranker-v2-m3)  bge-reranker-v2-m3

[`bge-reranker-v2-m3`](/models/bge-reranker-v2-m3) is a high-performance, multilingual reranking model that works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs).

**Details**

- Modality: Text
- Max tokens per query and document pair: 1024
- Max documents: 100

**Parameters**

The `bge-reranker-v2-m3` model supports the following parameters:

| Parameter | Type | Required/Optional | Description | Default |
| --- | --- | --- | --- | --- |
| `truncate` | string | Optional | How to handle inputs longer than those supported by the model. Accepted values: `END` or `NONE`.<br>`END` truncates the input sequence at the input token limit. `NONE` returns an error when the input exceeds the input token limit. | `NONE` |

**Rate limits**

Rate limits are defined at the project level and vary based on [pricing plan](https://www.pinecone.io/pricing/).

| Limit type | Starter plan | Paid plans |
| --- | --- | --- |
| Requests per minute | 60 | 60 |
| Requests per month | 500 | Unlimited |

To request a rate increase, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

### [​](\#pinecone-rerank-v0)  pinecone-rerank-v0

This feature is in [public preview](/release-notes/feature-availability).

[`pinecone-rerank-v0`](/models/pinecone-rerank-v0) is a state of the art reranking model that out-performs competitors on widely accepted benchmarks. It can handle chunks up to 512 tokens (1-2 paragraphs).

**Details**

- Modality: Text
- Max tokens per query and document pair: 512
- Max documents: 100

**Parameters**

The `pinecone-rerank-v0` model supports the following parameters:

| Parameter | Type | Required/Optional | Description | Default |
| --- | --- | --- | --- | --- |
| `truncate` | string | Optional | How to handle inputs longer than those supported by the model. Accepted values: `END` or `NONE`.<br>`END` truncates the input sequence at the input token limit. `NONE` returns an error when the input exceeds the input token limit. | `END` |

**Rate limits**

Rate limits are defined at the project level and vary based on [pricing plan](https://www.pinecone.io/pricing/).

| Limit type | Starter plan | Paid plans |
| --- | --- | --- |
| Requests per minute | 60 | 60 |
| Requests per month | 500 | Unlimited |

### [​](\#cohere-rerank-3-5)  cohere-rerank-3.5

This feature is available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).

[`cohere-rerank-3.5`](/models/cohere-rerank-3.5) is Cohere’s leading reranking model, balancing performance and latency for a wide range of enterprise search applications.

**Details**

- Modality: Text
- Max tokens per query and document pair: 40,000
- Max documents: 200

**Parameters**

The `cohere-rerank-3.5` model supports the following parameters:

| Parameter | Type | Required/Optional | Description |
| --- | --- | --- | --- |
| `max_chunks_per_doc` | integer | Optional | Long documents will be automatically truncated to the specified number of chunks. Accepted range: `1 - 3072`. |

**Rate limits**

Rate limits are defined at the project level and vary based on [pricing plan](https://www.pinecone.io/pricing/).

| Limit type | Starter plan | Paid plans |
| --- | --- | --- |
| Requests per minute | N/A | 300 |
| Requests per month | N/A | Unlimited |

## [​](\#sdk-support)  SDK support

Standalone inference operations ( [`embed`](/reference/api/2024-10/inference/generate-embeddings) and [`rerank`](/reference/api/2024-10/inference/rerank)) are supported by all [Pinecone SDKs](/reference/pinecone-sdks).

Integrated inference operations ( [`create_for_model`](/reference/api/2025-01/control-plane/create_for_model), [`records/upsert`](/reference/api/2025-01/data-plane/upsert_records), and [`records/search`](/reference/api/2025-01/data-plane/search_records)) are supported by the latest [Python SDK](/reference/python-sdk) plus the `pinecone-plugin-records` plugin. Install the latest SDK and the plugin as follows:

Copy

```shell
pip install --upgrade pinecone pinecone-plugin-records

```

The `pinecone-plugin-records` plugin is not currently compatible with the `pinecone[grpc]` version of the Python SDK.

## [​](\#cost)  Cost

Inference billing is based on tokens used. To learn more, see [Understanding cost](/guides/organizations/manage-cost/understanding-cost#inference-api).

Was this page helpful?

YesNo

[Query sparse-dense vectors](/guides/data/query-sparse-dense-vectors) [Generate embeddings](/guides/inference/generate-embeddings)

On this page

- [Workflows](#workflows)
- [Standalone inference](#standalone-inference)
- [Integrated inference](#integrated-inference)
- [Embedding models](#embedding-models)
- [multilingual-e5-large](#multilingual-e5-large)
- [pinecone-sparse-english-v0](#pinecone-sparse-english-v0)
- [Reranking models](#reranking-models)
- [bge-reranker-v2-m3](#bge-reranker-v2-m3)
- [pinecone-rerank-v0](#pinecone-rerank-v0)
- [cohere-rerank-3.5](#cohere-rerank-3-5)
- [SDK support](#sdk-support)
- [Cost](#cost)

[Pinecone Docs home page![logo](https://mintlify.s3.us-west-1.amazonaws.com/pinecone-2/logo/light.svg)](/)

2024-10 (latest)

Search or ask...

Search...

Navigation

Inference

Generate embeddings

[Guides](/guides/get-started/overview) [Reference](/reference/api/introduction) [Examples](/examples/notebooks) [Models](/models/overview) [Integrations](/integrations/overview) [Troubleshooting](/troubleshooting/contact-support) [Releases](/release-notes/2024)

This page shows you how to use the [Inference API `embed` endpoint](/reference/api/2024-10/inference/generate-embeddings) to generate vector embeddings for text data, such as passages and queries.

The Inference API is a stand-alone service. You can [store generated vector embeddings in a Pinecone vector database](/guides/data/upsert-data), but you are not required to do so.

## [​](\#1-install-an-sdk)  1\. Install an SDK

You can access the [`embed`](/reference/api/2024-10/inference/generate-embeddings) endpoint directly or use the latest [Python](/reference/python-sdk), [Node.js](/reference/node-sdk), [Go](/reference/go-sdk), or [Java](/reference/java-sdk) SDK.

To install the latest SDK version, run the following command:

Python

JavaScript

Java

Go

C#

Copy

```shell
pip install "pinecone[grpc]"

```

If you already have an SDK, upgrade to the latest version as follows:

Python

JavaScript

Go

C#

Copy

```shell
pip install --upgrade "pinecone[grpc]"

```

## [​](\#2-choose-a-model)  2\. Choose a model

Choose an [embedding model hosted by Pinecone](/guides/inference/understanding-inference#embedding-models) or an externally hosted embedding model.

## [​](\#3-generate-embeddings)  3\. Generate embeddings

To generate vector embeddings for upsert into a Pinecone index, use the [`inference.embed`](/reference/api/2024-10/inference/generate-embeddings) endpoint. Specify a [supported embedding model](/guides/inference/understanding-inference#embedding-models) and provide input data and any model-specific parameters.

For example, the following code uses the the [`multilingual-e5-large`](/models/multilingual-e5-large) model to generate embeddings for sentences related to the word “apple”:

Python

JavaScript

Java

Go

C#

curl

Copy

```python
# Import the Pinecone library
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
import time

# Initialize a Pinecone client with your API key
pc = Pinecone(api_key="YOUR_API_KEY")

# Define a sample dataset where each item has a unique ID and piece of text
data = [\
    {"id": "vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},\
    {"id": "vec2", "text": "The tech company Apple is known for its innovative products like the iPhone."},\
    {"id": "vec3", "text": "Many people enjoy eating apples as a healthy snack."},\
    {"id": "vec4", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},\
    {"id": "vec5", "text": "An apple a day keeps the doctor away, as the saying goes."},\
    {"id": "vec6", "text": "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership."}\
]

# Convert the text into numerical vectors that Pinecone can index
embeddings = pc.inference.embed(
    model="multilingual-e5-large",
    inputs=[d['text'] for d in data],
    parameters={"input_type": "passage", "truncate": "END"}
)

print(embeddings)

```

The returned object looks like this:

Python

JavaScript

Java

Go

C#

curl

Copy

```python
EmbeddingsList(
    model='multilingual-e5-large',
    data=[\
        {'values': [0.04925537109375, -0.01313018798828125, -0.0112762451171875, ...]},\
        ...\
    ],
    usage={'total_tokens': 130}
)

```

## [​](\#4-upsert-embeddings)  4\. Upsert embeddings

Once you’ve generated vector embeddings, use the [`upsert`](/guides/data/upsert-data) operation to store them in an index. Make sure to use an index with the same dimensionality as the embeddings.

Python

JavaScript

Java

Go

C#

curl

Copy

```python
# Target the index where you'll store the vector embeddings
index = pc.Index("example-index")

# Prepare the records for upsert
# Each contains an 'id', the embedding 'values', and the original text as 'metadata'
records = []
for d, e in zip(data, embeddings):
    records.append({
        "id": d['id'],
        "values": e['values'],
        "metadata": {'text': d['text']}
    })

# Upsert the records into the index
index.upsert(
    vectors=records,
    namespace="example-namespace"
)

```

## [​](\#5-embed-a-query-and-search)  5\. Embed a query and search

You can also use the [`inference.embed`](/reference/api/2024-10/inference/generate-embeddings) endpoint to generate vector embeddings for queries to a Pinecone index.

For example, the following code uses the the `multilingual-e5-large` model to convert a question about the tech company “Apple” into a query vector and then uses that query vector to search for the three most similar vectors in the index, i.e., the vectors that represent the most relevant answers to the question:

Python

JavaScript

Java

Go

C#

curl

Copy

```python
# Define your query
query = "Tell me about the tech company known as Apple."

# Convert the query into a numerical vector that Pinecone can search with
query_embedding = pc.inference.embed(
    model="multilingual-e5-large",
    inputs=[query],
    parameters={
        "input_type": "query"
    }
)

# Search the index for the three most similar vectors
results = index.query(
    namespace="example-namespace",
    vector=query_embedding[0].values,
    top_k=3,
    include_values=False,
    include_metadata=True
)

print(results)

```

The response includes only sentences about the tech company, not the fruit:

Python

JavaScript

Java

Go

C#

curl

Copy

```python
{'matches': [{'id': 'vec2',\
              'metadata': {'text': 'The tech company Apple is known for its '\
                                   'innovative products like the iPhone.'},\
              'score': 0.8727808,\
              'sparse_values': {'indices': [], 'values': []},\
              'values': []},\
             {'id': 'vec4',\
              'metadata': {'text': 'Apple Inc. has revolutionized the tech '\
                                   'industry with its sleek designs and '\
                                   'user-friendly interfaces.'},\
              'score': 0.8526099,\
              'sparse_values': {'indices': [], 'values': []},\
              'values': []},\
             {'id': 'vec6',\
              'metadata': {'text': 'Apple Computer Company was founded on '\
                                   'April 1, 1976, by Steve Jobs, Steve '\
                                   'Wozniak, and Ronald Wayne as a '\
                                   'partnership.'},\
              'score': 0.8499719,\
              'sparse_values': {'indices': [], 'values': []},\
              'values': []}],
 'namespace': 'example-namespace',
 'usage': {'read_units': 6}}

```

Was this page helpful?

YesNo

[Understanding Pinecone Inference](/guides/inference/understanding-inference) [Rerank documents](/guides/inference/rerank)

On this page

- [1\. Install an SDK](#1-install-an-sdk)
- [2\. Choose a model](#2-choose-a-model)
- [3\. Generate embeddings](#3-generate-embeddings)
- [4\. Upsert embeddings](#4-upsert-embeddings)
- [5\. Embed a query and search](#5-embed-a-query-and-search)

[Pinecone Docs home page![logo](https://mintlify.s3.us-west-1.amazonaws.com/pinecone-2/logo/light.svg)](/)

2024-10 (latest)

Search or ask...

Search...

Navigation

Inference

Rerank documents

[Guides](/guides/get-started/overview) [Reference](/reference/api/introduction) [Examples](/examples/notebooks) [Models](/models/overview) [Integrations](/integrations/overview) [Troubleshooting](/troubleshooting/contact-support) [Releases](/release-notes/2024)

You can use the [Inference API `rerank` endpoint](/reference/api/2024-10/inference/rerank) to rerank documents, such as text passages, according to their relevance to a query.

To run through this guide in your browser, see the [Rerank example notebook](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/pinecone-reranker.ipynb).

## [​](\#before-you-begin)  Before you begin

Ensure you have the following:

- A [Pinecone account](https://app.pinecone.io/)
- A [Pinecone API key](https://docs.pinecone.io/guides/operations/understanding-security#api-keys)

## [​](\#1-install-an-sdk)  1\. Install an SDK

You can access the [`rerank`](/reference/api/2024-10/inference/rerank) endpoint directly or use the latest [Python](/reference/python-sdk), [Node.js](/reference/node-sdk), [Go](/reference/go-sdk), or [Java](/reference/java-sdk) SDK.

To install the latest SDK version, run the following command:

Python

JavaScript

Java

Go

C#

Copy

```shell
pip install "pinecone[grpc]"

```

If you already have an SDK, upgrade to the latest version as follows:

Python

JavaScript

Go

C#

Copy

```shell
pip install --upgrade "pinecone[grpc]"

```

## [​](\#2-choose-a-model)  2\. Choose a model

Choose a [reranking model hosted by Pinecone](/guides/inference/understanding-inference#reranking-models) or an externally hosted reranking model.

## [​](\#3-rerank-documents)  3\. Rerank documents

To rerank documents, use the [`inference.rerank`](/reference/api/2024-10/inference/rerank) operation. Specify a [supported reranking model](/guides/inference/understanding-inference#rerank), and provide documents and a query as well as other model-specific parameters.

For example, the following request uses the `bge-reranker-v2-m3` model to rerank the values of the `documents.text` field based on their relevance to the query, `"The tech company Apple is known for its innovative products like the iPhone."`.

With `truncate` set to `"END"`, the input sequence ( `query` \+ `document`) is truncated at the token limit ( `1024`); to return an error instead, you’d set `truncate` to `"NONE"` or leave the parameter out.

Python

JavaScript

Java

Go

C#

curl

Copy

```python
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

result = pc.inference.rerank(
    model="bge-reranker-v2-m3",
    query="The tech company Apple is known for its innovative products like the iPhone.",
    documents=[\
        {"id": "vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},\
        {"id": "vec2", "text": "Many people enjoy eating apples as a healthy snack."},\
        {"id": "vec3", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},\
        {"id": "vec4", "text": "An apple a day keeps the doctor away, as the saying goes."},\
    ],
    top_n=4,
    return_documents=True,
    parameters={
        "truncate": "END"
    }
)

print(result)

```

The returned object contains documents with relevance scores:

Normalized between 0 and 1, the `score` represents the relevance of a passage to the query, with scores closer to 1 indicating higher relevance.

Python

JavaScript

Java

Go

C#

curl

Copy

```python
RerankResult(
  model='bge-reranker-v2-m3',
  data=[\
    { index=2, score=0.48357219,\
      document={id="vec3", text="Apple Inc. has re..."} },\
    { index=0, score=0.048405956,\
      document={id="vec1", text="Apple is a popula..."} },\
    { index=3, score=0.007846239,\
      document={id="vec4", text="An apple a day ke..."} },\
    { index=1, score=0.0006563728,\
      document={id="vec2", text="Many people enjoy..."} }\
  ],
  usage={'rerank_units': 1}
)

```

### [​](\#rerank-documents-on-a-custom-field)  Rerank documents on a custom field

To rerank documents on a field other than `documents.text`, use the [`inference.rerank`](/reference/api/2024-10/inference/rerank) endpoint, and provide the `rank_fields` parameter to specify the fields on which to rerank.

For example, the following request reranks documents based on the values of the `documents.my_field` field:

Python

JavaScript

Java

Go

C#

curl

Copy

```python
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

result = pc.inference.rerank(
    model="bge-reranker-v2-m3",
    query="The tech company Apple is known for its innovative products like the iPhone.",
    documents=[\
        {"id": "vec1", "my_field": "Apple is a popular fruit known for its sweetness and crisp texture."},\
        {"id": "vec2", "my_field": "Many people enjoy eating apples as a healthy snack."},\
        {"id": "vec3", "my_field": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},\
        {"id": "vec4", "my_field": "An apple a day keeps the doctor away, as the saying goes."},\
    ],
    rank_fields=["my_field"],
    top_n=4,
    return_documents=True,
    parameters={
        "truncate": "END"
    }
)

```

Was this page helpful?

YesNo

[Generate embeddings](/guides/inference/generate-embeddings) [Upsert and search with integrated inference](/guides/inference/integrated-inference)

On this page

- [Before you begin](#before-you-begin)
- [1\. Install an SDK](#1-install-an-sdk)
- [2\. Choose a model](#2-choose-a-model)
- [3\. Rerank documents](#3-rerank-documents)
- [Rerank documents on a custom field](#rerank-documents-on-a-custom-field)

[Pinecone Docs home page![logo](https://mintlify.s3.us-west-1.amazonaws.com/pinecone-2/logo/light.svg)](/)

2024-10 (latest)

Search or ask...

Search...

Navigation

Inference

Upsert and search with integrated inference

[Guides](/guides/get-started/overview) [Reference](/reference/api/introduction) [Examples](/examples/notebooks) [Models](/models/overview) [Integrations](/integrations/overview) [Troubleshooting](/troubleshooting/contact-support) [Releases](/release-notes/2024)

This page shows you how to use [integrated inference](/guides/inference/understanding-inference) to upsert and search without extra steps for embedding data and reranking results.

This feature is in [public preview](/release-notes/feature-availability).

## [​](\#1-install-dependencies)  1\. Install dependencies

Install the latest Pinecone Python SDK and integrated inference plugin as follows:

Copy

```shell
pip install --upgrade pinecone pinecone-plugin-records

```

The `pinecone-plugin-records` plugin is not currently compatible with the `pinecone[grpc]` version of the Python SDK.

## [​](\#2-create-or-configure-an-index)  2\. Create or configure an index

Integrated inference requires a serverless index configured for a specific embedding model. You can either create a new index for a model or configure an existing index for a model.

- New index
- Existing index

To create a serverless index with integrated embedding, use the [`create_for_model`](/reference/api/2025-01/control-plane/create_for_model) operation as follows:

- Provide a `name` for the index.
- Set `embed.model` to one of [Pinecone’s hosted embedding models](/guides/inference/understanding-inference#embedding-models).
- Set `spec.cloud` and `spec.region` to the [cloud and region](/guides/indexes/understanding-indexes#cloud-regions) where the index should be deployed.
- Set `embed.field_map` to the name of the field in your source document that contains the data for embedding.

Other parameters are optional. See the [API reference](/reference/api/2025-01/control-plane/create_for_model) for details.

Python

curl

Copy

```python
# pip install --upgrade pinecone pinecone-plugin-records
from pinecone import Pinecone
import time

pc = Pinecone(api_key="YOUR_API_KEY")

index_name = "example-index"

index_model = pc.create_index_for_model(
    name=index_name,
    cloud="aws",
    region="us-east-1",
    embed={
      "model":"multilingual-e5-large",
      "field_map":{"text": "chunk_text"}
    }
)

print(index_model)

```

The response will look like this:

Python

curl

Copy

```python
{'deletion_protection': 'disabled',
 'dimension': 1024,
 'embed': {'dimension': 1024,
           'field_map': {'text': 'chunk_text'},
           'metric': 'cosine',
           'model': 'multilingual-e5-large',
           'read_parameters': {'input_type': 'query', 'truncate': 'END'},
           'write_parameters': {'input_type': 'passage', 'truncate': 'END'},
           'vector_type': 'dense'},
 'host': 'example-index-govk0nt.svc.aped-4627-b74a.pinecone.io',
 'id': '9e8b39c5-a142-4776-9609-e8612ad03d92',
 'metric': 'cosine',
 'name': 'example-index',
 'spec': {'serverless': {'cloud': 'aws', 'region': 'us-east-1'}},
 'status': {'ready': True, 'state': 'Ready'},
 'tags': None}

```

## [​](\#3-upsert-data)  3\. Upsert data

Once you have an index configured for a specific embedding model, use the [`/records/upsert`](/reference/api/2025-01/data-plane/upsert_records) operation to convert your source data to embeddings and upsert them into a namespace in the index.

Note the following requirements for each document in the request body:

- Each document must contain a unique `_id`, which will serve as the unique record identifier in the index namespace.
- Each document must contain a field with the data for embedding. This field must match the `field_map` specified when creating the index.
- Any additional fields in the document will be stored in the index and can be returned in search results or used to filter search results.
- When using the API directly, documents are specified using the [NDJSON format](https://github.com/ndjson/ndjson-spec), also known as line-delimited JSON or JSONL, with one document per line. The Python SDK transforms the list of dictionary entries into the correct NDJSON format for you.

Python

curl

Copy

```python
# Target the created index for upsert and search
index = pc.Index(index_name)

index.upsert_records(
  "example-namespace",
  [\
      {\
          "_id": "rec1",\
          "chunk_text": "Apple's first product, the Apple I, was released in 1976 and was hand-built by co-founder Steve Wozniak.",\
          "category": "product",\
      },\
      {\
          "_id": "rec2",\
          "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.",\
          "category": "nutrition",\
      },\
      {\
          "_id": "rec3",\
          "chunk_text": "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.",\
          "category": "cultivation",\
      },\
      {\
          "_id": "rec4",\
          "chunk_text": "In 2001, Apple released the iPod, which transformed the music industry by making portable music widely accessible.",\
          "category": "product",\
      },\
      {\
          "_id": "rec5",\
          "chunk_text": "Apple went public in 1980, making history with one of the largest IPOs at that time.",\
          "category": "milestone",\
      },\
      {\
          "_id": "rec6",\
          "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.",\
          "category": "nutrition",\
      },\
      {\
          "_id": "rec7",\
          "chunk_text": "Known for its design-forward products, Apple's branding and market strategy have greatly influenced the technology sector and popularized minimalist design worldwide.",\
          "category": "influence",\
      },\
      {\
          "_id": "rec8",\
          "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.",\
          "category": "nutrition",\
      },\
  ],
)

time.sleep(10) # Wait for the upserted vectors to be indexed

```

## [​](\#4-search-the-index)  4\. Search the index

Use the [`/records/search`](/reference/api/2025-01/data-plane/search_records) operation to convert a query to a vector embedding and then search your namespace for the most semantically similar records, along with their similarity scores.

Note the following:

- The `inputs` field must be `text`.
- The `top_k` parameter must specify the number of similar records to return.
- Optionally, you can specify:
  - The `fields` to return. If not specified, the response will include all fields.
  - A `filter` to narrow down the search results.
  - `rerank` parameters to rerank the initial search results based on relevance to the query.

### [​](\#basic-search)  Basic search

In the previous step, you upserted 8 documents, some about Apple, the technology company, and some about apple, the fruit.

First, search for the 4 documents most semantically related to the query, “Disease prevention”:

Python

curl

Copy

```python
results = index.search_records(
    namespace="example-namespace",
    query={
        "inputs": {"text": "Disease prevention"},
        "top_k": 4
    },
    fields=["category", "chunk_text"]
)

print(results)

```

Notice that the response includes only documents about the fruit, not the tech company:

Python

curl

Copy

```python
{'result': {'hits': [{'_id': 'rec6',\
                      '_score': 0.8197098970413208,\
                      'fields': {'category': 'nutrition',\
                                 'chunk_text': 'Rich in vitamin C and other '\
                                               'antioxidants, apples '\
                                               'contribute to immune health '\
                                               'and may reduce the risk of '\
                                               'chronic diseases.'}},\
                     {'_id': 'rec2',\
                      '_score': 0.7929002642631531,\
                      'fields': {'category': 'nutrition',\
                                 'chunk_text': 'Apples are a great source of '\
                                               'dietary fiber, which supports '\
                                               'digestion and helps maintain a '\
                                               'healthy gut.'}},\
                     {'_id': 'rec8',\
                      '_score': 0.7800688147544861,\
                      'fields': {'category': 'nutrition',\
                                 'chunk_text': 'The high fiber content in '\
                                               'apples can also help regulate '\
                                               'blood sugar levels, making '\
                                               'them a favorable snack for '\
                                               'people with diabetes.'}},\
                     {'_id': 'rec3',\
                      '_score': 0.7553971409797668,\
                      'fields': {'category': 'cultivation',\
                                 'chunk_text': 'Apples originated in Central '\
                                               'Asia and have been cultivated '\
                                               'for thousands of years, with '\
                                               'over 7,500 varieties available '\
                                               'today.'}}]},
 'usage': {'embed_total_tokens': 8, 'read_units': 6}}

```

### [​](\#search-with-reranking)  Search with reranking

To rerank initial search results based on relevance to the query, add the `rerank` parameter, including the [reranking model](/guides/inference/understanding-inference#reranking-models) you want to use, the number of reranked results to return, and the fields to use for reranking, if different than the main query.

For example, repeat the search for the 4 documents most semantically related to the query, “Disease prevention”, but this time rerank the results and return only the 2 most relevant documents:

Python

curl

Copy

```python
ranked_results = index.search_records(
    namespace="example-namespace",
    query={
        "inputs": {"text": "Disease prevention"},
        "top_k": 4
    },
    rerank={
        "model": "pinecone-rerank-v0",
        "top_n": 2,
        "rank_fields": ["chunk_text"]
    },
    fields=["category", "chunk_text"]
)

print(ranked_results)

```

Notice that the 2 returned documents are the most relevant for the query, the first relating to reducing chronic diseases, the second relating to preventing diabetes:

Python

curl

Copy

```python
{'result': {'hits': [{'_id': 'rec6',\
                      '_score': 0.004433765076100826,\
                      'fields': {'category': 'nutrition',\
                                 'chunk_text': 'Rich in vitamin C and other '\
                                               'antioxidants, apples '\
                                               'contribute to immune health '\
                                               'and may reduce the risk of '\
                                               'chronic diseases.'}},\
                     {'_id': 'rec8',\
                      '_score': 0.0029121784027665854,\
                      'fields': {'category': 'nutrition',\
                                 'chunk_text': 'The high fiber content in '\
                                               'apples can also help regulate '\
                                               'blood sugar levels, making '\
                                               'them a favorable snack for '\
                                               'people with diabetes.'}}]},
 'usage': {'embed_total_tokens': 8, 'read_units': 6, 'rerank_units': 1}}

```

### [​](\#search-with-filtering)  Search with filtering

Your upserted documents also contain a `category` field. Now use that field as a filter to search for the 2 documents related to Apple, the tech company, that are in the “product” category:

Python

curl

Copy

```python
filtered_results = index.search_records(
    namespace="example-namespace",
    query={
        "inputs": {"text": "Apple tech company"},
        "top_k": 2,
        "filter": {"category": "product"}
    },
    fields=["category", "chunk_text"]
)

print(filtered_results)

```

Notice that the response includes only documents about Apple, the tech company, that are in the “product” category:

Python

curl

Copy

```python
{'result': {'hits': [{'_id': 'rec1',\
                      '_score': 0.8127778768539429,\
                      'fields': {'category': 'product',\
                                 'chunk_text': "Apple's first product, the "\
                                               'Apple I, was released in 1976 '\
                                               'and was hand-built by '\
                                               'co-founder Steve Wozniak.'}},\
                     {'_id': 'rec4',\
                      '_score': 0.7763848900794983,\
                      'fields': {'category': 'product',\
                                 'chunk_text': 'In 2001, Apple released the '\
                                               'iPod, which transformed the '\
                                               'music industry by making '\
                                               'portable music widely '\
                                               'accessible.'}}]},
 'usage': {'embed_total_tokens': 8, 'read_units': 6}}

```

Was this page helpful?

YesNo

[Rerank documents](/guides/inference/rerank) [Understanding Pinecone Assistant](/guides/assistant/understanding-assistant)

On this page

- [1\. Install dependencies](#1-install-dependencies)
- [2\. Create or configure an index](#2-create-or-configure-an-index)
- [3\. Upsert data](#3-upsert-data)
- [4\. Search the index](#4-search-the-index)
- [Basic search](#basic-search)
- [Search with reranking](#search-with-reranking)
- [Search with filtering](#search-with-filtering)


````