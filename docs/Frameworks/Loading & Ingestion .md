---
tags:
  - ai coding
Type:
  - Documentation
Framework:
  - Llamaindex
Phase:
  - Coding
Notes: Documentation for LlamaIndex - Loading Section
Model Optimised:
  - n.a.
Link: https://docs.llamaindex.ai/en/stable/module_guides/loading/
---
# Loading & Ingestion 

````markdown
[Skip to content](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/usage_pattern/#usage-pattern)

# Usage Pattern [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/usage_pattern/\#usage-pattern "Permanent link")

## Get Started [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/usage_pattern/\#get-started "Permanent link")

Each data loader contains a "Usage" section showing how that loader can be used. At the core of using each loader is a `download_loader` function, which
downloads the loader file into a module that you can use within your application.

Example usage:

```
from llama_index.core import VectorStoreIndex, download_loader

from llama_index.readers.google import GoogleDocsReader

gdoc_ids = ["1wf-y2pd9C878Oh-FmLH7Q_BQkljdm6TQal-c1pUfrec"]
loader = GoogleDocsReader()
documents = loader.load_data(document_ids=gdoc_ids)
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
query_engine.query("Where did the author go to school?")

```

Back to top
![](https://static.scarf.sh/a.png?x-pxid=2b5669c2-eb91-4d0a-81d6-dc7238350598)

[iframe](https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfESacpAAAAAIAiwrVpFehgscJonmg1gKhpKg2e&co=aHR0cHM6Ly9kb2NzLmxsYW1haW5kZXguYWk6NDQz&hl=en&v=zIriijn3uj5Vpknvt_LnfNbF&size=invisible&cb=a6odmryucgyi)


[Skip to content](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/llama_parse/#llamaparse)

# LlamaParse [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/llama_parse/\#llamaparse "Permanent link")

LlamaParse is a service created by LlamaIndex to efficiently parse and represent files for efficient retrieval and context augmentation using LlamaIndex frameworks.

LlamaParse directly integrates with [LlamaIndex](https://github.com/run-llama/llama_index).

You can sign up and use LlamaParse for free! Dozens of document types are supported including PDFs, Word Files, PowerPoint, Excel spreadsheets and many more.

For information on how to get started, check out the [LlamaParse documentation](https://docs.cloud.llamaindex.ai/llamaparse/getting_started).

Back to top
![](https://static.scarf.sh/a.png?x-pxid=2b5669c2-eb91-4d0a-81d6-dc7238350598)

[iframe](https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfESacpAAAAAIAiwrVpFehgscJonmg1gKhpKg2e&co=aHR0cHM6Ly9kb2NzLmxsYW1haW5kZXguYWk6NDQz&hl=en&v=zIriijn3uj5Vpknvt_LnfNbF&size=invisible&cb=5y7jglh9e4k3)


[Skip to content](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_metadata_extractor/#metadata-extraction-usage-pattern)

# Metadata Extraction Usage Pattern [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_metadata_extractor/\#metadata-extraction-usage-pattern "Permanent link")

You can use LLMs to automate metadata extraction with our `Metadata Extractor` modules.

Our metadata extractor modules include the following "feature extractors":

- `SummaryExtractor` \- automatically extracts a summary over a set of Nodes
- `QuestionsAnsweredExtractor` \- extracts a set of questions that each Node can answer
- `TitleExtractor` \- extracts a title over the context of each Node
- `EntityExtractor` \- extracts entities (i.e. names of places, people, things) mentioned in the content of each Node

Then you can chain the `Metadata Extractor` s with our node parser:

```
from llama_index.core.extractors import (
    TitleExtractor,
    QuestionsAnsweredExtractor,
)
from llama_index.core.node_parser import TokenTextSplitter

text_splitter = TokenTextSplitter(
    separator=" ", chunk_size=512, chunk_overlap=128
)
title_extractor = TitleExtractor(nodes=5)
qa_extractor = QuestionsAnsweredExtractor(questions=3)

# assume documents are defined -> extract nodes
from llama_index.core.ingestion import IngestionPipeline

pipeline = IngestionPipeline(
    transformations=[text_splitter, title_extractor, qa_extractor]
)

nodes = pipeline.run(
    documents=documents,
    in_place=True,
    show_progress=True,
)

```

or insert into an index:

```
from llama_index.core import VectorStoreIndex

index = VectorStoreIndex.from_documents(
    documents, transformations=[text_splitter, title_extractor, qa_extractor]
)

```

## Resources [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_metadata_extractor/\#resources "Permanent link")

- [SEC Documents Metadata Extraction](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/)
- [LLM Survey Extraction](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtraction_LLMSurvey/)
- [Entity Extraction](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/EntityExtractionClimate/)
- [Marvin Metadata Extraction](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MarvinMetadataExtractorDemo/)
- [Pydantic Metadata Extraction](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/PydanticExtractor/)

Back to top
![](https://static.scarf.sh/a.png?x-pxid=2b5669c2-eb91-4d0a-81d6-dc7238350598)

[iframe](https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfESacpAAAAAIAiwrVpFehgscJonmg1gKhpKg2e&co=aHR0cHM6Ly9kb2NzLmxsYW1haW5kZXguYWk6NDQz&hl=en&v=zIriijn3uj5Vpknvt_LnfNbF&size=invisible&cb=2jtxpf2aww3d)


[Skip to content](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/#simpledirectoryreader)

# SimpleDirectoryReader [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/\#simpledirectoryreader "Permanent link")

`SimpleDirectoryReader` is the simplest way to load data from local files into LlamaIndex. For production use cases it's more likely that you'll want to use one of the many Readers available on [LlamaHub](https://llamahub.ai/), but `SimpleDirectoryReader` is a great way to get started.

## Supported file types [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/\#supported-file-types "Permanent link")

By default `SimpleDirectoryReader` will try to read any files it finds, treating them all as text. In addition to plain text, it explicitly supports the following file types, which are automatically detected based on file extension:

- .csv - comma-separated values
- .docx - Microsoft Word
- .epub - EPUB ebook format
- .hwp - Hangul Word Processor
- .ipynb - Jupyter Notebook
- .jpeg, .jpg - JPEG image
- .mbox - MBOX email archive
- .md - Markdown
- .mp3, .mp4 - audio and video
- .pdf - Portable Document Format
- .png - Portable Network Graphics
- .ppt, .pptm, .pptx - Microsoft PowerPoint

One file type you may be expecting to find here is JSON; for that we recommend you use our [JSON Loader](https://llamahub.ai/l/readers/llama-index-readers-json).

## Usage [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/\#usage "Permanent link")

The most basic usage is to pass an `input_dir` and it will load all supported files in that directory:

```
from llama_index.core import SimpleDirectoryReader

reader = SimpleDirectoryReader(input_dir="path/to/directory")
documents = reader.load_data()

```

Documents can also be loaded with parallel processing if loading many files from
a directory. Note that there are differences when using `multiprocessing` with
Windows and Linux/MacOS machines, which is explained throughout the `multiprocessing` docs
(e.g. see [here](https://docs.python.org/3/library/multiprocessing.html?highlight=process#the-spawn-and-forkserver-start-methods)).
Ultimately, Windows users may see less or no performance gains whereas Linux/MacOS
users would see these gains when loading the exact same set of files.

```
...
documents = reader.load_data(num_workers=4)

```

### Reading from subdirectories [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/\#reading-from-subdirectories "Permanent link")

By default, `SimpleDirectoryReader` will only read files in the top level of the directory. To read from subdirectories, set `recursive=True`:

```
SimpleDirectoryReader(input_dir="path/to/directory", recursive=True)

```

### Iterating over files as they load [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/\#iterating-over-files-as-they-load "Permanent link")

You can also use the `iter_data()` method to iterate over and process files as they load

```
reader = SimpleDirectoryReader(input_dir="path/to/directory", recursive=True)
all_docs = []
for docs in reader.iter_data():
    # <do something with the documents per file>
    all_docs.extend(docs)

```

### Restricting the files loaded [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/\#restricting-the-files-loaded "Permanent link")

Instead of all files you can pass a list of file paths:

```
SimpleDirectoryReader(input_files=["path/to/file1", "path/to/file2"])

```

or you can pass a list of file paths to **exclude** using `exclude`:

```
SimpleDirectoryReader(
    input_dir="path/to/directory", exclude=["path/to/file1", "path/to/file2"]
)

```

You can also set `required_exts` to a list of file extensions to only load files with those extensions:

```
SimpleDirectoryReader(
    input_dir="path/to/directory", required_exts=[".pdf", ".docx"]
)

```

And you can set a maximum number of files to be loaded with `num_files_limit`:

```
SimpleDirectoryReader(input_dir="path/to/directory", num_files_limit=100)

```

### Specifying file encoding [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/\#specifying-file-encoding "Permanent link")

`SimpleDirectoryReader` expects files to be `utf-8` encoded but you can override this using the `encoding` parameter:

```
SimpleDirectoryReader(input_dir="path/to/directory", encoding="latin-1")

```

### Extracting metadata [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/\#extracting-metadata "Permanent link")

You can specify a function that will read each file and extract metadata that gets attached to the resulting `Document` object for each file by passing the function as `file_metadata`:

```
def get_meta(file_path):
    return {"foo": "bar", "file_path": file_path}

SimpleDirectoryReader(input_dir="path/to/directory", file_metadata=get_meta)

```

The function should take a single argument, the file path, and return a dictionary of metadata.

### Extending to other file types [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/\#extending-to-other-file-types "Permanent link")

You can extend `SimpleDirectoryReader` to read other file types by passing a dictionary of file extensions to instances of `BaseReader` as `file_extractor`. A BaseReader should read the file and return a list of Documents. For example, to add custom support for `.myfile` files :

```
from llama_index.core import SimpleDirectoryReader
from llama_index.core.readers.base import BaseReader
from llama_index.core import Document

class MyFileReader(BaseReader):
    def load_data(self, file, extra_info=None):
        with open(file, "r") as f:
            text = f.read()
        # load_data returns a list of Document objects
        return [Document(text=text + "Foobar", extra_info=extra_info or {})]

reader = SimpleDirectoryReader(
    input_dir="./data", file_extractor={".myfile": MyFileReader()}
)

documents = reader.load_data()
print(documents)

```

Note that this mapping will override the default file extractors for the file types you specify, so you'll need to add them back in if you want to support them.

### Support for External FileSystems [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/\#support-for-external-filesystems "Permanent link")

As with other modules, the `SimpleDirectoryReader` takes an optional `fs` parameter that can be used to traverse remote filesystems.

This can be any filesystem object that is implemented by the [`fsspec`](https://filesystem-spec.readthedocs.io/en/latest/) protocol.
The `fsspec` protocol has open-source implementations for a variety of remote filesystems including [AWS S3](https://github.com/fsspec/s3fs), [Azure Blob & DataLake](https://github.com/fsspec/adlfs), [Google Drive](https://github.com/fsspec/gdrivefs), [SFTP](https://github.com/fsspec/sshfs), and [many others](https://github.com/fsspec/).

Here's an example that connects to S3:

```
from s3fs import S3FileSystem

s3_fs = S3FileSystem(key="...", secret="...")
bucket_name = "my-document-bucket"

reader = SimpleDirectoryReader(
    input_dir=bucket_name,
    fs=s3_fs,
    recursive=True,  # recursively searches all subdirectories
)

documents = reader.load_data()
print(documents)

```

A full example notebook can be found [here](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/data_connectors/simple_directory_reader_remote_fs.ipynb).

Back to top
![](https://static.scarf.sh/a.png?x-pxid=2b5669c2-eb91-4d0a-81d6-dc7238350598)

[iframe](https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfESacpAAAAAIAiwrVpFehgscJonmg1gKhpKg2e&co=aHR0cHM6Ly9kb2NzLmxsYW1haW5kZXguYWk6NDQz&hl=en&v=zIriijn3uj5Vpknvt_LnfNbF&size=invisible&cb=biptj28hy7kv)


[Skip to content](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/#documents-nodes)

# Documents / Nodes [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/\#documents-nodes "Permanent link")

## Concept [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/\#concept "Permanent link")

Document and Node objects are core abstractions within LlamaIndex.

A **Document** is a generic container around any data source - for instance, a PDF, an API output, or retrieved data from a database. They can be constructed manually, or created automatically via our data loaders. By default, a Document stores text along with some other attributes. Some of these are listed below.

- `metadata` \- a dictionary of annotations that can be appended to the text.
- `relationships` \- a dictionary containing relationships to other Documents/Nodes.

_Note_: We have beta support for allowing Documents to store images, and are actively working on improving its multimodal capabilities.

A **Node** represents a "chunk" of a source Document, whether that is a text chunk, an image, or other. Similar to Documents, they contain metadata and relationship information with other nodes.

Nodes are a first-class citizen in LlamaIndex. You can choose to define Nodes and all its attributes directly. You may also choose to "parse" source Documents into Nodes through our `NodeParser` classes. By default every Node derived from a Document will inherit the same metadata from that Document (e.g. a "file\_name" filed in the Document is propagated to every Node).

## Usage Pattern [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/\#usage-pattern "Permanent link")

Here are some simple snippets to get started with Documents and Nodes.

#### Documents [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/\#documents "Permanent link")

```
from llama_index.core import Document, VectorStoreIndex

text_list = [text1, text2, ...]
documents = [Document(text=t) for t in text_list]

# build index
index = VectorStoreIndex.from_documents(documents)

```

#### Nodes [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/\#nodes "Permanent link")

```
from llama_index.core.node_parser import SentenceSplitter

# load documents
...

# parse nodes
parser = SentenceSplitter()
nodes = parser.get_nodes_from_documents(documents)

# build index
index = VectorStoreIndex(nodes)

```

### Document/Node Usage [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/\#documentnode-usage "Permanent link")

Take a look at our in-depth guides for more details on how to use Documents/Nodes.

- [Using Documents](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/)
- [Using Nodes](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_nodes/)
- [Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/)

Back to top
![](https://static.scarf.sh/a.png?x-pxid=2b5669c2-eb91-4d0a-81d6-dc7238350598)

[iframe](https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfESacpAAAAAIAiwrVpFehgscJonmg1gKhpKg2e&co=aHR0cHM6Ly9kb2NzLmxsYW1haW5kZXguYWk6NDQz&hl=en&v=zIriijn3uj5Vpknvt_LnfNbF&size=invisible&cb=v6wg2kfcga36)


[Skip to content](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/#loading-data-ingestion)

# Loading Data (Ingestion) [\#](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/\#loading-data-ingestion "Permanent link")

Before your chosen LLM can act on your data, you first need to process the data and load it. This has parallels to data cleaning/feature engineering pipelines in the ML world, or ETL pipelines in the traditional data setting.

This ingestion pipeline typically consists of three main stages:

1. Load the data
2. Transform the data
3. Index and store the data

We cover indexing/storage in [future](https://docs.llamaindex.ai/en/stable/understanding/indexing/indexing/) [sections](https://docs.llamaindex.ai/en/stable/understanding/storing/storing/). In this guide we'll mostly talk about loaders and transformations.

## Loaders [\#](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/\#loaders "Permanent link")

Before your chosen LLM can act on your data you need to load it. The way LlamaIndex does this is via data connectors, also called `Reader`. Data connectors ingest data from different data sources and format the data into `Document` objects. A `Document` is a collection of data (currently text, and in future, images and audio) and metadata about that data.

### Loading using SimpleDirectoryReader [\#](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/\#loading-using-simpledirectoryreader "Permanent link")

The easiest reader to use is our SimpleDirectoryReader, which creates documents out of every file in a given directory. It is built in to LlamaIndex and can read a variety of formats including Markdown, PDFs, Word documents, PowerPoint decks, images, audio and video.

```
from llama_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader("./data").load_data()

```

### Using Readers from LlamaHub [\#](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/\#using-readers-from-llamahub "Permanent link")

Because there are so many possible places to get data, they are not all built-in. Instead, you download them from our registry of data connectors, [LlamaHub](https://docs.llamaindex.ai/en/stable/understanding/loading/llamahub/).

In this example LlamaIndex downloads and installs the connector called [DatabaseReader](https://llamahub.ai/l/readers/llama-index-readers-database), which runs a query against a SQL database and returns every row of the results as a `Document`:

```
from llama_index.core import download_loader

from llama_index.readers.database import DatabaseReader

reader = DatabaseReader(
    scheme=os.getenv("DB_SCHEME"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    dbname=os.getenv("DB_NAME"),
)

query = "SELECT * FROM users"
documents = reader.load_data(query=query)

```

There are hundreds of connectors to use on [LlamaHub](https://llamahub.ai)!

### Creating Documents directly [\#](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/\#creating-documents-directly "Permanent link")

Instead of using a loader, you can also use a Document directly.

```
from llama_index.core import Document

doc = Document(text="text")

```

## Transformations [\#](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/\#transformations "Permanent link")

After the data is loaded, you then need to process and transform your data before putting it into a storage system. These transformations include chunking, extracting metadata, and embedding each chunk. This is necessary to make sure that the data can be retrieved, and used optimally by the LLM.

Transformation input/outputs are `Node` objects (a `Document` is a subclass of a `Node`). Transformations can also be stacked and reordered.

We have both a high-level and lower-level API for transforming documents.

### High-Level Transformation API [\#](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/\#high-level-transformation-api "Permanent link")

Indexes have a `.from_documents()` method which accepts an array of Document objects and will correctly parse and chunk them up. However, sometimes you will want greater control over how your documents are split up.

```
from llama_index.core import VectorStoreIndex

vector_index = VectorStoreIndex.from_documents(documents)
vector_index.as_query_engine()

```

Under the hood, this splits your Document into Node objects, which are similar to Documents (they contain text and metadata) but have a relationship to their parent Document.

If you want to customize core components, like the text splitter, through this abstraction you can pass in a custom `transformations` list or apply to the global `Settings`:

```
from llama_index.core.node_parser import SentenceSplitter

text_splitter = SentenceSplitter(chunk_size=512, chunk_overlap=10)

# global
from llama_index.core import Settings

Settings.text_splitter = text_splitter

# per-index
index = VectorStoreIndex.from_documents(
    documents, transformations=[text_splitter]
)

```

### Lower-Level Transformation API [\#](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/\#lower-level-transformation-api "Permanent link")

You can also define these steps explicitly.

You can do this by either using our transformation modules (text splitters, metadata extractors, etc.) as standalone components, or compose them in our declarative [Transformation Pipeline interface](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/).

Let's walk through the steps below.

#### Splitting Your Documents into Nodes [\#](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/\#splitting-your-documents-into-nodes "Permanent link")

A key step to process your documents is to split them into "chunks"/Node objects. The key idea is to process your data into bite-sized pieces that can be retrieved / fed to the LLM.

LlamaIndex has support for a wide range of [text splitters](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/), ranging from paragraph/sentence/token based splitters to file-based splitters like HTML, JSON.

These can be [used on their own or as part of an ingestion pipeline](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/).

```
from llama_index.core import SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import TokenTextSplitter

documents = SimpleDirectoryReader("./data").load_data()

pipeline = IngestionPipeline(transformations=[TokenTextSplitter(), ...])

nodes = pipeline.run(documents=documents)

```

### Adding Metadata [\#](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/\#adding-metadata "Permanent link")

You can also choose to add metadata to your documents and nodes. This can be done either manually or with [automatic metadata extractors](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_metadata_extractor/).

Here are guides on 1) [how to customize Documents](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/), and 2) [how to customize Nodes](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_nodes/).

```
document = Document(
    text="text",
    metadata={"filename": "<doc_file_name>", "category": "<category>"},
)

```

### Adding Embeddings [\#](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/\#adding-embeddings "Permanent link")

To insert a node into a vector index, it should have an embedding. See our [ingestion pipeline](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/) or our [embeddings guide](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/) for more details.

### Creating and passing Nodes directly [\#](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/\#creating-and-passing-nodes-directly "Permanent link")

If you want to, you can create nodes directly and pass a list of Nodes directly to an indexer:

```
from llama_index.core.schema import TextNode

node1 = TextNode(text="<text_chunk>", id_="<node_id>")
node2 = TextNode(text="<text_chunk>", id_="<node_id>")

index = VectorStoreIndex([node1, node2])

```

Back to top
![](https://static.scarf.sh/a.png?x-pxid=2b5669c2-eb91-4d0a-81d6-dc7238350598)

[iframe](https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfESacpAAAAAIAiwrVpFehgscJonmg1gKhpKg2e&co=aHR0cHM6Ly9kb2NzLmxsYW1haW5kZXguYWk6NDQz&hl=en&v=zIriijn3uj5Vpknvt_LnfNbF&size=invisible&cb=v30htydman0)


[Skip to content](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/#defining-and-customizing-documents)

# Defining and Customizing Documents [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/\#defining-and-customizing-documents "Permanent link")

## Defining Documents [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/\#defining-documents "Permanent link")

Documents can either be created automatically via data loaders, or constructed manually.

By default, all of our [data loaders](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/) (including those offered on LlamaHub) return `Document` objects through the `load_data` function.

```
from llama_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader("./data").load_data()

```

You can also choose to construct documents manually. LlamaIndex exposes the `Document` struct.

```
from llama_index.core import Document

text_list = [text1, text2, ...]
documents = [Document(text=t) for t in text_list]

```

To speed up prototyping and development, you can also quickly create a document using some default text:

```
document = Document.example()

```

## Customizing Documents [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/\#customizing-documents "Permanent link")

This section covers various ways to customize `Document` objects. Since the `Document` object is a subclass of our `TextNode` object, all these settings and details apply to the `TextNode` object class as well.

### Metadata [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/\#metadata "Permanent link")

Documents also offer the chance to include useful metadata. Using the `metadata` dictionary on each document, additional information can be included to help inform responses and track down sources for query responses. This information can be anything, such as filenames or categories. If you are integrating with a vector database, keep in mind that some vector databases require that the keys must be strings, and the values must be flat (either `str`, `float`, or `int`).

Any information set in the `metadata` dictionary of each document will show up in the `metadata` of each source node created from the document. Additionally, this information is included in the nodes, enabling the index to utilize it on queries and responses. By default, the metadata is injected into the text for both embedding and LLM model calls.

There are a few ways to set up this dictionary:

1. In the document constructor:

```
document = Document(
    text="text",
    metadata={"filename": "<doc_file_name>", "category": "<category>"},
)

```

1. After the document is created:

```
document.metadata = {"filename": "<doc_file_name>"}

```

1. Set the filename automatically using the `SimpleDirectoryReader` and `file_metadata` hook. This will automatically run the hook on each document to set the `metadata` field:

```
from llama_index.core import SimpleDirectoryReader

filename_fn = lambda filename: {"file_name": filename}

# automatically sets the metadata of each document according to filename_fn
documents = SimpleDirectoryReader(
    "./data", file_metadata=filename_fn
).load_data()

```

### Customizing the id [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/\#customizing-the-id "Permanent link")

As detailed in the section [Document Management](https://docs.llamaindex.ai/en/stable/module_guides/indexing/document_management/), the `doc_id` is used to enable efficient refreshing of documents in the index. When using the `SimpleDirectoryReader`, you can automatically set the doc `doc_id` to be the full path to each document:

```
from llama_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader("./data", filename_as_id=True).load_data()
print([x.doc_id for x in documents])

```

You can also set the `doc_id` of any `Document` directly!

```
document.doc_id = "My new document id!"

```

Note: the ID can also be set through the `node_id` or `id_` property on a Document object, similar to a `TextNode` object.

### Advanced - Metadata Customization [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/\#advanced-metadata-customization "Permanent link")

A key detail mentioned above is that by default, any metadata you set is included in the embeddings generation and LLM.

#### Customizing LLM Metadata Text [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/\#customizing-llm-metadata-text "Permanent link")

Typically, a document might have many metadata keys, but you might not want all of them visible to the LLM during response synthesis. In the above examples, we may not want the LLM to read the `file_name` of our document. However, the `file_name` might include information that will help generate better embeddings. A key advantage of doing this is to bias the embeddings for retrieval without changing what the LLM ends up reading.

We can exclude it like so:

```
document.excluded_llm_metadata_keys = ["file_name"]

```

Then, we can test what the LLM will actually end up reading using the `get_content()` function and specifying `MetadataMode.LLM`:

```
from llama_index.core.schema import MetadataMode

print(document.get_content(metadata_mode=MetadataMode.LLM))

```

#### Customizing Embedding Metadata Text [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/\#customizing-embedding-metadata-text "Permanent link")

Similar to customing the metadata visible to the LLM, we can also customize the metadata visible to embeddings. In this case, you can specifically exclude metadata visible to the embedding model, in case you DON'T want particular text to bias the embeddings.

```
document.excluded_embed_metadata_keys = ["file_name"]

```

Then, we can test what the embedding model will actually end up reading using the `get_content()` function and specifying `MetadataMode.EMBED`:

```
from llama_index.core.schema import MetadataMode

print(document.get_content(metadata_mode=MetadataMode.EMBED))

```

#### Customizing Metadata Format [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/\#customizing-metadata-format "Permanent link")

As you know by now, metadata is injected into the actual text of each document/node when sent to the LLM or embedding model. By default, the format of this metadata is controlled by three attributes:

1. `Document.metadata_seperator` -\> default = `"\n"`

When concatenating all key/value fields of your metadata, this field controls the separator between each key/value pair.

1. `Document.metadata_template` -\> default = `"{key}: {value}"`

This attribute controls how each key/value pair in your metadata is formatted. The two variables `key` and `value` string keys are required.

1. `Document.text_template` -\> default = `{metadata_str}\n\n{content}`

Once your metadata is converted into a string using `metadata_seperator` and `metadata_template`, this templates controls what that metadata looks like when joined with the text content of your document/node. The `metadata` and `content` string keys are required.

### Summary [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/\#summary "Permanent link")

Knowing all this, let's create a short example using all this power:

```
from llama_index.core import Document
from llama_index.core.schema import MetadataMode

document = Document(
    text="This is a super-customized document",
    metadata={
        "file_name": "super_secret_document.txt",
        "category": "finance",
        "author": "LlamaIndex",
    },
    excluded_llm_metadata_keys=["file_name"],
    metadata_seperator="::",
    metadata_template="{key}=>{value}",
    text_template="Metadata: {metadata_str}\n-----\nContent: {content}",
)

print(
    "The LLM sees this: \n",
    document.get_content(metadata_mode=MetadataMode.LLM),
)
print(
    "The Embedding model sees this: \n",
    document.get_content(metadata_mode=MetadataMode.EMBED),
)

```

### Advanced - Automatic Metadata Extraction [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/\#advanced-automatic-metadata-extraction "Permanent link")

We have [initial examples](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_metadata_extractor/) of using LLMs themselves to perform metadata extraction.

Back to top
![](https://static.scarf.sh/a.png?x-pxid=2b5669c2-eb91-4d0a-81d6-dc7238350598)

[iframe](https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfESacpAAAAAIAiwrVpFehgscJonmg1gKhpKg2e&co=aHR0cHM6Ly9kb2NzLmxsYW1haW5kZXguYWk6NDQz&hl=en&v=zIriijn3uj5Vpknvt_LnfNbF&size=invisible&cb=65kxs0m4oboo)


[Skip to content](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_nodes/#defining-and-customizing-nodes)

# Defining and Customizing Nodes [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_nodes/\#defining-and-customizing-nodes "Permanent link")

Nodes represent "chunks" of source Documents, whether that is a text chunk, an image, or more. They also contain metadata and relationship information
with other nodes and index structures.

Nodes are a first-class citizen in LlamaIndex. You can choose to define Nodes and all its attributes directly. You may also choose to "parse" source Documents into Nodes through our `NodeParser` classes.

For instance, you can do

```
from llama_index.core.node_parser import SentenceSplitter

parser = SentenceSplitter()

nodes = parser.get_nodes_from_documents(documents)

```

You can also choose to construct Node objects manually and skip the first section. For instance,

```
from llama_index.core.schema import TextNode, NodeRelationship, RelatedNodeInfo

node1 = TextNode(text="<text_chunk>", id_="<node_id>")
node2 = TextNode(text="<text_chunk>", id_="<node_id>")
# set relationships
node1.relationships[NodeRelationship.NEXT] = RelatedNodeInfo(
    node_id=node2.node_id
)
node2.relationships[NodeRelationship.PREVIOUS] = RelatedNodeInfo(
    node_id=node1.node_id
)
nodes = [node1, node2]

```

The `RelatedNodeInfo` class can also store additional `metadata` if needed:

```
node2.relationships[NodeRelationship.PARENT] = RelatedNodeInfo(
    node_id=node1.node_id, metadata={"key": "val"}
)

```

### Customizing the ID [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_nodes/\#customizing-the-id "Permanent link")

Each node has an `node_id` property that is automatically generated if not manually specified. This ID can be used for
a variety of purposes; this includes being able to update nodes in storage, being able to define relationships
between nodes (through `IndexNode`), and more.

You can also get and set the `node_id` of any `TextNode` directly.

```
print(node.node_id)
node.node_id = "My new node_id!"

```

Back to top
![](https://static.scarf.sh/a.png?x-pxid=2b5669c2-eb91-4d0a-81d6-dc7238350598)

[iframe](https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfESacpAAAAAIAiwrVpFehgscJonmg1gKhpKg2e&co=aHR0cHM6Ly9kb2NzLmxsYW1haW5kZXguYWk6NDQz&hl=en&v=zIriijn3uj5Vpknvt_LnfNbF&size=invisible&cb=jirrr3omkdkx)


[Skip to content](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/#data-connectors-llamahub)

# Data Connectors (LlamaHub) [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/\#data-connectors-llamahub "Permanent link")

## Concept [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/\#concept "Permanent link")

A data connector (aka `Reader`) ingest data from different data sources and data formats into a simple `Document` representation (text and simple metadata).

Tip

Once you've ingested your data, you can build an [Index](https://docs.llamaindex.ai/en/stable/module_guides/indexing/) on top, ask questions using a [Query Engine](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/), and have a conversation using a [Chat Engine](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/).

## LlamaHub [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/\#llamahub "Permanent link")

Our data connectors are offered through [LlamaHub](https://llamahub.ai/) 🦙.
LlamaHub is an open-source repository containing data loaders that you can easily plug and play into any LlamaIndex application.

![](https://docs.llamaindex.ai/en/stable/_static/data_connectors/llamahub.png)

## Usage Pattern [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/\#usage-pattern "Permanent link")

Get started with:

```
from llama_index.core import download_loader

from llama_index.readers.google import GoogleDocsReader

loader = GoogleDocsReader()
documents = loader.load_data(document_ids=[...])

```

See the full [usage pattern guide](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/usage_pattern/) for more details.

## Modules [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/\#modules "Permanent link")

Some sample data connectors:

- local file directory ( `SimpleDirectoryReader`). Can support parsing a wide range of file types: `.pdf`, `.jpg`, `.png`, `.docx`, etc.
- [Notion](https://developers.notion.com/) ( `NotionPageReader`)
- [Google Docs](https://developers.google.com/docs/api) ( `GoogleDocsReader`)
- [Slack](https://api.slack.com/) ( `SlackReader`)
- [Discord](https://discord.com/developers/docs/intro) ( `DiscordReader`)
- [Apify Actors](https://llamahub.ai/l/readers/llama-index-readers-apify) ( `ApifyActor`). Can crawl the web, scrape webpages, extract text content, download files including `.pdf`, `.jpg`, `.png`, `.docx`, etc.

See the [modules guide](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/modules/) for more details.

Back to top
![](https://static.scarf.sh/a.png?x-pxid=2b5669c2-eb91-4d0a-81d6-dc7238350598)

[iframe](https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfESacpAAAAAIAiwrVpFehgscJonmg1gKhpKg2e&co=aHR0cHM6Ly9kb2NzLmxsYW1haW5kZXguYWk6NDQz&hl=en&v=zIriijn3uj5Vpknvt_LnfNbF&size=invisible&cb=2ugczuf9ukgg)


[Skip to content](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/#extracting-metadata-for-better-document-indexing-and-understanding)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/metadata_extraction/MetadataExtractionSEC.ipynb)

# Extracting Metadata for Better Document Indexing and Understanding [¶](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/\#extracting-metadata-for-better-document-indexing-and-understanding)

In many cases, especially with long documents, a chunk of text may lack the context necessary to disambiguate the chunk from other similar chunks of text. One method of addressing this is manually labelling each chunk in our dataset or knowledge base. However, this can be labour intensive and time consuming for a large number or continually updated set of documents.

To combat this, we use LLMs to extract certain contextual information relevant to the document to better help the retrieval and language models disambiguate similar-looking passages.

We do this through our brand-new `Metadata Extractor` modules.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

```
%pip install llama-index-llms-openai
%pip install llama-index-extractors-entity

```

%pip install llama-index-llms-openai
%pip install llama-index-extractors-entity

In \[ \]:

Copied!

```
!pip install llama-index

```

!pip install llama-index

In \[ \]:

Copied!

```
import nest_asyncio

nest_asyncio.apply()

import os
import openai

os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY_HERE"

```

import nest\_asyncio

nest\_asyncio.apply()

import os
import openai

os.environ\["OPENAI\_API\_KEY"\] = "YOUR\_API\_KEY\_HERE"

In \[ \]:

Copied!

```
from llama_index.llms.openai import OpenAI
from llama_index.core.schema import MetadataMode

```

from llama\_index.llms.openai import OpenAI
from llama\_index.core.schema import MetadataMode

In \[ \]:

Copied!

```
llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo", max_tokens=512)

```

llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo", max\_tokens=512)

We create a node parser that extracts the document title and hypothetical question embeddings relevant to the document chunk.

We also show how to instantiate the `SummaryExtractor` and `KeywordExtractor`, as well as how to create your own custom extractor
based on the `BaseExtractor` base class

In \[ \]:

Copied!

```
from llama_index.core.extractors import (
    SummaryExtractor,
    QuestionsAnsweredExtractor,
    TitleExtractor,
    KeywordExtractor,
    BaseExtractor,
)
from llama_index.extractors.entity import EntityExtractor
from llama_index.core.node_parser import TokenTextSplitter

text_splitter = TokenTextSplitter(
    separator=" ", chunk_size=512, chunk_overlap=128
)

class CustomExtractor(BaseExtractor):
    def extract(self, nodes):
        metadata_list = [\
            {\
                "custom": (\
                    node.metadata["document_title"]\
                    + "\n"\
                    + node.metadata["excerpt_keywords"]\
                )\
            }\
            for node in nodes\
        ]
        return metadata_list

extractors = [\
    TitleExtractor(nodes=5, llm=llm),\
    QuestionsAnsweredExtractor(questions=3, llm=llm),\
    # EntityExtractor(prediction_threshold=0.5),\
    # SummaryExtractor(summaries=["prev", "self"], llm=llm),\
    # KeywordExtractor(keywords=10, llm=llm),\
    # CustomExtractor()\
]

transformations = [text_splitter] + extractors

```

from llama\_index.core.extractors import (
SummaryExtractor,
QuestionsAnsweredExtractor,
TitleExtractor,
KeywordExtractor,
BaseExtractor,
)
from llama\_index.extractors.entity import EntityExtractor
from llama\_index.core.node\_parser import TokenTextSplitter

text\_splitter = TokenTextSplitter(
separator=" ", chunk\_size=512, chunk\_overlap=128
)

class CustomExtractor(BaseExtractor):
def extract(self, nodes):
metadata\_list = \[\
{\
"custom": (\
node.metadata\["document\_title"\]\
\+ "\\n"\
\+ node.metadata\["excerpt\_keywords"\]\
)\
}\
for node in nodes\
\]
return metadata\_list

extractors = \[\
TitleExtractor(nodes=5, llm=llm),\
QuestionsAnsweredExtractor(questions=3, llm=llm),\
# EntityExtractor(prediction\_threshold=0.5),\
# SummaryExtractor(summaries=\["prev", "self"\], llm=llm),\
# KeywordExtractor(keywords=10, llm=llm),\
# CustomExtractor()\
\]

transformations = \[text\_splitter\] + extractors

In \[ \]:

Copied!

```
from llama_index.core import SimpleDirectoryReader

```

from llama\_index.core import SimpleDirectoryReader

We first load the 10k annual SEC report for Uber and Lyft for the years 2019 and 2020 respectively.

In \[ \]:

Copied!

```
!mkdir -p data
!wget -O "data/10k-132.pdf" "https://www.dropbox.com/scl/fi/6dlqdk6e2k1mjhi8dee5j/uber.pdf?rlkey=2jyoe49bg2vwdlz30l76czq6g&dl=1"
!wget -O "data/10k-vFinal.pdf" "https://www.dropbox.com/scl/fi/qn7g3vrk5mqb18ko4e5in/lyft.pdf?rlkey=j6jxtjwo8zbstdo4wz3ns8zoj&dl=1"

```

!mkdir -p data
!wget -O "data/10k-132.pdf" "https://www.dropbox.com/scl/fi/6dlqdk6e2k1mjhi8dee5j/uber.pdf?rlkey=2jyoe49bg2vwdlz30l76czq6g&dl=1"
!wget -O "data/10k-vFinal.pdf" "https://www.dropbox.com/scl/fi/qn7g3vrk5mqb18ko4e5in/lyft.pdf?rlkey=j6jxtjwo8zbstdo4wz3ns8zoj&dl=1"

In \[ \]:

Copied!

```
# Note the uninformative document file name, which may be a common scenario in a production setting
uber_docs = SimpleDirectoryReader(input_files=["data/10k-132.pdf"]).load_data()
uber_front_pages = uber_docs[0:3]
uber_content = uber_docs[63:69]
uber_docs = uber_front_pages + uber_content

```

\# Note the uninformative document file name, which may be a common scenario in a production setting
uber\_docs = SimpleDirectoryReader(input\_files=\["data/10k-132.pdf"\]).load\_data()
uber\_front\_pages = uber\_docs\[0:3\]
uber\_content = uber\_docs\[63:69\]
uber\_docs = uber\_front\_pages + uber\_content

In \[ \]:

Copied!

```
from llama_index.core.ingestion import IngestionPipeline

pipeline = IngestionPipeline(transformations=transformations)

uber_nodes = pipeline.run(documents=uber_docs)

```

from llama\_index.core.ingestion import IngestionPipeline

pipeline = IngestionPipeline(transformations=transformations)

uber\_nodes = pipeline.run(documents=uber\_docs)

In \[ \]:

Copied!

```
uber_nodes[1].metadata

```

uber\_nodes\[1\].metadata

Out\[ \]:

```
{'page_label': '2',
 'file_name': '10k-132.pdf',
 'document_title': 'Exploring the Diverse Landscape of 2019: A Comprehensive Annual Report on Uber Technologies, Inc.',
 'questions_this_excerpt_can_answer': '1. How many countries does Uber operate in?\n2. What is the total gross bookings of Uber in 2019?\n3. How many trips did Uber facilitate in 2019?'}
```

In \[ \]:

Copied!

```
# Note the uninformative document file name, which may be a common scenario in a production setting
lyft_docs = SimpleDirectoryReader(
    input_files=["data/10k-vFinal.pdf"]
).load_data()
lyft_front_pages = lyft_docs[0:3]
lyft_content = lyft_docs[68:73]
lyft_docs = lyft_front_pages + lyft_content

```

\# Note the uninformative document file name, which may be a common scenario in a production setting
lyft\_docs = SimpleDirectoryReader(
input\_files=\["data/10k-vFinal.pdf"\]
).load\_data()
lyft\_front\_pages = lyft\_docs\[0:3\]
lyft\_content = lyft\_docs\[68:73\]
lyft\_docs = lyft\_front\_pages + lyft\_content

In \[ \]:

Copied!

```
from llama_index.core.ingestion import IngestionPipeline

pipeline = IngestionPipeline(transformations=transformations)

lyft_nodes = pipeline.run(documents=lyft_docs)

```

from llama\_index.core.ingestion import IngestionPipeline

pipeline = IngestionPipeline(transformations=transformations)

lyft\_nodes = pipeline.run(documents=lyft\_docs)

In \[ \]:

Copied!

```
lyft_nodes[2].metadata

```

lyft\_nodes\[2\].metadata

Out\[ \]:

```
{'page_label': '2',
 'file_name': '10k-vFinal.pdf',
 'document_title': 'Lyft, Inc. Annual Report on Form 10-K for the Fiscal Year Ended December 31, 2020',
 'questions_this_excerpt_can_answer': "1. Has Lyft, Inc. filed a report on and attestation to its management's assessment of the effectiveness of its internal control over financial reporting under Section 404(b) of the Sarbanes-Oxley Act?\n2. Is Lyft, Inc. considered a shell company according to Rule 12b-2 of the Exchange Act?\n3. What was the aggregate market value of Lyft, Inc.'s common stock held by non-affiliates on June 30, 2020?"}
```

Since we are asking fairly sophisticated questions, we utilize a subquestion query engine for all QnA pipelines below, and prompt it to pay more attention to the relevance of the retrieved sources.

In \[ \]:

Copied!

```
from llama_index.core.question_gen import LLMQuestionGenerator
from llama_index.core.question_gen.prompts import (
    DEFAULT_SUB_QUESTION_PROMPT_TMPL,
)

question_gen = LLMQuestionGenerator.from_defaults(
    llm=llm,
    prompt_template_str="""
        Follow the example, but instead of giving a question, always prefix the question
        with: 'By first identifying and quoting the most relevant sources, '.
        """
    + DEFAULT_SUB_QUESTION_PROMPT_TMPL,
)

```

from llama\_index.core.question\_gen import LLMQuestionGenerator
from llama\_index.core.question\_gen.prompts import (
DEFAULT\_SUB\_QUESTION\_PROMPT\_TMPL,
)

question\_gen = LLMQuestionGenerator.from\_defaults(
llm=llm,
prompt\_template\_str="""
Follow the example, but instead of giving a question, always prefix the question
with: 'By first identifying and quoting the most relevant sources, '.
"""
\+ DEFAULT\_SUB\_QUESTION\_PROMPT\_TMPL,
)

## Querying an Index With No Extra Metadata [¶](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/\#querying-an-index-with-no-extra-metadata)

In \[ \]:

Copied!

```
from copy import deepcopy

nodes_no_metadata = deepcopy(uber_nodes) + deepcopy(lyft_nodes)
for node in nodes_no_metadata:
    node.metadata = {
        k: node.metadata[k]
        for k in node.metadata
        if k in ["page_label", "file_name"]
    }
print(
    "LLM sees:\n",
    (nodes_no_metadata)[9].get_content(metadata_mode=MetadataMode.LLM),
)

```

from copy import deepcopy

nodes\_no\_metadata = deepcopy(uber\_nodes) + deepcopy(lyft\_nodes)
for node in nodes\_no\_metadata:
node.metadata = {
k: node.metadata\[k\]
for k in node.metadata
if k in \["page\_label", "file\_name"\]
}
print(
"LLM sees:\\n",
(nodes\_no\_metadata)\[9\].get\_content(metadata\_mode=MetadataMode.LLM),
)

```
LLM sees:
 [Excerpt from document]
page_label: 65
file_name: 10k-132.pdf
Excerpt:
-----
See the section titled “Reconciliations of Non-GAAP Financial Measures” for our definition and a
reconciliation of net income (loss) attributable to  Uber Technologies, Inc. to Adjusted EBITDA.

  Year Ended December 31,   2017 to 2018   2018 to 2019
(In millions, exce pt percenta ges)  2017   2018   2019   % Chan ge  % Chan ge
Adjusted EBITDA ................................  $ (2,642) $ (1,847) $ (2,725)  30%  (48)%
-----

```

In \[ \]:

Copied!

```
from llama_index.core import VectorStoreIndex
from llama_index.core.query_engine import SubQuestionQueryEngine
from llama_index.core.tools import QueryEngineTool, ToolMetadata

```

from llama\_index.core import VectorStoreIndex
from llama\_index.core.query\_engine import SubQuestionQueryEngine
from llama\_index.core.tools import QueryEngineTool, ToolMetadata

In \[ \]:

Copied!

```
index_no_metadata = VectorStoreIndex(
    nodes=nodes_no_metadata,
)
engine_no_metadata = index_no_metadata.as_query_engine(
    similarity_top_k=10, llm=OpenAI(model="gpt-4")
)

```

index\_no\_metadata = VectorStoreIndex(
nodes=nodes\_no\_metadata,
)
engine\_no\_metadata = index\_no\_metadata.as\_query\_engine(
similarity\_top\_k=10, llm=OpenAI(model="gpt-4")
)

In \[ \]:

Copied!

```
final_engine_no_metadata = SubQuestionQueryEngine.from_defaults(
    query_engine_tools=[\
        QueryEngineTool(\
            query_engine=engine_no_metadata,\
            metadata=ToolMetadata(\
                name="sec_filing_documents",\
                description="financial information on companies",\
            ),\
        )\
    ],
    question_gen=question_gen,
    use_async=True,
)

```

final\_engine\_no\_metadata = SubQuestionQueryEngine.from\_defaults(
query\_engine\_tools=\[\
QueryEngineTool(\
query\_engine=engine\_no\_metadata,\
metadata=ToolMetadata(\
name="sec\_filing\_documents",\
description="financial information on companies",\
),\
)\
\],
question\_gen=question\_gen,
use\_async=True,
)

In \[ \]:

Copied!

```
response_no_metadata = final_engine_no_metadata.query(
    """
    What was the cost due to research and development v.s. sales and marketing for uber and lyft in 2019 in millions of USD?
    Give your answer as a JSON.
    """
)
print(response_no_metadata.response)
# Correct answer:
# {"Uber": {"Research and Development": 4836, "Sales and Marketing": 4626},
#  "Lyft": {"Research and Development": 1505.6, "Sales and Marketing": 814 }}

```

response\_no\_metadata = final\_engine\_no\_metadata.query(
"""
What was the cost due to research and development v.s. sales and marketing for uber and lyft in 2019 in millions of USD?
Give your answer as a JSON.
"""
)
print(response\_no\_metadata.response)
\# Correct answer:
\# {"Uber": {"Research and Development": 4836, "Sales and Marketing": 4626},
\# "Lyft": {"Research and Development": 1505.6, "Sales and Marketing": 814 }}

```
Generated 4 sub questions.
[sec_filing_documents] Q: What was the cost due to research and development for Uber in 2019
[sec_filing_documents] Q: What was the cost due to sales and marketing for Uber in 2019
[sec_filing_documents] Q: What was the cost due to research and development for Lyft in 2019
[sec_filing_documents] Q: What was the cost due to sales and marketing for Lyft in 2019
[sec_filing_documents] A: The cost due to sales and marketing for Uber in 2019 was $814,122 in thousands.
[sec_filing_documents] A: The cost due to research and development for Uber in 2019 was $1,505,640 in thousands.
[sec_filing_documents] A: The cost of research and development for Lyft in 2019 was $1,505,640 in thousands.
[sec_filing_documents] A: The cost due to sales and marketing for Lyft in 2019 was $814,122 in thousands.
{
  "Uber": {
    "Research and Development": 1505.64,
    "Sales and Marketing": 814.122
  },
  "Lyft": {
    "Research and Development": 1505.64,
    "Sales and Marketing": 814.122
  }
}

```

**RESULT**: As we can see, the QnA agent does not seem to know where to look for the right documents. As a result it gets the Lyft and Uber data completely mixed up.

## Querying an Index With Extracted Metadata [¶](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/\#querying-an-index-with-extracted-metadata)

In \[ \]:

Copied!

```
print(
    "LLM sees:\n",
    (uber_nodes + lyft_nodes)[9].get_content(metadata_mode=MetadataMode.LLM),
)

```

print(
"LLM sees:\\n",
(uber\_nodes + lyft\_nodes)\[9\].get\_content(metadata\_mode=MetadataMode.LLM),
)

```
LLM sees:
 [Excerpt from document]
page_label: 65
file_name: 10k-132.pdf
document_title: Exploring the Diverse Landscape of 2019: A Comprehensive Annual Report on Uber Technologies, Inc.
Excerpt:
-----
See the section titled “Reconciliations of Non-GAAP Financial Measures” for our definition and a
reconciliation of net income (loss) attributable to  Uber Technologies, Inc. to Adjusted EBITDA.

  Year Ended December 31,   2017 to 2018   2018 to 2019
(In millions, exce pt percenta ges)  2017   2018   2019   % Chan ge  % Chan ge
Adjusted EBITDA ................................  $ (2,642) $ (1,847) $ (2,725)  30%  (48)%
-----

```

In \[ \]:

Copied!

```
index = VectorStoreIndex(
    nodes=uber_nodes + lyft_nodes,
)
engine = index.as_query_engine(similarity_top_k=10, llm=OpenAI(model="gpt-4"))

```

index = VectorStoreIndex(
nodes=uber\_nodes + lyft\_nodes,
)
engine = index.as\_query\_engine(similarity\_top\_k=10, llm=OpenAI(model="gpt-4"))

In \[ \]:

Copied!

```
final_engine = SubQuestionQueryEngine.from_defaults(
    query_engine_tools=[\
        QueryEngineTool(\
            query_engine=engine,\
            metadata=ToolMetadata(\
                name="sec_filing_documents",\
                description="financial information on companies.",\
            ),\
        )\
    ],
    question_gen=question_gen,
    use_async=True,
)

```

final\_engine = SubQuestionQueryEngine.from\_defaults(
query\_engine\_tools=\[\
QueryEngineTool(\
query\_engine=engine,\
metadata=ToolMetadata(\
name="sec\_filing\_documents",\
description="financial information on companies.",\
),\
)\
\],
question\_gen=question\_gen,
use\_async=True,
)

In \[ \]:

Copied!

```
response = final_engine.query(
    """
    What was the cost due to research and development v.s. sales and marketing for uber and lyft in 2019 in millions of USD?
    Give your answer as a JSON.
    """
)
print(response.response)
# Correct answer:
# {"Uber": {"Research and Development": 4836, "Sales and Marketing": 4626},
#  "Lyft": {"Research and Development": 1505.6, "Sales and Marketing": 814 }}

```

response = final\_engine.query(
"""
What was the cost due to research and development v.s. sales and marketing for uber and lyft in 2019 in millions of USD?
Give your answer as a JSON.
"""
)
print(response.response)
\# Correct answer:
\# {"Uber": {"Research and Development": 4836, "Sales and Marketing": 4626},
\# "Lyft": {"Research and Development": 1505.6, "Sales and Marketing": 814 }}

```
Generated 4 sub questions.
[sec_filing_documents] Q: What was the cost due to research and development for Uber in 2019
[sec_filing_documents] Q: What was the cost due to sales and marketing for Uber in 2019
[sec_filing_documents] Q: What was the cost due to research and development for Lyft in 2019
[sec_filing_documents] Q: What was the cost due to sales and marketing for Lyft in 2019
[sec_filing_documents] A: The cost due to sales and marketing for Uber in 2019 was $4,626 million.
[sec_filing_documents] A: The cost due to research and development for Uber in 2019 was $4,836 million.
[sec_filing_documents] A: The cost due to sales and marketing for Lyft in 2019 was $814,122 in thousands.
[sec_filing_documents] A: The cost of research and development for Lyft in 2019 was $1,505,640 in thousands.
{
  "Uber": {
    "Research and Development": 4836,
    "Sales and Marketing": 4626
  },
  "Lyft": {
    "Research and Development": 1505.64,
    "Sales and Marketing": 814.122
  }
}

```

**RESULT**: As we can see, the LLM answers the questions correctly.

### Challenges Identified in the Problem Domain [¶](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/\#challenges-identified-in-the-problem-domain)

In this example, we observed that the search quality as provided by vector embeddings was rather poor. This was likely due to highly dense financial documents that were likely not representative of the training set for the model.

In order to improve the search quality, other methods of neural search that employ more keyword-based approaches may help, such as ColBERTv2/PLAID. In particular, this would help in matching on particular keywords to identify high-relevance chunks.

Other valid steps may include utilizing models that are fine-tuned on financial datasets such as Bloomberg GPT.

Finally, we can help to further enrich the metadata by providing more contextual information regarding the surrounding context that the chunk is located in.

### Improvements to this Example [¶](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/\#improvements-to-this-example)

Generally, this example can be improved further with more rigorous evaluation of both the metadata extraction accuracy, and the accuracy and recall of the QnA pipeline. Further, incorporating a larger set of documents as well as the full length documents, which may provide more confounding passages that are difficult to disambiguate, could further stresss test the system we have built and suggest further improvements.

Back to top
![](https://static.scarf.sh/a.png?x-pxid=2b5669c2-eb91-4d0a-81d6-dc7238350598)

[iframe](https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfESacpAAAAAIAiwrVpFehgscJonmg1gKhpKg2e&co=aHR0cHM6Ly9kb2NzLmxsYW1haW5kZXguYWk6NDQz&hl=en&v=zIriijn3uj5Vpknvt_LnfNbF&size=invisible&cb=53zm16sz9xvg)


[Skip to content](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/#ingestion-pipeline)

# Ingestion Pipeline [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/\#ingestion-pipeline "Permanent link")

An `IngestionPipeline` uses a concept of `Transformations` that are applied to input data. These `Transformations` are applied to your input data, and the resulting nodes are either returned or inserted into a vector database (if given). Each node+transformation pair is cached, so that subsequent runs (if the cache is persisted) with the same node+transformation combination can use the cached result and save you time.

To see an interactive example of `IngestionPipeline` being put in use, check out the [RAG CLI](https://docs.llamaindex.ai/en/stable/getting_started/starter_tools/rag_cli/).

## Usage Pattern [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/\#usage-pattern "Permanent link")

The simplest usage is to instantiate an `IngestionPipeline` like so:

```
from llama_index.core import Document
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor
from llama_index.core.ingestion import IngestionPipeline, IngestionCache

# create the pipeline with transformations
pipeline = IngestionPipeline(
    transformations=[\
        SentenceSplitter(chunk_size=25, chunk_overlap=0),\
        TitleExtractor(),\
        OpenAIEmbedding(),\
    ]
)

# run the pipeline
nodes = pipeline.run(documents=[Document.example()])

```

Note that in a real-world scenario, you would get your documents from `SimpleDirectoryReader` or another reader from Llama Hub.

## Connecting to Vector Databases [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/\#connecting-to-vector-databases "Permanent link")

When running an ingestion pipeline, you can also chose to automatically insert the resulting nodes into a remote vector store.

Then, you can construct an index from that vector store later on.

```
from llama_index.core import Document
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor
from llama_index.core.ingestion import IngestionPipeline
from llama_index.vector_stores.qdrant import QdrantVectorStore

import qdrant_client

client = qdrant_client.QdrantClient(location=":memory:")
vector_store = QdrantVectorStore(client=client, collection_name="test_store")

pipeline = IngestionPipeline(
    transformations=[\
        SentenceSplitter(chunk_size=25, chunk_overlap=0),\
        TitleExtractor(),\
        OpenAIEmbedding(),\
    ],
    vector_store=vector_store,
)

# Ingest directly into a vector db
pipeline.run(documents=[Document.example()])

# Create your index
from llama_index.core import VectorStoreIndex

index = VectorStoreIndex.from_vector_store(vector_store)

```

## Calculating embeddings in a pipeline [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/\#calculating-embeddings-in-a-pipeline "Permanent link")

Note that in the above example, embeddings are calculated as part of the pipeline. If you are connecting your pipeline to a vector store, embeddings must be a stage of your pipeline or your later instantiation of the index will fail.

You can omit embeddings from your pipeline if you are not connecting to a vector store, i.e. just producing a list of nodes.

## Caching [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/\#caching "Permanent link")

In an `IngestionPipeline`, each node + transformation combination is hashed and cached. This saves time on subsequent runs that use the same data.

The following sections describe some basic usage around caching.

### Local Cache Management [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/\#local-cache-management "Permanent link")

Once you have a pipeline, you may want to store and load the cache.

```
# save
pipeline.persist("./pipeline_storage")

# load and restore state
new_pipeline = IngestionPipeline(
    transformations=[\
        SentenceSplitter(chunk_size=25, chunk_overlap=0),\
        TitleExtractor(),\
    ],
)
new_pipeline.load("./pipeline_storage")

# will run instantly due to the cache
nodes = pipeline.run(documents=[Document.example()])

```

If the cache becomes too large, you can clear it

```
# delete all context of the cache
cache.clear()

```

### Remote Cache Management [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/\#remote-cache-management "Permanent link")

We support multiple remote storage backends for caches

- `RedisCache`
- `MongoDBCache`
- `FirestoreCache`

Here as an example using the `RedisCache`:

```
from llama_index.core import Document
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor
from llama_index.core.ingestion import IngestionPipeline, IngestionCache
from llama_index.storage.kvstore.redis import RedisKVStore as RedisCache

ingest_cache = IngestionCache(
    cache=RedisCache.from_host_and_port(host="127.0.0.1", port=6379),
    collection="my_test_cache",
)

pipeline = IngestionPipeline(
    transformations=[\
        SentenceSplitter(chunk_size=25, chunk_overlap=0),\
        TitleExtractor(),\
        OpenAIEmbedding(),\
    ],
    cache=ingest_cache,
)

# Ingest directly into a vector db
nodes = pipeline.run(documents=[Document.example()])

```

Here, no persist step is needed, since everything is cached as you go in the specified remote collection.

## Async Support [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/\#async-support "Permanent link")

The `IngestionPipeline` also has support for async operation

```
nodes = await pipeline.arun(documents=documents)

```

## Document Management [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/\#document-management "Permanent link")

Attaching a `docstore` to the ingestion pipeline will enable document management.

Using the `document.doc_id` or `node.ref_doc_id` as a grounding point, the ingestion pipeline will actively look for duplicate documents.

It works by:

- Storing a map of `doc_id` -\> `document_hash`
- If a vector store is attached:
- If a duplicate `doc_id` is detected, and the hash has changed, the document will be re-processed and upserted
- If a duplicate `doc_id` is detected and the hash is unchanged, the node is skipped
- If only a vector store is not attached:
- Checks all existing hashes for each node
- If a duplicate is found, the node is skipped
- Otherwise, the node is processed

**NOTE:** If we do not attach a vector store, we can only check for and remove duplicate inputs.

```
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.storage.docstore import SimpleDocumentStore

pipeline = IngestionPipeline(
    transformations=[...], docstore=SimpleDocumentStore()
)

```

A full walkthrough is found in our [demo notebook](https://docs.llamaindex.ai/en/stable/examples/ingestion/document_management_pipeline/).

Also check out another guide using [Redis as our entire ingestion stack](https://docs.llamaindex.ai/en/stable/examples/ingestion/redis_ingestion_pipeline/).

## Parallel Processing [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/\#parallel-processing "Permanent link")

The `run` method of `IngestionPipeline` can be executed with parallel processes.
It does so by making use of `multiprocessing.Pool` distributing batches of nodes
to across processors.

To execute with parallel processing, set `num_workers` to the number of processes
you'd like use:

```
from llama_index.core.ingestion import IngestionPipeline

pipeline = IngestionPipeline(
    transformations=[...],
)
pipeline.run(documents=[...], num_workers=4)

```

## Modules [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/\#modules "Permanent link")

- [Transformations Guide](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/transformations/)
- [Advanced Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/examples/ingestion/advanced_ingestion_pipeline/)
- [Async Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/examples/ingestion/async_ingestion_pipeline/)
- [Document Management Pipeline](https://docs.llamaindex.ai/en/stable/examples/ingestion/document_management_pipeline/)
- [Redis Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/examples/ingestion/redis_ingestion_pipeline/)
- [Google Drive Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/examples/ingestion/ingestion_gdrive/)
- [Parallel Execution Pipeline](https://docs.llamaindex.ai/en/stable/examples/ingestion/parallel_execution_ingestion_pipeline/)

Back to top
![](https://static.scarf.sh/a.png?x-pxid=2b5669c2-eb91-4d0a-81d6-dc7238350598)

[iframe](https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfESacpAAAAAIAiwrVpFehgscJonmg1gKhpKg2e&co=aHR0cHM6Ly9kb2NzLmxsYW1haW5kZXguYWk6NDQz&hl=en&v=zIriijn3uj5Vpknvt_LnfNbF&size=invisible&cb=8ltkknc6v33x)


[Skip to content](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/#node-parser-usage-pattern)

# Node Parser Usage Pattern [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/\#node-parser-usage-pattern "Permanent link")

Node parsers are a simple abstraction that take a list of documents, and chunk them into `Node` objects, such that each node is a specific chunk of the parent document. When a document is broken into nodes, all of it's attributes are inherited to the children nodes (i.e. `metadata`, text and metadata templates, etc.). You can read more about `Node` and `Document` properties [here](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/).

## Getting Started [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/\#getting-started "Permanent link")

### Standalone Usage [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/\#standalone-usage "Permanent link")

Node parsers can be used on their own:

```
from llama_index.core import Document
from llama_index.core.node_parser import SentenceSplitter

node_parser = SentenceSplitter(chunk_size=1024, chunk_overlap=20)

nodes = node_parser.get_nodes_from_documents(
    [Document(text="long text")], show_progress=False
)

```

### Transformation Usage [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/\#transformation-usage "Permanent link")

Node parsers can be included in any set of transformations with an ingestion pipeline.

```
from llama_index.core import SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import TokenTextSplitter

documents = SimpleDirectoryReader("./data").load_data()

pipeline = IngestionPipeline(transformations=[TokenTextSplitter(), ...])

nodes = pipeline.run(documents=documents)

```

### Index Usage [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/\#index-usage "Permanent link")

Or set inside a `transformations` or global settings to be used automatically when an index is constructed using `.from_documents()`:

```
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter

documents = SimpleDirectoryReader("./data").load_data()

# global
from llama_index.core import Settings

Settings.text_splitter = SentenceSplitter(chunk_size=1024, chunk_overlap=20)

# per-index
index = VectorStoreIndex.from_documents(
    documents,
    transformations=[SentenceSplitter(chunk_size=1024, chunk_overlap=20)],
)

```

## Modules [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/\#modules "Permanent link")

See the full [modules guide](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/).

Back to top
![](https://static.scarf.sh/a.png?x-pxid=2b5669c2-eb91-4d0a-81d6-dc7238350598)

[iframe](https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfESacpAAAAAIAiwrVpFehgscJonmg1gKhpKg2e&co=aHR0cHM6Ly9kb2NzLmxsYW1haW5kZXguYWk6NDQz&hl=en&v=zIriijn3uj5Vpknvt_LnfNbF&size=invisible&cb=s8g90mymmj39)


[Skip to content](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/#node-parser-modules)

# Node Parser Modules [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/\#node-parser-modules "Permanent link")

## File-Based Node Parsers [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/\#file-based-node-parsers "Permanent link")

There are several file-based node parsers, that will create nodes based on the type of content that is being parsed (JSON, Markdown, etc.)

The simplest flow is to combine the `FlatFileReader` with the `SimpleFileNodeParser` to automatically use the best node parser for each type of content. Then, you may want to chain the file-based node parser with a text-based node parser to account for the actual length of the text.

### SimpleFileNodeParser [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/\#simplefilenodeparser "Permanent link")

```
from llama_index.core.node_parser import SimpleFileNodeParser
from llama_index.readers.file import FlatReader
from pathlib import Path

md_docs = FlatReader().load_data(Path("./test.md"))

parser = SimpleFileNodeParser()
md_nodes = parser.get_nodes_from_documents(md_docs)

```

### HTMLNodeParser [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/\#htmlnodeparser "Permanent link")

This node parser uses `beautifulsoup` to parse raw HTML.

By default, it will parse a select subset of HTML tags, but you can override this.

The default tags are: `["p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "b", "i", "u", "section"]`

```
from llama_index.core.node_parser import HTMLNodeParser

parser = HTMLNodeParser(tags=["p", "h1"])  # optional list of tags
nodes = parser.get_nodes_from_documents(html_docs)

```

### JSONNodeParser [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/\#jsonnodeparser "Permanent link")

The `JSONNodeParser` parses raw JSON.

```
from llama_index.core.node_parser import JSONNodeParser

parser = JSONNodeParser()

nodes = parser.get_nodes_from_documents(json_docs)

```

### MarkdownNodeParser [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/\#markdownnodeparser "Permanent link")

The `MarkdownNodeParser` parses raw markdown text.

```
from llama_index.core.node_parser import MarkdownNodeParser

parser = MarkdownNodeParser()

nodes = parser.get_nodes_from_documents(markdown_docs)

```

## Text-Splitters [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/\#text-splitters "Permanent link")

### CodeSplitter [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/\#codesplitter "Permanent link")

Splits raw code-text based on the language it is written in.

Check the full list of [supported languages here](https://github.com/grantjenks/py-tree-sitter-languages#license).

```
from llama_index.core.node_parser import CodeSplitter

splitter = CodeSplitter(
    language="python",
    chunk_lines=40,  # lines per chunk
    chunk_lines_overlap=15,  # lines overlap between chunks
    max_chars=1500,  # max chars per chunk
)
nodes = splitter.get_nodes_from_documents(documents)

```

### LangchainNodeParser [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/\#langchainnodeparser "Permanent link")

You can also wrap any existing text splitter from langchain with a node parser.

```
from langchain.text_splitter import RecursiveCharacterTextSplitter
from llama_index.core.node_parser import LangchainNodeParser

parser = LangchainNodeParser(RecursiveCharacterTextSplitter())
nodes = parser.get_nodes_from_documents(documents)

```

### SentenceSplitter [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/\#sentencesplitter "Permanent link")

The `SentenceSplitter` attempts to split text while respecting the boundaries of sentences.

```
from llama_index.core.node_parser import SentenceSplitter

splitter = SentenceSplitter(
    chunk_size=1024,
    chunk_overlap=20,
)
nodes = splitter.get_nodes_from_documents(documents)

```

### SentenceWindowNodeParser [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/\#sentencewindownodeparser "Permanent link")

The `SentenceWindowNodeParser` is similar to other node parsers, except that it splits all documents into individual sentences. The resulting nodes also contain the surrounding "window" of sentences around each node in the metadata. Note that this metadata will not be visible to the LLM or embedding model.

This is most useful for generating embeddings that have a very specific scope. Then, combined with a `MetadataReplacementNodePostProcessor`, you can replace the sentence with it's surrounding context before sending the node to the LLM.

An example of setting up the parser with default settings is below. In practice, you would usually only want to adjust the window size of sentences.

```
from llama_index.core.node_parser import SentenceWindowNodeParser

node_parser = SentenceWindowNodeParser.from_defaults(
    # how many sentences on either side to capture
    window_size=3,
    # the metadata key that holds the window of surrounding sentences
    window_metadata_key="window",
    # the metadata key that holds the original sentence
    original_text_metadata_key="original_sentence",
)

```

A full example can be found [here in combination with the `MetadataReplacementNodePostProcessor`](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/MetadataReplacementDemo/).

### SemanticSplitterNodeParser [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/\#semanticsplitternodeparser "Permanent link")

"Semantic chunking" is a new concept proposed Greg Kamradt in his video tutorial on 5 levels of embedding chunking: [https://youtu.be/8OJC21T2SL4?t=1933](https://youtu.be/8OJC21T2SL4?t=1933).

Instead of chunking text with a **fixed** chunk size, the semantic splitter adaptively picks the breakpoint in-between sentences using embedding similarity. This ensures that a "chunk" contains sentences that are semantically related to each other.

We adapted it into a LlamaIndex module.

Check out our notebook below!

Caveats:

- The regex primarily works for English sentences
- You may have to tune the breakpoint percentile threshold.

```
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.embeddings.openai import OpenAIEmbedding

embed_model = OpenAIEmbedding()
splitter = SemanticSplitterNodeParser(
    buffer_size=1, breakpoint_percentile_threshold=95, embed_model=embed_model
)

```

A full example can be found in our [guide on using the `SemanticSplitterNodeParser`](https://docs.llamaindex.ai/en/stable/examples/node_parsers/semantic_chunking/).

### TokenTextSplitter [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/\#tokentextsplitter "Permanent link")

The `TokenTextSplitter` attempts to split to a consistent chunk size according to raw token counts.

```
from llama_index.core.node_parser import TokenTextSplitter

splitter = TokenTextSplitter(
    chunk_size=1024,
    chunk_overlap=20,
    separator=" ",
)
nodes = splitter.get_nodes_from_documents(documents)

```

## Relation-Based Node Parsers [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/\#relation-based-node-parsers "Permanent link")

### HierarchicalNodeParser [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/\#hierarchicalnodeparser "Permanent link")

This node parser will chunk nodes into hierarchical nodes. This means a single input will be chunked into several hierarchies of chunk sizes, with each node containing a reference to it's parent node.

When combined with the `AutoMergingRetriever`, this enables us to automatically replace retrieved nodes with their parents when a majority of children are retrieved. This process provides the LLM with more complete context for response synthesis.

```
from llama_index.core.node_parser import HierarchicalNodeParser

node_parser = HierarchicalNodeParser.from_defaults(
    chunk_sizes=[2048, 512, 128]
)

```

A full example can be found [here in combination with the `AutoMergingRetriever`](https://docs.llamaindex.ai/en/stable/examples/retrievers/auto_merging_retriever/).

Back to top
![](https://static.scarf.sh/a.png?x-pxid=2b5669c2-eb91-4d0a-81d6-dc7238350598)

[iframe](https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfESacpAAAAAIAiwrVpFehgscJonmg1gKhpKg2e&co=aHR0cHM6Ly9kb2NzLmxsYW1haW5kZXguYWk6NDQz&hl=en&v=zIriijn3uj5Vpknvt_LnfNbF&size=invisible&cb=ugy8gua8ft39)


[Skip to content](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/transformations/#transformations)

# Transformations [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/transformations/\#transformations "Permanent link")

A transformation is something that takes a list of nodes as an input, and returns a list of nodes. Each component that implements the `Transformation` base class has both a synchronous `__call__()` definition and an async `acall()` definition.

Currently, the following components are `Transformation` objects:

- [`TextSplitter`](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/#text-splitters)
- [`NodeParser`](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/)
- [`MetadataExtractor`](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_metadata_extractor/)
- `Embeddings` model (check our [list of supported embeddings](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/#list-of-supported-embeddings))

## Usage Pattern [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/transformations/\#usage-pattern "Permanent link")

While transformations are best used with with an [`IngestionPipeline`](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/), they can also be used directly.

```
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor

node_parser = SentenceSplitter(chunk_size=512)
extractor = TitleExtractor()

# use transforms directly
nodes = node_parser(documents)

# or use a transformation in async
nodes = await extractor.acall(nodes)

```

## Combining with An Index [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/transformations/\#combining-with-an-index "Permanent link")

Transformations can be passed into an index or overall global settings, and will be used when calling `from_documents()` or `insert()` on an index.

```
from llama_index.core import VectorStoreIndex
from llama_index.core.extractors import (
    TitleExtractor,
    QuestionsAnsweredExtractor,
)
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import TokenTextSplitter

transformations = [\
    TokenTextSplitter(chunk_size=512, chunk_overlap=128),\
    TitleExtractor(nodes=5),\
    QuestionsAnsweredExtractor(questions=3),\
]

# global
from llama_index.core import Settings

Settings.transformations = [text_splitter, title_extractor, qa_extractor]

# per-index
index = VectorStoreIndex.from_documents(
    documents, transformations=transformations
)

```

## Custom Transformations [\#](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/transformations/\#custom-transformations "Permanent link")

You can implement any transformation yourself by implementing the base class.

The following custom transformation will remove any special characters or punctutaion in text.

```
import re
from llama_index.core import Document
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.schema import TransformComponent

class TextCleaner(TransformComponent):
    def __call__(self, nodes, **kwargs):
        for node in nodes:
            node.text = re.sub(r"[^0-9A-Za-z ]", "", node.text)
        return nodes

```

These can then be used directly or in any `IngestionPipeline`.

```
# use in a pipeline
pipeline = IngestionPipeline(
    transformations=[\
        SentenceSplitter(chunk_size=25, chunk_overlap=0),\
        TextCleaner(),\
        OpenAIEmbedding(),\
    ],
)

nodes = pipeline.run(documents=[Document.example()])

```

Back to top
![](https://static.scarf.sh/a.png?x-pxid=2b5669c2-eb91-4d0a-81d6-dc7238350598)

[iframe](https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfESacpAAAAAIAiwrVpFehgscJonmg1gKhpKg2e&co=aHR0cHM6Ly9kb2NzLmxsYW1haW5kZXguYWk6NDQz&hl=en&v=zIriijn3uj5Vpknvt_LnfNbF&size=invisible&cb=ri8n0z4xl5kk)


````

+ URLs

   ```markdown
   urls = [
       "https://docs.llamaindex.ai/en/stable/understanding/loading/loading/",
       "https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/",
       "https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/",
       "https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_nodes/",
       "https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_metadata_extractor/",
       "https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/",
       "https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/",
       "https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/",
       "https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/usage_pattern/",
       "https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/llama_parse/",
       "https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/",
       "https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/",
       "https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/",
       "https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/transformations/",
       # Add more URLs as needed
   ]
   ```