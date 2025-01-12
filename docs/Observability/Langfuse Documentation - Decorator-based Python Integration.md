---
tags:
  - ai coding
Type:
  - Documentation
Framework:
  - Agnostic
Phase:
  - Coding
Notes: Langfuse Documentation for Python SDK Integration
Model Optimised:
  - n.a.
---
# Langfuse Documentation - Decorator-based Python Integration

# Decorator-based Python Integration and Detailled Information

# Decorator-based Python Integration

[Langfuse v3 is GA. Learn more →We've released Langfuse v3. Learn more →](/changelog/2024-12-09-Langfuse-v3-stable-release)

Docs [SDKs](/docs/sdk/overview "SDKs") PythonDecorators

# Decorator-based Python Integration

Integrate [Langfuse Tracing](/docs/tracing) into your LLM applications with the Langfuse Python SDK using the `@observe()` decorator.

The SDK supports both synchronous and asynchronous functions, automatically handling traces, spans, and generations, along with key execution details like inputs, outputs and timings. This setup allows you to concentrate on developing high-quality applications while benefitting from observability insights with minimal code. The decorator is fully interoperable with our main integrations (more on this below): [OpenAI](/docs/integrations/openai), [Langchain](/docs/integrations/langchain), [LlamaIndex](/docs/integrations/llama-index).

See the [reference](https://python.reference.langfuse.com/langfuse/decorators) for a comprehensive list of all available parameters and methods.

Want more control over the traces logged to Langfuse? Check out the [low-level Python SDK](/docs/sdk/python/low-level-sdk).

## Overview [Permalink for this section](#overview)

Decorator Integration

## Example [Permalink for this section](#example)

Simple example (decorator + OpenAI integration) from the [end-to-end example notebook](/docs/sdk/python/example):

[main.py](http://main.py)

```nextra-code
from langfuse.decorators import observe
from langfuse.openai import openai # OpenAI integration

@observe()
def story():
    return openai.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        messages=[\
          {"role": "system", "content": "You are a great storyteller."},\
          {"role": "user", "content": "Once upon a time in a galaxy far, far away..."}\
        ],
    ).choices[0].message.content

@observe()
def main():
    return story()

main()
```

*Trace in Langfuse ( [public link](https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/fac231bc-90ee-490a-aa32-78c4269474e3?observation=36544d09-dec7-48ff-88c3-6c2ae3fe2baf))*

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fpython-decorator-simple-trace.49a3968b.png&w=3840&q=75)

## Installation & setup [Permalink for this section](#installation--setup)

### Install the Langfuse Python SDK [Permalink for this section](#install-the-langfuse-python-sdk)



![](https://img.shields.io/pypi/v/langfuse?style=flat-square)



```nextra-code
pip install langfuse
```

### Add Langfuse API keys [Permalink for this section](#add-langfuse-api-keys)

If you haven’t done so yet, [sign up to Langfuse](https://cloud.langfuse.com/auth/sign-up) and obtain your API keys from the project settings. Alternatively, you can also run Langfuse locally or self-host.

Environment variableslangfuse_context.configure

os.environpython-dotenv

```nextra-code
import os

os.environ["LANGFUSE_SECRET_KEY"] = "sk-lf-..."
os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-lf-..."
# 🇪🇺 EU region
os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com"
# 🇺🇸 US region
# os.environ["LANGFUSE_HOST"] = "https://us.cloud.langfuse.com"
```

Use [`python-dotenv`](https://pypi.org/project/python-dotenv/) to load the
environment variables from a `.env` file at the root of your application.

.env

```nextra-code
LANGFUSE_SECRET_KEY="sk-lf-..."
LANGFUSE_PUBLIC_KEY="pk-lf-..."
# 🇪🇺 EU region
LANGFUSE_HOST="https://cloud.langfuse.com"
# �� US region
# LANGFUSE_HOST="https://us.cloud.langfuse.com"
```

If you prefer to set the API keys programmatically, you can do so via the `langfuse_context.configure` method. This method should be called **at the top of your application before executing any decorated functions**.

```nextra-code
from langfuse.decorators import langfuse_context

langfuse_context.configure(
    secret_key="sk-lf-...",
    public_key="pk-lf-...",
    host="https://cloud.langfuse.com", # 🇪🇺 EU region
    # host="https://us.cloud.langfuse.com" # 🇺🇸 US region
)
```

When no API keys are provided, a single warning is logged, and no traces are sent to Langfuse.

### Add the Langfuse decorator [Permalink for this section](#add-the-langfuse-decorator)

Import the `@observe()` decorator and apply it to the functions you want to trace. By default it captures:

- nesting via context vars

- timings/durations

- function name

- args and kwargs as input dict

- returned values as output

The decorator will automatically create a trace for the top-level function and spans for any nested functions. Learn more about the tracing data model [here](/docs/tracing).

```nextra-code
from langfuse.decorators import observe

@observe()
def fn():
    pass

@observe()
def main():
    fn()

main()
```

Done! ✨ Read on to learn how to capture additional information, LLM calls,
and more with Langfuse Python decorators.

⚠️

In a short-lived environment like AWS Lambda, make sure to call `flush()` before the
function terminates to avoid losing events. [Learn more](#flush).

```nextra-code
from langfuse.decorators import observe, langfuse_context

@observe()
def main():
    print("Hello, from the main function!")

main()

langfuse_context.flush()
```

## Decorator arguments [Permalink for this section](#decorator-arguments)

> See [SDK reference](https://python.reference.langfuse.com/langfuse/decorators#observe) for full details.

### Log any LLM call [Permalink for this section](#log-any-llm-call)

In addition to the native intgerations with LangChain, LlamaIndex, and OpenAI (details [below](#frameworks)), you can log any LLM call by decorating it with `@observe(as_type="generation")`. **Important:** Make sure the `as_type="generation"` decorated function is called inside another `@observe()`\-decorated function for it to have a top-level trace.

Optionally, you can parse some of the arguments to the LLM call and pass them to [`langfuse_context.update_current_observation`](#additional-attributes) to enrich the trace.

Model specific examples:

- [Mistral SDK](/guides/cookbook/integration_mistral_sdk)

- [Amazon Bedrock](/docs/integrations/amazon-bedrock)

*Example using the Anthropic SDK:*

[main.py](http://main.py)

```nextra-code
from langfuse.decorators import observe, langfuse_context
import anthropic

anthopic_client = anthropic.Anthropic()

# Wrap LLM function with decorator
@observe(as_type="generation")
def anthropic_completion(**kwargs):
  # optional, extract some fields from kwargs
  kwargs_clone = kwargs.copy()
  input = kwargs_clone.pop('messages', None)
  model = kwargs_clone.pop('model', None)
  langfuse_context.update_current_observation(
      input=input,
      model=model,
      metadata=kwargs_clone
  )

  response = anthopic_client.messages.create(**kwargs)

  # See docs for more details on token counts and usd cost in Langfuse
  # https://langfuse.com/docs/model-usage-and-cost
  langfuse_context.update_current_observation(
      usage_details={
          "input": response.usage.input_tokens,
          "output": response.usage.output_tokens
      }
  )

  # return result
  return response.content[0].text

@observe()
def main():
  return anthropic_completion(
      model="claude-3-opus-20240229",
      max_tokens=1024,
      messages=[\
          {"role": "user", "content": "Hello, Claude"}\
      ]
  )

main()
```

### Capturing of input/output [Permalink for this section](#capturing-of-inputoutput)

By default, the `@observe()` decorator captures the input arguments and output results of the function.

**You can disable this** behavior by setting the `capture_input` and `capture_output` parameters to `False`.

The decorator implementation supports capturing any serializable object as input and output such as strings, numbers, lists, dictionaries, and more. Python `generators` which are common when streaming LLM responses are supported as return values from decorated functions, but not as input arguments.

```nextra-code
from langfuse.decorators import observe

@observe(capture_input=False, capture_output=False)
def fn(secret_arg):
    return "super secret output"

fn("my secret arg")
```

You can **manually set the input and output** of the observation using `langfuse_context.update_current_observation` (details below).

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def fn(secret_arg):
    langfuse_context.update_current_observation(
        input="sanitized input", # any serializable object
        output="sanitized output", # any serializable object
    )
    return "super secret output"

fn("my secret arg")
```

This will result in a trace with only sanitized input and output, and no actual function arguments or return values.

## Decorator context [Permalink for this section](#decorator-context)

Use the `langfuse_context` object to interact with the decorator context. This object is a thread-local singleton and can be accessed from anywhere within the function context.

### Configure the Langfuse client [Permalink for this section](#configure-the-langfuse-client)

The decorator manages the Langfuse client for you. If you need to configure the client, you can do so via the `langfuse_context.configure` method **at the top of your application** before executing any decorated functions.

```nextra-code
from langfuse.decorators import langfuse_context

# Configure the Langfuse client
langfuse_context.configure(
    secret_key="sk-lf-...",
    public_key="pk-lf-...",
    httpx_client=custom_httpx_client,
    host=custom_host,
    enabled=True,
)
```

By setting the `enabled` parameter to `False`, you can disable the decorator and prevent any traces from being sent to Langfuse.

See the [API Reference](https://python.reference.langfuse.com/langfuse/decorators#LangfuseDecorator.configure) for more details on the available parameters.

### Add additional attributes to the trace and observations [Permalink for this section](#additional-attributes)

In addition to the attributes automatically captured by the decorator, you can add others to use the full features of Langfuse.

Please read the reference for more details on available parameters:

- `langfuse_context.update_current_observation` ( [reference](https://python.reference.langfuse.com/langfuse/decorators#LangfuseDecorator.update_current_observation)): Update the trace/span of the current function scope

- `langfuse_context.update_current_trace` ( [reference](https://python.reference.langfuse.com/langfuse/decorators#LangfuseDecorator.update_current_trace)): Update the trace itself, can also be called within any deeply nested span within the trace

Below is an example demonstrating how to enrich traces and observations with custom parameters:

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def deeply_nested_fn():
    # Enrich the current observation with a custom name, input, and output
    # All of these parameters override the default values captured by the decorator
    langfuse_context.update_current_observation(
        name="Deeply nested LLM call",
        input="Ping?",
        output="Pong!"
    )
    # Updates the trace, overriding the default trace name `main` (function name)
    langfuse_context.update_current_trace(
        name="Trace name set from deeply_nested_llm_call",
        session_id="1234",
        user_id="5678",
        tags=["tag1", "tag2"],
        public=True
    )
    return "output" # This output will not be captured as we have overridden it

@observe()
def nested_fn():
    # Update the current span with a custom name and level
    # Overrides the default span name
    langfuse_context.update_current_observation(
        name="Nested Span",
        level="WARNING"
    )
    deeply_nested_fn()

@observe()
def main():
    # This will be the trace as it is the highest level function
    nested_fn()

# Execute the main function to generate the enriched trace
main()
```

### Get trace URL [Permalink for this section](#get-trace-url)

You can get the URL of the current trace using `langfuse_context.get_current_trace_url()`. Works anywhere within the function context, also in deeply nested functions.

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def main():
    print(langfuse_context.get_current_trace_url())

main()
```

### Trace/observation IDs [Permalink for this section](#traceobservation-ids)

By default, Langfuse assigns random IDs to all logged events.

#### Get trace and observation IDs [Permalink for this section](#get-trace-and-observation-ids)

You can access the current trace and observation IDs from the `langfuse_context` object.

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def fn():
    print(langfuse_context.get_current_trace_id())
    print(langfuse_context.get_current_observation_id())

fn()
```

#### Set custom IDs [Permalink for this section](#set-custom-ids)

If you have your own unique ID (e.g. messageId, traceId, correlationId), you can easily set those as trace or observation IDs for effective lookups in Langfuse. Just pass the `langfuse_observation_id` keyword argument to the decorated function.

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def process_user_request(user_id, request_data, **kwargs):
    # Function logic here
    pass

@observe(**kwargs)
def main():
    process_user_request(
        "user_id",
        "request",
        langfuse_observation_id="my-custom-request-id",
    )


main(langfuse_observation_id="my-custom-request-id")
```

#### Set parent trace ID or parent span ID [Permalink for this section](#set-parent-trace-id-or-parent-span-id)

If you’d like to nest the the observations created from the decoratored function execution under an existing trace or span, you can pass the ID as a value to the `langfuse_parent_trace_id` or `langfuse_parent_observation_id` keyword argument to your decorated function. In that case, Langfuse will record that execution not under a standalone trace, but nest it under the provided entity.

This is useful for distributed tracing use-cases, where decorated function executions are running in parallel or in the background and should be associated to single existing trace.

The desired parent ID must be passed to the **top-level** decorated function
as a keyword argument, otherwise the parent ID setting will be ignored and the
node remains inside the trace in the execution context.

Passing `langfuse_parent_trace_id` is required whenever a
`langfuse_parent_observation_id` is requested.

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def process_user_request(user_id, request_data, **kwargs):
    # Function logic here
    pass

@observe(**kwargs)
def main():
    process_user_request(
        "user_id",
        "request",
        langfuse_observation_id="my-custom-request-id",
    )

# Set a parent trace id
main(
    langfuse_observation_id="my-custom-request-id",
    langfuse_parent_trace_id="some_existing_trace_id"
)

# Set a parent span id. Note that parent_trace_id must also be passed.
main(
    langfuse_observation_id="my-custom-request-id",
    langfuse_parent_trace_id="some_existing_trace_id",
    lanfuse_parent_observation_id="some_existing_span_id",
)
```

## Interoperability with framework integrations [Permalink for this section](#frameworks)

The decorator is fully interoperable with our main integrations: [OpenAI](/docs/integrations/openai), [Langchain](/docs/integrations/langchain), [LlamaIndex](/docs/integrations/llama-index). Thereby you can easily trace and evaluate functions that use (a combination of) these integrations.

### OpenAI [Permalink for this section](#openai)

The [drop-in OpenAI SDK integration](/docs/integrations/openai) is fully compatible with the `@observe()` decorator. It automatically adds a generation observation to the trace within the current context.

```nextra-code
from langfuse.decorators import observe
from langfuse.openai import openai

@observe()
def story():
    return openai.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        messages=[\
          {"role": "system", "content": "You are a great storyteller."},\
          {"role": "user", "content": "Once upon a time in a galaxy far, far away..."}\
        ],
    ).choices[0].message.content

@observe()
def main():
    return story()

main()
```

### LangChain [Permalink for this section](#langchain)

The [native LangChain integration](/docs/integrations/langchain) is fully compatible with the `@observe()` decorator. It automatically adds a generation to the trace within the current context.

`langfuse_context.get_current_langchain_handler()` exposes a callback handler scoped to the current trace context. Pass it to subsequent runs to your LangChain application to get full tracing within the scope of the current trace.

```nextra-code
from operator import itemgetter
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langfuse.decorators import observe

prompt = ChatPromptTemplate.from_template("what is the city {person} is from?")
model = ChatOpenAI()
chain = prompt | model | StrOutputParser()

@observe()
def langchain_fn(person: str):
    # Get Langchain Callback Handler scoped to the current trace context
    langfuse_handler = langfuse_context.get_current_langchain_handler()

    # Pass handler to invoke of your langchain chain/agent
    chain.invoke({"person": person}, config={"callbacks":[langfuse_handler]})

langchain_fn("John Doe")
```

### LlamaIndex [Permalink for this section](#llamaindex)

The [LlamaIndex integration](/docs/integrations/llama-index) is fully compatible with the `@observe()` decorator. It automatically adds a generation to the trace within the current context.

Via `Settings.callback_manager` you can configure the callback to use for tracing of the subsequent LlamaIndex executions. `langfuse_context.get_current_llama_index_handler()` exposes a callback handler scoped to the current trace context.

```nextra-code
from langfuse.decorators import langfuse_context, observe
from llama_index.core import Document, VectorStoreIndex
from llama_index.core import Settings
from llama_index.core.callbacks import CallbackManager

doc1 = Document(text="""
Maxwell "Max" Silverstein, a lauded movie director, screenwriter, and producer, was born on October 25, 1978, in Boston, Massachusetts. A film enthusiast from a young age, his journey began with home movies shot on a Super 8 camera. His passion led him to the University of Southern California (USC), majoring in Film Production. Eventually, he started his career as an assistant director at Paramount Pictures. Silverstein's directorial debut, “Doors Unseen,” a psychological thriller, earned him recognition at the Sundance Film Festival and marked the beginning of a successful directing career.
""")
doc2 = Document(text="""
Throughout his career, Silverstein has been celebrated for his diverse range of filmography and unique narrative technique. He masterfully blends suspense, human emotion, and subtle humor in his storylines. Among his notable works are "Fleeting Echoes," "Halcyon Dusk," and the Academy Award-winning sci-fi epic, "Event Horizon's Brink." His contribution to cinema revolves around examining human nature, the complexity of relationships, and probing reality and perception. Off-camera, he is a dedicated philanthropist living in Los Angeles with his wife and two children.
""")

@observe()
def llama_index_fn(question: str):
    # Set callback manager for LlamaIndex, will apply to all LlamaIndex executions in this function
    langfuse_handler = langfuse_context.get_current_llama_index_handler()
    Settings.callback_manager = CallbackManager([langfuse_handler])

    # Run application
    index = VectorStoreIndex.from_documents([doc1,doc2])
    response = index.as_query_engine().query(question)
    return response
```

## Adding scores [Permalink for this section](#adding-scores)

[Scores](https://langfuse.com/docs/scores/overview) are used to evaluate single observations or entire traces. They can be created via our annotation workflow in the Langfuse UI or via the SDKs.

| Parameter | Type | Optional | Description | 
|---|---|---|---|
| `name` | string | no | Identifier of the score. | 
| `value` | number | no | The value of the score. Can be any number, often standardized to 0..1 | 
| `comment` | string | yes | Additional context/explanation of the score. | 

Within the decorated contextOutside the decorated function

You can attach a score to the current observation context by calling `langfuse_context.score_current_observation`. You can also score the entire trace from anywhere inside the nesting hierarchy by calling `langfuse_context.score_current_trace`:

```nextra-code
from langfuse.decorators import langfuse_context, observe

# This will create a new span under the trace
@observe()
def nested_span():
    langfuse_context.score_current_observation(
        name="feedback-on-span",
        value=1,
        comment="I like how personalized the response is",
    )

    langfuse_context.score_current_trace(
        name="feedback-on-trace",
        value=1,
        comment="I like how personalized the response is",
    )


# This will create a new trace
@observe()
def main():
    nested_span()

main()
```

The decorators expose the trace_id and observation_id which are necessary to add scores outside of the decorated functions. This is useful whenever you want to add scores asynchronously, e.g. based on user feedback.

```nextra-code
from langfuse import Langfuse
from langfuse.decorators import langfuse_context, observe

# Create a new trace
@observe()
def main():
    trace_id = langfuse_context.get_current_trace_id()
    return "function_result", trace_id

# Execute the main function to generate a trace
_, trace_id = main()
```

```nextra-code
# Score the trace from outside the trace context using the low-level SDK
langfuse_client = Langfuse()
langfuse_client.score(
    trace_id=trace_id,
    name="user-explicit-feedback",
    value=1,
    comment="I like how personalized the response is"
)
```

## Additional configuration [Permalink for this section](#additional-configuration)

### Flush observations [Permalink for this section](#flush)

The Langfuse SDK executes network requests in the background on a separate thread for better performance of your application. This can lead to lost events in short lived environments such as AWS Lambda functions when the Python process is terminated before the SDK sent all events to our backend.

To avoid this, ensure that the `langfuse_context.flush()` method is called before termination. This method is waiting for all tasks to have completed, hence it is blocking.

### Debug mode [Permalink for this section](#debug-mode)

Enable debug mode to get verbose logs. Set the debug mode via the environment variable `LANGFUSE_DEBUG=True`.

### Sampling [Permalink for this section](#sampling)

Sampling can be controlled via the `LANGFUSE_SAMPLE_RATE` environment variable. See the [sampling documentation](/docs/tracing-features/sampling) for more details.

### Authentication check [Permalink for this section](#authentication-check)

Use `langfuse_context.auth_check()` to verify that your host and API credentials are valid. This operation is blocking and is not recommended for production use.

## Limitations [Permalink for this section](#limitations)

### Using ThreadPoolExecutors or ProcessPoolExecutors [Permalink for this section](#using-threadpoolexecutors-or-processpoolexecutors)

The decorator uses Python’s `contextvars` to store the current trace context and to ensure that the observations are correctly associated with the current execution context. However, when using Python’s ThreadPoolExecutors and ProcessPoolExecutors *and* when spawning threads from inside a trace (i.e. the executor is run inside a decorated function) the decorator will not work correctly as the `contextvars` are not correctly copied to the new threads or processes. There is an [existing issue](https://github.com/python/cpython/pull/9688#issuecomment-544304996) in Python’s standard library and a [great explanation](https://github.com/tiangolo/fastapi/issues/2776#issuecomment-776659392) in the fastapi repo that discusses this limitation.

For example when a @observe-decorated function uses a ThreadPoolExecutor to make concurrent LLM requests the context that holds important info on the nesting hierarchy (“we are inside another trace”) is not copied over correctly to the child threads. So the created generations will not be linked to the trace and be ‘orphaned’. In the UI, you will see a trace missing those generations.

When spawning threads manually with `threading.Thread` rather than via
`ThreadPoolExecutor`, contextvars are copied over correctly as no executor is
used. The decorator works as intended in this case.

There are 2 possible workarounds:

#### 1\. Pass the parent observation ID (recommended) [Permalink for this section](#1-pass-the-parent-observation-id-recommended)

The first and recommended workaround is to pass the parent observation id as a keyword argument to each multithreaded execution, thus re-establishing the link to the parent span or trace:

```nextra-code
from concurrent.futures import ThreadPoolExecutor, as_completed
from langfuse.decorators import langfuse_context, observe

@observe()
def execute_task(*args):
    return args

@observe()
def execute_groups(task_args):
    trace_id = langfuse_context.get_current_trace_id()
    observation_id = langfuse_context.get_current_observation_id()

    with ThreadPoolExecutor(3) as executor:
        futures = [\
            executor.submit(\
                execute_task,\
                *task_arg,\
                langfuse_parent_trace_id=trace_id,\
                langfuse_parent_observation_id=observation_id,\
            )\
            for task_arg in task_args\
        ]

        for future in as_completed(futures):
            future.result()

    return [f.result() for f in futures]

@observe()
def main():
    task_args = [["a", "b"], ["c", "d"]]

    execute_groups(task_args)

main()

langfuse_context.flush()
```

#### 2\. Copy over the context [Permalink for this section](#2-copy-over-the-context)

The second workaround is to manually copy over the context to the new threads or processes:

```nextra-code
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextvars import copy_context

from langfuse.decorators import langfuse_context, observe

@observe()
def execute_task(*args):
    return args

task_args = [["a", "b"], ["c", "d"]]

@observe()
def execute_groups(task_args):
    with ThreadPoolExecutor(3) as executor:
        futures = []

        for task_arg in task_args:
            ctx = copy_context()
            task = lambda p=task_arg: ctx.run(execute_task, *p)

            futures.append(executor.submit(task))

        for future in as_completed(futures):
            future.result()

    return [f.result() for f in futures]

execute_groups(task_args)

langfuse_context.flush()
```

The executions inside the ThreadPoolExecutor will now be correctly associated with the trace opened by the `execute_groups` function.

### Large input/output data [Permalink for this section](#large-inputoutput-data)

Large input/output data can lead to performance issues. We recommend disabling capturing input/output for these methods and manually add the relevant information via `langfuse_context.update_current_observation`.

Integrate Langfuse Tracing into your LLM applications with the Langfuse Python SDK using the `@observe()` decorator.

*Simple example (decorator + openai integration)*

```
from langfuse.decorators import observe
from langfuse.openai import openai # OpenAI integration

@observe()
def story():
    return openai.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        messages=[\
          {"role": "system", "content": "You are a great storyteller."},\
          {"role": "user", "content": "Once upon a time in a galaxy far, far away..."}\
        ],
    ).choices[0].message.content

@observe()
def main():
    return story()

main()

```

See [docs](https://langfuse.com/docs/sdk/python/decorators) for more information.

View Source

````
 1"""Integrate Langfuse Tracing into your LLM applications with the Langfuse Python SDK using the `@observe()` decorator.
 2
 3*Simple example (decorator + openai integration)*
 4
 5```python
 6from langfuse.decorators import observe
 7from langfuse.openai import openai # OpenAI integration
 8
 9@observe()
10def story():
11    return openai.chat.completions.create(
12        model="gpt-3.5-turbo",
13        max_tokens=100,
14        messages=[\
15          {"role": "system", "content": "You are a great storyteller."},\
16          {"role": "user", "content": "Once upon a time in a galaxy far, far away..."}\
17        ],
18    ).choices[0].message.content
19
20@observe()
21def main():
22    return story()
23
24main()
25```
26
27See [docs](https://langfuse.com/docs/sdk/python/decorators) for more information.
28"""
29
30from .langfuse_decorator import langfuse_context, observe, LangfuseDecorator
31
32__all__ = ["langfuse_context", "observe", "LangfuseDecorator"]

````

langfuse_context =
< [LangfuseDecorator](#LangfuseDecorator) object>

defobserve(func:Optional\[Callable\[~~P,~~R\]\]=None,\*,name:Optional\[str\]=None,as_type:Optional\[Literal\['generation'\]\]=None,capture_input:bool=True,capture_output:bool=True,transform_to_string:Optional\[Callable\[\[Iterable\],str\]\]=None) -> Callable\[\[Callable\[~~P,~~R\]\],Callable\[~~P,~~R\]\]:View Source

````
115    def observe(
116        self,
117        func: Optional[Callable[P, R]] = None,
118        *,
119        name: Optional[str] = None,
120        as_type: Optional[Literal["generation"]] = None,
121        capture_input: bool = True,
122        capture_output: bool = True,
123        transform_to_string: Optional[Callable[[Iterable], str]] = None,
124    ) -> Callable[[Callable[P, R]], Callable[P, R]]:
125        """Wrap a function to create and manage Langfuse tracing around its execution, supporting both synchronous and asynchronous functions.
126
127        It captures the function's execution context, including start/end times, input/output data, and automatically handles trace/span generation within the Langfuse observation context.
128        In case of an exception, the observation is updated with error details. The top-most decorated function is treated as a trace, with nested calls captured as spans or generations.
129
130        Attributes:
131            name (Optional[str]): Name of the created trace or span. Overwrites the function name as the default used for the trace or span name.
132            as_type (Optional[Literal["generation"]]): Specify "generation" to treat the observation as a generation type, suitable for language model invocations.
133            capture_input (bool): If True, captures the args and kwargs of the function as input. Default is True.
134            capture_output (bool): If True, captures the return value of the function as output. Default is True.
135            transform_to_string (Optional[Callable[[Iterable], str]]): When the decorated function returns a generator, this function transforms yielded values into a string representation for output capture
136
137        Returns:
138            Callable: A wrapped version of the original function that, upon execution, is automatically observed and managed by Langfuse.
139
140        Example:
141            For general tracing (functions/methods):
142            ```python
143            @observe()
144            def your_function(args):
145                # Your implementation here
146            ```
147            For observing language model generations:
148            ```python
149            @observe(as_type="generation")
150            def your_LLM_function(args):
151                # Your LLM invocation here
152            ```
153
154        Raises:
155            Exception: Propagates exceptions from the wrapped function after logging and updating the observation with error details.
156
157        Note:
158        - Automatic observation ID and context management is provided. Optionally, an observation ID can be specified using the `langfuse_observation_id` keyword when calling the wrapped function.
159        - To update observation or trace parameters (e.g., metadata, session_id), use `langfuse.update_current_observation` and `langfuse.update_current_trace` methods within the wrapped function.
160        """
161
162        def decorator(func: Callable[P, R]) -> Callable[P, R]:
163            return (
164                self._async_observe(
165                    func,
166                    name=name,
167                    as_type=as_type,
168                    capture_input=capture_input,
169                    capture_output=capture_output,
170                    transform_to_string=transform_to_string,
171                )
172                if asyncio.iscoroutinefunction(func)
173                else self._sync_observe(
174                    func,
175                    name=name,
176                    as_type=as_type,
177                    capture_input=capture_input,
178                    capture_output=capture_output,
179                    transform_to_string=transform_to_string,
180                )
181            )
182
183        """
184        If the decorator is called without arguments, return the decorator function itself.
185        This allows the decorator to be used with or without arguments.
186        Python calls the decorator function with the decorated function as an argument when the decorator is used without arguments.
187        """
188        if func is None:
189            return decorator
190        else:
191            return decorator(func)

````

Wrap a function to create and manage Langfuse tracing around its execution, supporting both synchronous and asynchronous functions.

It captures the function's execution context, including start/end times, input/output data, and automatically handles trace/span generation within the Langfuse observation context.
In case of an exception, the observation is updated with error details. The top-most decorated function is treated as a trace, with nested calls captured as spans or generations.

###### Attributes:

- **name (Optional\[str\]):** Name of the created trace or span. Overwrites the function name as the default used for the trace or span name.

- **as_type (Optional\[Literal\["generation"\]\]):** Specify "generation" to treat the observation as a generation type, suitable for language model invocations.

- **capture_input (bool):** If True, captures the args and kwargs of the function as input. Default is True.

- **capture_output (bool):** If True, captures the return value of the function as output. Default is True.

- **transform_to_string (Optional\[Callable\[\[Iterable\], str\]\]):** When the decorated function returns a generator, this function transforms yielded values into a string representation for output capture

###### Returns:

> Callable: A wrapped version of the original function that, upon execution, is automatically observed and managed by Langfuse.

###### Example:

> For general tracing (functions/methods):
>
> ```
> @observe()
> def your_function(args):
>     # Your implementation here
> 
> ```
>
> For observing language model generations:
>
> ```
> @observe(as_type="generation")
> def your_LLM_function(args):
>     # Your LLM invocation here
> 
> ```

###### Raises:

- **Exception:** Propagates exceptions from the wrapped function after logging and updating the observation with error details.

Note:

- Automatic observation ID and context management is provided. Optionally, an observation ID can be specified using the `langfuse_observation_id` keyword when calling the wrapped function.

- To update observation or trace parameters (e.g., metadata, session_id), use `langfuse.update_current_observation` and `langfuse.update_current_trace` methods within the wrapped function.

classLangfuseDecorator:

View Source

````
  94class LangfuseDecorator:
  95    _log = logging.getLogger("langfuse")
  96
  97    # Type overload for observe decorator with no arguments
  98    @overload
  99    def observe(self, func: F) -> F: ...
 100
 101    # Type overload for observe decorator with arguments
 102    @overload
 103    def observe(
 104        self,
 105        func: None = None,
 106        *,
 107        name: Optional[str] = None,
 108        as_type: Optional[Literal["generation"]] = None,
 109        capture_input: bool = True,
 110        capture_output: bool = True,
 111        transform_to_string: Optional[Callable[[Iterable], str]] = None,
 112    ) -> Callable[[Callable[P, R]], Callable[P, R]]: ...
 113
 114    # Implementation of observe decorator
 115    def observe(
 116        self,
 117        func: Optional[Callable[P, R]] = None,
 118        *,
 119        name: Optional[str] = None,
 120        as_type: Optional[Literal["generation"]] = None,
 121        capture_input: bool = True,
 122        capture_output: bool = True,
 123        transform_to_string: Optional[Callable[[Iterable], str]] = None,
 124    ) -> Callable[[Callable[P, R]], Callable[P, R]]:
 125        """Wrap a function to create and manage Langfuse tracing around its execution, supporting both synchronous and asynchronous functions.
 126
 127        It captures the function's execution context, including start/end times, input/output data, and automatically handles trace/span generation within the Langfuse observation context.
 128        In case of an exception, the observation is updated with error details. The top-most decorated function is treated as a trace, with nested calls captured as spans or generations.
 129
 130        Attributes:
 131            name (Optional[str]): Name of the created trace or span. Overwrites the function name as the default used for the trace or span name.
 132            as_type (Optional[Literal["generation"]]): Specify "generation" to treat the observation as a generation type, suitable for language model invocations.
 133            capture_input (bool): If True, captures the args and kwargs of the function as input. Default is True.
 134            capture_output (bool): If True, captures the return value of the function as output. Default is True.
 135            transform_to_string (Optional[Callable[[Iterable], str]]): When the decorated function returns a generator, this function transforms yielded values into a string representation for output capture
 136
 137        Returns:
 138            Callable: A wrapped version of the original function that, upon execution, is automatically observed and managed by Langfuse.
 139
 140        Example:
 141            For general tracing (functions/methods):
 142            ```python
 143            @observe()
 144            def your_function(args):
 145                # Your implementation here
 146            ```
 147            For observing language model generations:
 148            ```python
 149            @observe(as_type="generation")
 150            def your_LLM_function(args):
 151                # Your LLM invocation here
 152            ```
 153
 154        Raises:
 155            Exception: Propagates exceptions from the wrapped function after logging and updating the observation with error details.
 156
 157        Note:
 158        - Automatic observation ID and context management is provided. Optionally, an observation ID can be specified using the `langfuse_observation_id` keyword when calling the wrapped function.
 159        - To update observation or trace parameters (e.g., metadata, session_id), use `langfuse.update_current_observation` and `langfuse.update_current_trace` methods within the wrapped function.
 160        """
 161
 162        def decorator(func: Callable[P, R]) -> Callable[P, R]:
 163            return (
 164                self._async_observe(
 165                    func,
 166                    name=name,
 167                    as_type=as_type,
 168                    capture_input=capture_input,
 169                    capture_output=capture_output,
 170                    transform_to_string=transform_to_string,
 171                )
 172                if asyncio.iscoroutinefunction(func)
 173                else self._sync_observe(
 174                    func,
 175                    name=name,
 176                    as_type=as_type,
 177                    capture_input=capture_input,
 178                    capture_output=capture_output,
 179                    transform_to_string=transform_to_string,
 180                )
 181            )
 182
 183        """
 184        If the decorator is called without arguments, return the decorator function itself.
 185        This allows the decorator to be used with or without arguments.
 186        Python calls the decorator function with the decorated function as an argument when the decorator is used without arguments.
 187        """
 188        if func is None:
 189            return decorator
 190        else:
 191            return decorator(func)
 192
 193    def _async_observe(
 194        self,
 195        func: F,
 196        *,
 197        name: Optional[str],
 198        as_type: Optional[Literal["generation"]],
 199        capture_input: bool,
 200        capture_output: bool,
 201        transform_to_string: Optional[Callable[[Iterable], str]] = None,
 202    ) -> F:
 203        @wraps(func)
 204        async def async_wrapper(*args, **kwargs):
 205            observation = self._prepare_call(
 206                name=name or func.__name__,
 207                as_type=as_type,
 208                capture_input=capture_input,
 209                is_method=self._is_method(func),
 210                func_args=args,
 211                func_kwargs=kwargs,
 212            )
 213            result = None
 214
 215            try:
 216                result = await func(*args, **kwargs)
 217            except Exception as e:
 218                self._handle_exception(observation, e)
 219            finally:
 220                result = self._finalize_call(
 221                    observation, result, capture_output, transform_to_string
 222                )
 223
 224                # Returning from finally block may swallow errors, so only return if result is not None
 225                if result is not None:
 226                    return result
 227
 228        return cast(F, async_wrapper)
 229
 230    def _sync_observe(
 231        self,
 232        func: F,
 233        *,
 234        name: Optional[str],
 235        as_type: Optional[Literal["generation"]],
 236        capture_input: bool,
 237        capture_output: bool,
 238        transform_to_string: Optional[Callable[[Iterable], str]] = None,
 239    ) -> F:
 240        @wraps(func)
 241        def sync_wrapper(*args, **kwargs):
 242            observation = self._prepare_call(
 243                name=name or func.__name__,
 244                as_type=as_type,
 245                capture_input=capture_input,
 246                is_method=self._is_method(func),
 247                func_args=args,
 248                func_kwargs=kwargs,
 249            )
 250            result = None
 251
 252            try:
 253                result = func(*args, **kwargs)
 254            except Exception as e:
 255                self._handle_exception(observation, e)
 256            finally:
 257                result = self._finalize_call(
 258                    observation, result, capture_output, transform_to_string
 259                )
 260
 261                # Returning from finally block may swallow errors, so only return if result is not None
 262                if result is not None:
 263                    return result
 264
 265        return cast(F, sync_wrapper)
 266
 267    @staticmethod
 268    def _is_method(func: Callable) -> bool:
 269        """Check if a callable is likely an class or instance method based on its signature.
 270
 271        This method inspects the given callable's signature for the presence of a 'cls' or 'self' parameter, which is conventionally used for class and instance methods in Python classes. It returns True if 'class' or 'self' is found among the parameters, suggesting the callable is a method.
 272
 273        Note: This method relies on naming conventions and may not accurately identify instance methods if unconventional parameter names are used or if static or class methods incorrectly include a 'self' or 'cls' parameter. Additionally, during decorator execution, inspect.ismethod does not work as expected because the function has not yet been bound to an instance; it is still a function, not a method. This check attempts to infer method status based on signature, which can be useful in decorator contexts where traditional method identification techniques fail.
 274
 275        Returns:
 276        bool: True if 'cls' or 'self' is in the callable's parameters, False otherwise.
 277        """
 278        return (
 279            "self" in inspect.signature(func).parameters
 280            or "cls" in inspect.signature(func).parameters
 281        )
 282
 283    def _prepare_call(
 284        self,
 285        *,
 286        name: str,
 287        as_type: Optional[Literal["generation"]],
 288        capture_input: bool,
 289        is_method: bool = False,
 290        func_args: Tuple = (),
 291        func_kwargs: Dict = {},
 292    ) -> Optional[\
 293        Union[StatefulSpanClient, StatefulTraceClient, StatefulGenerationClient]\
 294    ]:
 295        try:
 296            stack = _observation_stack_context.get().copy()
 297            parent = stack[-1] if stack else None
 298
 299            # Collect default observation data
 300            observation_id = func_kwargs.pop("langfuse_observation_id", None)
 301            provided_parent_trace_id = func_kwargs.pop("langfuse_parent_trace_id", None)
 302            provided_parent_observation_id = func_kwargs.pop(
 303                "langfuse_parent_observation_id", None
 304            )
 305
 306            id = str(observation_id) if observation_id else None
 307            start_time = _get_timestamp()
 308
 309            input = (
 310                self._get_input_from_func_args(
 311                    is_method=is_method,
 312                    func_args=func_args,
 313                    func_kwargs=func_kwargs,
 314                )
 315                if capture_input
 316                else None
 317            )
 318
 319            params = {
 320                "id": id,
 321                "name": name,
 322                "start_time": start_time,
 323                "input": input,
 324            }
 325
 326            # Handle user-providedparent trace ID and observation ID
 327            if parent and (provided_parent_trace_id or provided_parent_observation_id):
 328                self._log.warning(
 329                    "Ignoring langfuse_parent_trace_id and/or langfuse_parent_observation_id as they can be only set in the top-level decorated function."
 330                )
 331
 332            elif provided_parent_observation_id and not provided_parent_trace_id:
 333                self._log.warning(
 334                    "Ignoring langfuse_parent_observation_id as langfuse_parent_trace_id is not set."
 335                )
 336
 337            elif provided_parent_observation_id and (
 338                provided_parent_observation_id != provided_parent_trace_id
 339            ):
 340                parent = StatefulSpanClient(
 341                    id=provided_parent_observation_id,
 342                    trace_id=provided_parent_trace_id,
 343                    task_manager=self.client_instance.task_manager,
 344                    client=self.client_instance.client,
 345                    state_type=StateType.OBSERVATION,
 346                )
 347                self._set_root_trace_id(provided_parent_trace_id)
 348
 349            elif provided_parent_trace_id:
 350                parent = StatefulTraceClient(
 351                    id=provided_parent_trace_id,
 352                    trace_id=provided_parent_trace_id,
 353                    task_manager=self.client_instance.task_manager,
 354                    client=self.client_instance.client,
 355                    state_type=StateType.TRACE,
 356                )
 357                self._set_root_trace_id(provided_parent_trace_id)
 358
 359            # Create observation
 360            if parent and as_type == "generation":
 361                observation = parent.generation(**params)
 362            elif as_type == "generation":
 363                # Create wrapper trace if generation is top-level
 364                # Do not add wrapper trace to stack, as it does not have a corresponding end that will pop it off again
 365                trace = self.client_instance.trace(
 366                    id=id, name=name, start_time=start_time
 367                )
 368                self._set_root_trace_id(trace.id)
 369
 370                observation = self.client_instance.generation(
 371                    name=name, start_time=start_time, input=input, trace_id=trace.id
 372                )
 373            elif parent:
 374                observation = parent.span(**params)
 375            else:
 376                params["id"] = _root_trace_id_context.get() or params["id"]
 377                observation = self.client_instance.trace(**params)
 378
 379            _observation_stack_context.set(stack + [observation])
 380
 381            return observation
 382        except Exception as e:
 383            self._log.error(f"Failed to prepare observation: {e}")
 384
 385    def _get_input_from_func_args(
 386        self,
 387        *,
 388        is_method: bool = False,
 389        func_args: Tuple = (),
 390        func_kwargs: Dict = {},
 391    ) -> Any:
 392        # Remove implicitly passed "self" or "cls" argument for instance or class methods
 393        logged_args = func_args[1:] if is_method else func_args
 394        raw_input = {
 395            "args": logged_args,
 396            "kwargs": func_kwargs,
 397        }
 398
 399        # Serialize and deserialize to ensure proper JSON serialization.
 400        # Objects are later serialized again so deserialization is necessary here to avoid unnecessary escaping of quotes.
 401        return json.loads(json.dumps(raw_input, cls=EventSerializer))
 402
 403    def _finalize_call(
 404        self,
 405        observation: Optional[\
 406            Union[\
 407                StatefulSpanClient,\
 408                StatefulTraceClient,\
 409                StatefulGenerationClient,\
 410            ]\
 411        ],
 412        result: Any,
 413        capture_output: bool,
 414        transform_to_string: Optional[Callable[[Iterable], str]] = None,
 415    ):
 416        if inspect.isgenerator(result):
 417            return self._wrap_sync_generator_result(
 418                observation, result, capture_output, transform_to_string
 419            )
 420        elif inspect.isasyncgen(result):
 421            return self._wrap_async_generator_result(
 422                observation, result, capture_output, transform_to_string
 423            )
 424
 425        else:
 426            return self._handle_call_result(observation, result, capture_output)
 427
 428    def _handle_call_result(
 429        self,
 430        observation: Optional[\
 431            Union[\
 432                StatefulSpanClient,\
 433                StatefulTraceClient,\
 434                StatefulGenerationClient,\
 435            ]\
 436        ],
 437        result: Any,
 438        capture_output: bool,
 439    ):
 440        try:
 441            if observation is None:
 442                raise ValueError("No observation found in the current context")
 443
 444            # Collect final observation data
 445            observation_params = self._pop_observation_params_from_context(
 446                observation.id
 447            )
 448
 449            end_time = observation_params["end_time"] or _get_timestamp()
 450
 451            output = observation_params["output"] or (
 452                # Serialize and deserialize to ensure proper JSON serialization.
 453                # Objects are later serialized again so deserialization is necessary here to avoid unnecessary escaping of quotes.
 454                json.loads(
 455                    json.dumps(
 456                        result if result and capture_output else None,
 457                        cls=EventSerializer,
 458                    )
 459                )
 460            )
 461
 462            observation_params.update(end_time=end_time, output=output)
 463
 464            if isinstance(observation, (StatefulSpanClient, StatefulGenerationClient)):
 465                observation.end(**observation_params)
 466            elif isinstance(observation, StatefulTraceClient):
 467                observation.update(**observation_params)
 468
 469            # Remove observation from top of stack
 470            stack = _observation_stack_context.get()
 471            _observation_stack_context.set(stack[:-1])
 472
 473            # Update trace that was provided directly and not part of the observation stack
 474            if not _observation_stack_context.get() and (
 475                provided_trace_id := _root_trace_id_context.get()
 476            ):
 477                observation_params = self._pop_observation_params_from_context(
 478                    provided_trace_id
 479                )
 480
 481                has_updates = any(observation_params.values())
 482
 483                if has_updates:
 484                    trace_client = StatefulTraceClient(
 485                        id=provided_trace_id,
 486                        trace_id=provided_trace_id,
 487                        task_manager=self.client_instance.task_manager,
 488                        client=self.client_instance.client,
 489                        state_type=StateType.TRACE,
 490                    )
 491                    trace_client.update(**observation_params)
 492
 493        except Exception as e:
 494            self._log.error(f"Failed to finalize observation: {e}")
 495
 496        finally:
 497            # Clear the context trace ID to avoid leaking to next execution
 498            if not _observation_stack_context.get():
 499                _root_trace_id_context.set(None)
 500
 501            return result
 502
 503    def _handle_exception(
 504        self,
 505        observation: Optional[\
 506            Union[StatefulSpanClient, StatefulTraceClient, StatefulGenerationClient]\
 507        ],
 508        e: Exception,
 509    ):
 510        if observation:
 511            _observation_params_context.get()[observation.id].update(
 512                level="ERROR", status_message=str(e)
 513            )
 514        raise e
 515
 516    def _wrap_sync_generator_result(
 517        self,
 518        observation: Optional[\
 519            Union[\
 520                StatefulSpanClient,\
 521                StatefulTraceClient,\
 522                StatefulGenerationClient,\
 523            ]\
 524        ],
 525        generator: Generator,
 526        capture_output: bool,
 527        transform_to_string: Optional[Callable[[Iterable], str]] = None,
 528    ):
 529        items = []
 530
 531        try:
 532            for item in generator:
 533                items.append(item)
 534
 535                yield item
 536
 537        finally:
 538            output = items
 539
 540            if transform_to_string is not None:
 541                output = transform_to_string(items)
 542
 543            elif all(isinstance(item, str) for item in items):
 544                output = "".join(items)
 545
 546            self._handle_call_result(observation, output, capture_output)
 547
 548    async def _wrap_async_generator_result(
 549        self,
 550        observation: Optional[\
 551            Union[\
 552                StatefulSpanClient,\
 553                StatefulTraceClient,\
 554                StatefulGenerationClient,\
 555            ]\
 556        ],
 557        generator: AsyncGenerator,
 558        capture_output: bool,
 559        transform_to_string: Optional[Callable[[Iterable], str]] = None,
 560    ) -> AsyncGenerator:
 561        items = []
 562
 563        try:
 564            async for item in generator:
 565                items.append(item)
 566
 567                yield item
 568
 569        finally:
 570            output = items
 571
 572            if transform_to_string is not None:
 573                output = transform_to_string(items)
 574
 575            elif all(isinstance(item, str) for item in items):
 576                output = "".join(items)
 577
 578            self._handle_call_result(observation, output, capture_output)
 579
 580    def get_current_llama_index_handler(self):
 581        """Retrieve the current LlamaIndexCallbackHandler associated with the most recent observation in the observation stack.
 582
 583        This method fetches the current observation from the observation stack and returns a LlamaIndexCallbackHandler initialized with this observation.
 584        It is intended to be used within the context of a trace, allowing access to a callback handler for operations that require interaction with the LlamaIndex API based on the current observation context.
 585
 586        See the Langfuse documentation for more information on integrating the LlamaIndexCallbackHandler.
 587
 588        Returns:
 589            LlamaIndexCallbackHandler or None: Returns a LlamaIndexCallbackHandler instance if there is an active observation in the current context; otherwise, returns None if no observation is found.
 590
 591        Note:
 592            - This method should be called within the context of a trace (i.e., within a function wrapped by @observe) to ensure that an observation context exists.
 593            - If no observation is found in the current context (e.g., if called outside of a trace or if the observation stack is empty), the method logs a warning and returns None.
 594        """
 595        try:
 596            from langfuse.llama_index import LlamaIndexCallbackHandler
 597        except ImportError:
 598            self._log.error(
 599                "LlamaIndexCallbackHandler is not available, most likely because llama-index is not installed. pip install llama-index"
 600            )
 601
 602            return None
 603
 604        stack = _observation_stack_context.get()
 605        observation = stack[-1] if stack else None
 606
 607        if observation is None:
 608            self._log.warning("No observation found in the current context")
 609
 610            return None
 611
 612        if isinstance(observation, StatefulGenerationClient):
 613            self._log.warning(
 614                "Current observation is of type GENERATION, LlamaIndex handler is not supported for this type of observation"
 615            )
 616
 617            return None
 618
 619        callback_handler = LlamaIndexCallbackHandler()
 620        callback_handler.set_root(observation)
 621
 622        return callback_handler
 623
 624    def get_current_langchain_handler(self):
 625        """Retrieve the current LangchainCallbackHandler associated with the most recent observation in the observation stack.
 626
 627        This method fetches the current observation from the observation stack and returns a LangchainCallbackHandler initialized with this observation.
 628        It is intended to be used within the context of a trace, allowing access to a callback handler for operations that require interaction with Langchain based on the current observation context.
 629
 630        See the Langfuse documentation for more information on integrating the LangchainCallbackHandler.
 631
 632        Returns:
 633            LangchainCallbackHandler or None: Returns a LangchainCallbackHandler instance if there is an active observation in the current context; otherwise, returns None if no observation is found.
 634
 635        Note:
 636            - This method should be called within the context of a trace (i.e., within a function wrapped by @observe) to ensure that an observation context exists.
 637            - If no observation is found in the current context (e.g., if called outside of a trace or if the observation stack is empty), the method logs a warning and returns None.
 638        """
 639        stack = _observation_stack_context.get()
 640        observation = stack[-1] if stack else None
 641
 642        if observation is None:
 643            self._log.warning("No observation found in the current context")
 644
 645            return None
 646
 647        if isinstance(observation, StatefulGenerationClient):
 648            self._log.warning(
 649                "Current observation is of type GENERATION, Langchain handler is not supported for this type of observation"
 650            )
 651
 652            return None
 653
 654        return observation.get_langchain_handler()
 655
 656    def get_current_trace_id(self):
 657        """Retrieve the ID of the current trace from the observation stack context.
 658
 659        This method examines the observation stack to find the root trace and returns its ID. It is useful for operations that require the trace ID,
 660        such as setting trace parameters or querying trace information. The trace ID is typically the ID of the first observation in the stack,
 661        representing the entry point of the traced execution context. If you have provided a langfuse_parent_trace_id directly, it will return that instead.
 662
 663        Returns:
 664            str or None: The ID of the current trace if available; otherwise, None. A return value of None indicates that there is no active trace in the current context,
 665            possibly due to the method being called outside of any @observe-decorated function execution.
 666
 667        Note:
 668            - This method should be called within the context of a trace (i.e., inside a function wrapped with the @observe decorator) to ensure that a current trace is indeed present and its ID can be retrieved.
 669            - If called outside of a trace context, or if the observation stack has somehow been corrupted or improperly managed, this method will log a warning and return None, indicating the absence of a traceable context.
 670        """
 671        context_trace_id = _root_trace_id_context.get()
 672        if context_trace_id:
 673            return context_trace_id
 674
 675        stack = _observation_stack_context.get()
 676        should_log_warning = self._get_caller_module_name() != "langfuse.openai"
 677
 678        if not stack:
 679            if should_log_warning:
 680                self._log.warning("No trace found in the current context")
 681
 682            return None
 683
 684        return stack[0].id
 685
 686    def _get_caller_module_name(self):
 687        try:
 688            caller_module = inspect.getmodule(inspect.stack()[2][0])
 689        except Exception as e:
 690            self._log.warning(f"Failed to get caller module: {e}")
 691
 692            return None
 693
 694        return caller_module.__name__ if caller_module else None
 695
 696    def get_current_trace_url(self) -> Optional[str]:
 697        """Retrieve the URL of the current trace in context.
 698
 699        Returns:
 700            str or None: The URL of the current trace if available; otherwise, None. A return value of None indicates that there is no active trace in the current context,
 701            possibly due to the method being called outside of any @observe-decorated function execution.
 702
 703        Note:
 704            - This method should be called within the context of a trace (i.e., inside a function wrapped with the @observe decorator) to ensure that a current trace is indeed present and its ID can be retrieved.
 705            - If called outside of a trace context, or if the observation stack has somehow been corrupted or improperly managed, this method will log a warning and return None, indicating the absence of a traceable context.
 706        """
 707        try:
 708            trace_id = self.get_current_trace_id()
 709
 710            if not trace_id:
 711                raise ValueError("No trace found in the current context")
 712
 713            return f"{self.client_instance.client._client_wrapper._base_url}/trace/{trace_id}"
 714
 715        except Exception as e:
 716            self._log.error(f"Failed to get current trace URL: {e}")
 717
 718            return None
 719
 720    def get_current_observation_id(self):
 721        """Retrieve the ID of the current observation in context.
 722
 723        Returns:
 724            str or None: The ID of the current observation if available; otherwise, None. A return value of None indicates that there is no active trace or observation in the current context,
 725            possibly due to the method being called outside of any @observe-decorated function execution.
 726
 727        Note:
 728            - This method should be called within the context of a trace or observation (i.e., inside a function wrapped with the @observe decorator) to ensure that a current observation is indeed present and its ID can be retrieved.
 729            - If called outside of a trace or observation context, or if the observation stack has somehow been corrupted or improperly managed, this method will log a warning and return None, indicating the absence of a traceable context.
 730            - If called at the top level of a trace, it will return the trace ID.
 731        """
 732        stack = _observation_stack_context.get()
 733        should_log_warning = self._get_caller_module_name() != "langfuse.openai"
 734
 735        if not stack:
 736            if should_log_warning:
 737                self._log.warning("No observation found in the current context")
 738
 739            return None
 740
 741        return stack[-1].id
 742
 743    def update_current_trace(
 744        self,
 745        name: Optional[str] = None,
 746        input: Optional[Any] = None,
 747        output: Optional[Any] = None,
 748        user_id: Optional[str] = None,
 749        session_id: Optional[str] = None,
 750        version: Optional[str] = None,
 751        release: Optional[str] = None,
 752        metadata: Optional[Any] = None,
 753        tags: Optional[List[str]] = None,
 754        public: Optional[bool] = None,
 755    ):
 756        """Set parameters for the current trace, updating the trace's metadata and context information.
 757
 758        This method allows for dynamically updating the trace parameters at any point during the execution of a trace.
 759        It updates the parameters of the current trace based on the provided arguments. These parameters include metadata, session information,
 760        and other trace attributes that can be useful for categorization, filtering, and analysis in the Langfuse UI.
 761
 762        Arguments:
 763            name (Optional[str]): Identifier of the trace. Useful for sorting/filtering in the UI..
 764            input (Optional[Any]): The input parameters of the trace, providing context about the observed operation or function call.
 765            output (Optional[Any]): The output or result of the trace
 766            user_id (Optional[str]): The id of the user that triggered the execution. Used to provide user-level analytics.
 767            session_id (Optional[str]): Used to group multiple traces into a session in Langfuse. Use your own session/thread identifier.
 768            version (Optional[str]): The version of the trace type. Used to understand how changes to the trace type affect metrics. Useful in debugging.
 769            release (Optional[str]): The release identifier of the current deployment. Used to understand how changes of different deployments affect metrics. Useful in debugging.
 770            metadata (Optional[Any]): Additional metadata of the trace. Can be any JSON object. Metadata is merged when being updated via the API.
 771            tags (Optional[List[str]]): Tags are used to categorize or label traces. Traces can be filtered by tags in the Langfuse UI and GET API.
 772
 773        Returns:
 774            None
 775
 776        Note:
 777            - This method should be used within the context of an active trace, typically within a function that is being traced using the @observe decorator.
 778            - The method updates the trace parameters for the currently executing trace. In nested trace scenarios, it affects the most recent trace context.
 779            - If called outside of an active trace context, a warning is logged, and a ValueError is raised to indicate the absence of a traceable context.
 780        """
 781        trace_id = self.get_current_trace_id()
 782
 783        if trace_id is None:
 784            self._log.warning("No trace found in the current context")
 785
 786            return
 787
 788        params_to_update = {
 789            k: v
 790            for k, v in {
 791                "name": name,
 792                "input": input,
 793                "output": output,
 794                "user_id": user_id,
 795                "session_id": session_id,
 796                "version": version,
 797                "release": release,
 798                "metadata": metadata,
 799                "tags": tags,
 800                "public": public,
 801            }.items()
 802            if v is not None
 803        }
 804
 805        _observation_params_context.get()[trace_id].update(params_to_update)
 806
 807    def update_current_observation(
 808        self,
 809        *,
 810        input: Optional[Any] = None,
 811        output: Optional[Any] = None,
 812        name: Optional[str] = None,
 813        version: Optional[str] = None,
 814        metadata: Optional[Any] = None,
 815        start_time: Optional[datetime] = None,
 816        end_time: Optional[datetime] = None,
 817        release: Optional[str] = None,
 818        tags: Optional[List[str]] = None,
 819        user_id: Optional[str] = None,
 820        session_id: Optional[str] = None,
 821        level: Optional[SpanLevel] = None,
 822        status_message: Optional[str] = None,
 823        completion_start_time: Optional[datetime] = None,
 824        model: Optional[str] = None,
 825        model_parameters: Optional[Dict[str, MapValue]] = None,
 826        usage: Optional[Union[BaseModel, ModelUsage]] = None,
 827        prompt: Optional[PromptClient] = None,
 828        public: Optional[bool] = None,
 829    ):
 830        """Update parameters for the current observation within an active trace context.
 831
 832        This method dynamically adjusts the parameters of the most recent observation on the observation stack.
 833        It allows for the enrichment of observation data with additional details such as input parameters, output results, metadata, and more,
 834        enhancing the observability and traceability of the execution context.
 835
 836        Note that if a param is not available on a specific observation type, it will be ignored.
 837
 838        Shared params:
 839            - `input` (Optional[Any]): The input parameters of the trace or observation, providing context about the observed operation or function call.
 840            - `output` (Optional[Any]): The output or result of the trace or observation
 841            - `name` (Optional[str]): Identifier of the trace or observation. Useful for sorting/filtering in the UI.
 842            - `metadata` (Optional[Any]): Additional metadata of the trace. Can be any JSON object. Metadata is merged when being updated via the API.
 843            - `start_time` (Optional[datetime]): The start time of the observation, allowing for custom time range specification.
 844            - `end_time` (Optional[datetime]): The end time of the observation, enabling precise control over the observation duration.
 845            - `version` (Optional[str]): The version of the trace type. Used to understand how changes to the trace type affect metrics. Useful in debugging.
 846
 847        Trace-specific params:
 848            - `user_id` (Optional[str]): The id of the user that triggered the execution. Used to provide user-level analytics.
 849            - `session_id` (Optional[str]): Used to group multiple traces into a session in Langfuse. Use your own session/thread identifier.
 850            - `release` (Optional[str]): The release identifier of the current deployment. Used to understand how changes of different deployments affect metrics. Useful in debugging.
 851            - `tags` (Optional[List[str]]): Tags are used to categorize or label traces. Traces can be filtered by tags in the Langfuse UI and GET API.
 852            - `public` (Optional[bool]): You can make a trace public to share it via a public link. This allows others to view the trace without needing to log in or be members of your Langfuse project.
 853
 854        Span-specific params:
 855            - `level` (Optional[SpanLevel]): The severity or importance level of the observation, such as "INFO", "WARNING", or "ERROR".
 856            - `status_message` (Optional[str]): A message or description associated with the observation's status, particularly useful for error reporting.
 857
 858        Generation-specific params:
 859            - `completion_start_time` (Optional[datetime]): The time at which the completion started (streaming). Set it to get latency analytics broken down into time until completion started and completion duration.
 860            - `model_parameters` (Optional[Dict[str, MapValue]]): The parameters of the model used for the generation; can be any key-value pairs.
 861            - `usage` (Optional[Union[BaseModel, ModelUsage]]): The usage object supports the OpenAi structure with {promptTokens, completionTokens, totalTokens} and a more generic version {input, output, total, unit, inputCost, outputCost, totalCost} where unit can be of value "TOKENS", "CHARACTERS", "MILLISECONDS", "SECONDS", or "IMAGES". Refer to the docs on how to automatically infer token usage and costs in Langfuse.
 862            - `prompt`(Optional[PromptClient]): The prompt object used for the generation.
 863
 864        Returns:
 865            None
 866
 867        Raises:
 868            ValueError: If no current observation is found in the context, indicating that this method was called outside of an observation's execution scope.
 869
 870        Note:
 871            - This method is intended to be used within the context of an active observation, typically within a function wrapped by the @observe decorator.
 872            - It updates the parameters of the most recently created observation on the observation stack. Care should be taken in nested observation contexts to ensure the updates are applied as intended.
 873            - Parameters set to `None` will not overwrite existing values for those parameters. This behavior allows for selective updates without clearing previously set information.
 874        """
 875        stack = _observation_stack_context.get()
 876        observation = stack[-1] if stack else None
 877
 878        if not observation:
 879            self._log.warning("No observation found in the current context")
 880
 881            return
 882
 883        update_params = {
 884            k: v
 885            for k, v in {
 886                "input": input,
 887                "output": output,
 888                "name": name,
 889                "version": version,
 890                "metadata": metadata,
 891                "start_time": start_time,
 892                "end_time": end_time,
 893                "release": release,
 894                "tags": tags,
 895                "user_id": user_id,
 896                "session_id": session_id,
 897                "level": level,
 898                "status_message": status_message,
 899                "completion_start_time": completion_start_time,
 900                "model": model,
 901                "model_parameters": model_parameters,
 902                "usage": usage,
 903                "prompt": prompt,
 904                "public": public,
 905            }.items()
 906            if v is not None
 907        }
 908
 909        _observation_params_context.get()[observation.id].update(update_params)
 910
 911    def score_current_observation(
 912        self,
 913        *,
 914        name: str,
 915        value: Union[float, str],
 916        data_type: Optional[ScoreDataType] = None,
 917        comment: Optional[str] = None,
 918        id: Optional[str] = None,
 919        config_id: Optional[str] = None,
 920    ):
 921        """Score the current observation within an active trace. If called on the top level of a trace, it will score the trace.
 922
 923        Arguments:
 924            name (str): The name of the score metric. This should be a clear and concise identifier for the metric being recorded.
 925            value (float): The numerical value of the score. This could represent performance metrics, error rates, or any other quantifiable measure.
 926            data_type (Optional[ScoreDataType]): The data type of the score. When not set, the data type is inferred from the score config's data type, when present.
 927              When no config is set, the data type is inferred from the value's type, i.e. float values are categorized as numeric scores and string values as categorical scores.
 928            comment (Optional[str]): An optional comment or description providing context or additional details about the score.
 929            id (Optional[str]): An optional custom ID for the scoring event. Useful for linking scores with external systems or for detailed tracking.
 930            config_id (Optional[str]): The id of the score config. When set, the score value is validated against the config. Defaults to None.
 931
 932        Returns:
 933            None
 934
 935        Note:
 936            This method is intended to be used within the context of an active trace or observation.
 937        """
 938        try:
 939            trace_id = self.get_current_trace_id()
 940            current_observation_id = self.get_current_observation_id()
 941
 942            observation_id = (
 943                current_observation_id if current_observation_id != trace_id else None
 944            )
 945
 946            if trace_id:
 947                self.client_instance.score(
 948                    trace_id=trace_id,
 949                    observation_id=observation_id,
 950                    name=name,
 951                    value=value,
 952                    data_type=data_type,
 953                    comment=comment,
 954                    id=id,
 955                    config_id=config_id,
 956                )
 957            else:
 958                raise ValueError("No trace or observation found in the current context")
 959
 960        except Exception as e:
 961            self._log.error(f"Failed to score observation: {e}")
 962
 963    def score_current_trace(
 964        self,
 965        *,
 966        name: str,
 967        value: Union[float, str],
 968        data_type: Optional[ScoreDataType] = None,
 969        comment: Optional[str] = None,
 970        id: Optional[str] = None,
 971        config_id: Optional[str] = None,
 972    ):
 973        """Score the current trace in context. This can be called anywhere in the nested trace to score the trace.
 974
 975        Arguments:
 976            name (str): The name of the score metric. This should be a clear and concise identifier for the metric being recorded.
 977            value (Union[float, str]): The value of the score. Should be passed as float for numeric and boolean scores and as string for categorical scores. This could represent performance metrics, error rates, or any other quantifiable measure.
 978            data_type (Optional[ScoreDataType]): The data type of the score. When not set, the data type is inferred from the score config's data type, when present.
 979              When no config is set, the data type is inferred from the value's type, i.e. float values are categorized as numeric scores and string values as categorical scores.
 980            comment (Optional[str]): An optional comment or description providing context or additional details about the score.
 981            id (Optional[str]): An optional custom ID for the scoring event. Useful for linking scores with external systems or for detailed tracking.
 982            config_id (Optional[str]): The id of the score config. When set, the score value is validated against the config. Defaults to None.
 983
 984        Returns:
 985            None
 986
 987        Note:
 988            This method is intended to be used within the context of an active trace or observation.
 989        """
 990        try:
 991            trace_id = self.get_current_trace_id()
 992
 993            if trace_id:
 994                self.client_instance.score(
 995                    trace_id=trace_id,
 996                    name=name,
 997                    value=value,
 998                    data_type=data_type,
 999                    comment=comment,
1000                    id=id,
1001                    config_id=config_id,
1002                )
1003            else:
1004                raise ValueError("No trace found in the current context")
1005
1006        except Exception as e:
1007            self._log.error(f"Failed to score observation: {e}")
1008
1009    @catch_and_log_errors
1010    def flush(self):
1011        """Force immediate flush of all buffered observations to the Langfuse backend.
1012
1013        This method triggers the explicit sending of all accumulated trace and observation data that has not yet been sent to Langfuse servers.
1014        It is typically used to ensure that data is promptly available for analysis, especially at the end of an execution context or before the application exits.
1015
1016        Usage:
1017            - This method can be called at strategic points in the application where it's crucial to ensure that all telemetry data captured up to that point is made persistent and visible on the Langfuse platform.
1018            - It's particularly useful in scenarios where the application might terminate abruptly or in batch processing tasks that require periodic flushing of trace data.
1019
1020        Returns:
1021            None
1022
1023        Raises:
1024            ValueError: If it fails to find a Langfuse client object in the current context, indicating potential misconfiguration or initialization issues.
1025
1026        Note:
1027            - The flush operation may involve network I/O to send data to the Langfuse backend, which could impact performance if called too frequently in performance-sensitive contexts.
1028            - In long-running applications, it's often sufficient to rely on the automatic flushing mechanism provided by the Langfuse client.
1029            However, explicit calls to `flush` can be beneficial in certain edge cases or for debugging purposes.
1030        """
1031        if self.client_instance:
1032            self.client_instance.flush()
1033        else:
1034            self._log.warning("No langfuse object found in the current context")
1035
1036    def configure(
1037        self,
1038        *,
1039        public_key: Optional[str] = None,
1040        secret_key: Optional[str] = None,
1041        host: Optional[str] = None,
1042        release: Optional[str] = None,
1043        debug: Optional[bool] = None,
1044        threads: Optional[int] = None,
1045        flush_at: Optional[int] = None,
1046        flush_interval: Optional[int] = None,
1047        max_retries: Optional[int] = None,
1048        timeout: Optional[int] = None,
1049        httpx_client: Optional[httpx.Client] = None,
1050        enabled: Optional[bool] = None,
1051        mask: Optional[Callable] = None,
1052    ):
1053        """Configure the Langfuse client.
1054
1055        If called, this method must be called before any other langfuse_context or observe decorated function to configure the Langfuse client with the necessary credentials and settings.
1056
1057        Args:
1058            public_key: Public API key of Langfuse project. Can be set via `LANGFUSE_PUBLIC_KEY` environment variable.
1059            secret_key: Secret API key of Langfuse project. Can be set via `LANGFUSE_SECRET_KEY` environment variable.
1060            host: Host of Langfuse API. Can be set via `LANGFUSE_HOST` environment variable. Defaults to `https://cloud.langfuse.com`.
1061            release: Release number/hash of the application to provide analytics grouped by release. Can be set via `LANGFUSE_RELEASE` environment variable.
1062            debug: Enables debug mode for more verbose logging. Can be set via `LANGFUSE_DEBUG` environment variable.
1063            threads: Number of consumer threads to execute network requests. Helps scaling the SDK for high load. Only increase this if you run into scaling issues.
1064            flush_at: Max batch size that's sent to the API.
1065            flush_interval: Max delay until a new batch is sent to the API.
1066            max_retries: Max number of retries in case of API/network errors.
1067            timeout: Timeout of API requests in seconds. Default is 20 seconds.
1068            httpx_client: Pass your own httpx client for more customizability of requests.
1069            enabled: Enables or disables the Langfuse client. Defaults to True. If disabled, no observability data will be sent to Langfuse. If data is requested while disabled, an error will be raised.
1070            mask (Callable): Function that masks sensitive information from input and output in log messages.
1071
1072        """
1073        langfuse_singleton = LangfuseSingleton()
1074        langfuse_singleton.reset()
1075
1076        langfuse_singleton.get(
1077            public_key=public_key,
1078            secret_key=secret_key,
1079            host=host,
1080            release=release,
1081            debug=debug,
1082            threads=threads,
1083            flush_at=flush_at,
1084            flush_interval=flush_interval,
1085            max_retries=max_retries,
1086            timeout=timeout,
1087            httpx_client=httpx_client,
1088            enabled=enabled,
1089            mask=mask,
1090        )
1091
1092    @property
1093    def client_instance(self) -> Langfuse:
1094        """Get the Langfuse client instance for the current decorator context."""
1095        return LangfuseSingleton().get()
1096
1097    def _set_root_trace_id(self, trace_id: str):
1098        if _observation_stack_context.get():
1099            self._log.warning(
1100                "Root Trace ID cannot be set on a already running trace. Skipping root trace ID assignment."
1101            )
1102            return
1103
1104        _root_trace_id_context.set(trace_id)
1105
1106    def _pop_observation_params_from_context(
1107        self, observation_id: str
1108    ) -> ObservationParams:
1109        params = _observation_params_context.get()[observation_id].copy()
1110
1111        # Remove observation params to avoid leaking
1112        del _observation_params_context.get()[observation_id]
1113
1114        return params
1115
1116    def auth_check(self) -> bool:
1117        """Check if the current Langfuse client is authenticated.
1118
1119        Returns:
1120            bool: True if the client is authenticated, False otherwise
1121        """
1122        try:
1123            return self.client_instance.auth_check()
1124        except Exception as e:
1125            self._log.error(
1126                "No Langfuse object found in the current context", exc_info=e
1127            )
1128
1129            return False

````

defobserve(self,func:Optional\[Callable\[~~P,~~R\]\]=None,\*,name:Optional\[str\]=None,as_type:Optional\[Literal\['generation'\]\]=None,capture_input:bool=True,capture_output:bool=True,transform_to_string:Optional\[Callable\[\[Iterable\],str\]\]=None) -> Callable\[\[Callable\[~~P,~~R\]\],Callable\[~~P,~~R\]\]:View Source

````
115    def observe(
116        self,
117        func: Optional[Callable[P, R]] = None,
118        *,
119        name: Optional[str] = None,
120        as_type: Optional[Literal["generation"]] = None,
121        capture_input: bool = True,
122        capture_output: bool = True,
123        transform_to_string: Optional[Callable[[Iterable], str]] = None,
124    ) -> Callable[[Callable[P, R]], Callable[P, R]]:
125        """Wrap a function to create and manage Langfuse tracing around its execution, supporting both synchronous and asynchronous functions.
126
127        It captures the function's execution context, including start/end times, input/output data, and automatically handles trace/span generation within the Langfuse observation context.
128        In case of an exception, the observation is updated with error details. The top-most decorated function is treated as a trace, with nested calls captured as spans or generations.
129
130        Attributes:
131            name (Optional[str]): Name of the created trace or span. Overwrites the function name as the default used for the trace or span name.
132            as_type (Optional[Literal["generation"]]): Specify "generation" to treat the observation as a generation type, suitable for language model invocations.
133            capture_input (bool): If True, captures the args and kwargs of the function as input. Default is True.
134            capture_output (bool): If True, captures the return value of the function as output. Default is True.
135            transform_to_string (Optional[Callable[[Iterable], str]]): When the decorated function returns a generator, this function transforms yielded values into a string representation for output capture
136
137        Returns:
138            Callable: A wrapped version of the original function that, upon execution, is automatically observed and managed by Langfuse.
139
140        Example:
141            For general tracing (functions/methods):
142            ```python
143            @observe()
144            def your_function(args):
145                # Your implementation here
146            ```
147            For observing language model generations:
148            ```python
149            @observe(as_type="generation")
150            def your_LLM_function(args):
151                # Your LLM invocation here
152            ```
153
154        Raises:
155            Exception: Propagates exceptions from the wrapped function after logging and updating the observation with error details.
156
157        Note:
158        - Automatic observation ID and context management is provided. Optionally, an observation ID can be specified using the `langfuse_observation_id` keyword when calling the wrapped function.
159        - To update observation or trace parameters (e.g., metadata, session_id), use `langfuse.update_current_observation` and `langfuse.update_current_trace` methods within the wrapped function.
160        """
161
162        def decorator(func: Callable[P, R]) -> Callable[P, R]:
163            return (
164                self._async_observe(
165                    func,
166                    name=name,
167                    as_type=as_type,
168                    capture_input=capture_input,
169                    capture_output=capture_output,
170                    transform_to_string=transform_to_string,
171                )
172                if asyncio.iscoroutinefunction(func)
173                else self._sync_observe(
174                    func,
175                    name=name,
176                    as_type=as_type,
177                    capture_input=capture_input,
178                    capture_output=capture_output,
179                    transform_to_string=transform_to_string,
180                )
181            )
182
183        """
184        If the decorator is called without arguments, return the decorator function itself.
185        This allows the decorator to be used with or without arguments.
186        Python calls the decorator function with the decorated function as an argument when the decorator is used without arguments.
187        """
188        if func is None:
189            return decorator
190        else:
191            return decorator(func)

````

Wrap a function to create and manage Langfuse tracing around its execution, supporting both synchronous and asynchronous functions.

It captures the function's execution context, including start/end times, input/output data, and automatically handles trace/span generation within the Langfuse observation context.
In case of an exception, the observation is updated with error details. The top-most decorated function is treated as a trace, with nested calls captured as spans or generations.

###### Attributes:

- **name (Optional\[str\]):** Name of the created trace or span. Overwrites the function name as the default used for the trace or span name.

- **as_type (Optional\[Literal\["generation"\]\]):** Specify "generation" to treat the observation as a generation type, suitable for language model invocations.

- **capture_input (bool):** If True, captures the args and kwargs of the function as input. Default is True.

- **capture_output (bool):** If True, captures the return value of the function as output. Default is True.

- **transform_to_string (Optional\[Callable\[\[Iterable\], str\]\]):** When the decorated function returns a generator, this function transforms yielded values into a string representation for output capture

###### Returns:

> Callable: A wrapped version of the original function that, upon execution, is automatically observed and managed by Langfuse.

###### Example:

> For general tracing (functions/methods):
>
> ```
> @observe()
> def your_function(args):
>     # Your implementation here
> 
> ```
>
> For observing language model generations:
>
> ```
> @observe(as_type="generation")
> def your_LLM_function(args):
>     # Your LLM invocation here
> 
> ```

###### Raises:

- **Exception:** Propagates exceptions from the wrapped function after logging and updating the observation with error details.

Note:

- Automatic observation ID and context management is provided. Optionally, an observation ID can be specified using the `langfuse_observation_id` keyword when calling the wrapped function.

- To update observation or trace parameters (e.g., metadata, session_id), use `langfuse.update_current_observation` and `langfuse.update_current_trace` methods within the wrapped function.

defget_current_llama_index_handler(self):View Source

```
580    def get_current_llama_index_handler(self):
581        """Retrieve the current LlamaIndexCallbackHandler associated with the most recent observation in the observation stack.
582
583        This method fetches the current observation from the observation stack and returns a LlamaIndexCallbackHandler initialized with this observation.
584        It is intended to be used within the context of a trace, allowing access to a callback handler for operations that require interaction with the LlamaIndex API based on the current observation context.
585
586        See the Langfuse documentation for more information on integrating the LlamaIndexCallbackHandler.
587
588        Returns:
589            LlamaIndexCallbackHandler or None: Returns a LlamaIndexCallbackHandler instance if there is an active observation in the current context; otherwise, returns None if no observation is found.
590
591        Note:
592            - This method should be called within the context of a trace (i.e., within a function wrapped by @observe) to ensure that an observation context exists.
593            - If no observation is found in the current context (e.g., if called outside of a trace or if the observation stack is empty), the method logs a warning and returns None.
594        """
595        try:
596            from langfuse.llama_index import LlamaIndexCallbackHandler
597        except ImportError:
598            self._log.error(
599                "LlamaIndexCallbackHandler is not available, most likely because llama-index is not installed. pip install llama-index"
600            )
601
602            return None
603
604        stack = _observation_stack_context.get()
605        observation = stack[-1] if stack else None
606
607        if observation is None:
608            self._log.warning("No observation found in the current context")
609
610            return None
611
612        if isinstance(observation, StatefulGenerationClient):
613            self._log.warning(
614                "Current observation is of type GENERATION, LlamaIndex handler is not supported for this type of observation"
615            )
616
617            return None
618
619        callback_handler = LlamaIndexCallbackHandler()
620        callback_handler.set_root(observation)
621
622        return callback_handler

```

Retrieve the current LlamaIndexCallbackHandler associated with the most recent observation in the observation stack.

This method fetches the current observation from the observation stack and returns a LlamaIndexCallbackHandler initialized with this observation.
It is intended to be used within the context of a trace, allowing access to a callback handler for operations that require interaction with the LlamaIndex API based on the current observation context.

See the Langfuse documentation for more information on integrating the LlamaIndexCallbackHandler.

###### Returns:

> LlamaIndexCallbackHandler or None: Returns a LlamaIndexCallbackHandler instance if there is an active observation in the current context; otherwise, returns None if no observation is found.

###### Note:

> - This method should be called within the context of a trace (i.e., within a function wrapped by @observe) to ensure that an observation context exists.
>
> - If no observation is found in the current context (e.g., if called outside of a trace or if the observation stack is empty), the method logs a warning and returns None.

defget_current_langchain_handler(self):View Source

```
624    def get_current_langchain_handler(self):
625        """Retrieve the current LangchainCallbackHandler associated with the most recent observation in the observation stack.
626
627        This method fetches the current observation from the observation stack and returns a LangchainCallbackHandler initialized with this observation.
628        It is intended to be used within the context of a trace, allowing access to a callback handler for operations that require interaction with Langchain based on the current observation context.
629
630        See the Langfuse documentation for more information on integrating the LangchainCallbackHandler.
631
632        Returns:
633            LangchainCallbackHandler or None: Returns a LangchainCallbackHandler instance if there is an active observation in the current context; otherwise, returns None if no observation is found.
634
635        Note:
636            - This method should be called within the context of a trace (i.e., within a function wrapped by @observe) to ensure that an observation context exists.
637            - If no observation is found in the current context (e.g., if called outside of a trace or if the observation stack is empty), the method logs a warning and returns None.
638        """
639        stack = _observation_stack_context.get()
640        observation = stack[-1] if stack else None
641
642        if observation is None:
643            self._log.warning("No observation found in the current context")
644
645            return None
646
647        if isinstance(observation, StatefulGenerationClient):
648            self._log.warning(
649                "Current observation is of type GENERATION, Langchain handler is not supported for this type of observation"
650            )
651
652            return None
653
654        return observation.get_langchain_handler()

```

Retrieve the current LangchainCallbackHandler associated with the most recent observation in the observation stack.

This method fetches the current observation from the observation stack and returns a LangchainCallbackHandler initialized with this observation.
It is intended to be used within the context of a trace, allowing access to a callback handler for operations that require interaction with Langchain based on the current observation context.

See the Langfuse documentation for more information on integrating the LangchainCallbackHandler.

###### Returns:

> LangchainCallbackHandler or None: Returns a LangchainCallbackHandler instance if there is an active observation in the current context; otherwise, returns None if no observation is found.

###### Note:

> - This method should be called within the context of a trace (i.e., within a function wrapped by @observe) to ensure that an observation context exists.
>
> - If no observation is found in the current context (e.g., if called outside of a trace or if the observation stack is empty), the method logs a warning and returns None.

defget_current_trace_id(self):View Source

```
656    def get_current_trace_id(self):
657        """Retrieve the ID of the current trace from the observation stack context.
658
659        This method examines the observation stack to find the root trace and returns its ID. It is useful for operations that require the trace ID,
660        such as setting trace parameters or querying trace information. The trace ID is typically the ID of the first observation in the stack,
661        representing the entry point of the traced execution context. If you have provided a langfuse_parent_trace_id directly, it will return that instead.
662
663        Returns:
664            str or None: The ID of the current trace if available; otherwise, None. A return value of None indicates that there is no active trace in the current context,
665            possibly due to the method being called outside of any @observe-decorated function execution.
666
667        Note:
668            - This method should be called within the context of a trace (i.e., inside a function wrapped with the @observe decorator) to ensure that a current trace is indeed present and its ID can be retrieved.
669            - If called outside of a trace context, or if the observation stack has somehow been corrupted or improperly managed, this method will log a warning and return None, indicating the absence of a traceable context.
670        """
671        context_trace_id = _root_trace_id_context.get()
672        if context_trace_id:
673            return context_trace_id
674
675        stack = _observation_stack_context.get()
676        should_log_warning = self._get_caller_module_name() != "langfuse.openai"
677
678        if not stack:
679            if should_log_warning:
680                self._log.warning("No trace found in the current context")
681
682            return None
683
684        return stack[0].id

```

Retrieve the ID of the current trace from the observation stack context.

This method examines the observation stack to find the root trace and returns its ID. It is useful for operations that require the trace ID,
such as setting trace parameters or querying trace information. The trace ID is typically the ID of the first observation in the stack,
representing the entry point of the traced execution context. If you have provided a langfuse_parent_trace_id directly, it will return that instead.

###### Returns:

> str or None: The ID of the current trace if available; otherwise, None. A return value of None indicates that there is no active trace in the current context,
> possibly due to the method being called outside of any @observe-decorated function execution.

###### Note:

> - This method should be called within the context of a trace (i.e., inside a function wrapped with the @observe decorator) to ensure that a current trace is indeed present and its ID can be retrieved.
>
> - If called outside of a trace context, or if the observation stack has somehow been corrupted or improperly managed, this method will log a warning and return None, indicating the absence of a traceable context.

defget_current_trace_url(self) -> Optional\[str\]:View Source

```
696    def get_current_trace_url(self) -> Optional[str]:
697        """Retrieve the URL of the current trace in context.
698
699        Returns:
700            str or None: The URL of the current trace if available; otherwise, None. A return value of None indicates that there is no active trace in the current context,
701            possibly due to the method being called outside of any @observe-decorated function execution.
702
703        Note:
704            - This method should be called within the context of a trace (i.e., inside a function wrapped with the @observe decorator) to ensure that a current trace is indeed present and its ID can be retrieved.
705            - If called outside of a trace context, or if the observation stack has somehow been corrupted or improperly managed, this method will log a warning and return None, indicating the absence of a traceable context.
706        """
707        try:
708            trace_id = self.get_current_trace_id()
709
710            if not trace_id:
711                raise ValueError("No trace found in the current context")
712
713            return f"{self.client_instance.client._client_wrapper._base_url}/trace/{trace_id}"
714
715        except Exception as e:
716            self._log.error(f"Failed to get current trace URL: {e}")
717
718            return None

```

Retrieve the URL of the current trace in context.

###### Returns:

> str or None: The URL of the current trace if available; otherwise, None. A return value of None indicates that there is no active trace in the current context,
> possibly due to the method being called outside of any @observe-decorated function execution.

###### Note:

> - This method should be called within the context of a trace (i.e., inside a function wrapped with the @observe decorator) to ensure that a current trace is indeed present and its ID can be retrieved.
>
> - If called outside of a trace context, or if the observation stack has somehow been corrupted or improperly managed, this method will log a warning and return None, indicating the absence of a traceable context.

defget_current_observation_id(self):View Source

```
720    def get_current_observation_id(self):
721        """Retrieve the ID of the current observation in context.
722
723        Returns:
724            str or None: The ID of the current observation if available; otherwise, None. A return value of None indicates that there is no active trace or observation in the current context,
725            possibly due to the method being called outside of any @observe-decorated function execution.
726
727        Note:
728            - This method should be called within the context of a trace or observation (i.e., inside a function wrapped with the @observe decorator) to ensure that a current observation is indeed present and its ID can be retrieved.
729            - If called outside of a trace or observation context, or if the observation stack has somehow been corrupted or improperly managed, this method will log a warning and return None, indicating the absence of a traceable context.
730            - If called at the top level of a trace, it will return the trace ID.
731        """
732        stack = _observation_stack_context.get()
733        should_log_warning = self._get_caller_module_name() != "langfuse.openai"
734
735        if not stack:
736            if should_log_warning:
737                self._log.warning("No observation found in the current context")
738
739            return None
740
741        return stack[-1].id

```

Retrieve the ID of the current observation in context.

###### Returns:

> str or None: The ID of the current observation if available; otherwise, None. A return value of None indicates that there is no active trace or observation in the current context,
> possibly due to the method being called outside of any @observe-decorated function execution.

###### Note:

> - This method should be called within the context of a trace or observation (i.e., inside a function wrapped with the @observe decorator) to ensure that a current observation is indeed present and its ID can be retrieved.
>
> - If called outside of a trace or observation context, or if the observation stack has somehow been corrupted or improperly managed, this method will log a warning and return None, indicating the absence of a traceable context.
>
> - If called at the top level of a trace, it will return the trace ID.

defupdate_current_trace(self,name:Optional\[str\]=None,input:Optional\[Any\]=None,output:Optional\[Any\]=None,user_id:Optional\[str\]=None,session_id:Optional\[str\]=None,version:Optional\[str\]=None,release:Optional\[str\]=None,metadata:Optional\[Any\]=None,tags:Optional\[List\[str\]\]=None,public:Optional\[bool\]=None):View Source

```
743    def update_current_trace(
744        self,
745        name: Optional[str] = None,
746        input: Optional[Any] = None,
747        output: Optional[Any] = None,
748        user_id: Optional[str] = None,
749        session_id: Optional[str] = None,
750        version: Optional[str] = None,
751        release: Optional[str] = None,
752        metadata: Optional[Any] = None,
753        tags: Optional[List[str]] = None,
754        public: Optional[bool] = None,
755    ):
756        """Set parameters for the current trace, updating the trace's metadata and context information.
757
758        This method allows for dynamically updating the trace parameters at any point during the execution of a trace.
759        It updates the parameters of the current trace based on the provided arguments. These parameters include metadata, session information,
760        and other trace attributes that can be useful for categorization, filtering, and analysis in the Langfuse UI.
761
762        Arguments:
763            name (Optional[str]): Identifier of the trace. Useful for sorting/filtering in the UI..
764            input (Optional[Any]): The input parameters of the trace, providing context about the observed operation or function call.
765            output (Optional[Any]): The output or result of the trace
766            user_id (Optional[str]): The id of the user that triggered the execution. Used to provide user-level analytics.
767            session_id (Optional[str]): Used to group multiple traces into a session in Langfuse. Use your own session/thread identifier.
768            version (Optional[str]): The version of the trace type. Used to understand how changes to the trace type affect metrics. Useful in debugging.
769            release (Optional[str]): The release identifier of the current deployment. Used to understand how changes of different deployments affect metrics. Useful in debugging.
770            metadata (Optional[Any]): Additional metadata of the trace. Can be any JSON object. Metadata is merged when being updated via the API.
771            tags (Optional[List[str]]): Tags are used to categorize or label traces. Traces can be filtered by tags in the Langfuse UI and GET API.
772
773        Returns:
774            None
775
776        Note:
777            - This method should be used within the context of an active trace, typically within a function that is being traced using the @observe decorator.
778            - The method updates the trace parameters for the currently executing trace. In nested trace scenarios, it affects the most recent trace context.
779            - If called outside of an active trace context, a warning is logged, and a ValueError is raised to indicate the absence of a traceable context.
780        """
781        trace_id = self.get_current_trace_id()
782
783        if trace_id is None:
784            self._log.warning("No trace found in the current context")
785
786            return
787
788        params_to_update = {
789            k: v
790            for k, v in {
791                "name": name,
792                "input": input,
793                "output": output,
794                "user_id": user_id,
795                "session_id": session_id,
796                "version": version,
797                "release": release,
798                "metadata": metadata,
799                "tags": tags,
800                "public": public,
801            }.items()
802            if v is not None
803        }
804
805        _observation_params_context.get()[trace_id].update(params_to_update)

```

Set parameters for the current trace, updating the trace's metadata and context information.

This method allows for dynamically updating the trace parameters at any point during the execution of a trace.
It updates the parameters of the current trace based on the provided arguments. These parameters include metadata, session information,
and other trace attributes that can be useful for categorization, filtering, and analysis in the Langfuse UI.

###### Arguments:

- **name (Optional\[str\]):** Identifier of the trace. Useful for sorting/filtering in the UI..

- **input (Optional\[Any\]):** The input parameters of the trace, providing context about the observed operation or function call.

- **output (Optional\[Any\]):** The output or result of the trace

- **user_id (Optional\[str\]):** The id of the user that triggered the execution. Used to provide user-level analytics.

- **session_id (Optional\[str\]):** Used to group multiple traces into a session in Langfuse. Use your own session/thread identifier.

- **version (Optional\[str\]):** The version of the trace type. Used to understand how changes to the trace type affect metrics. Useful in debugging.

- **release (Optional\[str\]):** The release identifier of the current deployment. Used to understand how changes of different deployments affect metrics. Useful in debugging.

- **metadata (Optional\[Any\]):** Additional metadata of the trace. Can be any JSON object. Metadata is merged when being updated via the API.

- **tags (Optional\[List\[str\]\]):** Tags are used to categorize or label traces. Traces can be filtered by tags in the Langfuse UI and GET API.

###### Returns:

> None

###### Note:

> - This method should be used within the context of an active trace, typically within a function that is being traced using the @observe decorator.
>
> - The method updates the trace parameters for the currently executing trace. In nested trace scenarios, it affects the most recent trace context.
>
> - If called outside of an active trace context, a warning is logged, and a ValueError is raised to indicate the absence of a traceable context.

defupdate_current_observation(self,\*,input:Optional\[Any\]=None,output:Optional\[Any\]=None,name:Optional\[str\]=None,version:Optional\[str\]=None,metadata:Optional\[Any\]=None,start_time:Optional\[datetime.datetime\]=None,end_time:Optional\[datetime.datetime\]=None,release:Optional\[str\]=None,tags:Optional\[List\[str\]\]=None,user_id:Optional\[str\]=None,session_id:Optional\[str\]=None,level:Optional\[Literal\['DEBUG','DEFAULT','WARNING','ERROR'\]\]=None,status_message:Optional\[str\]=None,completion_start_time:Optional\[datetime.datetime\]=None,model:Optional\[str\]=None,model_parameters:Optional\[Dict\[str,Union\[str,NoneType,int,bool,List\[str\]\]\]\]=None,usage:Union\[pydantic.main.BaseModel,[langfuse.model.ModelUsage](model.html#ModelUsage),NoneType\]=None,prompt:Union\[[langfuse.model.TextPromptClient](model.html#TextPromptClient),[langfuse.model.ChatPromptClient](model.html#ChatPromptClient),NoneType\]=None,public:Optional\[bool\]=None):View Source

```
807    def update_current_observation(
808        self,
809        *,
810        input: Optional[Any] = None,
811        output: Optional[Any] = None,
812        name: Optional[str] = None,
813        version: Optional[str] = None,
814        metadata: Optional[Any] = None,
815        start_time: Optional[datetime] = None,
816        end_time: Optional[datetime] = None,
817        release: Optional[str] = None,
818        tags: Optional[List[str]] = None,
819        user_id: Optional[str] = None,
820        session_id: Optional[str] = None,
821        level: Optional[SpanLevel] = None,
822        status_message: Optional[str] = None,
823        completion_start_time: Optional[datetime] = None,
824        model: Optional[str] = None,
825        model_parameters: Optional[Dict[str, MapValue]] = None,
826        usage: Optional[Union[BaseModel, ModelUsage]] = None,
827        prompt: Optional[PromptClient] = None,
828        public: Optional[bool] = None,
829    ):
830        """Update parameters for the current observation within an active trace context.
831
832        This method dynamically adjusts the parameters of the most recent observation on the observation stack.
833        It allows for the enrichment of observation data with additional details such as input parameters, output results, metadata, and more,
834        enhancing the observability and traceability of the execution context.
835
836        Note that if a param is not available on a specific observation type, it will be ignored.
837
838        Shared params:
839            - `input` (Optional[Any]): The input parameters of the trace or observation, providing context about the observed operation or function call.
840            - `output` (Optional[Any]): The output or result of the trace or observation
841            - `name` (Optional[str]): Identifier of the trace or observation. Useful for sorting/filtering in the UI.
842            - `metadata` (Optional[Any]): Additional metadata of the trace. Can be any JSON object. Metadata is merged when being updated via the API.
843            - `start_time` (Optional[datetime]): The start time of the observation, allowing for custom time range specification.
844            - `end_time` (Optional[datetime]): The end time of the observation, enabling precise control over the observation duration.
845            - `version` (Optional[str]): The version of the trace type. Used to understand how changes to the trace type affect metrics. Useful in debugging.
846
847        Trace-specific params:
848            - `user_id` (Optional[str]): The id of the user that triggered the execution. Used to provide user-level analytics.
849            - `session_id` (Optional[str]): Used to group multiple traces into a session in Langfuse. Use your own session/thread identifier.
850            - `release` (Optional[str]): The release identifier of the current deployment. Used to understand how changes of different deployments affect metrics. Useful in debugging.
851            - `tags` (Optional[List[str]]): Tags are used to categorize or label traces. Traces can be filtered by tags in the Langfuse UI and GET API.
852            - `public` (Optional[bool]): You can make a trace public to share it via a public link. This allows others to view the trace without needing to log in or be members of your Langfuse project.
853
854        Span-specific params:
855            - `level` (Optional[SpanLevel]): The severity or importance level of the observation, such as "INFO", "WARNING", or "ERROR".
856            - `status_message` (Optional[str]): A message or description associated with the observation's status, particularly useful for error reporting.
857
858        Generation-specific params:
859            - `completion_start_time` (Optional[datetime]): The time at which the completion started (streaming). Set it to get latency analytics broken down into time until completion started and completion duration.
860            - `model_parameters` (Optional[Dict[str, MapValue]]): The parameters of the model used for the generation; can be any key-value pairs.
861            - `usage` (Optional[Union[BaseModel, ModelUsage]]): The usage object supports the OpenAi structure with {promptTokens, completionTokens, totalTokens} and a more generic version {input, output, total, unit, inputCost, outputCost, totalCost} where unit can be of value "TOKENS", "CHARACTERS", "MILLISECONDS", "SECONDS", or "IMAGES". Refer to the docs on how to automatically infer token usage and costs in Langfuse.
862            - `prompt`(Optional[PromptClient]): The prompt object used for the generation.
863
864        Returns:
865            None
866
867        Raises:
868            ValueError: If no current observation is found in the context, indicating that this method was called outside of an observation's execution scope.
869
870        Note:
871            - This method is intended to be used within the context of an active observation, typically within a function wrapped by the @observe decorator.
872            - It updates the parameters of the most recently created observation on the observation stack. Care should be taken in nested observation contexts to ensure the updates are applied as intended.
873            - Parameters set to `None` will not overwrite existing values for those parameters. This behavior allows for selective updates without clearing previously set information.
874        """
875        stack = _observation_stack_context.get()
876        observation = stack[-1] if stack else None
877
878        if not observation:
879            self._log.warning("No observation found in the current context")
880
881            return
882
883        update_params = {
884            k: v
885            for k, v in {
886                "input": input,
887                "output": output,
888                "name": name,
889                "version": version,
890                "metadata": metadata,
891                "start_time": start_time,
892                "end_time": end_time,
893                "release": release,
894                "tags": tags,
895                "user_id": user_id,
896                "session_id": session_id,
897                "level": level,
898                "status_message": status_message,
899                "completion_start_time": completion_start_time,
900                "model": model,
901                "model_parameters": model_parameters,
902                "usage": usage,
903                "prompt": prompt,
904                "public": public,
905            }.items()
906            if v is not None
907        }
908
909        _observation_params_context.get()[observation.id].update(update_params)

```

Update parameters for the current observation within an active trace context.

This method dynamically adjusts the parameters of the most recent observation on the observation stack.
It allows for the enrichment of observation data with additional details such as input parameters, output results, metadata, and more,
enhancing the observability and traceability of the execution context.

Note that if a param is not available on a specific observation type, it will be ignored.

###### Shared params:

> - `input` (Optional\[Any\]): The input parameters of the trace or observation, providing context about the observed operation or function call.
>
> - `output` (Optional\[Any\]): The output or result of the trace or observation
>
> - `name` (Optional\[str\]): Identifier of the trace or observation. Useful for sorting/filtering in the UI.
>
> - `metadata` (Optional\[Any\]): Additional metadata of the trace. Can be any JSON object. Metadata is merged when being updated via the API.
>
> - `start_time` (Optional\[datetime\]): The start time of the observation, allowing for custom time range specification.
>
> - `end_time` (Optional\[datetime\]): The end time of the observation, enabling precise control over the observation duration.
>
> - `version` (Optional\[str\]): The version of the trace type. Used to understand how changes to the trace type affect metrics. Useful in debugging.

Trace-specific params:
\- `user_id` (Optional\[str\]): The id of the user that triggered the execution. Used to provide user-level analytics.
\- `session_id` (Optional\[str\]): Used to group multiple traces into a session in Langfuse. Use your own session/thread identifier.
\- `release` (Optional\[str\]): The release identifier of the current deployment. Used to understand how changes of different deployments affect metrics. Useful in debugging.
\- `tags` (Optional\[List\[str\]\]): Tags are used to categorize or label traces. Traces can be filtered by tags in the Langfuse UI and GET API.
\- `public` (Optional\[bool\]): You can make a trace public to share it via a public link. This allows others to view the trace without needing to log in or be members of your Langfuse project.

Span-specific params:
\- `level` (Optional\[SpanLevel\]): The severity or importance level of the observation, such as "INFO", "WARNING", or "ERROR".
\- `status_message` (Optional\[str\]): A message or description associated with the observation's status, particularly useful for error reporting.

Generation-specific params:
\- `completion_start_time` (Optional\[datetime\]): The time at which the completion started (streaming). Set it to get latency analytics broken down into time until completion started and completion duration.
\- `model_parameters` (Optional\[Dict\[str, MapValue\]\]): The parameters of the model used for the generation; can be any key-value pairs.
\- `usage` (Optional\[Union\[BaseModel, ModelUsage\]\]): The usage object supports the OpenAi structure with {promptTokens, completionTokens, totalTokens} and a more generic version {input, output, total, unit, inputCost, outputCost, totalCost} where unit can be of value "TOKENS", "CHARACTERS", "MILLISECONDS", "SECONDS", or "IMAGES". Refer to the docs on how to automatically infer token usage and costs in Langfuse.
\- `prompt`(Optional\[PromptClient\]): The prompt object used for the generation.

###### Returns:

> None

###### Raises:

- **ValueError:** If no current observation is found in the context, indicating that this method was called outside of an observation's execution scope.

###### Note:

> - This method is intended to be used within the context of an active observation, typically within a function wrapped by the @observe decorator.
>
> - It updates the parameters of the most recently created observation on the observation stack. Care should be taken in nested observation contexts to ensure the updates are applied as intended.
>
> - Parameters set to `None` will not overwrite existing values for those parameters. This behavior allows for selective updates without clearing previously set information.

defscore_current_observation(self,\*,name:str,value:Union\[float,str\],data_type:Optional\[Literal\['NUMERIC','CATEGORICAL','BOOLEAN'\]\]=None,comment:Optional\[str\]=None,id:Optional\[str\]=None,config_id:Optional\[str\]=None):View Source

```
911    def score_current_observation(
912        self,
913        *,
914        name: str,
915        value: Union[float, str],
916        data_type: Optional[ScoreDataType] = None,
917        comment: Optional[str] = None,
918        id: Optional[str] = None,
919        config_id: Optional[str] = None,
920    ):
921        """Score the current observation within an active trace. If called on the top level of a trace, it will score the trace.
922
923        Arguments:
924            name (str): The name of the score metric. This should be a clear and concise identifier for the metric being recorded.
925            value (float): The numerical value of the score. This could represent performance metrics, error rates, or any other quantifiable measure.
926            data_type (Optional[ScoreDataType]): The data type of the score. When not set, the data type is inferred from the score config's data type, when present.
927              When no config is set, the data type is inferred from the value's type, i.e. float values are categorized as numeric scores and string values as categorical scores.
928            comment (Optional[str]): An optional comment or description providing context or additional details about the score.
929            id (Optional[str]): An optional custom ID for the scoring event. Useful for linking scores with external systems or for detailed tracking.
930            config_id (Optional[str]): The id of the score config. When set, the score value is validated against the config. Defaults to None.
931
932        Returns:
933            None
934
935        Note:
936            This method is intended to be used within the context of an active trace or observation.
937        """
938        try:
939            trace_id = self.get_current_trace_id()
940            current_observation_id = self.get_current_observation_id()
941
942            observation_id = (
943                current_observation_id if current_observation_id != trace_id else None
944            )
945
946            if trace_id:
947                self.client_instance.score(
948                    trace_id=trace_id,
949                    observation_id=observation_id,
950                    name=name,
951                    value=value,
952                    data_type=data_type,
953                    comment=comment,
954                    id=id,
955                    config_id=config_id,
956                )
957            else:
958                raise ValueError("No trace or observation found in the current context")
959
960        except Exception as e:
961            self._log.error(f"Failed to score observation: {e}")

```

Score the current observation within an active trace. If called on the top level of a trace, it will score the trace.

###### Arguments:

- **name (str):** The name of the score metric. This should be a clear and concise identifier for the metric being recorded.

- **value (float):** The numerical value of the score. This could represent performance metrics, error rates, or any other quantifiable measure.

- **data_type (Optional\[ScoreDataType\]):** The data type of the score. When not set, the data type is inferred from the score config's data type, when present.
   When no config is set, the data type is inferred from the value's type, i.e. float values are categorized as numeric scores and string values as categorical scores.

- **comment (Optional\[str\]):** An optional comment or description providing context or additional details about the score.

- **id (Optional\[str\]):** An optional custom ID for the scoring event. Useful for linking scores with external systems or for detailed tracking.

- **config_id (Optional\[str\]):** The id of the score config. When set, the score value is validated against the config. Defaults to None.

###### Returns:

> None

###### Note:

> This method is intended to be used within the context of an active trace or observation.

defscore_current_trace(self,\*,name:str,value:Union\[float,str\],data_type:Optional\[Literal\['NUMERIC','CATEGORICAL','BOOLEAN'\]\]=None,comment:Optional\[str\]=None,id:Optional\[str\]=None,config_id:Optional\[str\]=None):View Source

```
 963    def score_current_trace(
 964        self,
 965        *,
 966        name: str,
 967        value: Union[float, str],
 968        data_type: Optional[ScoreDataType] = None,
 969        comment: Optional[str] = None,
 970        id: Optional[str] = None,
 971        config_id: Optional[str] = None,
 972    ):
 973        """Score the current trace in context. This can be called anywhere in the nested trace to score the trace.
 974
 975        Arguments:
 976            name (str): The name of the score metric. This should be a clear and concise identifier for the metric being recorded.
 977            value (Union[float, str]): The value of the score. Should be passed as float for numeric and boolean scores and as string for categorical scores. This could represent performance metrics, error rates, or any other quantifiable measure.
 978            data_type (Optional[ScoreDataType]): The data type of the score. When not set, the data type is inferred from the score config's data type, when present.
 979              When no config is set, the data type is inferred from the value's type, i.e. float values are categorized as numeric scores and string values as categorical scores.
 980            comment (Optional[str]): An optional comment or description providing context or additional details about the score.
 981            id (Optional[str]): An optional custom ID for the scoring event. Useful for linking scores with external systems or for detailed tracking.
 982            config_id (Optional[str]): The id of the score config. When set, the score value is validated against the config. Defaults to None.
 983
 984        Returns:
 985            None
 986
 987        Note:
 988            This method is intended to be used within the context of an active trace or observation.
 989        """
 990        try:
 991            trace_id = self.get_current_trace_id()
 992
 993            if trace_id:
 994                self.client_instance.score(
 995                    trace_id=trace_id,
 996                    name=name,
 997                    value=value,
 998                    data_type=data_type,
 999                    comment=comment,
1000                    id=id,
1001                    config_id=config_id,
1002                )
1003            else:
1004                raise ValueError("No trace found in the current context")
1005
1006        except Exception as e:
1007            self._log.error(f"Failed to score observation: {e}")

```

Score the current trace in context. This can be called anywhere in the nested trace to score the trace.

###### Arguments:

- **name (str):** The name of the score metric. This should be a clear and concise identifier for the metric being recorded.

- **value (Union\[float, str\]):** The value of the score. Should be passed as float for numeric and boolean scores and as string for categorical scores. This could represent performance metrics, error rates, or any other quantifiable measure.

- **data_type (Optional\[ScoreDataType\]):** The data type of the score. When not set, the data type is inferred from the score config's data type, when present.
   When no config is set, the data type is inferred from the value's type, i.e. float values are categorized as numeric scores and string values as categorical scores.

- **comment (Optional\[str\]):** An optional comment or description providing context or additional details about the score.

- **id (Optional\[str\]):** An optional custom ID for the scoring event. Useful for linking scores with external systems or for detailed tracking.

- **config_id (Optional\[str\]):** The id of the score config. When set, the score value is validated against the config. Defaults to None.

###### Returns:

> None

###### Note:

> This method is intended to be used within the context of an active trace or observation.

@catch_and_log_errors

defflush(self):View Source

```
1009    @catch_and_log_errors
1010    def flush(self):
1011        """Force immediate flush of all buffered observations to the Langfuse backend.
1012
1013        This method triggers the explicit sending of all accumulated trace and observation data that has not yet been sent to Langfuse servers.
1014        It is typically used to ensure that data is promptly available for analysis, especially at the end of an execution context or before the application exits.
1015
1016        Usage:
1017            - This method can be called at strategic points in the application where it's crucial to ensure that all telemetry data captured up to that point is made persistent and visible on the Langfuse platform.
1018            - It's particularly useful in scenarios where the application might terminate abruptly or in batch processing tasks that require periodic flushing of trace data.
1019
1020        Returns:
1021            None
1022
1023        Raises:
1024            ValueError: If it fails to find a Langfuse client object in the current context, indicating potential misconfiguration or initialization issues.
1025
1026        Note:
1027            - The flush operation may involve network I/O to send data to the Langfuse backend, which could impact performance if called too frequently in performance-sensitive contexts.
1028            - In long-running applications, it's often sufficient to rely on the automatic flushing mechanism provided by the Langfuse client.
1029            However, explicit calls to `flush` can be beneficial in certain edge cases or for debugging purposes.
1030        """
1031        if self.client_instance:
1032            self.client_instance.flush()
1033        else:
1034            self._log.warning("No langfuse object found in the current context")

```

Force immediate flush of all buffered observations to the Langfuse backend.

This method triggers the explicit sending of all accumulated trace and observation data that has not yet been sent to Langfuse servers.
It is typically used to ensure that data is promptly available for analysis, especially at the end of an execution context or before the application exits.

###### Usage:

> - This method can be called at strategic points in the application where it's crucial to ensure that all telemetry data captured up to that point is made persistent and visible on the Langfuse platform.
>
> - It's particularly useful in scenarios where the application might terminate abruptly or in batch processing tasks that require periodic flushing of trace data.

###### Returns:

> None

###### Raises:

- **ValueError:** If it fails to find a Langfuse client object in the current context, indicating potential misconfiguration or initialization issues.

###### Note:

> - The flush operation may involve network I/O to send data to the Langfuse backend, which could impact performance if called too frequently in performance-sensitive contexts.
>
> - In long-running applications, it's often sufficient to rely on the automatic flushing mechanism provided by the Langfuse client.
>    However, explicit calls to `flush` can be beneficial in certain edge cases or for debugging purposes.

defconfigure(self,\*,public_key:Optional\[str\]=None,secret_key:Optional\[str\]=None,host:Optional\[str\]=None,release:Optional\[str\]=None,debug:Optional\[bool\]=None,threads:Optional\[int\]=None,flush_at:Optional\[int\]=None,flush_interval:Optional\[int\]=None,max_retries:Optional\[int\]=None,timeout:Optional\[int\]=None,httpx_client:Optional\[httpx.Client\]=None,enabled:Optional\[bool\]=None,mask:Optional\[Callable\]=None):View Source

```
1036    def configure(
1037        self,
1038        *,
1039        public_key: Optional[str] = None,
1040        secret_key: Optional[str] = None,
1041        host: Optional[str] = None,
1042        release: Optional[str] = None,
1043        debug: Optional[bool] = None,
1044        threads: Optional[int] = None,
1045        flush_at: Optional[int] = None,
1046        flush_interval: Optional[int] = None,
1047        max_retries: Optional[int] = None,
1048        timeout: Optional[int] = None,
1049        httpx_client: Optional[httpx.Client] = None,
1050        enabled: Optional[bool] = None,
1051        mask: Optional[Callable] = None,
1052    ):
1053        """Configure the Langfuse client.
1054
1055        If called, this method must be called before any other langfuse_context or observe decorated function to configure the Langfuse client with the necessary credentials and settings.
1056
1057        Args:
1058            public_key: Public API key of Langfuse project. Can be set via `LANGFUSE_PUBLIC_KEY` environment variable.
1059            secret_key: Secret API key of Langfuse project. Can be set via `LANGFUSE_SECRET_KEY` environment variable.
1060            host: Host of Langfuse API. Can be set via `LANGFUSE_HOST` environment variable. Defaults to `https://cloud.langfuse.com`.
1061            release: Release number/hash of the application to provide analytics grouped by release. Can be set via `LANGFUSE_RELEASE` environment variable.
1062            debug: Enables debug mode for more verbose logging. Can be set via `LANGFUSE_DEBUG` environment variable.
1063            threads: Number of consumer threads to execute network requests. Helps scaling the SDK for high load. Only increase this if you run into scaling issues.
1064            flush_at: Max batch size that's sent to the API.
1065            flush_interval: Max delay until a new batch is sent to the API.
1066            max_retries: Max number of retries in case of API/network errors.
1067            timeout: Timeout of API requests in seconds. Default is 20 seconds.
1068            httpx_client: Pass your own httpx client for more customizability of requests.
1069            enabled: Enables or disables the Langfuse client. Defaults to True. If disabled, no observability data will be sent to Langfuse. If data is requested while disabled, an error will be raised.
1070            mask (Callable): Function that masks sensitive information from input and output in log messages.
1071
1072        """
1073        langfuse_singleton = LangfuseSingleton()
1074        langfuse_singleton.reset()
1075
1076        langfuse_singleton.get(
1077            public_key=public_key,
1078            secret_key=secret_key,
1079            host=host,
1080            release=release,
1081            debug=debug,
1082            threads=threads,
1083            flush_at=flush_at,
1084            flush_interval=flush_interval,
1085            max_retries=max_retries,
1086            timeout=timeout,
1087            httpx_client=httpx_client,
1088            enabled=enabled,
1089            mask=mask,
1090        )

```

Configure the Langfuse client.

If called, this method must be called before any other langfuse_context or observe decorated function to configure the Langfuse client with the necessary credentials and settings.

###### Arguments:

- **public_key:** Public API key of Langfuse project. Can be set via `LANGFUSE_PUBLIC_KEY` environment variable.

- **secret_key:** Secret API key of Langfuse project. Can be set via `LANGFUSE_SECRET_KEY` environment variable.

- **host:** Host of Langfuse API. Can be set via `LANGFUSE_HOST` environment variable. Defaults to `https://cloud.langfuse.com`.

- **release:** Release number/hash of the application to provide analytics grouped by release. Can be set via `LANGFUSE_RELEASE` environment variable.

- **debug:** Enables debug mode for more verbose logging. Can be set via `LANGFUSE_DEBUG` environment variable.

- **threads:** Number of consumer threads to execute network requests. Helps scaling the SDK for high load. Only increase this if you run into scaling issues.

- **flush_at:** Max batch size that's sent to the API.

- **flush_interval:** Max delay until a new batch is sent to the API.

- **max_retries:** Max number of retries in case of API/network errors.

- **timeout:** Timeout of API requests in seconds. Default is 20 seconds.

- **httpx_client:** Pass your own httpx client for more customizability of requests.

- **enabled:** Enables or disables the Langfuse client. Defaults to True. If disabled, no observability data will be sent to Langfuse. If data is requested while disabled, an error will be raised.

- **mask (Callable):** Function that masks sensitive information from input and output in log messages.

client_instance: angfuse.client.Langfuse\](client.html#Langfuse)View Source

```
1092    @property
1093    def client_instance(self) -> Langfuse:
1094        """Get the Langfuse client instance for the current decorator context."""
1095        return LangfuseSingleton().get()

```

Get the Langfuse client instance for the current decorator context.

defauth_check(self) -> bool:View Source

```
1116    def auth_check(self) -> bool:
1117        """Check if the current Langfuse client is authenticated.
1118
1119        Returns:
1120            bool: True if the client is authenticated, False otherwise
1121        """
1122        try:
1123            return self.client_instance.auth_check()
1124        except Exception as e:
1125            self._log.error(
1126                "No Langfuse object found in the current context", exc_info=e
1127            )
1128
1129            return False

```

Check if the current Langfuse client is authenticated.

###### Returns:

> bool: True if the client is authenticated, False otherwise

# Cookbook: Python Decorators

The Langfuse Python SDK uses decorators for you to effortlessly integrate observability into your LLM applications. It supports both synchronous and asynchronous functions, automatically handling traces, spans, and generations, along with key execution details like inputs and outputs. This setup allows you to concentrate on developing high-quality applications while benefitting from observability insights with minimal code.

This cookbook containes examples for all key functionalities of the decorator-based integration with Langfuse.

## Installation & setup [Permalink for this section](#installation--setup)

Install `langfuse`:

```nextra-code
%pip install langfuse
```

If you haven’t done so yet, [sign up to Langfuse](https://cloud.langfuse.com/auth/sign-up) and obtain your API keys from the project settings. You can also [self-host](https://langfuse.com/self-hosting) Langfuse.

```nextra-code
import os

# Get keys for your project from the project settings page
# https://cloud.langfuse.com
os.environ["LANGFUSE_PUBLIC_KEY"] = ""
os.environ["LANGFUSE_SECRET_KEY"] = ""
os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com" # 🇪🇺 EU region
# os.environ["LANGFUSE_HOST"] = "https://us.cloud.langfuse.com" # 🇺🇸 US region

# Your openai key
os.environ["OPENAI_API_KEY"] = ""
```

## Basic usage [Permalink for this section](#basic-usage)

Langfuse simplifies observability in LLM-powered applications by organizing activities into traces. Each trace contains observations: spans for nested activities, events for distinct actions, or generations for LLM interactions. This setup mirrors your app’s execution flow, offering insights into performance and behavior. See our [Tracing documentation](/docs/tracing) for more details on Langfuse’s telemetry model.

`@observe()` decorator automatically and asynchronously logs nested traces to Langfuse. The outermost function becomes a `trace` in Langfuse, all children are `spans` by default.

By default it captures:

- nesting via context vars

- timings/durations

- args and kwargs as input dict

- returned values as output

```nextra-code
from langfuse.decorators import langfuse_context, observe
import time

@observe()
def wait():
    time.sleep(1)

@observe()
def capitalize(input: str):
    return input.upper()

@observe()
def main_fn(query: str):
    wait()
    capitalized = capitalize(query)
    return f"Q:{capitalized}; A: nice too meet you!"

main_fn("hi there");
```

Voilà! ✨ Langfuse will generate a trace with a nested span for you.

> **Example trace**: <https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/21128edc-27bf-4643-92f9-84d66c63de8d>

## Add additional parameters to the trace [Permalink for this section](#add-additional-parameters-to-the-trace)

In addition to the attributes automatically captured by the decorator, you can add others to use the full features of Langfuse.

Two utility methods:

- `langfuse_context.update_current_observation`: Update the trace/span of the current function scope

- `langfuse_context.update_current_trace`: Update the trace itself, can also be called within any deeply nested span within the trace

For details on available attributes, have a look at the [reference](https://python.reference.langfuse.com/langfuse/decorators#LangfuseDecorator.update_current_observation)

Below is an example demonstrating how to enrich traces and observations with custom parameters:

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe(as_type="generation")
def deeply_nested_llm_call():
    # Enrich the current observation with a custom name, input, and output
    langfuse_context.update_current_observation(
        name="Deeply nested LLM call", input="Ping?", output="Pong!"
    )
    # Set the parent trace's name from within a nested observation
    langfuse_context.update_current_trace(
        name="Trace name set from deeply_nested_llm_call",
        session_id="1234",
        user_id="5678",
        tags=["tag1", "tag2"],
        public=True
    )

@observe()
def nested_span():
    # Update the current span with a custom name and level
    langfuse_context.update_current_observation(name="Nested Span", level="WARNING")
    deeply_nested_llm_call()

@observe()
def main():
    nested_span()

# Execute the main function to generate the enriched trace
main()
```

On the Langfuse platform the trace now shows with the updated name from the `deeply_nested_llm_call`, and the observations will be enriched with the appropriate data points.

> **Example trace**: <https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/f16e0151-cca8-4d90-bccf-1d9ea0958afb>

## Log an LLM Call using `as_type="generation"` [Permalink for this section](#log-an-llm-call-using-as_typegeneration)

Model calls are represented by `generations` in Langfuse and allow you to add additional attributes. Use the `as_type="generation"` flag to mark a function as a generation. Optionally, you can extract additional generation specific attributes ( [reference](https://python.reference.langfuse.com/langfuse/decorators#LangfuseDecorator.update_current_observation)).

This works with any LLM provider/SDK. In this example, we’ll use Anthropic.

```nextra-code
%pip install anthropic
```

```nextra-code
os.environ["ANTHROPIC_API_KEY"] = ""

import anthropic
anthopic_client = anthropic.Anthropic()
```

```nextra-code
# Wrap LLM function with decorator
@observe(as_type="generation")
def anthropic_completion(**kwargs):
  # extract some fields from kwargs
  kwargs_clone = kwargs.copy()
  input = kwargs_clone.pop('messages', None)
  model = kwargs_clone.pop('model', None)
  langfuse_context.update_current_observation(
      input=input,
      model=model,
      metadata=kwargs_clone
  )

  response = anthopic_client.messages.create(**kwargs)

  # See docs for more details on token counts and usd cost in Langfuse
  # https://langfuse.com/docs/model-usage-and-cost
  langfuse_context.update_current_observation(
      usage_details={
          "input": response.usage.input_tokens,
          "output": response.usage.output_tokens
      }
  )

  # return result
  return response.content[0].text

@observe()
def main():
  return anthropic_completion(
      model="claude-3-opus-20240229",
      max_tokens=1024,
      messages=[\
          {"role": "user", "content": "Hello, Claude"}\
      ]
  )

main()
```

> **Example trace**: <https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/66d06dd7-eeec-40c1-9b11-aac0e9c4f2fe?observation=d48a45f8-593c-4013-8a8a-23665b94aeda>

## Customize input/output [Permalink for this section](#customize-inputoutput)

By default, input/ouput of a function are captured by `@observe()`.

**You can disable capturing input/output** for a specific function:

```nextra-code
from langfuse.decorators import observe

@observe(capture_input=False, capture_output=False)
def stealth_fn(input: str):
    return input

stealth_fn("Super secret content")
```

> **Example trace**: <https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/6bdeb443-ef8c-41d8-a8a1-68fe75639428>

Alternatively, you can **override input and output** via `update_current_observation` (or `update_current_trace`):

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def fn_2():
    langfuse_context.update_current_observation(
        input="Table?", output="Tennis!"
    )
    # Logic for a deeply nested LLM call
    pass

@observe()
def main_fn():
    langfuse_context.update_current_observation(
        input="Ping?", output="Pong!"
    )
    fn_2()

main_fn()
```

> **Example trace**: <https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/d3c3ad92-d85d-4437-aaf3-7587d84f398c>

## Interoperability with other Integrations [Permalink for this section](#interoperability-with-other-integrations)

Langfuse is tightly integrated with the OpenAI SDK, LangChain, and LlamaIndex. The integrations are seamlessly interoperable with each other within a decorated function. The following example demonstrates this interoperability by using all three integrations within a single trace.

### 1\. Initializing example applications [Permalink for this section](#1-initializing-example-applications)

```nextra-code
%pip install llama-index langchain langchain_openai --upgrade
```

#### OpenAI [Permalink for this section](#openai)

The [OpenAI integration](https://langfuse.com/docs/integrations/openai/get-started) automatically detects the context in which it is executed. Just use `from langfuse.openai import openai` and get native tracing of all OpenAI calls.

```nextra-code
from langfuse.openai import openai
from langfuse.decorators import observe

@observe()
def openai_fn(calc: str):
    res = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[\
          {"role": "system", "content": "You are a very accurate calculator. You output only the result of the calculation."},\
          {"role": "user", "content": calc}],
    )
    return res.choices[0].message.content
```

#### LlamaIndex [Permalink for this section](#llamaindex)

Via `Settings.callback_manager` you can configure the callback to use for tracing of the subsequent LlamaIndex executions. `langfuse_context.get_current_llama_index_handler()` exposes a callback handler scoped to the current trace context, in this case `llama_index_fn()`.

```nextra-code
from langfuse.decorators import langfuse_context, observe
from llama_index.core import Document, VectorStoreIndex
from llama_index.core import Settings
from llama_index.core.callbacks import CallbackManager

doc1 = Document(text="""
Maxwell "Max" Silverstein, a lauded movie director, screenwriter, and producer, was born on October 25, 1978, in Boston, Massachusetts. A film enthusiast from a young age, his journey began with home movies shot on a Super 8 camera. His passion led him to the University of Southern California (USC), majoring in Film Production. Eventually, he started his career as an assistant director at Paramount Pictures. Silverstein's directorial debut, “Doors Unseen,” a psychological thriller, earned him recognition at the Sundance Film Festival and marked the beginning of a successful directing career.
""")
doc2 = Document(text="""
Throughout his career, Silverstein has been celebrated for his diverse range of filmography and unique narrative technique. He masterfully blends suspense, human emotion, and subtle humor in his storylines. Among his notable works are "Fleeting Echoes," "Halcyon Dusk," and the Academy Award-winning sci-fi epic, "Event Horizon's Brink." His contribution to cinema revolves around examining human nature, the complexity of relationships, and probing reality and perception. Off-camera, he is a dedicated philanthropist living in Los Angeles with his wife and two children.
""")

@observe()
def llama_index_fn(question: str):
    # Set callback manager for LlamaIndex, will apply to all LlamaIndex executions in this function
    langfuse_handler = langfuse_context.get_current_llama_index_handler()
    Settings.callback_manager = CallbackManager([langfuse_handler])

    # Run application
    index = VectorStoreIndex.from_documents([doc1,doc2])
    response = index.as_query_engine().query(question)
    return response
```

#### LangChain [Permalink for this section](#langchain)

`langfuse_context.get_current_llama_index_handler()` exposes a callback handler scoped to the current trace context, in this case `langchain_fn()`. Pass it to subsequent runs to your LangChain application to get full tracing within the scope of the current trace.

```nextra-code
from operator import itemgetter
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langfuse.decorators import observe

prompt = ChatPromptTemplate.from_template("what is the city {person} is from?")
model = ChatOpenAI()
chain = prompt | model | StrOutputParser()

@observe()
def langchain_fn(person: str):
    # Get Langchain Callback Handler scoped to the current trace context
    langfuse_handler = langfuse_context.get_current_langchain_handler()

    # Pass handler to invoke
    chain.invoke({"person": person}, config={"callbacks":[langfuse_handler]})
```

### 2\. Run all in a single trace [Permalink for this section](#2-run-all-in-a-single-trace)

```nextra-code
from langfuse.decorators import observe

@observe()
def main():
    output_openai = openai_fn("5+7")
    output_llamaindex = llama_index_fn("What did he do growing up?")
    output_langchain = langchain_fn("Feynman")

    return output_openai, output_llamaindex, output_langchain

main();
```

> **Example trace**: <https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/4fcd93e3-79f2-474a-8e25-0e21c616249a>

## Flush observations [Permalink for this section](#flush-observations)

The Langfuse SDK executes network requests in the background on a separate thread for better performance of your application. This can lead to lost events in short lived environments such as AWS Lambda functions when the Python process is terminated before the SDK sent all events to the Langfuse API.

Make sure to call `langfuse_context.flush()` before exiting to prevent this. This method waits for all tasks to finish.

## Additional features [Permalink for this section](#additional-features)

### Scoring [Permalink for this section](#scoring)

[Scores](https://langfuse.com/docs/scores/overview) are used to evaluate single observations or entire traces. You can create them via our annotation workflow in the Langfuse UI, run model-based evaluation or ingest via the SDK.

| Parameter | Type | Optional | Description | 
|---|---|---|---|
| name | string | no | Identifier of the score. | 
| value | number | no | The value of the score. Can be any number, often standardized to 0..1 | 
| comment | string | yes | Additional context/explanation of the score. | 

#### Within the decorated function [Permalink for this section](#within-the-decorated-function)

You can attach a score to the current observation context by calling `langfuse_context.score_current_observation`. You can also score the entire trace from anywhere inside the nesting hierarchy by calling `langfuse_context.score_current_trace`:

```nextra-code
from langfuse.decorators import langfuse_context, observe

@observe()
def nested_span():
    langfuse_context.score_current_observation(
        name="feedback-on-span",
        value=1,
        comment="I like how personalized the response is",
    )

    langfuse_context.score_current_trace(
        name="feedback-on-trace-from-nested-span",
        value=1,
        comment="I like how personalized the response is",
    )


# This will create a new trace
@observe()
def main():
    langfuse_context.score_current_trace(
        name="feedback-on-trace",
        value=1,
        comment="I like how personalized the response is",
    )
    nested_span()

main()
```

> **Example trace**: <https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/1dfcff43-34c3-4888-b99a-bb9b9afd57c9>

#### Outside the decorated function [Permalink for this section](#outside-the-decorated-function)

Alternatively you may also score a trace or observation from outside its context as often scores are added async. For example, based on user feedback.

The decorators expose the trace_id and observation_id which are necessary to add scores outside of the decorated functions:

```nextra-code
from langfuse import Langfuse
from langfuse.decorators import langfuse_context, observe

# Initialize the Langfuse client
langfuse_client = Langfuse()

@observe()
def nested_fn():
    span_id = langfuse_context.get_current_observation_id()

    # can also be accessed in main
    trace_id = langfuse_context.get_current_trace_id()

    return "foo_bar", trace_id, span_id

# Create a new trace
@observe()
def main():

    _, trace_id, span_id = nested_fn()

    return "main_result", trace_id, span_id


# Flush the trace to send it to the Langfuse platform
langfuse_context.flush()

# Execute the main function to generate a trace
_, trace_id, span_id = main()

# Score the trace from outside the trace context
langfuse_client.score(
    trace_id=trace_id,
    name="trace-score",
    value=1,
    comment="I like how personalized the response is"
)

# Score the specific span/function from outside the trace context
langfuse_client.score(
    trace_id=trace_id,
    observation_id=span_id,
    name="span-score",
    value=1,
    comment="I like how personalized the response is"
);
```

> **Example trace**: <https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/0090556d-015c-48cb-bc33-4af29b05af31>

### Customize IDs [Permalink for this section](#customize-ids)

By default, Langfuse assigns random ids to all logged events.

If you have your own unique ID (e.g. messageId, traceId, correlationId), you can easily set those as trace or observation IDs for effective lookups in Langfuse.

To dynamically set a custom ID for a trace or observation, simply pass a keyword argument `langfuse_observation_id` to the function decorated with `@observe()`. Thereby, the trace/observation in Langfuse will use this id. Note: ids in Langfuse are unique and traces/observations are upserted/merged on these ids.

```nextra-code
from langfuse.decorators import langfuse_context, observe
import uuid

@observe()
def process_user_request(user_id, request_data, **kwargs):
    # Function logic here
    pass


def main():
    user_id = "user123"
    request_data = {"action": "login"}

    # Custom ID for tracking
    custom_observation_id = "custom-" + str(uuid.uuid4())

    # Pass id as kwarg
    process_user_request(
        user_id=user_id,
        request_data=request_data,
        # Pass the custom observation ID to the function
        langfuse_observation_id=custom_observation_id,
    )

main()
```

> **Example trace**: <https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/custom-bbda815f-c61a-4cf5-a545-7fceeef1b635>

### Debug mode [Permalink for this section](#debug-mode)

Enable debug mode to get verbose logs. Set the debug mode via the environment variable `LANGFUSE_DEBUG=True`.

### Authentication check [Permalink for this section](#authentication-check)

Use `langfuse_context.auth_check()` to verify that your host and API credentials are valid.

```nextra-code
from langfuse.decorators import langfuse_context

assert langfuse_context.auth_check()
```