---
tags:
  - ai coding
Type:
  - Documentation
Framework:
  - Agnostic
Phase:
  - Coding
Notes: Short Intro to Cerebras AI Inference Endpoint Logic
Model Optimised:
  - n.a.
---
# Cerebras - Short Documentation

````markdown
## Introduction

The Cerebras Chat Completion API is a powerful tool for developers to integrate advanced AI capabilities into their applications. This API allows for seamless interaction with Cerebras' large language models, providing fast and efficient inference for various natural language processing tasks.

## Key Features

### Model Selection

The API supports multiple models, including:

- llama3.1-8b
- llama3.1-70b

These models offer different capabilities and performance characteristics, allowing developers to choose the most suitable option for their specific use case[4].

### Request Format

The API follows a familiar format, similar to the OpenAI Chat Completions API, making it easy for developers to integrate or migrate existing projects[5]. The basic structure of a chat completion request includes:

- Messages: An array of message objects, each with a "role" (e.g., "user" or "system") and "content"
- Model: The specific model to use for the completion
- Additional parameters for fine-tuning the output

### Customization Options

Developers can customize their requests with various parameters:

- **Temperature**: Controls the randomness of the output (between 0 and 1.5)
- **Max Tokens**: Limits the length of the generated response
- **Top_p**: An alternative to temperature for controlling output diversity
- **Stream**: Enables real-time streaming of the response
- **Stop Sequences**: Specifies up to 4 sequences where the API will stop generating tokens
- **User**: A unique identifier for the end-user, useful for abuse monitoring[4]

## Implementation

### Installation

To get started, install the Cerebras Inference library:

```bash
pip install cerebras_cloud_sdk
```

### Authentication

Set up your API key as an environment variable for security:

```bash
export CEREBRAS_API_KEY="your-api-key-here"
```

### Basic Usage

Here's a simple example of how to use the API for chat completion:

```python
import os
from cerebras_cloud_sdk import Cerebras

client = Cerebras(api_key=os.environ.get("CEREBRAS_API_KEY"))

response = client.chat.completions.create(
    messages=[{"role": "user", "content": "Why is fast inference important?"}],
    model="llama3.1-8b"
)

print(response.choices[0].message.content)
```

### Streaming Responses

For real-time responses, you can use the streaming feature:

```python
stream = await client.chat.completions.create(
    messages=[{"role": "user", "content": "Why is fast inference important?"}],
    model="llama3.1-8b",
    stream=True
)

for chunk in stream:
    print(chunk.choices[0].delta.content, end="")
```

## Advanced Features

### Tool Integration

The Cerebras API supports the integration of custom tools, allowing the model to perform specific functions when needed. This is particularly useful for tasks that require external data or computations[2].

### TypeScript Support

For TypeScript users, the API provides type definitions for request params and response fields, enhancing code quality and developer experience[1].

## Performance

Cerebras claims to offer "the world's fastest AI inference," providing high-speed processing for various AI tasks. This performance can be particularly beneficial for applications requiring real-time interactions or processing large volumes of data[5].

By leveraging the Cerebras Chat Completion API, developers can create sophisticated AI-powered applications with ease, benefiting from the advanced capabilities of Cerebras' language models and the flexibility of their API design.

Citations:
[1] https://github.com/Cerebras/cerebras-cloud-sdk-node
[2] https://inference-docs.cerebras.ai/agentbootcamp-section-2
[3] https://inference-docs.cerebras.ai/quickstart
[4] https://inference-docs.cerebras.ai/api-reference/completions
[5] https://www.reddit.com/r/LocalLLaMA/comments/1f2luab/cerebras_launches_the_worlds_fastest_ai_inference/
[6] https://github.com/Cerebras/inference-examples/blob/main/getting-started/README.md



The Cerebras Inference API provides fast model inference through Python integration. Here's a comprehensive guide on how to use it.

## Installation and Setup

First, install the required package:

```bash
pip install cerebras_cloud_sdk
```

Set up your API key as an environment variable[1]:

```bash
export CEREBRAS_API_KEY="your-api-key-here"
```

## Basic Usage

### Simple Chat Completion

```python
from cerebras.cloud.sdk import Cerebras
import os

# Initialize the client
client = Cerebras(api_key=os.environ.get("CEREBRAS_API_KEY"))

# Create a chat completion
response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Why is fast inference important?"
        }
    ],
    model="llama3.1-8b"
)

print(response)
```

### Async Implementation

```python
import asyncio
from cerebras.cloud.sdk import AsyncCerebras

async def main():
    client = AsyncCerebras(api_key=os.environ.get("CEREBRAS_API_KEY"))
    
    response = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Why is fast inference important?"
            }
        ],
        model="llama3.1-8b"
    )
    print(response)

asyncio.run(main())
```

## Advanced Features

### Structured Outputs with Instructor

```python
import instructor
from cerebras.cloud.sdk import Cerebras
from pydantic import BaseModel

# Initialize instructor client
client = instructor.from_cerebras(Cerebras())

# Define output structure
class Person(BaseModel):
    name: str
    age: int

# Extract structured data
response = client.chat.completions.create(
    model="llama3.1-70b",
    messages=[{
        "role": "user",
        "content": "Extract: John Smith is 29 years old."
    }],
    response_model=Person
)[1]
```

### Streaming Responses

```python
from cerebras.cloud.sdk import AsyncCerebras

async def main():
    client = AsyncCerebras()
    stream = await client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": "Write a story"
        }],
        model="llama3.1-8b",
        stream=True
    )
    
    async for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")

asyncio.run(main())
```

## Available Models

**Llama 3.1 8B**
- Model ID: `llama3.1-8b`
- Parameters: 8 billion
- Context Length: 8192 tokens
- Knowledge cutoff: March 2023[8]

**Llama 3.1 70B**
- Model ID: `llama3.1-70b`
- Parameters: 70 billion
- Context Length: 8192 tokens
- Knowledge cutoff: December 2023[8]

## Performance Considerations

The Cerebras API offers significantly faster inference speeds compared to traditional GPU solutions, with claims of up to 20x faster performance[1]. For optimal performance:

- Use batching when processing multiple requests
- Consider using async implementations for concurrent processing
- Monitor token usage and processing time through the response object's usage and time_info fields[7]

Citations:
[1] https://python.useinstructor.com/blog/2024/10/15/introducing-structured-outputs-with-cerebras-inference/
[2] https://github.com/Cerebras/inference-examples
[3] https://inference-docs.cerebras.ai/quickstart
[4] https://github.com/Cerebras/cerebras-cloud-sdk-python
[5] https://docs.cerebras.net/en/2.1.0/wsc/general/functional_inference.html
[6] https://docs.cerebras.net/en/rel-2.2.0/wsc/general/functional_inference.html
[7] https://github.com/Cerebras/inference-examples/blob/main/getting-started/README.md
[8] https://inference-docs.cerebras.ai/introduction
````