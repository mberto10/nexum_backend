---
tags:
  - ai coding
---
# Gemini API - Documentation



````python
# Text Generation Capability

# Generate text using the Gemini API

- On this page
- [Before you begin: Set up your project and API key](#set-up-project-and-api-key)
  - [Get and secure your API key](#get-and-secure-api-key)
  - [Install the SDK package and configure your API key](#install-package-and-configure-key)
- [Generate text from text-only input](#generate-text-from-text)
- [Generate text from text-and-image input](#generate-text-from-text-and-image)
- [Generate a text stream](#generate-a-text-stream)
- [Build an interactive chat](#chat)
- [Enable chat streaming](#chat-streaming)
- [Configure text generation](#configure)
- [What's next](#whats-next)

PythonNode.jsGoREST

The Gemini API can generate text output when provided text, images, video, and
audio as input.

This guide shows you how to generate text using the
[`generateContent`](https://ai.google.dev/api/rest/v1/models/generateContent?authuser=2) and
[`streamGenerateContent`](https://ai.google.dev/api/rest/v1/models/streamGenerateContent?authuser=2)
methods. To learn about working with Gemini's vision and audio capabilities,
refer to the [Vision](https://ai.google.dev/gemini-api/docs/vision?authuser=2) and [Audio](https://ai.google.dev/gemini-api/docs/audio?authuser=2)
guides.

## Before you begin: Set up your project and API key

Before calling the Gemini API, you need to set up your project and configure
your API key.

**Expand to view how to set up your project and API key**

### Get and secure your API key

You need an API key to call the Gemini API. If you don't already have one,
create a key in Google AI Studio.

[Get an API key](https://aistudio.google.com/app/apikey?authuser=2)

It's strongly recommended that you do _not_ check an API key into your version
control system.

You should store your API key in a secrets store such as Google Cloud
[Secret Manager](https://cloud.google.com/secret-manager/docs?authuser=2).

This tutorial assumes that you're accessing your API key as an environment
variable.

### Install the SDK package and configure your API key

The Python SDK for the Gemini API is contained in the
[`google-generativeai`](https://pypi.org/project/google-generativeai/) package.

1. Install the dependency using pip:








```
pip install -U google-generativeai

```

2. Import the package and configure the service with your API key:








```
import os
import google.generativeai as genai

genai.configure(api_key=os.environ['API_KEY'])

```


## Generate text from text-only input

The simplest way to generate text using the Gemini API is to provide the model
with a single text-only input, as shown in this example:

```
import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)
text_generation.py

```

In this case, the prompt ("Write a story about a magic backpack") doesn't
include any output examples, system instructions, or formatting information.
It's a [zero-shot](https://ai.google.dev/gemini-api/docs/models/generative-models?authuser=2#zero-shot-prompts)
approach. For some use cases, a
[one-shot](https://ai.google.dev/gemini-api/docs/models/generative-models?authuser=2#one-shot-prompts) or
[few-shot](https://ai.google.dev/gemini-api/docs/models/generative-models?authuser=2#few-shot-prompts) prompt
might produce output that's more aligned with user expectations. In some cases,
you might also want to provide
[system instructions](https://ai.google.dev/gemini-api/docs/system-instructions?authuser=2) to help the model
understand the task or follow specific guidelines.

## Generate text from text-and-image input

The Gemini API supports multimodal inputs that combine text with media files.
The following example shows how to generate text from text-and-image input:

```
import google.generativeai as genai

import PIL.Image

model = genai.GenerativeModel("gemini-1.5-flash")
organ = PIL.Image.open(media / "organ.jpg")
response = model.generate_content(["Tell me about this instrument", organ])
print(response.text)
text_generation.py

```

As with text-only prompting, multimodal prompting can involve various approaches
and refinements. Depending on the output from this example, you might want to
add steps to the prompt or be more specific in your instructions. To learn more,
see [File prompting strategies](https://ai.google.dev/gemini-api/docs/file-prompting-strategies?authuser=2).

## Generate a text stream

By default, the model returns a response after completing the entire text
generation process. You can achieve faster interactions by not waiting for the
entire result, and instead use streaming to handle partial results.

The following example shows how to implement streaming using the
[`streamGenerateContent`](https://ai.google.dev/api/rest/v1/models/streamGenerateContent?authuser=2) method to
generate text from a text-only input prompt.

```
import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.", stream=True)
for chunk in response:
    print(chunk.text)
    print("_" * 80)
text_generation.py

```

## Build an interactive chat

You can use the Gemini API to build interactive chat experiences for your users.
Using the chat feature of the API lets you collect multiple rounds of questions
and responses, allowing users to step incrementally toward answers or get help
with multipart problems. This feature is ideal for applications that require
ongoing communication, such as chatbots, interactive tutors, or customer support
assistants.

The following code example shows a basic chat implementation:

```
import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[\
        {"role": "user", "parts": "Hello"},\
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},\
    ]
)
response = chat.send_message("I have 2 dogs in my house.")
print(response.text)
response = chat.send_message("How many paws are in my house?")
print(response.text)
chat.py

```

## Enable chat streaming

You can also use streaming with chat, as shown in the following example:

```
import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[\
        {"role": "user", "parts": "Hello"},\
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},\
    ]
)
response = chat.send_message("I have 2 dogs in my house.", stream=True)
for chunk in response:
    print(chunk.text)
    print("_" * 80)
response = chat.send_message("How many paws are in my house?", stream=True)
for chunk in response:
    print(chunk.text)
    print("_" * 80)

print(chat.history)
chat.py

```

## Configure text generation

Every prompt you send to the model includes
[parameters](https://ai.google.dev/gemini-api/docs/models/generative-models?authuser=2#model-parameters) that
control how the model generates responses. You can use
[`GenerationConfig`](https://ai.google.dev/api/rest/v1/GenerationConfig?authuser=2) to
configure these parameters. If you don't configure the parameters, the model
uses default options, which can vary by model.

The following example shows how to configure several of the available options.

```
import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(
    "Tell me a story about a magic backpack.",
    generation_config=genai.types.GenerationConfig(
        # Only one candidate for now.
        candidate_count=1,
        stop_sequences=["x"],
        max_output_tokens=20,
        temperature=1.0,
    ),
)

print(response.text)
configure_model_parameters.py

```

`candidateCount` specifies the number of generated responses to return.
Currently, this value can only be set to 1. If unset, this will default to 1.

`stopSequences` specifies the set of character sequences (up to 5) that will
stop output generation. If specified, the API will stop at the first appearance
of a `stop_sequence`. The stop sequence won't be included as part of the
response.

`maxOutputTokens` sets the maximum number of tokens to include in a candidate.

`temperature` controls the randomness of the output. Use higher values for more
creative responses, and lower values for more deterministic responses. Values
can range from \[0.0, 2.0\].

You can also configure individual calls to `generateContent`:

```
response = model.generate_content(
    'Write a story about a magic backpack.',
    generation_config = genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=0.1,
    )
)

```

Any values set on the individual call override values on the model constructor.

## What's next

Now that you have explored the basics of the Gemini API, you might want to
try:

- [Vision understanding](https://ai.google.dev/gemini-api/docs/vision?authuser=2): Learn how to use
Gemini's native vision understanding to process images and videos.
- [System instructions](https://ai.google.dev/gemini-api/docs/system-instructions?authuser=2): System
instructions let you steer the behavior of the model based on your specific
needs and use cases.
- [Audio understanding](https://ai.google.dev/gemini-api/docs/audio?authuser=2): Learn how to use
Gemini's native audio understanding to process audio files.

# Structured Outputs

[![Gemini API](https://ai.google.dev/_static/googledevai/images/lockup-new.svg?authuser=2)](/)

# Generate structured output with the Gemini API

- On this page
- [Before you begin: Set up your project and API key](#set-up-project-and-api-key)
  - [Get and secure your API key](#get-and-secure-api-key)
  - [Install the SDK package and configure your API key](#install-package-and-configure-key)
- [Generate JSON](#generate-json)
  - [Supply a schema as text in the prompt](#supply-schema-in-prompt)
  - [Supply a schema through model configuration](#supply-schema-in-config)
- [Use an enum to constrain output](#use-an-enum)

PythonNode.jsGoDart (Flutter)AndroidSwiftWebREST

Gemini generates unstructured text by default, but some applications require
structured text. For these use cases, you can constrain Gemini to respond with
JSON, a structured data format suitable for automated processing. You can also
constrain the model to respond with one of the options specified in an enum.

Here are a few use cases that might require structured output from the model:

- Build a database of companies by pulling company information out of
newspaper articles.
- Pull standardized information out of resumes.
- Extract ingredients from recipes and display a link to a grocery website for
each ingredient.

In your prompt, you can ask Gemini to produce JSON-formatted output, but note
that the model is not guaranteed to produce JSON and nothing but JSON.
For a more deterministic response, you can pass a specific JSON schema in a
[`responseSchema`](https://ai.google.dev/api/rest/v1beta/GenerationConfig?authuser=2#FIELDS.response_schema)
field so that Gemini always responds with an expected structure.

This guide shows you how to generate JSON using the
[`generateContent`](https://ai.google.dev/api/rest/v1/models/generateContent?authuser=2) method through the SDK
of your choice or using the REST API directly. The examples show text-only
input, although Gemini can also produce JSON responses to multimodal requests
that include [images](https://ai.google.dev/gemini-api/docs/vision?authuser=2),
[videos](https://ai.google.dev/gemini-api/docs/vision?authuser=2), and [audio](https://ai.google.dev/gemini-api/docs/audio?authuser=2).

## Before you begin: Set up your project and API key

Before calling the Gemini API, you need to set up your project and configure
your API key.

**Expand to view how to set up your project and API key**

### Get and secure your API key

You need an API key to call the Gemini API. If you don't already have one,
create a key in Google AI Studio.

[Get an API key](https://aistudio.google.com/app/apikey?authuser=2)

It's strongly recommended that you do _not_ check an API key into your version
control system.

You should store your API key in a secrets store such as Google Cloud
[Secret Manager](https://cloud.google.com/secret-manager/docs?authuser=2).

This tutorial assumes that you're accessing your API key as an environment
variable.

### Install the SDK package and configure your API key

The Python SDK for the Gemini API is contained in the
[`google-generativeai`](https://pypi.org/project/google-generativeai/) package.

1. Install the dependency using pip:








```
pip install -U google-generativeai

```

2. Import the package and configure the service with your API key:








```
import os
import google.generativeai as genai

genai.configure(api_key=os.environ['API_KEY'])

```


## Generate JSON

When the model is configured to output JSON, it responds to any prompt with
JSON-formatted output.

You can control the structure of the JSON response by supplying a schema. There
are two ways to supply a schema to the model:

- As text in the prompt
- As a structured schema supplied through model configuration

Both approaches work in both Gemini 1.5 Flash and Gemini 1.5 Pro.

### Supply a schema as text in the prompt

The following example prompts the model to return cookie recipes in a specific
JSON format.

Since the model gets the format specification from text in the prompt, you may
have some flexibility in how you represent the specification. Any reasonable
format for representing a JSON schema may work.

```
import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-pro-latest")
prompt = """List a few popular cookie recipes in JSON format.

Use this JSON schema:

Recipe = {'recipe_name': str, 'ingredients': list[str]}
Return: list[Recipe]"""
result = model.generate_content(prompt)
print(result)
controlled_generation.py

```

The output might look like this:

```
[{"ingredients": ["1 cup (2 sticks) unsalted butter, softened", "1 cup granulated sugar", "1 cup packed light brown sugar", "2 teaspoons pure vanilla extract", "2 large eggs", "3 cups all-purpose flour", "1 teaspoon baking soda", "1 teaspoon salt", "2 cups chocolate chips"], "recipe_name": "Chocolate Chip Cookies"}, {"ingredients": ["1 cup (2 sticks) unsalted butter, softened", "¾ cup granulated sugar", "¾ cup packed light brown sugar", "1 teaspoon pure vanilla extract", "2 large eggs", "2 ¼ cups all-purpose flour", "1 teaspoon baking soda", "1 teaspoon salt", "1 cup rolled oats", "1 cup raisins"], "recipe_name": "Oatmeal Raisin Cookies"}, {"ingredients": ["1 cup (2 sticks) unsalted butter, softened", "1 ½ cups powdered sugar", "1 teaspoon pure vanilla extract", "2 ¼ cups all-purpose flour", "¼ teaspoon salt", "Sprinkles or colored sugar for decoration"], "recipe_name": "Sugar Cookies"}, {"ingredients": ["1 cup peanut butter", "1 cup granulated sugar", "1 large egg"], "recipe_name": "3-Ingredient Peanut Butter Cookies"}]

```

### Supply a schema through model configuration

The following example does the following:

1. Instantiates a model configured through a schema to respond with JSON.
2. Prompts the model to return cookie recipes.

```
import google.generativeai as genai

import typing_extensions as typing

class Recipe(typing.TypedDict):
    recipe_name: str
    ingredients: list[str]

model = genai.GenerativeModel("gemini-1.5-pro-latest")
result = model.generate_content(
    "List a few popular cookie recipes.",
    generation_config=genai.GenerationConfig(
        response_mime_type="application/json", response_schema=list[Recipe]
    ),
)
print(result)
controlled_generation.py

```

The output might look like this:

```
[{"ingredients": ["1 cup (2 sticks) unsalted butter, softened", "1 cup granulated sugar", "1 cup packed light brown sugar", "2 teaspoons pure vanilla extract", "2 large eggs", "3 cups all-purpose flour", "1 teaspoon baking soda", "1 teaspoon salt", "2 cups chocolate chips"], "recipe_name": "Chocolate Chip Cookies"}, {"ingredients": ["1 cup (2 sticks) unsalted butter, softened", "¾ cup granulated sugar", "¾ cup packed light brown sugar", "1 teaspoon pure vanilla extract", "2 large eggs", "2 ¼ cups all-purpose flour", "1 teaspoon baking soda", "1 teaspoon salt", "1 cup rolled oats", "1 cup raisins"], "recipe_name": "Oatmeal Raisin Cookies"}, {"ingredients": ["1 cup (2 sticks) unsalted butter, softened", "1 ½ cups powdered sugar", "1 teaspoon pure vanilla extract", "2 ¼ cups all-purpose flour", "¼ teaspoon salt", "Sprinkles or colored sugar for decoration"], "recipe_name": "Sugar Cookies"}, {"ingredients": ["1 cup peanut butter", "1 cup granulated sugar", "1 large egg"], "recipe_name": "3-Ingredient Peanut Butter Cookies"}]

```

#### Schema Definition Syntax

Specify the schema for the JSON response in the `response_schema` property of
your model configuration. The value of `response_schema` must be a either:

- A type hint annotation, as defined in the Python [`typing` module](https://docs.python.org/3/library/typing.html)
module.
- An instance of [`genai.protos.Schema`](https://ai.google.dev/api/python/google/generativeai/protos/Schema?authuser=2).

##### Define a Schema with a Type Hint Annotation

The easiest way to define a schema is with a type hint annotation. This is the
approach used in the preceding example:

```
generation_config={"response_mime_type": "application/json",
                   "response_schema": list[Recipe]}

```

The Gemini API Python client library supports schemas defined with the
following subset of `typing` annotations (where `AllowedType` is any allowed
type annotation):

- `int`
- `float`
- `bool`
- `str` (or enum)
- `list[AllowedType]`
- For dict types:
  - `dict[str, AllowedType]`. This annotation declares all dict values to
     be the same type, but doesn't specify what keys should be included.
  - User-defined subclasses of
     [`typing.TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict).
     This approach lets you specify the key names and define different
     types for the values associated with each of the keys.
  - User-defined [Data Classes](https://docs.python.org/3/library/dataclasses.html).
     Like `TypedDict` subclasses, this approach lets you
     specify the key names and define different types for the values
     associated with each of the keys.

##### Define a Schema with `genai.protos.Schema` Protocol Buffer

The Gemini API `genai.protos.Schema` protocol buffer definition supports a few
additional schema features not supported for type hints, including:

- Enums for strings
- Specifying the format for numeric types ( `int32` or `int64` for integers,
for example)
- Specifying which fields are required.

If you need these features, instantiate a `genai.protos.Schema` using one of the
methods illustrated in [Function Calling: Low Level Access](https://ai.google.dev/gemini-api/docs/function-calling/tutorial?lang=python&authuser=2#optional_low_level_access).

## Use an enum to constrain output

In some cases you might want the model to choose a single option from a list of
options. To implement this behavior, you can pass an _enum_ in your schema. You
can use an enum option anywhere you could use a `str` in the `response_schema`,
because an enum is actually a list of strings. Like a JSON schema, an enum lets
you constrain model output to meet the requirements of your application.

For example, assume that you're developing an application to classify images of
musical instruments into one of five categories: `"Percussion"`, `"String"`,
`"Woodwind"`, `"Brass"`, or " `Keyboard`". You could create an enum to help with
this task.

Before running the code examples in this section, make sure to import the
Google Generative AI library:

```
import google.generativeai as genai

```

In the following example, you pass the enum class `Choice` as the
`response_schema`, and the model should choose the most appropriate enum option.

```
import google.generativeai as genai

import enum

class Choice(enum.Enum):
    PERCUSSION = "Percussion"
    STRING = "String"
    WOODWIND = "Woodwind"
    BRASS = "Brass"
    KEYBOARD = "Keyboard"

model = genai.GenerativeModel("gemini-1.5-pro-latest")

organ = genai.upload_file(media / "organ.jpg")
result = model.generate_content(
    ["What kind of instrument is this:", organ],
    generation_config=genai.GenerationConfig(
        response_mime_type="text/x.enum", response_schema=Choice
    ),
)
print(result)  # Keyboard
controlled_generation.py

```

The Python SDK will translate the type declarations for the API. But the API
actually accepts a subset of the OpenAPI 3.0 schema
( [Schema](https://ai.google.dev/api/caching?authuser=2#schema)). You can also pass the
schema as JSON:

```
import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-pro-latest")

organ = genai.upload_file(media / "organ.jpg")
result = model.generate_content(
    ["What kind of instrument is this:", organ],
    generation_config=genai.GenerationConfig(
        response_mime_type="text/x.enum",
        response_schema={
            "type": "STRING",
            "enum": ["Percussion", "String", "Woodwind", "Brass", "Keyboard"],
        },
    ),
)
print(result)  # Keyboard
controlled_generation.py

```

Beyond basic multiple choice problems, you can use an enum anywhere in a schema
for JSON or function calling. For example, you could ask the model for a list of
recipe titles and use a `Grade` enum to give each title a popularity grade:

```
import google.generativeai as genai

import enum
from typing_extensions import TypedDict

class Grade(enum.Enum):
    A_PLUS = "a+"
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    F = "f"

class Recipe(TypedDict):
    recipe_name: str
    grade: Grade

model = genai.GenerativeModel("gemini-1.5-pro-latest")

result = model.generate_content(
    "List about 10 cookie recipes, grade them based on popularity",
    generation_config=genai.GenerationConfig(
        response_mime_type="application/json", response_schema=list[Recipe]
    ),
)
print(result)  # [{"grade": "a+", "recipe_name": "Chocolate Chip Cookies"}, ...]
controlled_generation.py

```
[![Gemini API](https://ai.google.dev/_static/googledevai/images/lockup-new.svg?authuser=2)](/)

`/`

- [English](https://ai.google.dev/gemini-api/docs/long-context?authuser=2)
- [Deutsch](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs/long-context?authuser=2&hl=ko)

[Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Flong-context&prompt=select_account)

- On this page
- [What is a context window?](#what-is-context-window)
- [Getting started with long context](#getting-started-with-long-context)
- [Long context use cases](#long-context-use-cases)
  - [Long form text](#long-form-text)
  - [Long form video](#long-form-video)
  - [Long form audio](#long-form-audio)
- [Long context optimizations](#long-context-optimizations)
- [Long context limitations](#long-context-limitations)
- [FAQs](#faqs)
  - [Do I lose model performance when I add more tokens to a query?](#do_i_lose_model_performance_when_i_add_more_tokens_to_a_query)
  - [How does Gemini 1.5 Pro perform on the standard needle-in-a-haystack test?](#how_does_gemini_15_pro_perform_on_the_standard_needle-in-a-haystack_test)
  - [How can I lower my cost with long-context queries?](#how_can_i_lower_my_cost_with_long-context_queries)
  - [How can I get access to the 2-million-token context window?](#how_can_i_get_access_to_the_2-million-token_context_window)
  - [Does the context length affect the model latency?](#does_the_context_length_affect_the_model_latency)
  - [Do the long context capabilities differ between Gemini 1.5 Flash and Gemini 1.5 Pro?](#do_the_long_context_capabilities_differ_between_gemini_15_flash_and_gemini_15_pro)

Gemini 2.0 Flash Experimental is now available! [Learn more](https://developers.googleblog.com/en/the-next-chapter-of-the-gemini-era-for-developers/)

- [Home](https://ai.google.dev/?authuser=2)
- [Gemini API](https://ai.google.dev/gemini-api?authuser=2)
- [Models](https://ai.google.dev/gemini-api/docs?authuser=2)

Was this helpful?



 Send feedback



# Long context

- On this page
- [What is a context window?](#what-is-context-window)
- [Getting started with long context](#getting-started-with-long-context)
- [Long context use cases](#long-context-use-cases)
  - [Long form text](#long-form-text)
  - [Long form video](#long-form-video)
  - [Long form audio](#long-form-audio)
- [Long context optimizations](#long-context-optimizations)
- [Long context limitations](#long-context-limitations)
- [FAQs](#faqs)
  - [Do I lose model performance when I add more tokens to a query?](#do_i_lose_model_performance_when_i_add_more_tokens_to_a_query)
  - [How does Gemini 1.5 Pro perform on the standard needle-in-a-haystack test?](#how_does_gemini_15_pro_perform_on_the_standard_needle-in-a-haystack_test)
  - [How can I lower my cost with long-context queries?](#how_can_i_lower_my_cost_with_long-context_queries)
  - [How can I get access to the 2-million-token context window?](#how_can_i_get_access_to_the_2-million-token_context_window)
  - [Does the context length affect the model latency?](#does_the_context_length_affect_the_model_latency)
  - [Do the long context capabilities differ between Gemini 1.5 Flash and Gemini 1.5 Pro?](#do_the_long_context_capabilities_differ_between_gemini_15_flash_and_gemini_15_pro)

Gemini 1.5 Flash comes standard with a 1-million-token context window, and
Gemini 1.5 Pro comes with a 2-million-token context window. Historically, large
language models (LLMs) were significantly limited by the amount of text (or
tokens) that could be passed to the model at one time. The Gemini 1.5 long
context window, with [near-perfect retrieval\\
(>99%)](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf),
unlocks many new use cases and developer paradigms.

The code you already use for cases like [text\\
generation](https://ai.google.dev/gemini-api/docs/text-generation?authuser=2) or [multimodal\\
inputs](https://ai.google.dev/gemini-api/docs/vision?authuser=2) will work out of the box with long context.

Throughout this guide, you briefly explore the basics of the context window, how
developers should think about long context, various real world use cases for
long context, and ways to optimize the usage of long context.

## What is a context window?

The basic way you use the Gemini 1.5 models is by passing information (context)
to the model, which will subsequently generate a response. An analogy for the
context window is short term memory. There is a limited amount of information
that can be stored in someone's short term memory, and the same is true for
generative models.

You can read more about how models work under the hood in our [generative models\\
guide](https://ai.google.dev/gemini-api/docs/models/generative-models?authuser=2).

## Getting started with long context

Most generative models created in the last few years were only capable of
processing 8,000 tokens at a time. Newer models pushed this further by accepting
32,000 tokens or 128,000 tokens. Gemini 1.5 is the first model capable of
accepting 1 million tokens, and now [2 million tokens with Gemini 1.5\\
Pro](https://developers.googleblog.com/en/new-features-for-the-gemini-api-and-google-ai-studio/).

In practice, 1 million tokens would look like:

- 50,000 lines of code (with the standard 80 characters per line)
- All the text messages you have sent in the last 5 years
- 8 average length English novels
- Transcripts of over 200 average length podcast episodes

Even though the models can take in more and more context, much of the
conventional wisdom about using large language models assumes this inherent
limitation on the model, which as of 2024, is no longer the case.

Some common strategies to handle the limitation of small context windows
included:

- Arbitrarily dropping old messages / text from the context window as new text
comes in
- Summarizing previous content and replacing it with the summary when the
context window gets close to being full
- Using RAG with semantic search to move data out of the context window and
into a vector database
- Using deterministic or generative filters to remove certain text /
characters from prompts to save tokens

While many of these are still relevant in certain cases, the default place to
start is now just putting all of the tokens into the context window. Because
Gemini 1.5 models were purpose-built with a long context window, they are much
more capable of in-context learning. For example, with only instructional
materials (a 500-page reference grammar, a dictionary, and ≈ 400 extra parallel
sentences) all provided in context, Gemini 1.5 Pro and Gemini 1.5 Flash are
[capable of learning to translate](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf)
from English to Kalamang— a Papuan language with fewer than 200 speakers and
therefore almost no online presence—with quality similar to a person who learned
from the same materials.

This example underscores how you can start to think about what is possible with
long context and the in-context learning capabilities of Gemini 1.5.

## Long context use cases

While the standard use case for most generative models is still text input, the
Gemini 1.5 model family enables a new paradigm of multimodal use cases. These
models can natively understand text, video, audio, and images. They are
accompanied by the [Gemini API that takes in multimodal file\\
types](https://ai.google.dev/gemini-api/docs/prompting_with_media?authuser=2) for
convenience.

### Long form text

Text has proved to be the layer of intelligence underpinning much of the
momentum around LLMs. As mentioned earlier, much of the practical limitation of
LLMs was because of not having a large enough context window to do certain
tasks. This led to the rapid adoption of retrieval augmented generation (RAG)
and other techniques which dynamically provide the model with relevant
contextual information. Now, with larger and larger context windows (currently
up to 2 million on Gemini 1.5 Pro), there are new techniques becoming available
which unlock new use cases.

Some emerging and standard use cases for text based long context include:

- Summarizing large corpuses of text
  - Previous summarization options with smaller context models would require
    a sliding window or another technique to keep state of previous sections
    as new tokens are passed to the model
- Question and answering
  - Historically this was only possible with RAG given the limited amount of
    context and models' factual recall being low
- Agentic workflows
  - Text is the underpinning of how agents keep state of what they have done
    and what they need to do; not having enough information about the world
    and the agent's goal is a limitation on the reliability of agents

[Many-shot in-context learning](https://arxiv.org/pdf/2404.11018) is one of the
most unique capabilities unlocked by long context models. Research has shown
that taking the common "single shot" or "multi-shot" example paradigm, where the
model is presented with one or a few examples of a task, and scaling that up to
hundreds, thousands, or even hundreds of thousands of examples, can lead to
novel model capabilities. This many-shot approach has also been shown to perform
similarly to models which were fine-tuned for a specific task. For use cases
where a Gemini model's performance is not yet sufficient for a production
rollout, you can try the many-shot approach. As you might explore later in the
long context optimization section, context caching makes this type of high input
token workload much more economically feasible and even lower latency in some
cases.

### Long form video

Video content's utility has long been constrained by the lack of accessibility
of the medium itself. It was hard to skim the content, transcripts often failed
to capture the nuance of a video, and most tools don't process image, text, and
audio together. With Gemini 1.5, the long-context text capabilities translate to
the ability to reason and answer questions about multimodal inputs with
sustained performance. Gemini 1.5 Flash, when tested on the needle in a video
haystack problem with 1M tokens, obtained >99.8% recall of the video in the
context window, and 1.5 Pro reached state of the art performance on the
[Video-MME benchmark](https://video-mme.github.io/home_page.html).

Some emerging and standard use cases for video long context include:

- Video question and answering
- Video memory, as shown with [Google's Project Astra](https://deepmind.google/technologies/gemini/project-astra/?authuser=2)
- Video captioning
- Video recommendation systems, by enriching existing metadata with new
multimodal understanding
- Video customization, by looking at a corpus of data and associated video
metadata and then removing parts of videos that are not relevant to the
viewer
- Video content moderation
- Real-time video processing

When working with videos, it is important to consider how the [videos are\\
processed into tokens](https://ai.google.dev/gemini-api/docs/tokens?authuser=2#media-token), which affects
billing and usage limits. You can learn more about prompting with video files in
the [Prompting\\
guide](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&authuser=2#prompting-with-videos).

### Long form audio

The Gemini 1.5 models were the first natively multimodal large language models
that could understand audio. Historically, the typical developer workflow would
involve stringing together multiple domain specific models, like a
speech-to-text model and a text-to-text model, in order to process audio. This
led to additional latency required by performing multiple round-trip requests
and decreased performance usually attributed to disconnected architectures of
the multiple model setup.

On standard audio-haystack evaluations, Gemini 1.5 Pro is able to find the
hidden audio in 100% of the tests and Gemini 1.5 Flash is able to find it in
98.7% [of the\\
tests](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf).
Gemini 1.5 Flash accepts up to 9.5 hours of [audio in a single\\
request](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&authuser=2#audio_formats) and
Gemini 1.5 Pro can accept up to 19 hours of audio using the 2-million-token
context window. Further, on a test set of 15-minute audio clips, Gemini 1.5 Pro
archives a word error rate (WER) of ~5.5%, much lower than even specialized
speech-to-text models, without the added complexity of extra input segmentation
and pre-processing.

Some emerging and standard use cases for audio context include:

- Real-time transcription and translation
- Podcast / video question and answering
- Meeting transcription and summarization
- Voice assistants

You can learn more about prompting with audio files in the [Prompting\\
guide](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&authuser=2#prompting-with-videos).

## Long context optimizations

The primary optimization when working with long context and the Gemini 1.5
models is to use [context\\
caching](https://ai.google.dev/gemini-api/docs/caching?authuser=2). Beyond the previous
impossibility of processing lots of tokens in a single request, the other main
constraint was the cost. If you have a "chat with your data" app where a user
uploads 10 PDFs, a video, and some work documents, you would historically have
to work with a more complex retrieval augmented generation (RAG) tool /
framework in order to process these requests and pay a significant amount for
tokens moved into the context window. Now, you can cache the files the user
uploads and pay to store them on a per hour basis. The input / output cost per
request with Gemini
1.5 Flash for example is ~4x less than the standard input / output cost, so if
the user chats with their data enough, it becomes a huge cost saving for you as
the developer.

## Long context limitations

In various sections of this guide, we talked about how Gemini 1.5 models achieve
high performance across various needle-in-a-haystack retrieval evals. These
tests consider the most basic setup, where you have a single needle you are
looking for. In cases where you might have multiple "needles" or specific pieces
of information you are looking for, the model does not perform with the same
accuracy. Performance can vary to a wide degree depending on the context. This
is important to consider as there is an inherent tradeoff between getting the
right information retrieved and cost. You can get ~99% on a single query, but
you have to pay the input token cost every time you send that query. So for 100
pieces of information to be retrieved, if you needed 99% performance, you would
likely need to send 100 requests. This is a good example of where context
caching can significantly reduce the cost associated with using Gemini models
while keeping the performance high.

## FAQs

### Do I lose model performance when I add more tokens to a query?

Generally, if you don't need tokens to be passed to the model, it is best to
avoid passing them. However, if you have a large chunk of tokens with some
information and want to ask questions about that information, the model is
highly capable of extracting that information (up to 99% accuracy in many
cases).

### How does Gemini 1.5 Pro perform on the standard needle-in-a-haystack test?

Gemini 1.5 Pro achieves 100% recall up to 530k tokens and >99.7% recall [up to\\
1M\\
tokens](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf).

### How can I lower my cost with long-context queries?

If you have a similar set of tokens / context that you want to re-use many
times, [context caching](https://ai.google.dev/gemini-api/docs/caching?authuser=2) can help reduce the costs
associated with asking questions about that information.

### How can I get access to the 2-million-token context window?

All developers now have access to the 2-million-token context window with Gemini
1.5 Pro.

### Does the context length affect the model latency?

There is some fixed amount of latency in any given request, regardless of the
size, but generally longer queries will have higher latency (time to first
token).

### Do the long context capabilities differ between Gemini 1.5 Flash and Gemini 1.5 Pro?

Yes, some of the numbers were mentioned in different sections of this guide, but
generally Gemini 1.5 Pro is more performant on most long context use cases.

Was this helpful?



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies?authuser=2). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-09-28 UTC.




          
````


