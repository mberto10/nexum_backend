---
tags:
  - ai coding
Type:
  - Documentation
Framework:
  - Agnostic
Phase:
  - Coding
Notes: Langfuse Documentation - Tracing Features
Model Optimised:
  - n.a.
---
# Langfuse Documentation - Tracing Features



Table of Contents

## Log-Level Tracing

## Masking

## Metadata

## Sessions

## URL

[Langfuse v3 is GA. Learn more →We've released Langfuse v3. Learn more →](/changelog/2024-12-09-Langfuse-v3-stable-release)

Docs [Tracing Features](/docs/tracing-features/log-levels "Tracing Features") Masking

# Masking of sensitive LLM data

Masking is a feature that allows precise control over the [tracing](/docs/tracing/overview) data sent to the Langfuse server. It enables you to:

1. Redact sensitive information from trace or observation inputs and outputs.

2. Customize the content of events before transmission.

3. Implement fine-grained data filtering based on your specific requirements.

The process works as follows:

1. You define a custom masking function and pass it to the Langfuse client constructor.

2. All event inputs and outputs are processed through this function.

3. The masked data is then sent to the Langfuse server.

This approach ensures that you have complete control over the event input and output data traced by your application.

PythonJS/TSOpenAILangchain (Python)Langchain (JS/TS)LlamaIndex (instrumentor)

Define a masking function:

```nextra-code
def masking_function(data):
  if isinstance(data, str) and data.startswith("SECRET_"):
    return "REDACTED"

  return data
```

Use with the [`@observe()` decorator](/docs/sdk/python/decorators):

```nextra-code
from langfuse.decorators import langfuse_context, observe

langfuse_context.configure(mask=masking_function)

@observe()
def fn():
    return "SECRET_DATA"

fn()

langfuse_context.flush()

# The trace output in Langfuse will have the output masked as "REDACTED".
```

Use with the [low-level SDK](/docs/sdk/python/low-level-sdk):

```nextra-code
from langfuse import Langfuse

langfuse = Langfuse(mask=masking_function)

trace = langfuse.trace(output="SECRET_DATA")

langfuse.flush()

# The trace output in Langfuse will have the output masked as "REDACTED".
```

```nextra-code
import { Langfuse } from "langfuse";

function maskingFunction(params: { data: any }) {
if (typeof params.data === "string" && params.data.startsWith("SECRET\_")) {
return "REDACTED";
}

return params.data;
}

const langfuse = new Langfuse({ mask: maskingFunction });

const trace = langfuse.trace({
output: "SECRET_DATA",
});

await langfuse.flushAsync();

// The trace output in Langfuse will have the output masked as "REDACTED".

```

See [JS/TS SDK docs](/docs/sdk/typescript/guide) for more details.

When using the [OpenAI SDK Integration](/docs/integrations/openai), set `openai.langfuse_mask` to the masking function:

```nextra-code
from langfuse.openai import openai

def masking_function(data):
  if isinstance(data, str) and data.startswith("SECRET_"):
    return "REDACTED"

  return data

openai.langfuse_mask = masking_function

completion = openai.chat.completions.create(
  name="test-chat",
  model="gpt-3.5-turbo",
  messages=[\
    {"role": "system", "content": "You are a bot."},\
    {"role": "user", "content": "1 + 1 = "}],
  temperature=0,
)

openai.flush_langfuse()
```

When using the integration with the `@observe()` decorator (see [interop docs](/docs/integrations/openai/get-started#use-traces)), set masking function via the `langfuse_context`:

```nextra-code
from langfuse.decorators import langfuse_context, observe
from langfuse.openai import openai

def masking_function(data):
  if isinstance(data, str) and data.startswith("SECRET_"):
    return "REDACTED"

  return data

langfuse_context.configure(mask=masking_function)

@observe()
def fn():
    completion = openai.chat.completions.create(
      name="test-chat",
      model="gpt-3.5-turbo",
      messages=[\
        {"role": "system", "content": "You are a calculator."},\
        {"role": "user", "content": "1 + 1 = "}],
      temperature=0,
    )

fn()
```

When using the [CallbackHandler](/docs/integrations/langchain/tracing), you can pass `mask` as a keyword argument:

```nextra-code
from langfuse.callback import CallbackHandler

def masking_function(data):
  if isinstance(data, str) and data.startswith("SECRET_"):
    return "REDACTED"

  return data

handler = CallbackHandler(
  mask=masking_function
)
```

When using the integration with the `@observe()` decorator (see [interop docs](/docs/integrations/langchain/tracing#interoperability)), set `mask` via the `langfuse_context`:

```nextra-code
from langfuse.decorators import langfuse_context, observe

def masking_function(data):
  if isinstance(data, str) and data.startswith("SECRET_"):
    return "REDACTED"

  return data

langfuse_context.configure(mask=masking_function)

@observe()
def fn():
    langfuse_handler = langfuse_context.get_current_langchain_handler()

    # Pass handler to invoke of your langchain chain/agent
    chain.invoke({"person": person}, config={"callbacks":[langfuse_handler]})

fn()
```

When using the [CallbackHandler](/docs/integrations/langchain/tracing), you can pass `mask` to the constructor:

```nextra-code
import { CallbackHandler } from "langfuse-langchain";

function maskingFunction(params: { data: any }) {
  if (typeof params.data === "string" && params.data.startsWith("SECRET_")) {
    return "REDACTED";
  }

  return params.data;
}

const handler = new CallbackHandler({
  mask: maskingFunction,
});
```

When using the [LlamaIndex Integration](/docs/integrations/llama-index/get-started), set the `mask` via the `instrumentor.observe()` context manager:

```nextra-code
from langfuse.llama_index import LlamaIndexInstrumentor

def masking_function(data):
  if isinstance(data, str) and data.startswith("SECRET_"):
    return "REDACTED"

  return data

instrumentor = LlamaIndexInstrumentor(mask=masking_function)

with instrumentor.observe():
    # ... your LlamaIndex index creation ...

    index.as_query_engine().query("What is the capital of France?")

instrumentor.flush()
```

When using the integration with the `@observe()` decorator (see [interop docs](/docs/integrations/llama-index/get-started#interoperability-with-langfuse-sdk)), set the `mask` via the `langfuse_context`:

```nextra-code
from langfuse.decorators import langfuse_context, observe
from langfuse.llama_index import LlamaIndexInstrumentor

def masking_function(data):
  if isinstance(data, str) and data.startswith("SECRET_"):
    return "REDACTED"

  return data

langfuse_context.configure(mask=masking_function)

@observe()
def llama_index_fn(question: str):
    # Get IDs
    current_trace_id = langfuse_context.get_current_trace_id()
    current_observation_id = langfuse_context.get_current_observation_id()

    # Pass to instrumentor
    with instrumentor.observe(
        trace_id=current_trace_id,
        parent_observation_id=current_observation_id,
        update_parent=False
    ) as trace:
        # ... your LlamaIndex index creation ...

        index.as_query_engine().query("What is the capital of France?")

        # Run application
        index = VectorStoreIndex.from_documents([doc1, doc2])
        response = index.as_query_engine().query(question)

        return response
```

## GitHub Discussions [Permalink for this section](#github-discussions)

[Specify data masking on decorator itself](https://github.com/orgs/langfuse/discussions/4078 "Langfuse Ideas: Specify data masking on decorator itself") [Customizable data mask (input/output, observation names, observation type)](https://github.com/orgs/langfuse/discussions/4076 "Langfuse Ideas: Customizable data mask (input/output, observation names, observation type)") [Async support for data masking in JS/TS SDK](https://github.com/orgs/langfuse/discussions/3981 "Langfuse Ideas: Async support for data masking in JS/TS SDK")

GitHubSupportGitHubIdeas

Upvotes [GitHubNew](https://github.com/orgs/langfuse/discussions/new/choose)

- 3votes

[Async support for data masking in JS/TS SDK](https://github.com/orgs/langfuse/discussions/3981)

pexxi•10/31/2024•

3

- 2votes

[Specify data masking on decorator itself](https://github.com/orgs/langfuse/discussions/4078)

marcklingen•11/6/2024•

0

- 2votes

[Customizable data mask (input/output, observation names, observation type)](https://github.com/orgs/langfuse/discussions/4076)

marcklingen•11/6/2024•

0

Discussions last updated: 12/30/2024, 1:05:52 AM (5 hours ago)

Last updated on October 31, 2024

[Log Levels](/docs/tracing-features/log-levels "Log Levels") [Metadata](/docs/tracing-features/metadata "Metadata")

### Was this page useful?

YesCould be better

### Questions? We're here to help

[GitHub Q&AGitHub](/gh-support) Chat[Email](mailto:support@langfuse.com) [Talk to sales](/schedule-demo)

### Subscribe to updates

Get updates

# Metadata

[Langfuse v3 is GA. Learn more →We've released Langfuse v3. Learn more →](/changelog/2024-12-09-Langfuse-v3-stable-release)

Docs [Tracing Features](/docs/tracing-features/log-levels "Tracing Features") Metadata

# Metadata

Traces and observations (see [Langfuse Data Model](/docs/tracing)) can be enriched with metadata to better understand your users, application, and experiments. Metadata can be added to traces in the form of arbitrary JSON.

PythonJS/TSOpenAI (Python)OpenAI (JS)Langchain (Python)Langchain (JS/TS)LlamaIndex (instrumentor)LlamaIndex (callback)Flowise

When using the [`@observe()` decorator](/docs/sdk/python/decorators):

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def fn():
    langfuse_context.update_current_trace(
        metadata={"key":"value"}
    )

fn()
```

When using the [low-level SDK](/docs/sdk/python/low-level-sdk):

```nextra-code
from langfuse import Langfuse
langfuse = Langfuse()

trace = langfuse.trace(
    metadata={"key":"value"}
)
```

```nextra-code
import { Langfuse } from "langfuse";
const langfuse = new Langfuse();

const trace = langfuse.trace({
  metadata: { key: "value" },
});
```

See [JS/TS SDK docs](/docs/sdk/typescript/guide) for more details.

When using the [OpenAI SDK Integration](/docs/integrations/openai), pass `metadata` as an additional argument:

```nextra-code
from langfuse.openai import openai

completion = openai.chat.completions.create(
  name="test-chat",
  model="gpt-3.5-turbo",
  messages=[\
    {"role": "system", "content": "You are a calculator."},\
    {"role": "user", "content": "1 + 1 = "}],
  temperature=0,

  # add metadata as additional argument
  metadata={"key":"value"}
)
```

When using the integration with the `@observe()` decorator (see [interop docs](/docs/integrations/openai/get-started#use-traces)), set `metadata` via the `langfuse_context`:

```nextra-code
from langfuse.decorators import langfuse_context, observe
from langfuse.openai import openai

@observe()
def fn():
    langfuse_context.update_current_trace(
        metadata={"key":"value"}
    )

    completion = openai.chat.completions.create(
      name="test-chat",
      model="gpt-3.5-turbo",
      messages=[\
        {"role": "system", "content": "You are a calculator."},\
        {"role": "user", "content": "1 + 1 = "}],
      temperature=0,
    )

fn()
```

When using the [OpenAI SDK Integration (JS)](/docs/integrations/openai/js), pass `metadata` as an additional argument:

```nextra-code
import OpenAI from "openai";
import { observeOpenAI } from "langfuse";

const res = await observeOpenAI(new OpenAI(), {
  metadata: { someMetadataKey: "someValue" },
}).chat.completions.create({
  messages: [{ role: "system", content: "Tell me a story about a dog." }],
  model: "gpt-3.5-turbo",
  max_tokens: 300,
});
```

When using the [CallbackHandler](/docs/integrations/langchain/tracing), you can pass `metadata` as a keyword argument:

```nextra-code
handler = CallbackHandler(
  metadata={"key":"value"}
)
```

When using the integration with the `@observe()` decorator (see [interop docs](/docs/integrations/langchain/tracing#interoperability)), set `metadata` via the `langfuse_context`:

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def fn():
    langfuse_context.update_current_trace(
        metadata={"key":"value"}
    )

    langfuse_handler = langfuse_context.get_current_langchain_handler()

    # Pass handler to invoke of your langchain chain/agent
    chain.invoke({"person": person}, config={"callbacks":[langfuse_handler]})

fn()
```

When using the [CallbackHandler](/docs/integrations/langchain/tracing), you can pass `metadata` to the constructor:

```nextra-code
const handler = new CallbackHandler({
  metadata: { key: "value" },
});
```

When using the integration with the JS SDK (see [interop docs](/docs/integrations/langchain/tracing#interoperability)), set `metadata` via `langfuse.trace()`:

```nextra-code
import { CallbackHandler, Langfuse } from "langfuse-langchain";
const langfuse = new Langfuse();

const trace = langfuse.trace({
  metadata: { key: "value" },
});
const langfuseHandler = new CallbackHandler({ root: trace });

// Add Langfuse handler as callback to your langchain chain/agent
await chain.invoke({ input: "<user_input>" }, { callbacks: [langfuseHandler] });
```

When using the [LlamaIndex Integration](/docs/integrations/llama-index/get-started), set the `metadata` via the `instrumentor.observe()` context manager:

```nextra-code
from langfuse.llama_index import LlamaIndexInstrumentor

instrumentor = LlamaIndexInstrumentor()

with instrumentor.observe(metadata={"key":"value"}):
    # ... your LlamaIndex index creation ...

    index.as_query_engine().query("What is the capital of France?")

instrumentor.flush()
```

When using the integration with the `@observe()` decorator (see [interop docs](/docs/integrations/llama-index/get-started#interoperability-with-langfuse-sdk)), set the metadata via the `langfuse_context`:

```nextra-code
from langfuse.decorators import langfuse_context, observe
from langfuse.llama_index import LlamaIndexInstrumentor

instrumentor = LlamaIndexInstrumentor()

@observe()
def llama_index_fn(question: str):
    # Update context
    langfuse_context.update_current_trace(metadata={"key":"value"})

    # Get IDs
    current_trace_id = langfuse_context.get_current_trace_id()
    current_observation_id = langfuse_context.get_current_observation_id()

    # Pass to instrumentor
    with instrumentor.observe(
        trace_id=current_trace_id,
        parent_observation_id=current_observation_id,
        update_parent=False
    ) as trace:
        # ... your LlamaIndex index creation ...

        index.as_query_engine().query("What is the capital of France?")

        # Run application
        index = VectorStoreIndex.from_documents([doc1, doc2])
        response = index.as_query_engine().query(question)

        return response
```

When using the (deprecated) [LlamaIndex Callback Integration](/docs/integrations/llama-index/deprecated-llama-index-callback), set the `metadata` via `set_trace_params`. All LlamaIndex traces created after `set_trace_params` will include the `metadata`. Learn more about `set_trace_params` [here](/docs/integrations/llama-index/deprecated-llama-index-callback#set-trace-params).

```nextra-code
from llama_index.core import Settings
from llama_index.core.callbacks import CallbackManager
from langfuse import langfuse

# Instantiate a new LlamaIndexCallbackHandler and register it in the LlamaIndex Settings
langfuse_callback_handler = LlamaIndexCallbackHandler()
Settings.callback_manager = CallbackManager([langfuse_callback_handler])

langfuse_callback_handler.set_trace_params(
  metadata={"key":"value"}
)
```

When using the integration with the `@observe()` decorator (see [interop docs](/docs/integrations/llama-index/deprecated-llama-index-callback#interoperability-with-langfuse-sdk)), set the metadata via the `langfuse_context`:

```nextra-code
from langfuse.decorators import langfuse_context, observe
from llama_index.core import Document, VectorStoreIndex
from llama_index.core import Settings
from llama_index.core.callbacks import CallbackManager

@observe()
def llama_index_fn(question: str):
    langfuse_context.update_current_trace(
        metadata={"key":"value"}
    )

    # Set callback manager for LlamaIndex, will apply to all LlamaIndex executions in this function
    langfuse_handler = langfuse_context.get_current_llama_index_handler()
    Settings.callback_manager = CallbackManager([langfuse_handler])

    # Run application
    index = VectorStoreIndex.from_documents([doc1,doc2])
    response = index.as_query_engine().query(question)
    return response
```

You can set the `metadata` via the override configs, see the [Flowise Integration docs](/docs/flowise) for more details.

## GitHub Discussions [Permalink for this section](#github-discussions)

[Retrieve the trace by metdata](https://github.com/orgs/langfuse/discussions/3276 "Langfuse Ideas: Retrieve the trace by metdata") [filtering sessions with metadata](https://github.com/orgs/langfuse/discussions/990 "Langfuse Ideas: filtering sessions with metadata")

GitHubSupportGitHubIdeas

Upvotes [GitHubNew](https://github.com/orgs/langfuse/discussions/new/choose)

[Langfuse v3 is GA. Learn more →We've released Langfuse v3. Learn more →](/changelog/2024-12-09-Langfuse-v3-stable-release)

Docs [Tracing Features](/docs/tracing-features/log-levels "Tracing Features") Multi-modality & Attachments

# Multi-Modality and Attachments

Support for media attachments to traces is currently in beta. Please report any [issues](/issues) and add feature requests to this ongoing [discussion thread](https://github.com/orgs/langfuse/discussions/3004).

Langfuse supports multi-modal traces including **text, images, audio, and other attachments**.

By default, **[base64 encoded data URIs](https://developer.mozilla.org/en-US/docs/Web/URI/Schemes/data#syntax) are handled automatically by the Langfuse SDKs**. They are extracted from the payloads commonly used in multi-modal LLMs, uploaded to Langfuse’s object storage, and linked to the trace.

This also works if you:

1. Reference media files via external URLs.

2. Customize the handling of media files in the SDKs via the `LangfuseMedia` class.

3. Integrate via the Langfuse API directly.

Learn more on how to get started and how this works under the hood below.

*Examples*

ImagesAudioAttachments

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fmulti-modal-trace-image.ce4c7665.jpg&w=3840&q=75)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fmulti-modal-trace-audio.1557617f.png&w=3840&q=75)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fmulti-modal-trace-attachment.73676dcc.png&w=3840&q=75)

## Availability [Permalink for this section](#availability)

### Langfuse Cloud [Permalink for this section](#langfuse-cloud)

Multi-modal attachments on Langfuse Cloud are free while in beta. We will be rolling out a new pricing metric to account for the additional storage and compute costs associated with large multi-modal traces in the coming weeks.

### Self-hosting [Permalink for this section](#self-hosting)

Multi-modal attachments are available today. You need to configure your own object storage bucket via the Langfuse environment variables ( `LANGFUSE_S3_MEDIA_UPLOAD_*`). See self-hosting documentation for details on these environment variables. S3-compatible APIs are supported across all major cloud providers and can be self-hosted via minio. Note that the configured storage bucket must have a publicly resolvable hostname to support direct uploads via our SDKs and media asset fetching directly from the browser.

## Supported media formats [Permalink for this section](#supported-media-formats)

Langfuse supports:

- **Images**: .png, .jpg, .webp

- **Audio files**: .mpeg, .mp3, .wav

- **Other attachments**: .pdf, plain text

If you require support for additional file types, please let us know in our [GitHub Discussion](https://github.com/orgs/langfuse/discussions/3004) where we’re actively gathering feedback on multi-modal support.

## Get Started [Permalink for this section](#get-started)

### Base64 data URI encoded media [Permalink for this section](#base64-data-uri-encoded-media)

If you use base64 encoded images, audio, or other files in your LLM applications, upgrade to the latest version of the Langfuse SDKs. The Langfuse SDKs automatically detect and handle base64 encoded media by extracting it, uploading it separately as a Langfuse Media file, and including a reference in the trace.

This works with standard Data URI ( [MDN](https://developer.mozilla.org/en-US/docs/Web/URI/Schemes/data#syntax)) formatted media (like those used by OpenAI and other LLMs).

This [notebook](/guides/cookbook/example_multi_modal_traces) includes a couple of examples using the OpenAI SDK and LangChain.

### External media (URLs) [Permalink for this section](#external-media-urls)

Langfuse supports in-line rendering of media files via URLs if they follow common formats. In this case, the media file is not uploaded to Langfuse’s object storage but simply rendered in the UI directly from the source.

Supported formats:

Markdown imagesOpenAI content parts

```nextra-code
![Alt text](https://example.com/image.jpg)
```

```nextra-code
{
  "content": [\
    {\
      "role": "system",\
      "content": "You are an AI trained to describe and interpret images. Describe the main objects and actions in the image."\
    },\
    {\
      "role": "user",\
      "content": [\
        {\
          "type": "text",\
          "text": "What's happening in this image?"\
        },\
        {\
          "type": "image_url",\
          "image_url": {\
            "url": "https://example.com/image.jpg"\
          }\
        }\
      ]\
    }\
  ]
}
```

### Custom attachments [Permalink for this section](#custom-attachments)

If you want to have more control or your media is not base64 encoded, you can upload arbitrary media attachments to Langfuse via the SDKs using the new `LangfuseMedia` class. Wrap media with LangfuseMedia before including it in trace inputs, outputs, or metadata. See the multi-modal documentation for examples.

PythonJS/TS

```nextra-code
from langfuse.decorators import observe, langfuse_context
from langfuse.media import LangfuseMedia

with open("static/bitcoin.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

# Wrap media in LangfuseMedia class
wrapped_obj = LangfuseMedia(
    obj=pdf_bytes, content_bytes=pdf_bytes, content_type="application/pdf"
)

# Optionally, access media via wrapped_obj.obj
wrapped_obj.obj

@observe()
def main():
    langfuse_context.update_current_trace(
      input=wrapped_obj,
      metadata={
          "context": wrapped_obj
      },
    )

    return # Limitation: LangfuseMedia object does not work in decorated function IO, needs to be set via update_current_trace or update_current_observation

main()
```

```nextra-code
import { Langfuse, LangfuseMedia } from "langfuse";
import fs from "fs";

// Initialize Langfuse client
const langfuse = new Langfuse();

// Wrap media in LangfuseMedia class
const wrappedMedia = new LangfuseMedia({
  contentBytes: fs.readFileSync("./static/bitcoin.pdf"),
  contentType: "application/pdf",
});

// Optionally, access media via wrappedMedia.obj
console.log(wrappedMedia.obj);

// Include media in any trace or observation
const trace = langfuse.trace({
  name: "test-trace-10",
  metadata: {
    context: wrappedMedia,
  },
});
```

### API [Permalink for this section](#api)

If you use the API directly to log traces to Langfuse, you need to follow these steps:

### Upload media to Langfuse [Permalink for this section](#upload-media-to-langfuse)

1. If you use base64 encoded media: you need to extract it from the trace payloads similar to how the Langfuse SDKs do it.

2. Initialize the upload and get a `mediaId` and `presignedURL`: [`POST /api/public/media`](https://api.reference.langfuse.com/#post-/api/public/media).

3. Upload media file: `PUT [presignedURL]`.

See this [end-to-end example](/guides/cookbook/example_multi_modal_traces#custom-via-api) (Python) on how to use the API directly to upload media files.

### Add reference to mediaId in trace/observation [Permalink for this section](#add-reference-to-mediaid-in-traceobservation)

Use the [Langfuse Media Token](#media-token) to reference the `mediaId` in the trace or observation `input`, `output`, or `metadata`.

## How does it work? [Permalink for this section](#how-does-it-work)

When using media files (that are not referenced via external URLs), Langfuse handles them in the following way:

### 1\. Media Upload Process [Permalink for this section](#1-media-upload-process)

#### Detection and Extraction [Permalink for this section](#detection-and-extraction)

- Langfuse supports media files in traces and observations on `input`, `output`, and `metadata` fields

- SDKs separate media from tracing data client-side for performance optimization

- Media files are uploaded directly to object storage (AWS S3 or compatible)

- Original media content is replaced with a reference string

#### Security and Optimization [Permalink for this section](#security-and-optimization)

- Uploads use presigned URLs with content validation (content length, content type, content SHA256 hash)

- Deduplication: Files are simply replaced by their `mediaId` reference string if already uploaded

- File uniqueness determined by project, content type, and content SHA256 hash

#### Implementation Details [Permalink for this section](#implementation-details)

- Python SDK: Background thread handling for non-blocking execution

- JS/TS SDKs: Asynchronous, non-blocking implementation

- API support for direct uploads (see [guide](/guides/cookbook/example_multi_modal_traces#custom-via-api))

### 2\. Media Reference System [Permalink for this section](#media-reference)

The base64 data URIs and the wrapped `LangfuseMedia` objects in Langfuse traces are replaced by references to the `mediaId` in the following standardized token format, which helps reconstruct the original payload if needed:

```nextra-code
@@@langfuseMedia:type={MIME_TYPE}|id={LANGFUSE_MEDIA_ID}|source={SOURCE_TYPE}@@@
```

- `MIME_TYPE`: MIME type of the media file, e.g., `image/jpeg`

- `LANGFUSE_MEDIA_ID`: ID of the media file in Langfuse’s object storage

- `SOURCE_TYPE`: Source type of the media file, can be `base64_data_uri`, `bytes`, or `file`

Based on this token, the Langfuse UI can automatically detect the `mediaId` and render the media file inline. The `LangfuseMedia` class provides utility functions to extract the `mediaId` from the reference string.

### 3\. Resolving Media References [Permalink for this section](#3-resolving-media-references)

When dealing with traces, observations, or dataset items that include media references, you can convert them back to their base64 data URI format using the `resolve_media_references` utility method provided by the Langfuse client. This is particularly useful for reinserting the original content during fine-tuning, dataset runs, or replaying a generation. The utility method traverses the parsed object and returns a deep copy with all media reference strings replaced by the corresponding base64 data URI representations.

PythonJS/TS

```nextra-code
from langfuse import Langfuse

# Initialize Langfuse client
langfuse = Langfuse()

# Example object with media references
obj = {
    "image": "@@@langfuseMedia:type=image/jpeg|id=some-uuid|source=bytes@@@",
    "nested": {
        "pdf": "@@@langfuseMedia:type=application/pdf|id=some-other-uuid|source=bytes@@@"
    }
}

# Resolve media references to base64 data URIs
resolved_trace = langfuse.resolve_media_references(
    obj=obj,
    resolve_with="base64_data_uri"
)

# Result:
# {
#     "image": "data:image/jpeg;base64,/9j/4AAQSkZJRg...",
#     "nested": {
#         "pdf": "data:application/pdf;base64,JVBERi0xLjcK..."
#     }
# }
```

```nextra-code
import { Langfuse } from "langfuse";

// Initialize Langfuse client
const langfuse = new Langfuse();

// Example object with media references
const obj = {
  image: "@@@langfuseMedia:type=image/jpeg|id=some-uuid|source=bytes@@@",
  nested: {
    pdf: "@@@langfuseMedia:type=application/pdf|id=some-other-uuid|source=bytes@@@",
  },
};

// Resolve media references to base64 data URIs
const resolvedTrace = await langfuse.resolveMediaReferences({
  obj: obj,
  resolveWith: "base64DataUri",
});

// Result:
// {
//     image: "data:image/jpeg;base64,/9j/4AAQSkZJRg...",
//     nested: {
//         pdf: "data:application/pdf;base64,JVBERi0xLjcK..."
//     }
// }
```

[Langfuse v3 is GA. Learn more →We've released Langfuse v3. Learn more →](/changelog/2024-12-09-Langfuse-v3-stable-release)

Docs [Tracing Features](/docs/tracing-features/log-levels "Tracing Features") Releases & Versioning

# Releases & Versioning

You can track the effect of changes to your LLM app on metrics in Langfuse. This allows you to:

- **Run experiments (A/B tests)** in production and measure the impact on costs, latencies and quality.

   - *Example*: “What is the impact of switching to a new model?”

- **Explain changes to metrics** over time.

   - *Example:* “Why did latency in this chain increase?”

## Releases [Permalink for this section](#releases)

LLM application

release:v2.1.23

LLM application

release:v2.1.24

A `release` tracks the overall version of your application. Commonly it is set to the *semantic version* or *git commit hash* of your application.

The SDKs look for a `release` in the following order:

1. SDK initialization

2. Environment variable

3. Automatically on popular platforms

#### SDK initialization [Permalink for this section](#sdk-initialization)

PythonJS/TSLangchain (Python)Langchain (JS)

Decorators

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def fn():
    langfuse_context.update_current_trace(
        release="<release_tag>"
    )

fn()
```

Low-level SDK

```nextra-code
from langfuse import Langfuse

langfuse = Langfuse(
  release="<release_tag>"
)
```

```nextra-code
import { Langfuse } from "langfuse";

langfuse = new Langfuse({
  release: "<release_tag>",
});
```

```nextra-code
from langfuse.callback import CallbackHandler

handler = CallbackHandler(release="<release_tag>")
```

```nextra-code
import { CallbackHandler } from "langfuse-langchain";

const handler = new CallbackHandler({
  release: "<release_tag>",
});
```

#### Via environment variable [Permalink for this section](#via-environment-variable)

The SDKs will look for a `LANGFUSE_RELEASE` environment variable. Use it to configure the release e.g. in your CI/CD pipeline.

```nextra-code
LANGFUSE_RELEASE = "<release_tag>" # <- github sha or other identifier
```

#### Automatically on popular platforms [Permalink for this section](#automatically-on-popular-platforms)

If no other `release` is set, the Langfuse SDKs default to a set of known release environment variables.

Supported platforms include: Vercel, Heroku, Netlify. See the full list of support environment variables for [JS/TS](https://github.com/langfuse/langfuse-js/blob/main/langfuse-core/src/release-env.ts) and [Python](https://github.com/langfuse/langfuse-python/blob/main/langfuse/environment.py#L3).

## Versions [Permalink for this section](#versions)

Generation

name:guess-countries

version:1.0

Generation

name:guess-countries

version:1.1

The `version` parameter can be added to `traces` and all observation types ( `span`, `generation`, `event`). Thereby, you can track the effect of a new `version` on the metrics of an object with a specific `name` using [Langfuse analytics](/docs/analytics).

PythonJS/TSLangchain (Python)Langchain (JS)

Decorators

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def fn():
    # trace level
    langfuse_context.update_current_trace(
        version="1.0",
    )

    # observation level
    langfuse_context.update_current_observation(
        version="1.0",
    )
fn()
```

Low-level SDK

```nextra-code
langfuse.generation(
  name="guess-countries",
  version="1.0",
)
```

`langfuse.trace()`, `langfuse.span()` and `langfuse.event()` also take an optional `version` parameter.

```nextra-code
langfuse.generation({
  name: "guess-countries",
  version: "1.0",
});
```

`langfuse.trace()`, `langfuse.span()` and `langfuse.event()` also take an optional `version` parameter.

```nextra-code
from langfuse.callback import CallbackHandler

handler = CallbackHandler(version="1.0")
```

```nextra-code
import { CallbackHandler } from "langfuse-langchain";

const handler = new CallbackHandler({
  version: "1.0",
});
```

# Sessions

[Langfuse v3 is GA. Learn more →We've released Langfuse v3. Learn more →](/changelog/2024-12-09-Langfuse-v3-stable-release)

Docs [Tracing Features](/docs/tracing-features/log-levels "Tracing Features") Sessions

# Sessions

Many interactions with LLM applications span multiple traces. `Sessions` in Langfuse are a way to group these traces together and see a simple **session replay** of the entire interaction. Get started by adding a `sessionId` when creating a trace.

Add a `sessionId` when creating/updating a trace. This can be any string that you use to identify the session. All traces with the same `sessionId` will be grouped together.

PythonJS/TSOpenAILangchain (Python)Langchain (JS/TS)LlamaIndex (instrumentor)LlamaIndex (callback)Flowise

When using the [`@observe()` decorator](/docs/sdk/python/decorators):

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def fn():
    langfuse_context.update_current_trace(
        session_id="your-session-id"
    )

fn()
```

When using the [low-level SDK](/docs/sdk/python/low-level-sdk):

```nextra-code
from langfuse import Langfuse
langfuse = Langfuse()

trace = langfuse.trace(
    session_id="your-session-id"
)
```

```nextra-code
import { Langfuse } from "langfuse";
const langfuse = new Langfuse();

const trace = langfuse.trace({
  sessionId: "your-session-id",
});
```

See [JS/TS SDK docs](/docs/sdk/typescript/guide) for more details.

When using the [OpenAI SDK Integration](/docs/integrations/openai), pass the `session_id` as an additional argument:

```nextra-code
from langfuse.openai import openai

completion = openai.chat.completions.create(
  name="test-chat",
  model="gpt-3.5-turbo",
  messages=[\
    {"role": "system", "content": "You are a calculator."},\
    {"role": "user", "content": "1 + 1 = "}],
  temperature=0,

  # add session_id as additional argument
  session_id="your-session-id"
)
```

When using the integration with the `@observe()` decorator (see [interop docs](/docs/integrations/openai/get-started#use-traces)), set the session_id via the `langfuse_context`:

```nextra-code
from langfuse.decorators import langfuse_context, observe
from langfuse.openai import openai

@observe()
def fn():
    langfuse_context.update_current_trace(
        session_id="your-session-id"
    )

    completion = openai.chat.completions.create(
      name="test-chat",
      model="gpt-3.5-turbo",
      messages=[\
        {"role": "system", "content": "You are a calculator."},\
        {"role": "user", "content": "1 + 1 = "}],
      temperature=0,
    )

fn()
```

When using the [CallbackHandler](/docs/integrations/langchain/tracing), you can pass the `session_id` as a keyword argument:

```nextra-code
handler = CallbackHandler(
  session_id="your-session-id"
)
```

You can also set the `session_id` dynamically via the runnable configuration in the chain invocation:

```nextra-code
from langfuse.callback import CallbackHandler

handler = CallbackHandler()

# Your existing Langchain code to create the chain
...

# Pass langfuse_session_id as metadata to the chain invocation to be parsed as the Langfuse session_id
chain.invoke(
    {"animal": "dog"},
    config={
        "callbacks": [handler],
        "metadata": {
            "langfuse_session_id": "your-session-id",
        },
    },
)
```

When using the integration with the `@observe()` decorator (see [interop docs](/docs/integrations/langchain/tracing#interoperability)), set the session_id via the `langfuse_context`:

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def fn():
    langfuse_context.update_current_trace(
        session_id="your-session-id"
    )

    langfuse_handler = langfuse_context.get_current_langchain_handler()

    # Pass handler to invoke of your langchain chain/agent
    chain.invoke({"person": person}, config={"callbacks":[langfuse_handler]})

fn()
```

When using the [CallbackHandler](/docs/integrations/langchain/tracing), you can pass the `sessionId` to the constructor:

```nextra-code
const handler = new CallbackHandler({
  sessionId: "your-session-id",
});
```

You can also set the `session_id` dynamically via the runnable configuration in the chain invocation:

```nextra-code
import { CallbackHandler } from "langfuse-langchain";

const langfuseHandler = new CallbackHandler();

// Your existing Langchain code to create the chain
...

// Pass langfuseSessionId as metadata to the chain invocation to be parsed as the Langfuse session_id
await chain.invoke(
  { input: "<user_input>" },
  { callbacks: [langfuseHandler], metadata: { langfuseSessionId: "your-session-id" } }
);
```

When using the integration with the JS SDK (see [interop docs](/docs/integrations/langchain/tracing#interoperability)), set the sessionId via `langfuse.trace()`:

```nextra-code
import { CallbackHandler, Langfuse } from "langfuse-langchain";
const langfuse = new Langfuse();

const trace = langfuse.trace({
  sessionId: "your-session-id",
});
const langfuseHandler = new CallbackHandler({ root: trace });

// Add Langfuse handler as callback to your langchain chain/agent
await chain.invoke({ input: "<user_input>" }, { callbacks: [langfuseHandler] });
```

When using the [LlamaIndex Integration](/docs/integrations/llama-index/get-started), set the `session_id` via the `instrumentor.observe()` context manager:

```nextra-code
from langfuse.llama_index import LlamaIndexInstrumentor

instrumentor = LlamaIndexInstrumentor()

with instrumentor.observe(session_id="my-session"):
    # ... your LlamaIndex index creation ...

    index.as_query_engine().query("What is the capital of France?")

instrumentor.flush()
```

When using the integration with the `@observe()` decorator (see [interop docs](/docs/integrations/llama-index/get-started#interoperability-with-langfuse-sdk)), set the session_id via the `langfuse_context`:

```nextra-code
from langfuse.decorators import langfuse_context, observe
from langfuse.llama_index import LlamaIndexInstrumentor

instrumentor = LlamaIndexInstrumentor()

@observe()
def llama_index_fn(question: str):
    # Update context
    langfuse_context.update_current_trace(session_id="your-session-id")

    # Get IDs
    current_trace_id = langfuse_context.get_current_trace_id()
    current_observation_id = langfuse_context.get_current_observation_id()

    # Pass to instrumentor
    with instrumentor.observe(
        trace_id=current_trace_id,
        parent_observation_id=current_observation_id,
        update_parent=False
    ) as trace:
        # ... your LlamaIndex index creation ...

        index.as_query_engine().query("What is the capital of France?")

        # Run application
        index = VectorStoreIndex.from_documents([doc1, doc2])
        response = index.as_query_engine().query(question)

        return response
```

When using the (deprecated) [LlamaIndex Callback Integration](/docs/integrations/llama-index/deprecated-llama-index-callback), set the `session_id` via `set_trace_params`. All LlamaIndex traces created after `set_trace_params` will include the `session_id`. Learn more about `set_trace_params` [here](/docs/integrations/llama-index/deprecated-llama-index-callback#set-trace-params).

```nextra-code
from llama_index.core import Settings
from llama_index.core.callbacks import CallbackManager
from langfuse import langfuse

# Instantiate a new LlamaIndexCallbackHandler and register it in the LlamaIndex Settings
langfuse_callback_handler = LlamaIndexCallbackHandler()
Settings.callback_manager = CallbackManager([langfuse_callback_handler])

langfuse_callback_handler.set_trace_params(
  session_id="session-abc",
)
```

When using the integration with the `@observe()` decorator (see [interop docs](/docs/integrations/llama-index/deprecated-llama-index-callback#interoperability-with-langfuse-sdk)), set the session_id via the `langfuse_context`:

```nextra-code
from langfuse.decorators import langfuse_context, observe
from llama_index.core import Document, VectorStoreIndex
from llama_index.core import Settings
from llama_index.core.callbacks import CallbackManager

@observe()
def llama_index_fn(question: str):
    langfuse_context.update_current_trace(
        session_id="your-session-id"
    )

    # Set callback manager for LlamaIndex, will apply to all LlamaIndex executions in this function
    langfuse_handler = langfuse_context.get_current_llama_index_handler()
    Settings.callback_manager = CallbackManager([langfuse_handler])

    # Run application
    index = VectorStoreIndex.from_documents([doc1,doc2])
    response = index.as_query_engine().query(question)
    return response
```

[Langfuse v3 is GA. Learn more →We've released Langfuse v3. Learn more →](/changelog/2024-12-09-Langfuse-v3-stable-release)

Docs [Tracing Features](/docs/tracing-features/log-levels "Tracing Features") Tags

# Tagging traces

Tags allow you to categorize and filter traces. You can tag traces (1) when they are created using the Langfuse SDKs and integrations or (2) from the Langfuse UI. To tag a trace, add a list of tags to the tags field of the trace object. Tags are strings and a trace may have multiple tags.

PythonJS/TSOpenAILangchain (Python)Langchain (JS/TS)LlamaIndex (instrumentor)LlamaIndex (callback)

When using the [`@observe()` decorator](/docs/sdk/python/decorators):

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def fn():
    langfuse_context.update_current_trace(
        tags=["tag-1", "tag-2"]
    )

fn()
```

When using the [low-level SDK](/docs/sdk/python/low-level-sdk):

```nextra-code
from langfuse import Langfuse
langfuse = Langfuse()

trace = langfuse.trace(
    tags=["tag-1", "tag-2"]
)
```

```nextra-code
import { Langfuse } from "langfuse";
const langfuse = new Langfuse();

const trace = langfuse.trace({
  tags: ["tag-1", "tag-2"],
});
```

See [JS/TS SDK docs](/docs/sdk/typescript/guide) for more details.

When using the [OpenAI SDK Integration](/docs/integrations/openai), pass `tags` as an additional argument:

```nextra-code
from langfuse.openai import openai

completion = openai.chat.completions.create(
  name="test-chat",
  model="gpt-3.5-turbo",
  messages=[\
    {"role": "system", "content": "You are a calculator."},\
    {"role": "user", "content": "1 + 1 = "}],
  temperature=0,

  # add tags as additional argument
  tags=["tag-1", "tag-2"]
)
```

When using the integration with the `@observe()` decorator (see [interop docs](/docs/integrations/openai/get-started#use-traces)), set tags via the `langfuse_context`:

```nextra-code
from langfuse.decorators import langfuse_context, observe
from langfuse.openai import openai

@observe()
def fn():
    langfuse_context.update_current_trace(
        tags=["tag-1", "tag-2"]
    )

    completion = openai.chat.completions.create(
      name="test-chat",
      model="gpt-3.5-turbo",
      messages=[\
        {"role": "system", "content": "You are a calculator."},\
        {"role": "user", "content": "1 + 1 = "}],
      temperature=0,
    )

fn()
```

When using the [CallbackHandler](/docs/integrations/langchain/tracing), you can pass `tags` as a keyword argument:

```nextra-code
handler = CallbackHandler(
  tags=["tag-1", "tag-2"]
)
```

You can also set tags dynamically via the runnable configuration in the chain invocation:

```nextra-code
from langfuse.callback import CallbackHandler

handler = CallbackHandler()
tags = ["tag-1", "tag-2"]

chain.invoke(
    {"animal": "dog"},
    config={
        "callbacks": [handler],
        "tags": tags,
    },
)
```

When using the integration with the `@observe()` decorator (see [interop docs](/docs/integrations/langchain/tracing#interoperability)), set tags via the `langfuse_context`:

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def fn():
    langfuse_context.update_current_trace(
        tags=["tag-1", "tag-2"]
    )

    langfuse_handler = langfuse_context.get_current_langchain_handler()

    # Pass handler to invoke of your langchain chain/agent
    chain.invoke({"person": person}, config={"callbacks":[langfuse_handler]})

fn()
```

When using the [CallbackHandler](/docs/integrations/langchain/tracing), you can pass `tags` to the constructor:

```nextra-code
const handler = new CallbackHandler({
  tags: ["tag-1", "tag-2"],
});
```

You can also set tags dynamically via the runnable configuration in the chain invocation:

```nextra-code
const langfuseHandler = new CallbackHandler()
const tags = ["tag-1", "tag-2"];

// Your existing Langchain code to create the chain
...

// Pass config to the chain invocation to be parsed as Langfuse trace attributes
await chain.invoke({ input: "<user_input>" }, { callbacks: [langfuseHandler], tags: tags });
```

When using the integration with the JS SDK (see [interop docs](/docs/integrations/langchain/tracing#interoperability)), set tags via `langfuse.trace()`:

```nextra-code
import { CallbackHandler, Langfuse } from "langfuse-langchain";
const langfuse = new Langfuse();

const trace = langfuse.trace({
  tags: ["tag-1", "tag-2"],
});
const langfuseHandler = new CallbackHandler({ root: trace });

// Add Langfuse handler as callback to your langchain chain/agent
await chain.invoke({ input: "<user_input>" }, { callbacks: [langfuseHandler] });
```

When using the [LlamaIndex Integration](/docs/integrations/llama-index/get-started), set the `tags` via the `instrumentor.observe()` context manager:

```nextra-code
from langfuse.llama_index import LlamaIndexInstrumentor

instrumentor = LlamaIndexInstrumentor()

with instrumentor.observe(tags=["tag-1", "tag-2"]):
    # ... your LlamaIndex index creation ...

    index.as_query_engine().query("What is the capital of France?")

instrumentor.flush()
```

When using the integration with the `@observe()` decorator (see [interop docs](/docs/integrations/llama-index/get-started#interoperability-with-langfuse-sdk)), set the tags via the `langfuse_context`:

```nextra-code
from langfuse.decorators import langfuse_context, observe
from langfuse.llama_index import LlamaIndexInstrumentor

instrumentor = LlamaIndexInstrumentor()

@observe()
def llama_index_fn(question: str):s
    # Update context
    langfuse_context.update_current_trace(tags=["tag-1", "tag-2"])

    # Get IDs
    current_trace_id = langfuse_context.get_current_trace_id()
    current_observation_id = langfuse_context.get_current_observation_id()

    # Pass to instrumentor
    with instrumentor.observe(
        trace_id=current_trace_id,
        parent_observation_id=current_observation_id,
        update_parent=False
    ) as trace:
        # ... your LlamaIndex index creation ...

        index.as_query_engine().query("What is the capital of France?")

        # Run application
        index = VectorStoreIndex.from_documents([doc1, doc2])
        response = index.as_query_engine().query(question)

        return response
```

When using the (deprecated) [LlamaIndex Callback Integration](/docs/integrations/llama-index/deprecated-llama-index-callback), set the `tags` via `set_trace_params`. All LlamaIndex traces created after `set_trace_params` will include the `tags`. Learn more about `set_trace_params` [here](/docs/integrations/llama-index/deprecated-llama-index-callback#set-trace-params).

```nextra-code
from llama_index.core import Settings
from llama_index.core.callbacks import CallbackManager
from langfuse import langfuse

# Instantiate a new LlamaIndexCallbackHandler and register it in the LlamaIndex Settings
langfuse_callback_handler = LlamaIndexCallbackHandler()
Settings.callback_manager = CallbackManager([langfuse_callback_handler])

langfuse_callback_handler.set_trace_params(
  tags=["tag-1", "tag-2"]
)
```

When using the integration with the `@observe()` decorator (see [interop docs](/docs/integrations/llama-index/deprecated-llama-index-callback#interoperability-with-langfuse-sdk)), set the tags via the `langfuse_context`:

```nextra-code
from langfuse.decorators import langfuse_context, observe
from llama_index.core import Document, VectorStoreIndex
from llama_index.core import Settings
from llama_index.core.callbacks import CallbackManager

@observe()
def llama_index_fn(question: str):
    langfuse_context.update_current_trace(
        tags=["tag-1", "tag-2"]
    )

    # Set callback manager for LlamaIndex, will apply to all LlamaIndex executions in this function
    langfuse_handler = langfuse_context.get_current_llama_index_handler()
    Settings.callback_manager = CallbackManager([langfuse_handler])

    # Run application
    index = VectorStoreIndex.from_documents([doc1,doc2])
    response = index.as_query_engine().query(question)
    return response
```

### Working with tags [Permalink for this section](#working-with-tags)

Tags enable you to flexibly add metadata to your traces. You can filter for tags in the Langfuse UI and [GET API](https://api.reference.langfuse.com/).

When choosing tags, consider what aspects of the traces you might want to filter for or group by in your analysis. You may use tags to indicate specific versions of your app (‘app-v1’, ‘app-v2’), specific LLM techniques you used (‘rag’, ‘one-shot’, ‘few-shot’), or the environment of your app (‘local’, ‘staging’, ‘prod’). See [Intent Classification Notebook](/docs/analytics/example-intent-classification) for an end-to-end example on how tags can be created programmatically.

## GitHub Discussions [Permalink for this section](#github-discussions)

[How to set tags when using the Langchain Callback handler](https://github.com/orgs/langfuse/discussions/1186 "Langfuse Support: How to set tags when using the Langchain Callback handler") [Chart: usage/metrics grouped by tags](https://github.com/orgs/langfuse/discussions/3476 "Langfuse Ideas: Chart: usage/metrics grouped by tags") [Deleting old, unused tags or making them unseen if weren't used in the chosen time window.](https://github.com/orgs/langfuse/discussions/3289 "Langfuse Ideas: Deleting old, unused tags or making them unseen if weren't used in the chosen time window.") [Tag based usage](https://github.com/orgs/langfuse/discussions/2967 "Langfuse Ideas: Tag based usage") [Feat: Allow not sorting tags](https://github.com/orgs/langfuse/discussions/2848 "Langfuse Ideas: Feat: Allow not sorting tags")

GitHubSupportGitHubIdeas

Upvotes [GitHubNew](https://github.com/orgs/langfuse/discussions/new/choose)

- 2votes

[How to set tags when using the Langchain Callback handler](https://github.com/orgs/langfuse/discussions/1186)

reza-mohideen•2/16/2024•

2Resolved

[Langfuse v3 is GA. Learn more →We've released Langfuse v3. Learn more →](/changelog/2024-12-09-Langfuse-v3-stable-release)

Docs [Tracing Features](/docs/tracing-features/log-levels "Tracing Features") Trace URL

# Trace URLs

Each trace has a unique URL that you can use to share it with others or to access it directly.

## Get trace url [Permalink for this section](#get-trace-url)

Sometimes, it is useful to get the trace URL directly in the SDK. E.g. to add it to your logs or interactively look at it when running experiments in notebooks.

PythonJS/TSLangchain (Python)Langchain (JS)

When using the [`@observe()` decorator](/docs/sdk/python/decorators):

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def fn():
    langfuse_context.get_current_trace_url()

fn()
```

When using the [low-level SDK](/docs/sdk/python/low-level-sdk):

```nextra-code
trace = langfuse.trace(...)
trace.get_trace_url()
```

```nextra-code
const trace = langfuse.trace(...)
trace.getTraceUrl()
```

Use the interoperability of the Langfuse Python `@observe()` Decorator with the Langchain integration to get the URL of a trace ( [interop docs](/docs/integrations/langchain/tracing#interoperability)).

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def fn():
    langfuse_handler = langfuse_context.get_current_langchain_handler()

    # Your Langchain code

    # Add Langfuse handler as callback (classic and LCEL)
    chain.invoke({"input": "<user_input>"}, config={"callbacks": [langfuse_handler]})

    langfuse_context.get_current_trace_url()

fn()
```

**Deprecated:** flaky in cases of concurrent requests as it depends on the state of the handler.

```nextra-code
handler.get_trace_url()
```

Use the interoperability of the Langfuse SDK with the Langchain integration to get the URL of a trace ( [interop docs](/docs/integrations/langchain/tracing#interoperability)).

```nextra-code
// Intialize Langfuse Client
import { CallbackHandler, Langfuse } from "langfuse-langchain";
const langfuse = new Langfuse();

// Create a Langfuse trace for an execution of your application
const trace = langfuse.trace();

// Get Langchain handler for this trace
const langfuseHandler = new CallbackHandler({ root: trace });

// Get the trace URL
langfuseHandler.getTraceUrl();
```

**Deprecated:** flaky in cases of concurrent requests as it depends on the state of the handler.

```nextra-code
handler.getTraceUrl();
```

## Share trace via url [Permalink for this section](#share-trace-via-url)

By default, only members of your Langfuse project can view a trace.

You can make a trace `public` to share it via a public link. This allows others to view the trace without needing to log in or be members of your Langfuse project.

*Example: <https://cloud.langfuse.com/project/clkpwwm0m000gmm094odg11gi/traces/2d6b96f2-0a4d-4366-99a5-1ad558c66e99>*

Langfuse UIPythonJS/TS

Decorators

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def fn():
    langfuse_context.update_current_trace(
        public=True
    )

fn()
```

Low-level SDK

```nextra-code
trace = langfuse.trace(
    ...
+   public=True
    ...
)
```

```nextra-code
const trace = langfuse.trace({
    ...
+   public: true,
    ...
});
```