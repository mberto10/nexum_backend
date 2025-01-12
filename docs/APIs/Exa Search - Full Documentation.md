---
tags:
  - ai coding
Type:
  - Documentation
Framework:
  - Agnostic
Phase:
  - Coding
Notes: Full Exa Search Documentation Scraped
Model Optimised:
  - n.a.
---
# Exa Search - Full Documentation

````markdown
# docs.exa.ai llms.txt

[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Concepts

Contents retrieval with Exa API

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

When using the Exa API, you can request different types of content to be returned for each search result. The three content return types are:

### [](\#text-text-true)  Text (text=True):

Returns the full text content of the result, such as the main body of an article or webpage. This is extractive content directly taken from the source.

### [](\#highlights-highlights-true)  Highlights (highlights=True):

Delivers key excerpts from the text that are most relevant to your search query, emphasizing important information within the content. This is also extractive content from the source.

### [](\#summary-summary-true)  Summary (summary=True):

Provides a concise summary generated from the text, tailored to a specific query you provide. This is abstractive content created by processing the source text using Gemini Flash.

By specifying these options in your API call, you can control the depth and focus of the information returned, making your search results more actionable and relevant.

To see the full configurability of the contents returns, [check out our Dashboard](https://dashboard.exa.ai/) and sample queries.

[Prompting Guide](/reference/prompting-guide) [Exa's Capabilities Explained](/reference/exas-capabilities-explained)

On this page

- [Text (text=True):](#text-text-true)
- [Highlights (highlights=True):](#highlights-highlights-true)
- [Summary (summary=True):](#summary-summary-true)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Admin

Setting Up and Managing Your Team

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa organizes account usage and paid feature access through ‘Teams’:

Upon account creation, you’re placed in a ‘Personal’ Team. You can use the dropdown in the top-left of the Exa dashboard shown below to create a new Team or select between other Teams you have. You can make as many Teams as you like.

## [](\#seeing-your-teams)  Seeing your teams

![Team dropdown (top-left) within the Exa dashboard under Team settings](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/7f964a0-Screenshot_2024-07-14_at_18.55.37.png)

Team dropdown (top-left) within the Exa dashboard under Team settings

## [](\#topping-up-a-teams-balance)  Topping up a Team’s balance

With the desired Team selected, you can top up your credit balance in the Billing page.

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/522f9a0-Screenshot_2024-07-14_at_18.57.25.png)

## [](\#inviting-people-to-your-team)  Inviting people to your team

Team admins can add members via the Invite feature in Team settings.

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/ac51b5b-Screenshot_2024-07-14_at_18.57.50.png)

Once a team member is invited, their status will be ‘Pending’ on the team management menu.

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/291cf4a-Screenshot_2024-07-14_at_18.59.29.png)

They will receive an email inviting them to join the team.

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/5168c00-Screenshot_2024-07-08_at_21.01.10.png)

Once accepted, you’ll see both members are ‘Accepted’. All Team members share the usage limits and features of their respective Team’s plan.

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/858e63a-Screenshot_2024-07-14_at_19.01.19.png)

[Exa LiveCrawl](/reference/should-we-use-livecrawl) [Rate Limits](/reference/rate-limits)

On this page

- [Seeing your teams](#seeing-your-teams)
- [Topping up a Team’s balance](#topping-up-a-teams-balance)
- [Inviting people to your team](#inviting-people-to-your-team)

![Team dropdown (top-left) within the Exa dashboard under Team settings](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/7f964a0-Screenshot_2024-07-14_at_18.55.37.png)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/522f9a0-Screenshot_2024-07-14_at_18.57.25.png)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/ac51b5b-Screenshot_2024-07-14_at_18.57.50.png)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/291cf4a-Screenshot_2024-07-14_at_18.59.29.png)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/5168c00-Screenshot_2024-07-08_at_21.01.10.png)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/858e63a-Screenshot_2024-07-14_at_19.01.19.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Concepts

How Exa Search Works

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

## [](\#introducing-neural-searches-via-next-link-prediction)  Introducing neural searches via ‘next-link prediction’

At Exa, we’ve built our very own index of high quality web content, and have trained a model to query this index powered by the same embeddings-based technology that makes modern LLMs so powerful.

By using embeddings, we move beyond keyword searches to use ‘next-link prediction’, understanding the semantic content of queries and indexed documents. This method predicts which web links are most relevant based on the semantic meaning, not just direct word matches.

By doing this, our model anticipates the most relevant links by understanding complex queries, including indirect or thematic relationships. This approach is especially effective for exploratory searches, where precise terms may be unknown, or where queries demand many, often semantically dense, layered filters.

## [](\#combining-neural-and-keyword-the-best-of-both-worlds-through-exa-auto-search)  Combining neural and keyword - the best of both worlds through Exa Auto Search

Sometimes keyword search is the best way to query the web - for instance, you may have a specific word or piece of jargon that you want to match explicitly with results (often the case with proper nouns like place-names). In these cases, semantic searches are not the most useful.

To ensure our engine is comprehensive, we have built keyword search in parallel to our novel neural search capability. This means Exa is an ‘all-in-one’ search solution, no matter what your query needs are.

Lastly, we surface both query archetypes through ‘Auto Search’, to give users the best of both worlds - we have built a small categorization model that understands your query, our search infrastructure and therefore routes your particular query to the best matched search type.

See here for the way we set Auto Search in a simple Python example. Type has options `neural`, `keyword` or `auto`.

At one point, Exa auto Auto Search was named Magic Search - this has been changed

Python

Copy

```Python
result = exa.search_and_contents(
  "hottest AI startups",
  type="auto",
)

```

[Tool calling with Claude](/reference/tool-calling-with-claude) [The Exa Index](/reference/the-exa-index)

On this page

- [Introducing neural searches via ‘next-link prediction’](#introducing-neural-searches-via-next-link-prediction)
- [Combining neural and keyword - the best of both worlds through Exa Auto Search](#combining-neural-and-keyword-the-best-of-both-worlds-through-exa-auto-search)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Live Demos

Exa-powered Hallucination Detector

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

[\> try the app](https://demo.exa.ai/hallucination-detector)

* * *

We built a live hallucination detector that uses Exa to verify LLM-generated content. When you input text, the app breaks it into individual claims, searches for evidence to verify each one, and returns relevant sources with a verification confidence score.

A claim is a single, verifiable statement that can be proven true or false - like “The Eiffel Tower is in Paris” or “It was built in 1822.”

[![Screenshot%202024-11-19%20at%203.19.48%E2%80%AFPM](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/Screenshot%202024-11-19%20at%203.19.48%E2%80%AFPM.png)\\
\\
**Click here to try it out.**](https://demo.exa.ai/hallucination-detector)

This document explains the functions behind the three steps of the fact-checker:

1. The LLM extracts verifiable claims from your text
2. Exa searches for relevant sources for each claim
3. The LLM evaluates each claim against its sources, returning whether or not its true, along with a confidence score.

See the full [step-by-step guide](/examples/identifying-hallucinations-with-exa) and [github repo](https://github.com/exa-labs/exa-hallucination-detector) if you’d like to recreate.

* * *

## [](\#function-breakdown)  Function breakdown

1

Extracting claims

The `extract_claims` function uses an LLM (Anthropic’s, in this case) to identify distinct, verifiable statements from your inputted text, returning these claims as a JSON array of strings.

For simpilicity, we did not include a try/catch block in the code below. However, if you are building your own hallucination detector, you should include one that catches any errors in the LLM parsing and uses a regex method that treats each sentence (text between capital letter and end punctuation) as a claim.

Python

Copy

```python
def extract_claims(text: str) -> List[str]:
    """Extract factual claims from the text using an LLM."""
    system_message = SystemMessage(content="""
        You are an expert at extracting claims from text.
        Your task is to identify and list all claims present, true or false,
        in the given text. Each claim should be a single, verifiable statement.
        Present the claims as a JSON array of strings.
    """)

    human_message = HumanMessage(content=f"Extract factual claims from this text: {text}")
    response = llm.invoke([system_message, human_message])

    claims = json.loads(response.content)
    return claims

```

2

Searching for evidence

The `exa_search` function uses Exa search to find evidence for each extracted claim. For every claim, it retrieves the 5 most relevant sources, formats them with their URLs and content ( `text`), passing them to the next function for verification.

Python

Copy

```python
def exa_search(query: str) -> List[str]:
    """Retrieve relevant documents using Exa's semantic search."""
    search = ExaSearchRetriever(k=5, text=True, use_autoprompt=False)

    document_prompt = PromptTemplate.from_template("""
        <source>
            <url>{url}</url>
            <text>{text}</text>
        </source>
    """)

    parse_info = RunnableLambda(
        lambda document: {
            "url": document.metadata["url"],
            "text": document.page_content or "No text available",
        }
    )

    document_chain = (parse_info | document_prompt)
    search_chain = search | document_chain.map()
    documents = search_chain.invoke(query)

    return [str(doc) for doc in documents]

```

3

Verifying claims

The `verify_claim` function checks each claim against the sources from `exa_search`. It uses an LLM to determine if the sources support or refute the claim and returns a decision with a confidence score. If no sources are found, it returns “insufficient information”.

Python

Copy

```python
def verify_claim(claim: str, sources: List[str]) -> Dict[str, Any]:
    """Verify a single claim using combined Exa search sources."""
    if not sources:
        return {
            "claim": claim,
            "assessment": "Insufficient information",
            "confidence_score": 0.5,
            "supporting_sources": [],
            "refuting_sources": []
        }

    combined_sources = "\n\n".join(sources)

    system_message = SystemMessage(content="""
        You are an expert fact-checker.
        Given a claim and sources, determine whether the claim is supported,
        refuted, or lacks sufficient evidence.
        Provide your answer as a JSON object with assessment and confidence score.
    """)

    human_message = HumanMessage(content=f'Claim: "{claim}"\nSources:\n{combined_sources}')
    response = llm.invoke([system_message, human_message])

    return json.loads(response.content)

```

Using LLMs to extract claims and verify them against Exa search sources is a simple way to detect hallucinations in content. If you’d like to recreate it, the full documentation for the script is [here](/examples/identifying-hallucinations-with-exa) and the github repo is [here](https://github.com/exa-labs/exa-hallucination-detector).

[Exa-powered Writing Assistant](/examples/demo-exa-powered-writing-assistant)

On this page

- [Function breakdown](#function-breakdown)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Tutorials

Exa Researcher - Python

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

### [](\#what-this-doc-covers)  What this doc covers

1. Using Exa’s Auto Search to pick the best search setting for each query (keyword or neural)
2. Using search\_and\_contents() through Exa’s Python SDK

* * *

In this example, we will build Exa Researcher, a Python app that, given a research topic, automatically searches for relevant sources with Exa’s [auto search](../reference/exa-s-capabilities-explained) and synthesizes the information into a reliable research report.

To run this code, first we need a [Exa API key](https://dashboard.exa.ai/api-keys) and an [OpenAI API key](https://platform.openai.com/api-keys).

If you would like to se the full code for this tutorial as a Colab notebook, [click here](https://colab.research.google.com/drive/1Aj6bBptSHWxZO7GVG2RoWtQSEkpabuaF?usp=sharing)

## [](\#setup)  Setup

Let’s import the Exa and OpenAI SDKs and set up our API keys to create client objects for each. We’ll use environment variables to securely store our API keys.

Python

Copy

```Python
import os
import exa_py
from openai import OpenAI

EXA_API_KEY = os.environ.get('EXA_API_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

exa = exa_py.Exa(EXA_API_KEY)
openai_client = OpenAI(api_key=OPENAI_API_KEY)

```

Since we’ll be making several calls to the OpenAI API to get a completion from GPT-3.5 Turbo, let’s make a simple utility function so we can pass in the system and user messages directly, and get the LLM’s response back as a string.

Python

Copy

```Python
def get_llm_response(system='You are a helpful assistant.', user='', temperature=1, model='gpt-3.5-turbo'):
    completion = openai_client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[\
            {'role': 'system', 'content': system},\
            {'role': 'user', 'content': user},\
        ]
    )
    return completion.choices[0].message.content

```

Okay, great! Now let’s start building Exa Researcher.

## [](\#exa-auto-search)  Exa Auto Search

The researcher should be able to automatically generate research reports for all kinds of different topics. Here’s two to start:

Python

Copy

```Python
SAMA_TOPIC = 'Sam Altman'
ART_TOPIC = 'renaissance art'

```

The first thing our researcher has to do is decide what kind of search to do for the given topic.

Exa offers two kinds of search: **neural** and **keyword** search. Here’s how we decide:

- Neural search is preferred when the query is broad and complex because it lets us retrieve high quality, semantically relevant data. Neural search is especially suitable when a topic is well-known and popularly discussed on the Internet, allowing the machine learning model to retrieve contents which are more likely recommended by real humans.
- Keyword search is useful when the topic is specific, local or obscure. If the query is a specific person’s name, and identifier, or acronym, such that relevant results will contain the query itself, keyword search may do well. And if the machine learning model doesn’t know about the topic, but relevant documents can be found by directly matching the search query, keyword search may be necessary.

Conveniently, Exa’s [auto search](../reference/exa-s-capabilities-explained) feature (on by default) will automatically decide whether to use `keyword` or `neural` search for each query. For example, if a query is a specific person’s name, Exa would decide to use keyword search.

Now, we’ll create a helper function to generate search queries for our topic.

Python

Copy

```Python
def generate_search_queries(topic, n):
    user_prompt = f"""I'm writing a research report on {topic} and need help coming up with diverse search queries.
Please generate a list of {n} search queries that would be useful for writing a research report on {topic}. These queries can be in various formats, from simple keywords to more complex phrases. Do not add any formatting or numbering to the queries."""

    completion = get_llm_response(
        system='The user will ask you to help generate some search queries. Respond with only the suggested queries in plain text with no extra formatting, each on its own line.',
        user=user_prompt,
        temperature=1
    )
    return [s.strip() for s in completion.split('\n') if s.strip()][:n]

```

Next, let’s write another function that actually calls the Exa API to perform searches using Auto Search.

Python

Copy

```Python
def get_search_results(queries, links_per_query=2):
    results = []
    for query in queries:
        search_response = exa.search_and_contents(query,
            num_results=links_per_query,
            use_autoprompt=False
        )
        results.extend(search_response.results)
    return results

```

## [](\#writing-a-report-with-gpt-3-5-turbo)  Writing a report with GPT-3.5 Turbo

The final step is to instruct the LLM to synthesize the content into a research report, including citations of the original links. We can do that by pairing the content and the URLs and writing them into the prompt.

Python

Copy

```Python
def synthesize_report(topic, search_contents, content_slice=750):
    input_data = '\n'.join([f"--START ITEM--\nURL: {item.url}\nCONTENT: {item.text[:content_slice]}\n--END ITEM--\n" for item in search_contents])
    return get_llm_response(
        system='You are a helpful research assistant. Write a report according to the user\'s instructions.',
        user=f'Input Data:\n{input_data}Write a two paragraph research report about {topic} based on the provided information. Include as many sources as possible. Provide citations in the text using footnote notation ([#]). First provide the report, followed by a single "References" section that lists all the URLs used, in the format [#] <url>.',
        # model='gpt-4'  # want a better report? use gpt-4 (but it costs more)
    )

```

## [](\#all-together-now)  All Together Now

Now, let’s just wrap everything into one Researcher function that strings together all the functions we’ve written. Given a user’s research topic, the Researcher will generate search queries, feed those queries to Exa Auto Search, and finally use an LLM to synthesize the retrieved information. Three simple steps!

Python

Copy

```Python
def researcher(topic):
    print(f'Starting research on topic: "{topic}"')

    search_queries = generate_search_queries(topic, 3)
    print("Generated search queries:", search_queries)

    search_results = get_search_results(search_queries)
    print(f"Found {len(search_results)} search results. Here's the first one:", search_results[0])

    print("Synthesizing report...")
    report = synthesize_report(topic, search_results)

    return report

```

In just a couple lines of code, we’ve used Exa to go from a research topic to a valuable essay with up-to-date sources.

Python

Copy

```Python
def run_examples():
    print("Researching Sam Altman:")
    sama_report = researcher(SAMA_TOPIC)
    print(sama_report)

    print("\n\nResearching Renaissance Art:")
    art_report = researcher(ART_TOPIC)
    print(art_report)

# To use the researcher on the examples, simply call the run_examples() function:
if __name__ == "__main__":
    run_examples()

# Or, to research a specific topic:
# print(researcher("llama antibodies"))

```

This Python implementation of Exa Researcher demonstrates how to leverage Exa’s Auto Search feature and the OpenAI API to create an automated research tool. By combining Exa’s powerful search capabilities with GPT-3.5 Turbo’s language understanding and generation, we’ve created a system that can quickly gather and synthesize information on any given topic.

[Exa Researcher - JavaScript](/examples/exa-researcher) [Recruiting Agent](/examples/exa-recruiting-agent)

On this page

- [What this doc covers](#what-this-doc-covers)
- [Setup](#setup)
- [Exa Auto Search](#exa-auto-search)
- [Writing a report with GPT-3.5 Turbo](#writing-a-report-with-gpt-3-5-turbo)
- [All Together Now](#all-together-now)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Live Demos

Exa-powered Writing Assistant

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

[Click here to try the Exa-powered Writing Assistant](https://demo.exa.ai/writing)

[Click here to see the relevant GitHub repo and hosting instructions](https://github.com/exa-labs/exa-writing-assist)

### [](\#what-this-doc-covers)  What this doc covers

- Live demo link for hands-on experience (above!)
- Overview of a real-time writing assistant using Exa and Claude
- Breakdown of Exa query prompt engineering and generative AI system prompt

* * *

### [](\#demo-overview)  Demo overview

#### [](\#high-level-overview)  High-level overview

This demo showcases a real-time writing assistant that uses Exa’s search capabilities to provide relevant information and citations as a user writes. The system combines Exa’s neural search with Anthropic’s Claude AI model to generate contextually appropriate content and citations.

![Conceptual block diagram of how the writing assistant works](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/77dd3c1-image.png)

Conceptual block diagram of how the writing assistant works

#### [](\#exa-prompting-and-query-style)  Exa prompting and query style

The Exa search is performed using a unique query style that appends the user’s input with a prompt for continuation. Here’s the relevant code snippet:

JavaScript

Copy

```JavaScript

let exaQuery = conversationState.length > 1000
    ? (conversationState.slice(-1000))+"\n\nIf you found the above interesting, here's another useful resource to read:"
    : conversationState+"\n\nIf you found the above interesting, here's another useful resource to read:"

let exaReturnedResults = await exa.searchAndContents(
    exaQuery,
    {
        type: "neural",
        useAutoprompt: false,
        numResults: 10,
        highlights: {
            numSentences: 1,
            highlightsPerUrl: 1
        }
    }
)

```

**Key aspects of this query style:**

- **Continuation prompt:** The crucial post-pend “A helpful source to read so you can continue writing the above:“

  - This prompt is designed to find sources that can logically continue the user’s writing when passed to an LLM to generate content.
  - It leverages Exa’s ability to understand context and find semantically relevant results.
  - By framing the query as a request for continuation, it aligns with how people naturally share helpful links.
- **Length limitation:** It caps the query at 1000 characters to maintain relevance and continue writing just based on the last section of the text.

Note this prompt is not a hard and fast rule for this use-case - we encourage experimentation with query styles to get the best results for your specific use case. For instance, you could further constrain down to just research papers.

#### [](\#prompting-claude-with-exa-results)  Prompting Claude with Exa results

The Claude AI model is prompted with a carefully crafted system message and passed the above formatted Exa results. Here is an example system prompt:

TypeScript

Copy

```typescript
const systemPrompt = `You are an essay-completion bot that continues/completes a sentence given some input stub of an essay/prose. You only complete 1-2 SHORT sentence MAX. If you get an input of a half sentence or similar, DO NOT repeat any of the preceding text of the prose. THIS MEANS DO NOT INCLUDE THE STARTS OF INCOMPLETE SENTENCES IN YOUR RESPONSE. This is also the case when there is a spelling, punctuation, capitalization or other error in the starter stub - e.g.:

USER INPUT: pokemon is a
YOUR CORRECT OUTPUT: Japanese franchise created by Satoshi Tajiri.
NEVER/INCORRECT: Pokémon is a Japanese franchise created by Satoshi Tajiri.

USER INPUT: Once upon a time there
YOUR CORRECT OUTPUT: was a princess.
NEVER/INCORRECT: Once upon a time, there was a princess.

USER INPUT: Colonial england was a
YOUR CORRECT OUTPUT: time of great change and upheaval.
NEVER/INCORRECT: Colonial England was a time of great change and upheaval.

USER INPUT: The fog in san francisco
YOUR CORRECT OUTPUT: is a defining characteristic of the city's climate.
NEVER/INCORRECT: The fog in San Francisco is a defining characteristic of the city's climate.

USER INPUT: The fog in san francisco
YOUR CORRECT OUTPUT: is a defining characteristic of the city's climate.
NEVER/INCORRECT: The fog in San Francisco is a defining characteristic of the city's climate.

 Once you have made one citation, stop generating. BE PITHY. Where there is a full sentence fed in,
 you should continue on the next sentence as a generally good flowing essay would. You have a
 specialty in including content that is cited. Given the following two items, (1) citation context and
 (2) current essay writing, continue on the essay or prose inputting in-line citations in
 parentheses with the author's name, right after that followed by the relevant URL in square brackets.
 THEN put a parentheses around all of the above. If you cannot find an author (sometimes it is empty), use the generic name 'Source'.
 ample citation for you to follow the structure of: ((AUTHOR_X, 2021)[URL_X]).
 If there are more than 3 author names to include, use the first author name plus 'et al'`

```

This prompt ensures that:

- Claude will only do completions, not parrot back the user query like in a typical chat based scenario. Note the inclusion of multiple examples that demonstrate Claude should not reply back with the stub even if there are errors, like spelling or grammar, in the input text (which we found to be a common issue)
- We define the citation style and formatting. We also tell the bot went to collapse authors into ‘et al’ style citations, as some webpages have many authors

Once again, experimenting with this prompt is crucial to getting best results for your particular use case.

### [](\#conclusion)  Conclusion

This demo illustrates the power of combining Exa’s advanced search capabilities with generative AI to create a writing assistant. By leveraging Exa’s neural search and content retrieval features, the system can provide relevant, up-to-date information to any AI model, resulting in contextually appropriate content generation with citations.

This approach showcases how Exa can be integrated into AI-powered applications to enhance user experiences and productivity.

[Click here to try the Exa-powered Writing Assistant](https://demo.exa.ai/writing)

[Exa-powered Hallucination Detector](/examples/demo-hallucination-detector) [Twitter/X post Retrieval](/examples/live-demo-twitterx-post-retrieval)

On this page

- [What this doc covers](#what-this-doc-covers)
- [Demo overview](#demo-overview)
- [High-level overview](#high-level-overview)
- [Exa prompting and query style](#exa-prompting-and-query-style)
- [Prompting Claude with Exa results](#prompting-claude-with-exa-results)
- [Conclusion](#conclusion)

![Conceptual block diagram of how the writing assistant works](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/77dd3c1-image.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

RAG Quick Start Guide

CrewAI agents with Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

[CrewAI](https://crewai.com/) is a framework for orchestrating AI agents that work together to accomplish complex tasks.
In this guide, we’ll create a crew of two agents that generate a newsletter based on Exa’s search results. We’ll go over how to:

1. Create a custom Exa-powered CrewAI tool
2. Set up agents and assign them specific roles that use the Exa-powered search tool
3. Organize the agents into a crew that will write a newsletter

* * *

## [](\#get-started)  Get Started

1

Pre-requisites and installation

Install the crewAI core, crewAI tools and Exa Python SDK libraries.

Python

Copy

```Python
pip install crewai 'crewai[tools]' exa_py

```

2

Defining a custom Exa-based tool in crewAI

We set up a [custom tool](https://docs.crewai.com/concepts/tools) using the crewAI [@tool decorator](https://docs.crewai.com/concepts/tools#utilizing-the-tool-decorator). Within the tool, we can initialize the Exa class from the [Exa Python SDK](https://github.com/exa-labs/exa-py), make a request, and return a parsed out result.

Python

Copy

```Python
from crewai_tools import tool
from exa_py import Exa
import os

exa_api_key = os.getenv("EXA_API_KEY")

@tool("Exa search and get contents")
def search_and_get_contents_tool(question: str) -> str:
    """Tool using Exa's Python SDK to run semantic search and return result highlights."""

    exa = Exa(exa_api_key)

    response = exa.search_and_contents(
        question,
        type="neural",
        use_autoprompt=True,
        num_results=3,
        highlights=True
    )

    parsedResult = ''.join([\
      f'<Title id={idx}>{eachResult.title}</Title>\
      f'<URL id={idx}>{eachResult.url}</URL>\
      f'<Highlight id={idx}>{"".join(eachResult.highlights)}</Highlight>'\
      for (idx, eachResult) in enumerate(response.results)\
    ])

    return parsedResult

```

Make sure your API keys are initialized properly. For this demonstration, the environment variable names are `OPENAI_API_KEY` and `EXA_API_KEY` for OpenAI and Exa keys respectively.

[**Get your Exa API key**](https://dashboard.exa.ai/api-keys)

3

Setting up CrewAI agent

Import the relevant crewAI modules. Then, define `exa_tools` to reference the custom search method we defined above.

Python

Copy

```Python
from crewai import Task, Crew, Agent

exa_tools = search_and_get_contents_tool

```

We then set up [two agents](https://docs.crewai.com/concepts/Agents/) and place them in a [crew together](https://docs.crewai.com/concepts/Crews/):

- One to research with Exa (providing the custom tool defined above)
- Another to write a newsletter as an output (using an LLM)

Python

Copy

```Python
# Creating a senior researcher agent with memory and verbose mode
researcher = Agent(
  role='Researcher',
  goal='Get the latest research on {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "Driven by curiosity, you're at the forefront of"
    "innovation, eager to explore and share knowledge that could change"
    "the world."
  ),
  tools=[exa_tools],
  allow_delegation=False
)

article_writer = Agent(
  role='Researcher',
  goal='Write a great newsletter article on {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "Driven by a love of writing and passion for"
    "innovation, you are eager to share knowledge with"
    "the world."
  ),
  tools=[exa_tools],
  allow_delegation=False
)

```

4

Defining tasks for the agents

Next, we’ll define [tasks](https://docs.crewai.com/concepts/Tasks/) for each agent and create the crew overall using all of the components we’ve set up above.

Python

Copy

```Python
`research_task = Task(
  description=(
    "Identify the latest research in {topic}."
    "Your final report should clearly articulate the key points,"
  ),
  expected_output='A comprehensive 3 paragraphs long report on the {topic}.',
  tools=[exa_tools],
  agent=researcher,
)

write_article = Task(
  description=(
    "Write a newsletter article on the latest research in {topic}."
    "Your article should be engaging, informative, and accurate."
    "The article should address the audience with a greeting to the newsletter audience \"Hi readers!\", plus a similar signoff"
  ),
  expected_output='A comprehensive 3 paragraphs long newsletter article on the {topic}.',
  agent=article_writer,
)

crew = Crew(
  agents=[researcher, article_writer],
  tasks=[research_task, write_article],
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

```

5

Kicking off the crew

Finally, we kick off the crew by providing a research topic as our input query.

Python

Copy

```Python
response = crew.kickoff(inputs={'topic': 'Latest AI research'})

print(response)

```

6

Output

As you can see, Exa’s search results enriched the output generation!

Stdout

Copy

```Stdout
`[... Prior output truncated ...]

> Finished chain.
Hi readers!

As we step into the promising arena of 2024, we bring you some of the most significant advancements in the field of AI research. The year witnessed a considerable focus on the development of AI agents and LLMs (Large Language Models). Adept, a frontrunner in the space, showcased an agent that can find apartments on Redfin, input information into Salesforce, and interact with Google Sheets using natural language. While there is no clear winner on the commercial front yet, this development promises a future where AI can perform tasks for us.

The year also saw a continued focus on LLMs, with efforts directed towards matching the text performance of GPT-4 with smaller models. An interesting outcome of these efforts was the Falcon 7B model, which matches the performance of the 8B PaLM model. This model, interestingly, uses 100% web data for pretraining. It's worth mentioning that LLMs were also used to generate imitation models, which mimic the style of upstream LLMs. One study found that these models are highly rated by crowd workers.

In the field of computer vision, there were numerous developments. One noteworthy mention is the ASSET paper that introduced an architecture capable of modifying an input high-resolution image according to a user's edits on its semantic segmentation map. This advancement points to the possibility of synthesizing interesting phenomena in scenes, which has the potential to revolutionize the way we interact with digital imagery.

As we continue to explore the ever-evolving landscape of AI, we hope to bring you more such exciting updates. Stay tuned and until next time, keep exploring!

Best,
[Your Name]

```

[OpenAI Exa Wrapper](/reference/openai) [RAG with LlamaIndex](/reference/llamaindex)

On this page

- [Get Started](#get-started)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Tutorials

News Summarizer

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

### [](\#what-this-doc-covers)  What this doc covers

1\. Generating search queries for Exa using an LLM
2\. Retrieving relevant URLs and their contents using Exa
3\. Summarizing webpage contents using an LLM

In this example, we will build an LLM-based news summarizer with the Exa API to keep us up-to-date with the latest news on a given topic. We will use Exa to retrieve recent news articles and then feed the article contents to GPT-3.5 Turbo for summarization. This is a form of Retrieval Augmented Generation (RAG).

The Jupyter notebook for this tutorial is available on [Colab](https://colab.research.google.com/drive/1uZ0kxFCWmCqozl3ArTJohNpRbeEYlwlT?usp=sharing) for easy experimentation. You can also [check it out on Github](https://github.com/exa-labs/exa-py/tree/master/examples/newssummarizer/summarizer.ipynb), including a [plain Python version](https://github.com/exa-labs/exa-py/tree/master/examples/newssummarizer/summarizer.py) if you want to skip to the complete product.

To play with this code, we just need a [Exa API key](https://dashboard.exa.ai/overview) and an [OpenAI API key](https://platform.openai.com/api-keys). Get 1000 free Exa searches per month just for [signing up](https://dashboard.exa.ai/overview)!

## [](\#setup)  Setup

Python

Copy

```Python
# install Exa and OpenAI SDKs
!pip install exa_py
!pip install openai

```

Python

Copy

```Python
from google.colab import userdata # comment this out if you're not using Colab

EXA_API_KEY = userdata.get('EXA_API_KEY') # replace userdata.get(...) with your API key, or add your API key to Colab Secrets
OPENAI_API_KEY = userdata.get('OPENAI_API_KEY') # replace userdata.get(...) with your API key, or add your API key to Colab Secrets

```

## [](\#retrieving-news-with-exa)  Retrieving news with Exa

Let’s use the Exa neural search engine to search the web for relevant links to the user’s question.

First, we ask the LLM to generate a search engine query based on the question.

Python

Copy

```Python
import openai
from exa_py import Exa

openai.api_key = OPENAI_API_KEY
exa = Exa(EXA_API_KEY)

SYSTEM_MESSAGE = "You are a helpful assistant that generates search queries based on user questions. Only generate one search query."
USER_QUESTION = "What's the recent news in physics this week?"

completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[\
        {"role": "system", "content": SYSTEM_MESSAGE},\
        {"role": "user", "content": USER_QUESTION},\
    ],
)

search_query = completion.choices[0].message.content

print("Search query:")
print(search_query)

```

query:

Copy

```Search
Recent news in physics this week

```

Looks good! Now let’s put the search query into Exa. Let’s also use `start_published_date` to filter the results to pages published in the last week. Notice that we set `use_autoprompt=True` which lets the Exa API further optimize our search query for best results. Essentially, there is a special way to format Exa queries for best results, which `autoprompt` does automatically.

Python

Copy

```Python
from datetime import datetime, timedelta

one_week_ago = (datetime.now() - timedelta(days=7))
date_cutoff = one_week_ago.strftime("%Y-%m-%d")

search_response = exa.search_and_contents(
    search_query, use_autoprompt=True, start_published_date=date_cutoff
)

urls = [result.url for result in search_response.results]
print("URLs:")
for url in urls:
    print(url)

```

Copy

```
URLs:
https://phys.org/news/2024-01-carrots-reveals-mechanics-root-vegetable.html?utm_source=twitter.com&utm_medium=social&utm_campaign=v2
https://phys.org/news/2024-01-astrophysicists-theoretical-proof-traversable-wormholes.html
https://gizmodo.com/proton-physics-strong-force-quarks-measurement-1851192840
https://www.nytimes.com/2024/01/24/science/space/black-holes-photography-m87.html
https://phys.org/news/2024-01-liquid-lithium-walls-fusion-device.html?utm_source=twitter.com&utm_medium=social&utm_campaign=v2
https://physics.aps.org/articles/v17/s13
https://phys.org/news/2024-01-validating-hypothesis-complex.html?utm_source=twitter.com&utm_medium=social&utm_campaign=v2
https://phys.org/news/2024-01-scientists-previously-unknown-colonies-emperor.html?utm_source=twitter.com&utm_medium=social&utm_campaign=v2
https://phys.org/news/2024-01-reveals-quantum-topological-potential-material.html?utm_source=twitter.com&utm_medium=social&utm_campaign=v2
https://phys.org/news/2024-01-shallow-soda-lakes-cradles-life.html?utm_source=twitter.com&utm_medium=social&utm_campaign=v2

```

Now we’re getting somewhere! Exa gave our app a list of relevant, useful URLs based on the original question.

By the way, we might be wondering what makes Exa special. Why can’t we just search with Google? Well, [let’s take a look for ourselves](https://www.google.com/search?q=Recent+news+in+physics+this+week) at the Google search results. It gives us the front page of lots of news aggregators, but not the news articles themselves. And since we used Exa’s `search_and_contents`, our search also returns the webpage contents, so we can use Exa to skip writing a web crawler and access the knowledge directly!

Python

Copy

```Python
results = search_response.results
result_item = results[0]
print(f"{len(results)} items total, printing the first one:")
print(result_item.text)

```

Copy

```
10 items total, printing the first one:

 Credit: CC0 Public Domain

Chopped carrot pieces are among the most universally enjoyed foods and a snacking staple—a mainstay of school lunchboxes, picnics and party platters year-round.
Now researchers from the University of Bath have uncovered the secret science of prepping the popular root vegetable and quantified the processes that make them curl up if left uneaten for too long.
Mechanical Engineering student Nguyen Vo-Bui carried out the research as part of his final-year studies, in the limited circumstances of COVID-19 lockdowns of 2021. The research paper, "Modelling of longitudinally cut carrot curling induced by the vascular cylinder-cortex interference pressure", is published in Royal Society Open Science.
Without access to labs, Nguyen aimed to identify the geometrical and environmental factors that have the most influence on carrots' longevity. Working in his kitchen, he characterized, analytically modeled and verified the aging of over 100 Lancashire Nantes carrot halves, cut lengthways, using finite-element (FE) models normally used in structural engineering.
The research team concluded that residual stresses and dehydration were the two key factors behind the curling behavior. The starchy outer layer of the carrot (the cortex) is stiffer than the soft central vein (also known as the vascular cylinder). When cut lengthwise, the two carrot halves curl because the difference in stress becomes unbalanced. Dehydration leads to further loss of stiffness, further driving the curling effect.
Their recommendations to manufacturers include handling carrots in cold, moist, airtight and humidity-controlled environments to protect their natural properties and increase their edible life span.
They say the study provides a methodology to predict the deformation of cut root vegetables, adding that the procedure is likely to apply to other plant structures. The study gives food producers a new mathematical tool that could be applied to the design of packaging and food handling processes, potentially reducing food waste.
One of the world's top crops by market value, carrots are known for their high production efficiency—but despite this, wastage is high. Around 25–30% of this occurs prior to processing and packaging—due to deformities, mechanical damage or infected sections. Fresh cut and minimally processed carrots are a convenient ready-to-use ingredient that make possible the use of carrots that might otherwise be discarded, reducing food waste.
Dr. Elise Pegg, a senior lecturer in Bath's Department of Mechanical Engineering, is one of the research paper authors and oversaw the study. She said, "We have mathematically represented the curl of a cut carrot over time, and showed the factors that contribute to curling.
"Our motivation was to look for ways to improve the sustainability of carrot processing and make them as long-lasting as possible. We have produced a methodology that a food producer could use to change their processes, reducing food waste and making packaging and transportation more efficient. Understanding the bending behavior in such systems can help us to design and manufacture products with higher durability.
"A question like this would normally be investigated from a biological perspective, but we have done this work using purely mechanical principles. I'm so pleased for Nguyen—it's a measure of his resourcefulness and dedication to produce such interesting research in a challenging situation."
Over the course of a week, the curl of the carrot halves increased—with the average radius of each carrot's curvature falling from 1.61m to 1.1m. A 1.32-times reduction in stiffness was also seen, correlating with the carrots drying out; on average, their weight fell by 22%.
Nguyen added, "This was interesting research—to apply mechanical principles to vegetables was surprising and fun.
"One of the big challenges was to devise an experiment that could be done in a lockdown setting, without access to normal labs and equipment. To now be in a position to have this work published in an academic journal and potentially be used by the food industry is really rewarding.
"This project has inspired me to continue my studies at the University of Bath and I now study residual stresses in porous ferroelectric ceramics for my Ph.D."
As well as having to use a suitcase to collect the 30kg of carrots the experiment demanded from a farmers' market, a further challenge was finding ways to use them afterward. Carrot cake, the Indian carrot dessert Gajar Ka Halwa, carrot pesto and many other dishes kept Nguyen and his flatmates fed for several days.

More information:
	Modelling of longitudinally cut carrot curling induced by the vascular cylinder-cortex interference pressure, Royal Society Open Science (2024). DOI: 10.1098/rsos.230420. royalsocietypublishing.org/doi/10.1098/rsos.230420

Citation:
	Why do carrots curl? Research reveals the mechanics behind root vegetable aging (2024, January 23)
	retrieved 24 January 2024
	from https://phys.org/news/2024-01-carrots-reveals-mechanics-root-vegetable.html

	 This document is subject to copyright. Apart from any fair dealing for the purpose of private study or research, no
	 part may be reproduced without the written permission. The content is provided for information purposes only.

```

Awesome! That’s really interesting, or it would be if we had bothered to read it all. But there’s no way we’re doing that, so let’s ask the LLM to summarize it for us.

## [](\#summarizing-with-gpt-3-5-turbo)  Summarizing with GPT-3.5 Turbo

Python

Copy

```Python
import textwrap

SYSTEM_MESSAGE = "You are a helpful assistant that briefly summarizes the content of a webpage. Summarize the users input."

completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[\
        {"role": "system", "content": SYSTEM_MESSAGE},\
        {"role": "user", "content": result_item.text},\
    ],
)

summary = completion.choices[0].message.content

print(f"Summary for {urls[0]}:")
print(result_item.title)
print(textwrap.fill(summary, 80))

```

Copy

```
Summary for https://phys.org/news/2024-01-carrots-reveals-mechanics-root-vegetable.html?utm_source=twitter.com&utm_medium=social&utm_campaign=v2:
Why do carrots curl? Research reveals the mechanics behind root vegetable aging
Researchers from the University of Bath have conducted a study on the curling
behavior of chopped carrot pieces. The study found that residual stresses and
dehydration were the main factors behind the curling effect. The starchy outer
layer of the carrot is stiffer than the soft central vein, and when cut
lengthwise, the difference in stress causes the carrot to curl. Dehydration
further contributes to the curling effect. The research provides recommendations
to manufacturers on how to handle carrots to increase their edible lifespan. The
study also offers a methodology that can be used to predict the deformation of
cut root vegetables and potentially reduce food waste. The findings have
implications for the design of packaging and food handling processes. Carrots
are a highly produced crop, but wastage is still high, with a significant amount
occurring before processing and packaging. The study was carried out by
Mechanical Engineering student Nguyen Vo-Bui during the COVID-19 lockdowns of
2021.

```

And we’re done! We built an app that translates a question into a search query, uses Exa to search for useful links, uses Exa to grab clean content from those links, and summarizes the content to effortlessly answer your question about the latest news, or whatever we want.

We can be sure that the information is fresh, we have the source in front of us, and we did all this with an Exa query and LLM call. No web scraping or crawling needed!

**Through Exa, we have given our LLM access to the entire Internet.** The possibilities are endless.

[Hacker News Clone](/examples/live-demo-hacker-news-clone) [Identifying Hallucinations with Exa](/examples/identifying-hallucinations-with-exa)

On this page

- [What this doc covers](#what-this-doc-covers)
- [Setup](#setup)
- [Retrieving news with Exa](#retrieving-news-with-exa)
- [Summarizing with GPT-3.5 Turbo](#summarizing-with-gpt-3-5-turbo)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Concepts

Exa's Capabilities Explained

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

### [](\#search-types)  Search Types

#### [](\#auto-search-prev-magic-search)  Auto Search (prev. Magic Search)

| Where you would use it |
| --- |
| When you want optimal results without manually choosing between neural and keyword search. When you might not know ahead of time what the best search type is. Note Auto Search is the default search type - when unspecified, Auto Search is used. |

Python

Copy

```Python
result = exa.search("hottest AI startups", type="auto")

```

#### [](\#neural-search)  Neural Search

| Description | Where you would use it |
| --- | --- |
| Uses Exa’s embeddings-based index and query model to perform complex queries and provide semantically relevant results. | For exploratory searches or when looking for conceptually related content rather than exact keyword matches. To find hard to find, specific results from the web |

Python

Copy

```Python
result = exa.search("Here is a startup building innovative solutions for climate change:", type="neural")

```

#### [](\#keyword-search)  Keyword Search

| Description | Where you would use it |
| --- | --- |
| Traditional search method that matches specific words or phrases. | When doing simple, broad searches where the user can refine results manually. Good for general browsing and finding exact matches. Good for matching proper nouns or terms of art that are rarely used in other contexts. When neural search fails to return what you are looking for. |

Python

Copy

```Python

result = exa.search("Paris", type="keyword")

```

#### [](\#phrase-filter-search)  Phrase Filter Search

| Description | Where you would use it |
| --- | --- |
| Apply keyword filters atop of a neural search before returning results | When you want the power of Neural Search but also need to specify and filter on some key phrase. Often helpful when filtering on a piece of jargon where a specific match is crucial |

Python

Copy

```Python
result = exa.search(query, type='neural', includeText='Some_key_phrase_to_fiter_on')

```

[See a worked example here](/tutorials/phrase-filters-niche-company-finder)

#### [](\#large-scale-searches)  Large-scale Searches

| Description | Where you would use it |
| --- | --- |
| Exa searches that return a large number of search results. | When desiring comprehensive, semantically relevant data for batch use cases, e.g., for enrichment of CRMs or full topic scraping. |

Python

Copy

```Python
result = exa.search("Companies selling sonar technology", num_results=1000)

```

Note high return results cost more and higher result caps (e.g., 1000 returns) are restricted to Enterprise/Custom plans only. [Get in touch](https://cal.com/team/exa/exa-intro-chat?date=2024-11-14&month=2024-11) if you are interested in learning more.

* * *

### [](\#content-retrieval)  Content Retrieval

#### [](\#contents-retrieval)  Contents Retrieval

| Description | Where you would use it |
| --- | --- |
| Instantly retrieves whole, cleaned and parsed webpage contents from search results. | When you need the full text of webpages for analysis, summarization, or other post-processing. |

Python

Copy

```Python
result = exa.search_and_contents("latest advancements in quantum computing", text=True)

```

#### [](\#highlights-retrieval)  Highlights Retrieval

| Description | Where you would use it |
| --- | --- |
| Extracts relevant excerpts or highlights from retrieved content. | When you want a quick or targeted outputs from the most relevant parts of a search entity without wanted to handle the full text. |

Python

Copy

```Python
result = exa.search_and_contents("AI ethics", highlights=True)

```

* * *

### [](\#prompt-engineering)  Prompt Engineering

Prompt engineering is crucial for getting the most out of Exa’s capabilities. The right prompt can dramatically improve the relevance and usefulness of your search results. This is especially important for neural search and advanced features like writing continuation.

#### [](\#writing-continuation-queries)  Writing continuation queries

| Description | Where you would use it |
| --- | --- |
| Prompt crafted by post-pending ‘Here is a great resource to continue writing this piece of writing:‘. Useful for research writing or any other citation-based text generation after passing to an LLM. | When you’re in the middle of writing a piece and need to find relevant sources to continue or expand your content. This is particularly useful for academic writing, content creation, or any scenario where you need to find information that logically follows from what you’ve already written. |

Python

Copy

```Python
current_text = """
The impact of climate change on global agriculture has been significant.
Rising temperatures and changing precipitation patterns have led to shifts
in crop yields and growing seasons. Some regions have experienced increased
drought stress, while
"""
continuation_query = current_text + " If you found the above interesting, here's another useful resource to read:"
result = exa.search(continuation_query, type="neural", use_autoprompt=False)

```

#### [](\#long-queries)  Long queries

| Description | Where you would use it |
| --- | --- |
| Utilizing Exa’s long query window to perform matches against semantically rich content. | When you need to find content that matches complex, detailed descriptions or when you want to find content similar to a large piece of text. This is particularly useful for finding niche content or when you’re looking for very specific information. |

Python

Copy

```Python
long_query = """
Abstract: In this study, we investigate the potential of quantum-enhanced machine learning algorithms
for drug discovery applications. We present a novel quantum-classical hybrid approach that leverages
quantum annealing for feature selection and a quantum-inspired tensor network for model training.
Our results demonstrate a 30% improvement in prediction accuracy for binding affinity in protein-ligand
interactions compared to classical machine learning methods. Furthermore, we show a significant
reduction in computational time for large-scale molecular dynamics simulations. These findings
suggest that quantum machine learning techniques could accelerate the drug discovery process
and potentially lead to more efficient identification of promising drug candidates.
"""
result = exa.search(long_query, type="neural", use_autoprompt=False)

```

#### [](\#use-autoprompt-incl-autodate)  Use Autoprompt (incl. Autodate)

| Description | Where you would use it |
| --- | --- |
| Automatically optimizes your query for Exa’s neural search. | When you want to leverage Exa’s neural search capabilities without manually crafting the perfect prompt. It’s particularly useful for general-purpose queries or when you’re not sure how to phrase your query for optimal results. |

Python

Copy

```Python
result = exa.search("AI startups in healthcare", use_autoprompt=True)

```

Note: `use_autoprompt` is set to `False` in some examples above where manual prompt engineering is demonstrated. For most general use cases, leaving it as `True` (the default) will yield good results.

Using autoprompt will also automatically fetch date information as a filter to apply onto searches. For instance, the query:

`Here is the latest news from Russia in the last 7 days`

On July 15 2024, will produce results with an `autoDate` response attribute:

Copy

```{
  "autopromptString": "\"Here is the latest news from Russia:",
  "autoDate": "2024-07-08T17:18:57.152Z",
  "results": ...
}

```

Note the date is no longer in the query, but rather is applied as a strict filter as though you had applied it as a date.

[Contents retrieval with Exa API](/reference/contents-retrieval-with-exa-api) [FAQs](/reference/faqs)

On this page

- [Search Types](#search-types)
- [Auto Search (prev. Magic Search)](#auto-search-prev-magic-search)
- [Neural Search](#neural-search)
- [Keyword Search](#keyword-search)
- [Phrase Filter Search](#phrase-filter-search)
- [Large-scale Searches](#large-scale-searches)
- [Content Retrieval](#content-retrieval)
- [Contents Retrieval](#contents-retrieval)
- [Highlights Retrieval](#highlights-retrieval)
- [Prompt Engineering](#prompt-engineering)
- [Writing continuation queries](#writing-continuation-queries)
- [Long queries](#long-queries)
- [Use Autoprompt (incl. Autodate)](#use-autoprompt-incl-autodate)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

RAG Quick Start Guide

RAG with LlamaIndex

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

LlamaIndex is a framework for building LLM applications powered by structured data. In this guide, we’ll use Exa’s LlamaIndex integration to:

1. Specify Exa’s Search and Retrieve Highlight Tool as a LlamaIndex retriever
2. Set up an OpenAI Agent that uses this tool in its response generation

* * *

## [](\#get-started)  Get Started

1

Pre-requisites and installation

Install the llama-index, llama-index core, llama-index-tools-exa libraries. OpenAI dependencies are within the core library, so we don’t need to specify that.

Python

Copy

```Python
pip install llama-index llama-index-core llama-index-tools-exa

```

Also ensure API keys are initialized properly. The following code uses the `EXA_API_KEY` as the relevant environment variable name.

[**Get your Exa API key**](https://dashboard.exa.ai/api-keys)

2

Instantiate Exa tool

Import the relevant Exa integration library and instantiate LlamaIndex’s `ExaToolSpec`.

Python

Copy

```Python
from llama_index.tools.exa import ExaToolSpec
import os

exa_tool = ExaToolSpec(
    api_key=os.environ["EXA_API_KEY"],
)

```

3

Choose the Exa method to use

For this example, we are only interested in passing the [search\_and\_retrieve\_highlights](search) method to our agent, so we specify this using the `.to_tool_list` LlamaIndex method. We also pass `current_date`, a simple utility so our agent knows the current date.

Python

Copy

```Python
print('Tools that are provide by Exa LlamdaIndex integration:')
print('\n'.join(map(str, (exa_tool.spec_functions))))

search_and_retrieve_highlights_tool = exa_tool.to_tool_list(
    spec_functions=["search_and_retrieve_highlights", "current_date"]
)

```

4

Set up an OpenAI Agent and make Exa-powered requests

Set up the [OpenAIAgent](https://docs.llamaindex.ai/en/stable/examples/agent/Chatbot%5FSEC/), passing the filtered down toolset from above.

Python

Copy

```Python
from llama_index.agent.openai import OpenAIAgent

agent = OpenAIAgent.from_tools(
    search_and_retrieve_highlights_tool,
    verbose=True,
)

```

We can then use the chat method to interact with the agent.

Python

Copy

```Python
agent.chat(
    "Can you summarize the news from the last month related to the US stock market?"
)

```

5

Sample outputs

Output 1: Verbose output of agent operation

Stdout

Copy

```js
Added user message to memory: Can you summarize the news from the last month related to the US stock market?
=== Calling Function ===
Calling function: current_date with args: {}
Got output: 2024-05-09
========================

=== Calling Function ===
Calling function: search_and_retrieve_highlights with args: {"query":"US stock market news","num_results":5,"start_published_date":"2024-04-09","end_published_date":"2024-05-09"}
[Exa Tool] Autoprompt: Here is the latest news on the US stock market:
Got output: [Document(id_='26e0ccec-3b57-4785-ba20-fe0478051db3', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, text='Companies have repurchased more than $383 billion in shares over the past 13 weeks, according to Deutsche Bank research reported by Yahoo. This marks a 30% increase from the same period last year and is the highest level since June 2018. The Dow rose 75 points, or 0.2%, to 38,958 near midday. The S&P 500 dipped 0.1%, and the Nasdaq dropped 0.2%. AMC Entertainment and Robinhood will release their quarterly reports after markets close.', start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='5ffa10c4-700a-4c08-84f5-cdfe69189547', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, text='The California-based company reported a net loss of $270.6 million, or 43 cents per share, for the current period. This is compared to a loss of $268.3 million, or 44 cents per share, in the same period last year. Wall Street’s analysts predicted a per-share loss of 53 cents. Revenue increased by 22.3% to $801.3 million, falling short of the expectation of $918.8 million. Its bookings rose by 19% to $923.8 million, just missing expectations of $930.4 million.', start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='1bca8b42-4322-46ac-b423-fc9b076baf25', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, text="The Dow and other indexes opened higher on Thursday as the latest jobs report suggests the Federal Reserve may lower interest rates this year. Why McDonald's and Starbucks stocks should be avoided according to one analyst Off English Weekly jobless claims have risen to 231,000, up by 22,000 from the previous week. , this marks the highest level since August. This has raised hopes among investors that the central bank may reduce interest rates at some point this year. Meanwhile, , while the Swedish Riksbank and is expected to do so again this year.", start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='12cf1913-b637-4351-96fa-dd0a4e1dc6bd', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, text='Following the news, the stock declined 9.5% in mid-morning trading. Bitcoin jumps to $64,000 rebounded to morning The latest surge in Bitcoin price comes amid the resurgence of. Grayscale’s Bitcoin ETF has finally seen inflows. According to data compiled by , , which is the biggest Bitcoin ETF in terms of assets, received $63 million from investors on Friday. This marks the end of daily outflows that had been occurring for almost four months since its conversion to a spot ETF structure in January.', start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='fbd457e6-188f-464d-83f3-99303e2f2fc2', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, text='Its debt due 2025 is trading at 73 cents on the dollar, and its 2026 debt is at 55 cents. Following the news, the stock declined 9.7% by the end of the day. On the other hand, Spirit Airlines’ rivals soar on Monday. American Airlines, Southwest Airlines, and United Airlines were among the top-performing stocks, up 5.7%, 4.8%, and 4.4%, respectively. Stocks of Paramount soar amid acquisition discussions Shares of Paramount Global went up 3% by the end of the day amid ongoing discussions about who will acquire the streaming and entertainment company.', start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n')]
========================

```

Output 2: Agent response

Stdout

Copy

```js
AgentChatResponse(response="Here are some highlights related to the US stock market news from the last month:\n\n1. Companies have repurchased more than $383 billion in shares over the past 13 weeks, marking a 30% increase from the same period last year. This is the highest level since June 2018. The Dow rose 75 points, the S&P 500 dipped 0.1%, and the Nasdaq dropped 0.2%. AMC Entertainment and Robinhood will release their quarterly reports after markets close.\n\n2. A California-based company reported a net loss of $270.6 million, or 43 cents per share, for the current period. Revenue increased by 22.3% to $801.3 million, falling short of expectations. Bookings rose by 19% to $923.8 million, just missing expectations.\n\n3. The Dow and other indexes opened higher as the latest jobs report suggests the Federal Reserve may lower interest rates this year. Weekly jobless claims have risen to 231,000, the highest level since August, raising hopes among investors for a potential interest rate reduction.\n\n4. Following the news, a stock declined 9.5% in mid-morning trading. Bitcoin price surged to $64,000 amid the resurgence of Grayscale’s Bitcoin ETF seeing inflows after daily outflows for almost four months.\n\n5. Debt due in 2025 is trading at 73 cents on the dollar, and 2026 debt is at 55 cents. Following the news, a stock declined 9.7% by the end of the day. Spirit Airlines’ rivals, including American Airlines, Southwest Airlines, and United Airlines, saw their stocks soar. Paramount Global's shares went up 3% amid acquisition discussions.\n\nThese are some of the key highlights from the US stock market news in the last month.", sources=[ToolOutput(content='2024-05-09', tool_name='current_date', raw_input={'args': (), 'kwargs': {}}, raw_output=datetime.date(2024, 5, 9), is_error=False), ToolOutput(content='[Document(id_=\'26e0ccec-3b57-4785-ba20-fe0478051db3\', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, text=\'Companies have repurchased more than $383 billion in shares over the past 13 weeks, according to Deutsche Bank research reported by Yahoo. This marks a 30% increase from the same period last year and is the highest level since June 2018. The Dow rose 75 points, or 0.2%, to 38,958 near midday. The S&P 500 dipped 0.1%, and the Nasdaq dropped 0.2%. AMC Entertainment and Robinhood will release their quarterly reports after markets close.\', start_char_idx=None, end_char_idx=None, text_template=\'{metadata_str}\\n\\n{content}\', metadata_template=\'{key}: {value}\', metadata_seperator=\'\\n\'), Document(id_=\'5ffa10c4-700a-4c08-84f5-cdfe69189547\', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, text=\'The California-based company reported a net loss of $270.6 million, or 43 cents per share, for the current period. This is compared to a loss of $268.3 million, or 44 cents per share, in the same period last year. Wall Street’s analysts predicted a per-share loss of 53 cents. Revenue increased by 22.3% to $801.3 million, falling short of the expectation of $918.8 million. Its bookings rose by 19% to $923.8 million, just missing expectations of $930.4 million.\', start_char_idx=None, end_char_idx=None, text_template=\'{metadata_str}\\n\\n{content}\', metadata_template=\'{key}: {value}\', metadata_seperator=\'\\n\'), Document(id_=\'1bca8b42-4322-46ac-b423-fc9b076baf25\', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, text="The Dow and other indexes opened higher on Thursday as the latest jobs report suggests the Federal Reserve may lower interest rates this year. Why McDonald\'s and Starbucks stocks should be avoided according to one analyst Off English Weekly jobless claims have risen to 231,000, up by 22,000 from the previous week. , this marks the highest level since August. This has raised hopes among investors that the central bank may reduce interest rates at some point this year. Meanwhile, , while the Swedish Riksbank and is expected to do so again this year.", start_char_idx=None, end_char_idx=None, text_template=\'{metadata_str}\\n\\n{content}\', metadata_template=\'{key}: {value}\', metadata_seperator=\'\\n\'), Document(id_=\'12cf1913-b637-4351-96fa-dd0a4e1dc6bd\', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, text=\'Following the news, the stock declined 9.5% in mid-morning trading. Bitcoin jumps to $64,000 rebounded to morning The latest surge in Bitcoin price comes amid the resurgence of. Grayscale’s Bitcoin ETF has finally seen inflows. According to data compiled by , , which is the biggest Bitcoin ETF in terms of assets, received $63 million from investors on Friday. This marks the end of daily outflows that had been occurring for almost four months since its conversion to a spot ETF structure in January.\', start_char_idx=None, end_char_idx=None, text_template=\'{metadata_str}\\n\\n{content}\', metadata_template=\'{key}: {value}\', metadata_seperator=\'\\n\'), Document(id_=\'fbd457e6-188f-464d-83f3-99303e2f2fc2\', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, text=\'Its debt due 2025 is trading at 73 cents on the dollar, and its 2026 debt is at 55 cents. Following the news, the stock declined 9.7% by the end of the day. On the other hand, Spirit Airlines’ rivals soar on Monday. American Airlines, Southwest Airlines, and United Airlines were among the top-performing stocks, up 5.7%, 4.8%, and 4.4%, respectively. Stocks of Paramount soar amid acquisition discussions Shares of Paramount Global went up 3% by the end of the day amid ongoing discussions about who will acquire the streaming and entertainment company.\', start_char_idx=None, end_char_idx=None, text_template=\'{metadata_str}\\n\\n{content}\', metadata_template=\'{key}: {value}\', metadata_seperator=\'\\n\')]', tool_name='search_and_retrieve_highlights', raw_input={'args': (), 'kwargs': {'query': 'US stock market news', 'num_results': 5, 'start_published_date': '2024-04-09', 'end_published_date': '2024-05-09'}}, raw_output=[Document(id_='26e0ccec-3b57-4785-ba20-fe0478051db3', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, text='Companies have repurchased more than $383 billion in shares over the past 13 weeks, according to Deutsche Bank research reported by Yahoo. This marks a 30% increase from the same period last year and is the highest level since June 2018. The Dow rose 75 points, or 0.2%, to 38,958 near midday. The S&P 500 dipped 0.1%, and the Nasdaq dropped 0.2%. AMC Entertainment and Robinhood will release their quarterly reports after markets close.', start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='5ffa10c4-700a-4c08-84f5-cdfe69189547', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, text='The California-based company reported a net loss of $270.6 million, or 43 cents per share, for the current period. This is compared to a loss of $268.3 million, or 44 cents per share, in the same period last year. Wall Street’s analysts predicted a per-share loss of 53 cents. Revenue increased by 22.3% to $801.3 million, falling short of the expectation of $918.8 million. Its bookings rose by 19% to $923.8 million, just missing expectations of $930.4 million.', start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='1bca8b42-4322-46ac-b423-fc9b076baf25', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, text="The Dow and other indexes opened higher on Thursday as the latest jobs report suggests the Federal Reserve may lower interest rates this year. Why McDonald's and Starbucks stocks should be avoided according to one analyst Off English Weekly jobless claims have risen to 231,000, up by 22,000 from the previous week. , this marks the highest level since August. This has raised hopes among investors that the central bank may reduce interest rates at some point this year. Meanwhile, , while the Swedish Riksbank and is expected to do so again this year.", start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='12cf1913-b637-4351-96fa-dd0a4e1dc6bd', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, text='Following the news, the stock declined 9.5% in mid-morning trading. Bitcoin jumps to $64,000 rebounded to morning The latest surge in Bitcoin price comes amid the resurgence of. Grayscale’s Bitcoin ETF has finally seen inflows. According to data compiled by , , which is the biggest Bitcoin ETF in terms of assets, received $63 million from investors on Friday. This marks the end of daily outflows that had been occurring for almost four months since its conversion to a spot ETF structure in January.', start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='fbd457e6-188f-464d-83f3-99303e2f2fc2', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, text='Its debt due 2025 is trading at 73 cents on the dollar, and its 2026 debt is at 55 cents. Following the news, the stock declined 9.7% by the end of the day. On the other hand, Spirit Airlines’ rivals soar on Monday. American Airlines, Southwest Airlines, and United Airlines were among the top-performing stocks, up 5.7%, 4.8%, and 4.4%, respectively. Stocks of Paramount soar amid acquisition discussions Shares of Paramount Global went up 3% by the end of the day amid ongoing discussions about who will acquire the streaming and entertainment company.', start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n')], is_error=False)], source_nodes=[], is_dummy_stream=False)

```

As you can see, the output generation is enriched with the context of our Exa Search query result!

[CrewAI agents with Exa](/reference/crewai) [Tool calling with GPT](/reference/tool-calling-with-gpt4o)

On this page

- [Get Started](#get-started)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

SDK References

Python SDK Specification

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

For ChatGPT-based [Python SDK](https://github.com/exa-labs/exa-py) assistance, [go here](https://chat.openai.com/g/g-dTeZqs0tX-exa-formerly-metaphor-python-sdk-guide).

## [](\#getting-started)  Getting started

Install the [exa-py](https://github.com/exa-labs/exa-py) SDK

Bash

Copy

```Bash
pip install exa_py

```

and then instantiate an Exa client

Python

Copy

```Python
from exa_py import Exa

import os

exa = Exa(os.getenv('EXA_API_KEY'))

```

[**Get API Key** \\
\\
Follow this link to get your API key](https://dashboard.exa.ai/login?redirect=/docs?path=/reference/python-sdk-specification)

## [](\#search-method)  `search` Method

Perform an Exa search given an input query and retrieve a list of relevant results as links.

### [](\#input-example)  Input Example

Python

Copy

```Python
`result = exa.search(
  "hottest AI startups",
  use_autoprompt=True,
  num_results=2
)

```

### [](\#input-parameters)  Input Parameters

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| query | str | The input query string. | Required |
| num\_results | Optional\[int\] | Number of search results to return. | 10 |
| include\_domains | Optional\[List\[str\]\] | List of domains to include in the search. | None |
| exclude\_domains | Optional\[List\[str\]\] | List of domains to exclude in the search. | None |
| start\_crawl\_date | Optional\[str\] | Results will only include links **crawled** after this date. | None |
| end\_crawl\_date | Optional\[str\] | Results will only include links **crawled** before this date. | None |
| start\_published\_date | Optional\[str\] | Results will only include links with a **published** date after this date. | None |
| end\_published\_date | Optional\[str\] | Results will only include links with a **published** date before this date. | None |
| use\_autoprompt | Optional\[bool\] | If true, convert query to a query best suited for Exa. | False |
| type | Optional\[str\] | [The type of search](/integrations/python-sdk-specification#), keyword or neural. | ”auto” |
| category | Optional\[str\] | A data category to focus on when searching, with higher comprehensivity and data cleanliness. Currently, the available categories are: company, research paper, news, linkedin profile, github, tweet, movie, song, personal site, pdf | None |

### [](\#returns-example)  Returns Example

Returns:

JSON

Copy

```JSON
{
  "autopromptString": "Here is a link to one of the hottest AI startups:",
  "results": [\
    {\
      "score": 0.17025552690029144,\
      "title": "Adept: Useful General Intelligence",\
      "id": "https://www.adept.ai/",\
      "url": "https://www.adept.ai/",\
      "publishedDate": "2000-01-01",\
      "author": null\
    },\
    {\
      "score": 0.1700288951396942,\
      "title": "Home | Tenyx, Inc.",\
      "id": "https://www.tenyx.com/",\
      "url": "https://www.tenyx.com/",\
      "publishedDate": "2019-09-10",\
      "author": null\
    }\
  ],
  "requestId": "a78ebce717f4d712b6f8fe0d5d7753f8"
}

```

### [](\#return-parameters)  Return Parameters

#### [](\#searchresponse-result)  SearchResponse\[Result\]

| Field | Type | Description |
| --- | --- | --- |
| results | List\[Result\] | List of Result objects |
| autoprompt\_string | Optional\[str\] | Exa query created by autoprompt functionality |

#### [](\#result-object)  Result Object

| Field | Type | Description |
| --- | --- | --- |
| url | str | URL of the search result |
| id | str | Temporary ID for the document |
| title | Optional\[str\] | Title of the search result |
| score | Optional\[float\] | Similarity score between query/url and result |
| published\_date | Optional\[str\] | Estimated creation date |
| author | Optional\[str\] | Author of the content, if available |

## [](\#search-and-contents-method)  `search_and_contents` Method

Perform an Exa search given an input query and retrieve a list of relevant results as links, optionally including the full text and/or highlights of the content.

### [](\#input-example-2)  Input Example

Python

Copy

```Python
`# Search with full text content
result_with_text = exa.search_and_contents(
    "AI in healthcare",
    text=True,
    num_results=2
)

# Search with highlights
result_with_highlights = exa.search_and_contents(
    "AI in healthcare",
    highlights=True,
    num_results=2
)

# Search with both text and highlights
result_with_text_and_highlights = exa.search_and_contents(
    "AI in healthcare",
    text=True,
    highlights=True,
    num_results=2
)

```

### [](\#input-parameters-2)  Input Parameters

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| query | str | The input query string. | Required |
| text | Union\[TextContentsOptions, Literal\[True\]\] | If provided, includes the full text of the content in the results. | None |
| highlights | Union\[HighlightsContentsOptions, Literal\[True\]\] | If provided, includes highlights of the content in the results. | None |
| num\_results | Optional\[int\] | Number of search results to return. | 10 |
| include\_domains | Optional\[List\[str\]\] | List of domains to include in the search. | None |
| exclude\_domains | Optional\[List\[str\]\] | List of domains to exclude in the search. | None |
| start\_crawl\_date | Optional\[str\] | Results will only include links **crawled** after this date. | None |
| end\_crawl\_date | Optional\[str\] | Results will only include links **crawled** before this date. | None |
| start\_published\_date | Optional\[str\] | Results will only include links with a **published** date after this date. | None |
| end\_published\_date | Optional\[str\] | Results will only include links with a **published** date before this date. | None |
| use\_autoprompt | Optional\[bool\] | If true, convert query to a query best suited for Exa. | False |
| type | Optional\[str\] | [The type of search](/integrations/python-sdk-specification#), keyword or neural. | ”auto” |
| category | Optional\[str\] | A data category to focus on when searching, with higher comprehensivity and data cleanliness. Currently, the available categories are: company, research paper, news, linkedin profile, github, tweet, movie, song, personal site, pdf | None |

### [](\#returns-example-2)  Returns Example

JSON

Copy

```JSON
`{
  "results": [\
    {\
      "score": 0.20826785266399384,\
      "title": "2023 AI Trends in Health Care",\
      "id": "https://aibusiness.com/verticals/2023-ai-trends-in-health-care-",\
      "url": "https://aibusiness.com/verticals/2023-ai-trends-in-health-care-",\
      "publishedDate": "2022-12-29",\
      "author": "Wylie Wong",\
      "text": "While the health care industry was initially slow to [... TRUNCATED IN THESE DOCS FOR BREVITY ...]",\
      "highlights": [\
        "But to do so, many health care institutions would like to share data, so they can build a more comprehensive dataset to use to train an AI model. Traditionally, they would have to move the data to one central repository. However, with federated or swarm learning, the data does not have to move. Instead, the AI model goes to each individual health care facility and trains on the data, he said. This way, health care providers can maintain security and governance over their data."\
      ],\
      "highlightScores": [\
        0.5566554069519043\
      ]\
    },\
    {\
      "score": 0.20796334743499756,\
      "title": "AI in healthcare: Innovative use cases and applications",\
      "id": "https://www.leewayhertz.com/ai-use-cases-in-healthcare",\
      "url": "https://www.leewayhertz.com/ai-use-cases-in-healthcare",\
      "publishedDate": "2023-02-13",\
      "author": "Akash Takyar",\
      "text": "The integration of AI in healthcare is not [... TRUNCATED IN THESE DOCS FOR BREVITY ...]",\
      "highlights": [\
        "The ability of AI to analyze large amounts of medical data and identify patterns has led to more accurate and timely diagnoses. This has been especially helpful in identifying complex medical conditions, which may be difficult to detect using traditional methods. Here are some examples of successful implementation of AI in healthcare. IBM Watson Health: IBM Watson Health is an AI-powered system used in healthcare to improve patient care and outcomes. The system uses natural language processing and machine learning to analyze large amounts of data and provide personalized treatment plans for patients."\
      ],\
      "highlightScores": [\
        0.6563674807548523\
      ]\
    }\
  ],
  "requestId": "d8fd59c78d34afc9da173f1fe5aa8965"
}

```

### [](\#return-parameters-2)  Return Parameters

The return type depends on the combination of `text` and `highlights` parameters:

- `SearchResponse[ResultWithText]`: When only `text` is provided.
- `SearchResponse[ResultWithHighlights]`: When only `highlights` is provided.
- `SearchResponse[ResultWithTextAndHighlights]`: When both `text` and `highlights` are provided.

#### [](\#searchresponse-resultwithtextandhighlights)  SearchResponse\[ResultWithTextAndHighlights\]

| Field | Type | Description |
| --- | --- | --- |
| results | List\[ResultWithTextAndHighlights\] | List of ResultWithTextAndHighlights objects |
| autoprompt\_string | Optional\[str\] | Exa query created by autoprompt functionality |

#### [](\#resultwithtextandhighlights-object)  ResultWithTextAndHighlights Object

| Field | Type | Description |
| --- | --- | --- |
| url | str | URL of the search result |
| id | str | Temporary ID for the document |
| title | Optional\[str\] | Title of the search result |
| score | Optional\[float\] | Similarity score between query/url and result |
| published\_date | Optional\[str\] | Estimated creation date |
| author | Optional\[str\] | Author of the content, if available |
| text | str | Text of the search result page (always present) |
| highlights | List\[str\] | Highlights of the search result (always present) |
| highlight\_scores | List\[float\] | Scores of the highlights (always present) |

Note: If neither `text` nor `highlights` is specified, the method defaults to including the full text content.

## [](\#find-similar-method)  `find_similar` Method

Find a list of similar results based on a webpage’s URL.

### [](\#input-example-3)  Input Example

Python

Copy

```Python
similar_results = exa.find_similar(
    "miniclip.com",
    num_results=2,
    exclude_source_domain=True
)

```

### [](\#input-parameters-3)  Input Parameters

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| url | str | The URL of the webpage to find similar results for. | Required |
| num\_results | Optional\[int\] | Number of similar results to return. | None |
| include\_domains | Optional\[List\[str\]\] | List of domains to include in the search. | None |
| exclude\_domains | Optional\[List\[str\]\] | List of domains to exclude from the search. | None |
| start\_crawl\_date | Optional\[str\] | Results will only include links **crawled** after this date. | None |
| end\_crawl\_date | Optional\[str\] | Results will only include links **crawled** before this date. | None |
| start\_published\_date | Optional\[str\] | Results will only include links with a **published** date after this date. | None |
| end\_published\_date | Optional\[str\] | Results will only include links with a **published** date before this date. | None |
| exclude\_source\_domain | Optional\[bool\] | If true, excludes results from the same domain as the input URL. | None |
| category | Optional\[str\] | A data category to focus on when searching, with higher comprehensivity and data cleanliness. | None |

### [](\#returns-example-3)  Returns Example

JSON

Copy

```JSON
{
  "results": [\
    {\
      "score": 0.8777582049369812,\
      "title": "Play New Free Online Games Every Day",\
      "id": "https://www.minigames.com/new-games",\
      "url": "https://www.minigames.com/new-games",\
      "publishedDate": "2000-01-01",\
      "author": null\
    },\
    {\
      "score": 0.87653648853302,\
      "title": "Play The best Online Games",\
      "id": "https://www.minigames.com/",\
      "url": "https://www.minigames.com/",\
      "publishedDate": "2000-01-01",\
      "author": null\
    }\
  ],
  "requestId": "08fdc6f20e9f3ea87f860af3f6ccc30f"
}

```

### [](\#return-parameters-3)  Return Parameters

`SearchResponse[_Result]`: The response containing similar results and optional autoprompt string.

#### [](\#searchresponse-results)  SearchResponse\[Results\]

| Field | Type | Description |
| --- | --- | --- |
| results | List\[ResultWithTextAndHighlights\] | List of ResultWithTextAndHighlights objects |
| autoprompt\_string | Optional\[str\] | Exa query created by autoprompt functionality |

#### [](\#results-object)  Results Object

| Field | Type | Description |
| --- | --- | --- |
| url | str | URL of the search result |
| id | str | Temporary ID for the document |
| title | Optional\[str\] | Title of the search result |
| score | Optional\[float\] | Similarity score between query/url and result |
| published\_date | Optional\[str\] | Estimated creation date |
| author | Optional\[str\] | Author of the content, if available |

## [](\#find-similar-and-contents-method)  `find_similar_and_contents` Method

Find a list of similar results based on a webpage’s URL, optionally including the text content or highlights of each result.

### [](\#input-example-4)  Input Example

Python

Copy

```Python
# Find similar with full text content
similar_with_text = exa.find_similar_and_contents(
    "https://example.com/article",
    text=True,
    num_results=2
)

# Find similar with highlights
similar_with_highlights = exa.find_similar_and_contents(
    "https://example.com/article",
    highlights=True,
    num_results=2
)

# Find similar with both text and highlights
similar_with_text_and_highlights = exa.find_similar_and_contents(
    "https://example.com/article",
    text=True,
    highlights=True,
    num_results=2
)

```

### [](\#input-parameters-4)  Input Parameters

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| url | str | The URL of the webpage to find similar results for. | Required |
| text | Union\[TextContentsOptions, Literal\[True\]\] | If provided, includes the full text of the content in the results. | None |
| highlights | Union\[HighlightsContentsOptions, Literal\[True\]\] | If provided, includes highlights of the content in the results. | None |
| num\_results | Optional\[int\] | Number of similar results to return. | None |
| include\_domains | Optional\[List\[str\]\] | List of domains to include in the search. | None |
| exclude\_domains | Optional\[List\[str\]\] | List of domains to exclude from the search. | None |
| start\_crawl\_date | Optional\[str\] | Results will only include links **crawled** after this date. | None |
| end\_crawl\_date | Optional\[str\] | Results will only include links **crawled** before this date. | None |
| start\_published\_date | Optional\[str\] | Results will only include links with a **published** date after this date. | None |
| end\_published\_date | Optional\[str\] | Results will only include links with a **published** date before this date. | None |
| exclude\_source\_domain | Optional\[bool\] | If true, excludes results from the same domain as the input URL. | None |
| category | Optional\[str\] | A data category to focus on when searching, with higher comprehensivity and data cleanliness. | None |

### [](\#returns)  Returns

The return type depends on the combination of `text` and `highlights` parameters:

- `SearchResponse[ResultWithText]`: When only `text` is provided or when neither `text` nor `highlights` is provided (defaults to including text).
- `SearchResponse[ResultWithHighlights]`: When only `highlights` is provided.
- `SearchResponse[ResultWithTextAndHighlights]`: When both `text` and `highlights` are provided.

The response contains similar results and an optional autoprompt string.

Note: If neither `text` nor `highlights` is specified, the method defaults to including the full text content.

[TypeScript SDK Specification](/integrations/typescript-sdk-specification)

On this page

- [Getting started](#getting-started)
- [search Method](#search-method)
- [Input Example](#input-example)
- [Input Parameters](#input-parameters)
- [Returns Example](#returns-example)
- [Return Parameters](#return-parameters)
- [SearchResponse\[Result\]](#searchresponse-result)
- [Result Object](#result-object)
- [search\_and\_contents Method](#search-and-contents-method)
- [Input Example](#input-example-2)
- [Input Parameters](#input-parameters-2)
- [Returns Example](#returns-example-2)
- [Return Parameters](#return-parameters-2)
- [SearchResponse\[ResultWithTextAndHighlights\]](#searchresponse-resultwithtextandhighlights)
- [ResultWithTextAndHighlights Object](#resultwithtextandhighlights-object)
- [find\_similar Method](#find-similar-method)
- [Input Example](#input-example-3)
- [Input Parameters](#input-parameters-3)
- [Returns Example](#returns-example-3)
- [Return Parameters](#return-parameters-3)
- [SearchResponse\[Results\]](#searchresponse-results)
- [Results Object](#results-object)
- [find\_similar\_and\_contents Method](#find-similar-and-contents-method)
- [Input Example](#input-example-4)
- [Input Parameters](#input-parameters-4)
- [Returns](#returns)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Tutorials

Exa Researcher - JavaScript

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

### [](\#what-this-doc-covers)  What this doc covers

1. Using Exa’s Auto Search to pick the best search setting for each query (keyword or neural)
2. Using searchAndContents() through Exa’s JavaScript SDK

* * *

In this example, we will build Exa Researcher, a JavaScript app that, given a research topic, automatically searches for relevant sources with Exa’s [**Auto Search**](/v2.0/reference/magic-search-as-default) and synthesizes the information into a reliable research report.

Fastest setup: Interact with the code in your browser with this Replit [template](https://replit.com/@olafblitz/exa-researcher?v=1).

Alternatively, this [interactive notebook](https://github.com/exa-labs/exa-js/tree/master/examples/researcher/researcher.ipynb) was made with the Deno Javascript kernel for Jupyter so you can easily run it locally. Check out the [plain JS version](https://github.com/exa-labs/exa-js/tree/master/examples/researcher/researcher.mjs) if you prefer a regular Javascript file you can run with NodeJS, or want to skip to the final result. If you’d like to run this notebook locally, [Installing Deno](https://docs.deno.com/runtime/manual/getting%5Fstarted/installation) and [connecting Deno to Jupyter](https://docs.deno.com/runtime/manual/tools/jupyter) is fast and easy.

To play with this code, first we need a [Exa API key](https://dashboard.exa.ai/api-keys) and an [OpenAI API key](https://platform.openai.com/api-keys).

## [](\#setup)  Setup

Let’s import the Exa and OpenAI SDKs and put in our API keys to create a client object for each. Make sure to pick the right imports for your runtime and paste or load your API keys.

TypeScript

Copy

```TypeScript
// Deno imports
import Exa from 'npm:exa-js';
import OpenAI from 'npm:openai';

// NodeJS imports
//import Exa from 'exa-js';
//import OpenAI from 'openai';

// Replit imports
//const Exa = require("exa-js").default;
//const OpenAI = require("openai");

const EXA_API_KEY = "" // insert or load your API key here
const OPENAI_API_KEY = ""// insert or load your API key here

const exa = new Exa(EXA_API_KEY);
const openai = new OpenAI({ apiKey: OPENAI_API_KEY });

```

Since we’ll be making several calls to the OpenAI API to get a completion from GPT-3.5 Turbo, let’s make a simple utility function so we can pass in the system and user messages directly, and get the LLM’s response back as a string.

TypeScript

Copy

```TypeScript
async function getLLMResponse({system = 'You are a helpful assistant.', user = '', temperature = 1, model = 'gpt-3.5-turbo'}){
    const completion = await openai.chat.completions.create({
        model,
        temperature,
        messages: [\
            {'role': 'system', 'content': system},\
            {'role': 'user', 'content': user},\
        ]
    });
    return completion.choices[0].message.content;
}

```

Okay, great! Now let’s starting building Exa Researcher.

## [](\#exa-auto-search)  Exa Auto Search

The researcher should be able to automatically generate research reports for all kinds of different topics. Here’s two to start:

TypeScript

Copy

```TypeScript

const SAMA_TOPIC = 'Sam Altman';
const ART_TOPIC = 'renaissance art';

```

The first thing our researcher has to do is decide what kind of search to do for the given topic.

Exa offers two kinds of search: **neural** and **keyword** search. Here’s how we decide:

- Neural search is preferred when the query is broad and complex because it lets us retrieve high quality, semantically relevant data. Neural search is especially suitable when a topic is well-known and popularly discussed on the Internet, allowing the machine learning model to retrieve contents which are more likely recommended by real humans.
- Keyword search is useful when the topic is specific, local or obscure. If the query is a specific person’s name, and identifier, or acronym, such that relevant results will contain the query itself, keyword search may do well. And if the machine learning model doesn’t know about the topic, but relevant documents can be found by directly matching the search query, keyword search may be necessary.

Conveniently, Exa’s autosearch feature (on by default) will automatically decide whether to use `keyword` or `neural` search for each query. For example, if a query is a specific person’s name, Exa would decide to use keyword search.

Now, we’ll create a helper function to generate search queries for our topic.

TypeScript

Copy

```TypeScript
async function generateSearchQueries(topic, n){
    const userPrompt = `I'm writing a research report on ${topic} and need help coming up with diverse search queries.
Please generate a list of ${n} search queries that would be useful for writing a research report on ${topic}. These queries can be in various formats, from simple keywords to more complex phrases. Do not add any formatting or numbering to the queries.`;

    const completion = await getLLMResponse({
        system: 'The user will ask you to help generate some search queries. Respond with only the suggested queries in plain text with no extra formatting, each on its own line.',
        user: userPrompt,
        temperature: 1
    });
    return completion.split('\n').filter(s => s.trim().length > 0).slice(0, n);
}

```

Next, let’s write another function that actually calls the Exa API to perform searches using Auto Search.

TypeScript

Copy

```TypeScript
async function getSearchResults(queries, linksPerQuery=2){
    let results = [];
    for (const query of queries){
        const searchResponse = await exa.searchAndContents(query, {
            numResults: linksPerQuery,
            useAutoprompt: false
        });
        results.push(...searchResponse.results);
    }
    return results;
}

```

## [](\#writing-a-report-with-gpt-4)  Writing a report with GPT-4

The final step is to instruct the LLM to synthesize the content into a research report, including citations of the original links. We can do that by pairing the content and the URLs and writing them into the prompt.

TypeScript

Copy

```TypeScript
 async function synthesizeReport(topic, searchContents, contentSlice = 750){
    const inputData = searchContents.map(item => `--START ITEM--\nURL: ${item.url}\nCONTENT: ${item.text.slice(0, contentSlice)}\n--END ITEM--\n`).join('');
    return await getLLMResponse({
        system: 'You are a helpful research assistant. Write a report according to the user\'s instructions.',
        user: 'Input Data:\n' + inputData + `Write a two paragraph research report about ${topic} based on the provided information. Include as many sources as possible. Provide citations in the text using footnote notation ([#]). First provide the report, followed by a single "References" section that lists all the URLs used, in the format [#] <url>.`,
        //model: 'gpt-4' //want a better report? use gpt-4 (but it costs more)
    });
}

```

## [](\#all-together-now)  All Together Now

Now, let’s just wrap everything into one Researcher function that strings together all the functions we’ve written. Given a user’s research topic, the Researcher will generate search queries, feed those queries to Exa Auto Search, and finally use an LLM to synthesize the retrieved information. Three simple steps!

TypeScript

Copy

```TypeScript
 async function researcher(topic){
    console.log(`Starting research on topic: "${topic}"`);

    const searchQueries = await generateSearchQueries(topic, 3);
    console.log("Generated search queries:", searchQueries);

    const searchResults = await getSearchResults(searchQueries);
    console.log(`Found ${searchResults.length} search results. Here's the first one:`, searchResults[0]);

    console.log("Synthesizing report...");
    const report = await synthesizeReport(topic, searchResults);

    return report;
}

```

In just a couple lines of code, we’ve used Exa to go from a research topic to a valuable essay with up-to-date sources.

TypeScript

Copy

```TypeScript
async function runExamples() {
    console.log("Researching Sam Altman:");
    const samaReport = await researcher(SAMA_TOPIC);
    console.log(samaReport);

    console.log("\n\nResearching Renaissance Art:");
    const artReport = await researcher(ART_TOPIC);
    console.log(artReport);
}

// To use the researcher on the examples, simply call the runExamples() function:
runExamples();

// Or, to research a specific topic:
researcher("llama antibodies").then(console.log);

```

For a link to a complete, cleaned up version of this project that you can execute in your NodeJS environment, check out the [alternative JS-only version](https://github.com/exa-labs/exa-js/tree/master/examples/researcher/researcher.mjs).

[Company Analyst](/examples/company-analyst) [Exa Researcher - Python](/examples/exa-researcher-python)

On this page

- [What this doc covers](#what-this-doc-covers)
- [Setup](#setup)
- [Exa Auto Search](#exa-auto-search)
- [Writing a report with GPT-4](#writing-a-report-with-gpt-4)
- [All Together Now](#all-together-now)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Concepts

The Exa Index

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

There are many types of content, and we’re constantly discovering new things to search for as well. If there’s anything you want to be more highly covered, just reach out to [hello@exa.ai](mailto:hello@exa.ai). See the following table for a high level overview of what is available in our index:

| Category | Availability in Exa Index | Description | Example prompt link |
| :-: | :-: | :-: | :-: |
| Research papers | Very High | Offer semantic search over a very vast index of papers, enabling sophisticated, multi-layer and complex filtering for use cases | [If you’re looking for the most helpful academic paper on “embeddings for document retrieval”, check this out (pdf:](https://search.exa.ai/search?q=If+you%27re+looking+for+the+most+helpful+academic+paper+on+%22embeddings+for+document+retrieval%22&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22resolvedSearchType%22%3A%22neural%22%2C%22useAutoprompt%22%3Afalse%7D&resolvedSearchType=neural) |
| Personal pages | Very High | Excels at finding personal pages, which are often extremely hard/impossible to find on services like Google | [Here is a link to the best life coach for when you’re unhappy at work:](https://exa.ai/search?q=Here%20is%20a%20link%20to%20the%20best%20life%20coach%20for%20when%20you%27re%20unhappy%20at%20work%3A&c=personal%20site&filters=%7B%22numResults%22%3A30%2C%22useAutoprompt%22%3Afalse%2C%22domainFilterType%22%3A%22include%22%7D) |
| Wikipedia | Very High | Covers all of Wikipedia, providing comprehensive access to this vast knowledge base via semantic search | [Here is a Wikipedia page about a Roman emperor:](https://search.exa.ai/search?q=Here+is+a+Wikipedia+page+about+a+Roman+emperor%3A&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neurall) |
| News | Very High | Includes a wide, robust index of web news sources, providing coverage of current events | [Here is news about war in the Middle East:](https://exa.ai/search?q=Here+is+news+about+war+in+the+Middle+East%3A&c=personal+site&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22auto%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%2C%22startPublishedDate%22%3A%222024-10-29T01%3A45%3A46.055Z%22%7D&resolvedSearchType=keyword) |
| LinkedIn profiles | _Very High (US+EU)_ | Will provide extensive coverage of LinkedIn personal profiles, allowing for detailed professional information searches | b [est theoretical computer scientist at uc berkeley](https://exa.ai/search?q=best+theoretical+computer+scientist+at+uc+berkeley&c=linkedin+profile&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22useAutoprompt%22%3Atrue%2C%22resolvedSearchType%22%3A%22neural%22%7D&autopromptString=A+leading+theoretical+computer+scientist+at+UC+Berkeley.&resolvedSearchType=neural) |
| LinkedIn company pages | _Coming Soon_ | Will offer comprehensive access to LinkedIn company pages, enabling in-depth research on businesses and organization | (Best-practice example TBC) |
| Company home-pages | Very High | Wide index of companies covered; also available are curated, customized company datasets - reach out to learn more | [Here is the homepage of a company working on making space travel cheaper:](https://search.exa.ai/search?q=Here+is+the+homepage+of+a+company+working+on+making+space+travel+cheaper%3A&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |
| GitHub repos | High | Indexes open source code (which the Exa team use frequently!) | [Here’s a Github repo if you want to convert OpenAPI specs to Rust code:](https://exa.ai/search?q=Here%27s+a+Github+repo+if+you+want+to+convert+OpenAPI+specs+to+Rust+code%3A&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |
| Blogs | High | Excels at finding high quality reading material, particularly useful for niche topics | [If you’re a huge fan of Japandi decor, you’d love this blog:](https://exa.ai/search?q=If+you%27re+a+huge+fan+of+Japandi+decor%2C+you%27d+love+this+blog%3A&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |
| Places and things | High | Covers a wide range of entities including hospitals, schools, restaurants, appliances, and electronics | [Here is a high-rated Italian restaurant in downtown Chicago:](https://exa.ai/search?q=Here+is+a+high-rated+Italian+restaurant+in+downtown+Chicago%3A&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |
| Legal and policy sources | High | Strong coverage of legal and policy information, (e.g., including sources like CPUC, Justia, Findlaw, etc.) | [Here is a common law case in california on marital property rights:](https://search.exa.ai/search?q=Here+is+a+common+law+case+in+california+on+marital+property+rights%3A&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22useAutoprompt%22%3Afalse%2C%22includeDomains%22%3A%5B%22law.justia.com%22%5D%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |
| Financial information | High | Includes sources like Yahoo Finance, with some results containing detailed financial data | [Here is a source on Apple’s revenue growth rate over the past years:](https://exa.ai/search?q=Here+is+a+source+on+Apple%27s+revenue+growth+rate+over+the+past+years%3A&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22startPublishedDate%22%3A%222023-11-18T22%3A35%3A50.022Z%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |
| Government and international organization sources | High | Includes content from sources like the IMF and CDC amongst others | [Here is a recent World Health Organization site on global vaccination rates:](https://exa.ai/search?q=Here+is+a+recent+World+Health+Organization+site+on+global+vaccination+rates%3A&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22startPublishedDate%22%3A%222023-11-18T22%3A35%3A50.022Z%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |
| Events | Moderate | Reasonable coverage of events in major municipalities, suggesting room for improvement | [Here is an AI hackathon in SF:](https://search.exa.ai/search?q=Here+is+an+AI+hackathon+in+SF&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22exclude%22%2C%22type%22%3A%22neural%22%2C%22startPublishedDate%22%3A%222024-07-02T23%3A36%3A15.511Z%22%2C%22useAutoprompt%22%3Afalse%2C%22endPublishedDate%22%3A%222024-07-09T23%3A36%3A15.511Z%22%2C%22excludeDomains%22%3A%5B%22twitter.com%22%5D%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |
| Jobs | Moderate | Can find some job listings | [If you’re looking for a software engineering job at a small startup working on an important mission, check out](https://search.exa.ai/search?q=If+you%27re+looking+for+a+software+engineering+job+at+a+small+startup+working+on+an+important+mission%2C+check+out&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |

[How Exa Search Works](/reference/how-exa-search-works) [Prompting Guide](/reference/prompting-guide)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Admin

Rate Limits

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Our rate limit for an individual account is currently 5 requests per second.

To discuss an Enterprise plan with rate limits above this level, you can contact us at [hello@exa.ai](mailto:hello@exa.ai)

[Setting Up and Managing Your Team](/reference/setting-up-team) [Enterprise Documentation & Security](/reference/security)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

SDK References

Python and TS Cheat Sheets

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

- Python
- typeScript

Python

Copy

```Python
from exa_py import Exa

# instantiate the Exa client
exa = Exa("YOUR API KEY")

# basic search
results = exa.search("This is a Exa query:")

# autoprompted search
results = exa.search("autopromptable query", use_autoprompt=True)

# search with date filters
results = exa.search("This is a Exa query:", start_published_date="2019-01-01", end_published_date="2019-01-31")

# search with domain filters
results = exa.search("This is a Exa query:", include_domains=["www.cnn.com", "www.nytimes.com"])

# search and get text contents
results = exa.search_and_contents("This is a Exa query:")

# search and get highlights
results = exa.search_and_contents("This is a Exa query:", highlights=True)

# search and get contents with contents options
results = exa.search_and_contents("This is a Exa query:",
                                text={"include_html_tags": True, "max_characters": 1000},
                                highlights={"highlights_per_url": 2, "num_sentences": 1, "query": "This is the highlight query:"})

# find similar documents
results = exa.find_similar("https://example.com")

# find similar excluding source domain
results = exa.find_similar("https://example.com", exclude_source_domain=True)

# find similar with contents
results = exa.find_similar_and_contents("https://example.com", text=True, highlights=True)

# get text contents
results = exa.get_contents(["ids"])

# get highlights
results = exa.get_contents(["ids"], highlights=True)

# get contents with contents options
results = exa.get_contents(["ids"],
                         text={"include_html_tags": True, "max_characters": 1000},
                         highlights={"highlights_per_url": 2, "num_sentences": 1, "query": "This is the highlight query:"})

```

[TypeScript SDK Specification](/integrations/typescript-sdk-specification) [LangChain Docs](/integrations/lang-chain-docs)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Live Demos

Hacker News Clone

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

[Click here to try Exa-powered Hacker News for Anything.](https://hackernews-by-exa.replit.app/)

### [](\#what-this-doc-covers)  What this doc covers:

- How to create a personalized Hacker News clone using Exa’s API.
- Steps to set up and run your own news site with custom prompts.
- Customization options for the site’s content, appearance, and deployment.

_Estimated time to complete: 20 minutes_

* * *

Built by Silicon Valley legend Paul Graham in 2007, [Hacker News](https://news.ycombinator.com/) is a popular website where users post interesting tech-adjacent content. The most interesting content often comes from small blogs and personal sites. However, these gems can be really hard to find.

Thankfully, Exa’s search models are good at finding interesting sites from all corners of the web, no matter how big or small. Exa searches the web semantically, enabling you to find information based on meaning rather than SEO. We can use Exa to find super interesting tech articles without specific keywords, topics, or blogs in mind.

In this tutorial, we’ll use Exa’s API to create a clone of Hacker News. Here’s our [live example](https://hackernews-by-exa.replit.app/).

You’ll get to create your own personalized version about anything, not just tech. For instance, you could make Business News, a site that displays relevant corporate updates. Your website will automatically update to get the newest content on whatever topic you choose.

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/315a2e9-Screenshot_2024-07-14_at_7.49.35_PM.png)

### [](\#getting-started)  Getting Started

First, grab a free Exa API key by signing up [here](https://exa.ai/). You get 1000 free queries a month.

Next, fork (clone) our [template](https://replit.com/@olafblitz/exa-hackernews-demo-nodejs?v=1) on Replit.

Once you’ve forked the template, go to the lower left corner of the screen and scroll through the options until you see “Secrets” (where you manage environment variables like API keys).

![Click on Secrets](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/0screenshot_2024-05-15_at_11.12.21___pm.png)

Add your Exa API key as a secret named “EXA\_API\_KEY” (original, we know).

![Add your API key!](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/0screenshot_2024-05-15_at_11.13.34___pm.png)

After you’ve added your API key, click the green Run button in the top center of the window.

![Run button](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/0screenshot_2024-05-15_at_10.08.03___pm.png)

After a few seconds, a Webview window will pop up with your website. You’ll see a website that vaguely resembles Hacker News. It’s a basic Express.js app with some CSS styling.

![What you should see](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/0screenshot_2024-05-15_at_10.12.09___pm.png)

### [](\#how-exa-works)  How Exa works

In the index.js file (should be open by default), scroll to **line 19**. This is the brains of the site. It’s where we call the Exa API with a custom prompt to get back Hacker News-style content.

Copy

```
const response = await fetch('https://api.exa.ai/search', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    // Add your API key named "EXA_API_KEY" to Repl.it Secrets
    'x-api-key': process.env.EXA_API_KEY,
  },
  body: JSON.stringify({
    // change this prompt!
    query: 'here is a really interesting techy article:',
    // specify the maximum number of results to retrieve (10 is the limit for free API users)
    numResults: 10,
    // Set the start date for the article search
    startPublishedDate: startPublishedDate,
    // Set the end date for the article search
    endPublishedDate: endPublishedDate,
  }),
});

```

The prompt is set to “here is a really interesting tech article:“. This is because of how Exa works behind the scenes. Exa uses embeddings to help predict which links would naturally follow a query. For example, on the Internet, you’ll frequently see people recommend great content like this: “this tutorial really helped me understand linked lists: linkedlisttutorial.com”. When you prompt Exa, you pretend to be someone recommending what you’re looking for. In this case, our prompt nudges Exa to find links that someone would share when discussing a “really interesting tech article”.

Check out the [results](https://exa.ai/search?q=here%20is%20a%20really%20interesting%20tech%20article%3A&filters=%7B%22numResults%22%3A30%2C%22useAutoprompt%22%3Afalse%2C%22domainFilterType%22%3A%22include%22%7D) Exa returns for our prompt. Aren’t they nice?

More example prompts to help you get a sense of prompting with Exa:

- [this gadget saves me so much time:](https://exa.ai/search?c=all&q=this%20gadget%20saves%20me%20so%20much%20time%3A&filters=%7B%22domainFilterType%22%3A%22include%22%2C%22timeFilterOption%22%3A%22any%5Ftime%22%2C%22activeTabFilter%22%3A%22all%22%7D)
- [i loved my wedding dress from this boutique:](https://exa.ai/search?c=all&q=i%20loved%20my%20wedding%20dress%20from%20this%20boutique%3A&filters=%7B%22domainFilterType%22%3A%22include%22%2C%22timeFilterOption%22%3A%22any%5Ftime%22%2C%22activeTabFilter%22%3A%22all%22%7D)
- [this video helped me understand attention mechanisms:](https://exa.ai/search?c=all&q=this%20video%20helped%20me%20understand%20attention%20mechanisms%3A&filters=%7B%22domainFilterType%22%3A%22include%22%2C%22timeFilterOption%22%3A%22any%5Ftime%22%2C%22activeTabFilter%22%3A%22all%22%7D)

More examples in the Exa [docs](/reference/the-metaphor-index).

Starting to get it? If not, fear not. Exa’s API offers an autoprompt feature that automatically converts a regular query into a good Exa-style prompt. For example, Exa’s [autoprompt](/reference/search) feature turns “deforestation” into “Here is an informative article about deforestation:“.

At this point, please craft your own Exa prompt for your Hacker News site. It can be about anything you find interesting.

Example ideas:

- [this is a really exciting machine learning paper:](https://exa.ai/search?c=all&q=this%20is%20a%20really%20exciting%20machine%20learning%20paper%3A&filters=%7B%22domainFilterType%22%3A%22include%22%2C%22timeFilterOption%22%3A%22past%5Fday%22%2C%22activeTabFilter%22%3A%22all%22%7D)
- [here’s a delicious new recipe:](https://exa.ai/search?c=all&q=here%27s%20a%20delicious%20new%20recipe%3A&filters=%7B%22domainFilterType%22%3A%22include%22%2C%22timeFilterOption%22%3A%22any%5Ftime%22%2C%22activeTabFilter%22%3A%22all%22%7D)
- [this company just got acquired:](https://exa.ai/search?c=all&q=this%20company%20just%20got%20acquired%3A&filters=%7B%22domainFilterType%22%3A%22include%22%2C%22timeFilterOption%22%3A%22past%5Fday%22%2C%22activeTabFilter%22%3A%22all%22%7D)
- [here’s how the basketball game went:](https://exa.ai/search?c=all&q=here%27s%20how%20the%20basketball%20game%20went%3A&filters=%7B%22domainFilterType%22%3A%22include%22%2C%22timeFilterOption%22%3A%22past%5Fday%22%2C%22activeTabFilter%22%3A%22all%22%7D)

Once you have your prompt, replace the old one (line 28 of index.js). Hit the Stop button (where the Run button was) and hit Run again to restart your site with the new prompt.

Feel free to keep tweaking your prompt until you get results you like.

### [](\#customize-your-site)  Customize your site

Now, other things you can modify in the site template include the time window to search over, the number of results to return, the text on the site (title, description, footer), and styling (colors, fonts, etc.).

By default, the site asks the Exa API to get the ten most relevant results from the last 24 hours every time you visit the site. On the free plan, you can only get up to ten results, so you’ll have to sign up for an Exa plan to increase this. You _can_ tweak the time window though. Lines 12 to 17 in index.js is where we set the time window. You can adjust this as you like to get results from the last week, month, year, etc. Note that you don’t have to search starting from the current date. You can search between any arbitrary dates, like October 31, 2015 and January 1, 2018.

To adjust the site title and other text, go to line 51 in index.js where the dynamic HTML starts. You can Ctrl-F “change” to find all the places where you can edit the text.

If orange isn’t your vibe, go to the styles.css. To get there, go to the left side panel on Replit and click on the “public” folder.

To keep your site running all the time, you’ll need to deploy it on Replit using Deployments. Click Deploy in the top right corner and select Autoscale. You can leave the default settings and click Deploy. This does cost money though. Alternatively you can deploy the site on your own. It’s only two files (index.js and public/styles.css).

Well, there you have it! You just made your very own Hacker News-style site using the Exa API. Share it on X and [tag us](https://x.com/ExaAILabs) for a retweet!

[Twitter/X post Retrieval](/examples/live-demo-twitterx-post-retrieval) [News Summarizer](/examples/recent-news-summarizer)

On this page

- [What this doc covers:](#what-this-doc-covers)
- [Getting Started](#getting-started)
- [How Exa works](#how-exa-works)
- [Customize your site](#customize-your-site)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/315a2e9-Screenshot_2024-07-14_at_7.49.35_PM.png)

![Click on Secrets](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/0screenshot_2024-05-15_at_11.12.21___pm.png)

![Add your API key!](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/0screenshot_2024-05-15_at_11.13.34___pm.png)

![Run button](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/0screenshot_2024-05-15_at_10.08.03___pm.png)

![What you should see](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/0screenshot_2024-05-15_at_10.12.09___pm.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Tutorials

Job Search with Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

### [](\#what-this-doc-covers)  What This Doc Covers

- The problem with traditional job search tools
- How to use Exa, an AI-powered search engine, for job hunting
- Other cool ways to use Exa beyond job searching

* * *

Finding a job is way harder than it should be. Tools like LinkedIn, Handshake, or Google are supposed to solve this problem, but they’re filled with too many noisy results to actually be useful.

Here’s how you can use AI to find hundreds of hidden job listings in less than 5 minutes.

At a high level, Exa is a search engine that understands your query. So, when searching for “ML internships for new grads in San Francisco” here’s what gets returned:

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/5d5309c-Screenshot_2024-07-18_at_12.44.34.png)

And, by filtering for only things that were posted recently, you can make sure that the positions were new and not-filled.

But, there’s actually an even better way to take advantage of Exa. You can just paste a job posting and get similar ones:

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/eb97595-Screenshot_2024-07-18_at_12.40.27.png)

### [](\#more-than-just-jobs)  More than just jobs

Job search is really just one use case of Exa. Exa is a search engine built using novel representation learning techniques.

For example, Exa excels at finding similar things.

- **Shopping**: if you want a similar (but cheaper) shirt, paste a link to your shirt and it’ll give you hundreds like it
- **Research**: paste a link to a research paper to find hundreds of other relevant papers
- **Startups**: if you’re building a startup, find your competitors by searching a link to your startup

[Phrase Filters: Niche Company Finder](/examples/niche-company-finder-with-phrase-filters) [Build a Retrieval Agent with LangGraph](/examples/getting-started-with-rag-in-langgraph)

On this page

- [What This Doc Covers](#what-this-doc-covers)
- [More than just jobs](#more-than-just-jobs)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/5d5309c-Screenshot_2024-07-18_at_12.44.34.png)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/eb97595-Screenshot_2024-07-18_at_12.40.27.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Tutorials

Phrase Filters: Niche Company Finder

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

### [](\#what-this-doc-covers)  What this doc covers

1. What Phrase filters are and how they work
2. Using ‘Phrase Filters’ to find specific results, in this case filtering by a foreign company suffix

In this simple example, we’ll demonstrate a company discovery search that helps find relevant companies incorporated in the Germany (and a few nearby countries) via Phrase Filters. This example will use the fact that companies incorporated in these locations [have a suffix of GmbH](https://en.wikipedia.org/wiki/GmbH), which is a term in the region similar to the US ‘incorporated’.

### [](\#how-phrase-filters-work)  How Phrase Filters work

Exa’s search combines semantic relevance with precise filtering: a neural query first retrieves contextually relevant documents, then a phrase filter refines these results by checking for specific text in the content. This two-stage approach delivers highly targeted outputs by leveraging both semantic understanding and exact text matching.

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/1864e57-Screenshot_2024-07-16_at_05.41.13.png)

### [](\#running-a-query-with-phrase-filter)  Running a query with phrase filter

Using Phrase Filters is super simple. As usual, install the `exa_py` library with `pip install exa_py`. Then instantiate the library:

Python

Copy

```Python
# Now, import the Exa class and pass your API key to it.
from exa_py import Exa

my_exa_api_key = "YOUR_API_KEY_HERE"
exa = Exa(my_exa_api_key)

```

Make a query, in this example searching for the most innovative climate tech companies. To use Phrase Filters, specify a string corresponding to the `includeText` input parameter

Python

Copy

```Python
result = exa.search_and_contents(
  "Here is an innovative climate technology company",
  type="neural",
  use_autoprompt=True,
  num_results=10,
  text=True,
	include_text=["GmbH"]
)

print(result)

```

Which outputs:

Copy

```
{
	"results": [\
		{\
			"score": 0.4694329500198364,\
			"title": "Sorption Technologies |",\
			"id": "https://sorption-technologies.com/",\
			"url": "https://sorption-technologies.com/",\
			"publishedDate": "2024-02-10",\
			"author": null,\
			"text": ""\
		},\
		{\
			"score": 0.46858930587768555,\
			"title": "FenX | VentureRadar",\
			"id": "https://www.ventureradar.com/organisation/FenX/364b6fb7-0033-4c88-a4e9-9c3b1f530d72",\
			"url": "https://www.ventureradar.com/organisation/FenX/364b6fb7-0033-4c88-a4e9-9c3b1f530d72",\
			"publishedDate": "2023-03-28",\
			"author": null,\
			"text": "Follow\n\nFollowing\n\nLocation: Switzerland\n\nFounded in 2019\n\nPrivate Company\n\n\"FenX is a Spinoff of ETH Zurich tackling the world’s energy and greenhouse gas challenges by disrupting the building insulation market. Based on a innovative foaming technique, the company produces high-performance insulation foams made from abandoned waste materials such as fly ash from coal power stations. The final products are fully recyclable, emit low CO2 emissions and are economically competitive.\"\n Description Source: VentureRadar Research / Company Website\n\nExport Similar Companies Similar Companies\n\nCompany \n Country\n Status\n Description\n\nVecor Australia Australia n/a Every year the world’s coal-fired power stations produce approximately 1 billion tonnes of a very fine ash called fly ash. This nuisance ash, which resembles smoke, can be... MCC Technologies USA Private MCC Technologies builds, owns and operates processing plants utilizing coal fly ash waste from landfills and ash ponds. The company processes large volumes of low-quality Class F... Climeworks GmbH Switzerland Private Climeworks has developed an ecologically and economically attractive method to extract CO2 from ambient air. Our goal is to deliver CO2 for the production of synthetic liquid... Errcive Inc USA Private The company is involved in developing a novel fly ash based material to mitigate exhaust pollution. The commercial impact of the work is to allow: the reduction of exhaust fumes... 4 Envi Denmark n/a Danish 4 Envi develops a system for the cleaning and re-use of biomass-fuelled plant’s fly ash. After cleaning, the ash and some of its components can be reused as fertilizers,... Neolithe France n/a Néolithe wants to reduce global greenhouse gas emissions by 5% by tackling a problem that concerns us all: waste treatment! They transform non-recyclable waste into aggregates...\n\nShow all\n\nWebsite Archive\n\nInternet Archive snapshots for |\n\nhttps://fenx.ch/\n\nThe archive allows you to go back in time and view historical versions of the company website\n\nThe site\n\nhttps://fenx.ch/\n\nwas first archived on\n\n4th Jul 2019\n\nIs this your company? Claim this profile andupdate details for free\n\nSub-Scores\n\nPopularity on VentureRadar\n\nWebsite Popularity\n\nLow Traffic Sites\n Low\n\nHigh Traffic Sites\n High\n\nAlexa Global Rank:\n\n3,478,846 | \n fenx.ch\n\nAuto Analyst Score\n\n68\n\nAuto Analyst Score:\n 68 | \n fenx.ch\n\nVentureRadar Popularity\n\nHigh\n\nVentureRadar Popularity:\n High The popularity score combines profile views, clicks and the number of times the company appears in search results.\n\nor\n\nTo continue, please confirm you\n are not a robot"\
		},\
		{\
			"score": 0.4682174026966095,\
			"title": "intelligent fluids | LinkedIn",\
			"id": "https://www.linkedin.com/company/intelligentfluids",\
			"url": "https://www.linkedin.com/company/intelligentfluids",\
			"publishedDate": "2023-06-08",\
			"author": null,\
			"text": "Sign in to see who you already know at intelligent fluids GmbH (SMARTCHEM)\n\nWelcome back\n\nEmail or phone\n\nPassword\n\nForgot password?\n\nor\n\nNew to LinkedIn? Join now\n\nor\n\nNew to LinkedIn? Join now"\
		},\
		{\
			"score": 0.46611523628234863,\
			"title": "justairtech GmbH – Umweltfreundliche Kühlsysteme mit Luft als Kältemittel",\
			"id": "https://www.justairtech.de/",\
			"url": "https://www.justairtech.de/",\
			"publishedDate": "2024-06-13",\
			"author": null,\
			"text": "decouple cooling from climate change with air as refrigerant.\n\nWir entwickeln eine hocheffziente Kühlanlage, die Luft als Kältemittel verwendet. Wieso? Die Welt verändert sich tiefgreifender und schneller als in allen Generationen vor uns. Wir sehen darin nicht nur eine Bedrohung, sondern begreifen dies auch als Chance, Prozesse nachhaltig zu gestalten.\n\nUnsere Arbeit konzentriert sich auf die Revolutio­nie­rung der Kühlung für Ziel­tempera­turen von 0–40 °C bei beliebiger Umwelt­temperatur. Dabei verwenden wir Luft als Kältemittel.\n\nzielgruppe\n\nDer globale Kühlbedarf macht aktuell 10% des weltweiten Strom­bedarfs aus und steigt rasant an. Es werden zwischen 2020 und 2070 knapp 10 Klima­anlagen pro Sekunde verkauft (viele weitere Zahlen und Statistiken rund um das Thema Kühlung findest Du bei der International Energy Agency ) . Mit unserer Technologie können wir verhindern, dass der Strom­verbrauch und die CO2-Emissionen propor­tional mit der Anzahl der verkauften Anlagen wächst.\n\nWir entwickeln eine Technologie, die 4–5 mal so effizient wie konventio­nelle Kühlanlagen arbeitet. Außerdem verwendet sie Luft als Kühlmittel. Luft ist ein natürliches Kältemittel, ist unbegrenzt frei verfügbar und hat ein Global Warming Potential von 0 (mehr zu natürlichen Kältemittel bei der Green Cooling Initiative) . Der Einsatz von Luft als Kältemittel ist nicht neu, aber mit konventio­nellen Anlagen im Ziel­temperatur­bereich nicht wettbewerbs­fähig umsetzbar. Unser erstes Produkt wird für die Kühlung von Rechen­zentren ausgelegt. Weitere Produkte im Bereich der gewerblichen und industriellen Kälte­erzeugung werden folgen.\n\nroadmap\n\n06/2020 \n Q4 2020 erste Seed-Finanzierungsrunde Q4 2020 \n 10/2020 erste Patentanmeldungen 10/2020 \n Q4 2021 zweite Seed-Finanzierungsrunde Q4 2021 \n Q4 2021 erste Patenterteilungen beantragt Q4 2021 \n 05/2022 Prototyp des fraktalen Wärmetauschers 05/2022 \n Q3 2022 Start-Up-Finanzierungsrunde Q3 2022\n\nQ4 2023 per CCS ausgeblendet Q4 2023 \n Q4 2023 physischer Anlagenprototyp Q4 2023 \n Q3 2024 Serienüberleitung und Beta-Tests Q3 2024 \n Q3 2025 \n ab 2025\n\nour core values\n\nWe love innovation. And disruption is even better! Failing is part of the game, but we are curious and continuous learners. \n We help and enable each other. Cooperative interaction with our clients, our partners and our colleagues is central. \n We are pragmatic. Our goals always remain our focus. We are dedicated team players. \n We interact respectfully. With each other and our environment.\n\nteam\n\nGerrit Barth Product Development & Technology \n Anna Herzog Head of Sales & Marketing, PR \n Bikbulat Khabibullin Product Development & Technology\n\nJohannes Lampl Product Development & Technology \n Anne Murmann Product Development & Technology \n Jens Schäfer Co-Founder and CEO\n\nHolger Sedlak Inventor, Co-Founder and CTO \n Adrian Zajac Product Development & Technology\n\nstellenangebote\n\npartner & förderungen"\
		},\
		{\
			"score": 0.4648257791996002,\
			"title": "Let’s capture CO2 and tackle climate change",\
			"id": "https://blancair.com/",\
			"url": "https://blancair.com/",\
			"publishedDate": "2023-03-01",\
			"author": null,\
			"text": "Let’s capture CO2 and tackle climate change\n\nWe need to keep global warming below 1.5°C. This requires a deployment of Negative Emission Technologies (NETs) of around 8 Gt of CO2 in 2050. Natural Climate solutions cannot do it alone.Technology has to give support. BLANCAIR can turn back human-emitted carbon dioxide from our atmosphere by capturing it and sequestering it back into the planet.\n\nGet to know us, our Hamburg team, partnerships and network\n\nTake a look at the BLANCAIR technology, our milestones & our next goals\n\nJoin our BLANCAIR team & help us to fight climate change!"\
		},\
		{\
			"score": 0.46323055028915405,\
			"title": "bionero - Der Erde zuliebe. Carbon Removal | Terra Preta",\
			"id": "https://www.bionero.de/",\
			"url": "https://www.bionero.de/",\
			"publishedDate": "2023-10-28",\
			"author": null,\
			"text": "Mehr Wachstum. Echter Klimaschutz. bionero ist eines der ersten Unternehmen weltweit, das zertifiziert klimapositiv arbeitet. Das Familienunternehmen, das in der Nähe von Bayreuth beheimatet ist, stellt qualitativ höchstwertige Erden und Substrate her, die durch das einzigartige Produktionsverfahren aktiv CO2 aus der Atmosphäre entziehen und gleichzeitig enorm fruchtbar sind. Aus Liebe und der Ehrfurcht zur Natur entwickelte bionero ein hochmodernes, industrialisiertes Verfahren, das aus biogenen Reststoffen eine höchstwertige Pflanzenkohle herstellt und zu fruchtbaren Schwarzerden made in Germany verwandelt. Hier kannst du bionero im Einzelhandel finden Wir liefern Gutes aus der Natur, für die Natur. Terra Preta (portugiesisch für \"Schwarze Erde\") gilt als \"wiederentdeckte Wundererde\". Sie wurde vor circa 40 Jahren in den Tiefen des Amazonasgebiets entdeckt und intensiv erforscht. Das Besondere an ihr ist ihre Fruchtbarkeit. Tatsächlich gilt dieser Boden als der fruchtbarste unseres Planeten. bionero hat gemeinsam mit Professor Bruno Glaser, einem weltweit anerkannten Experten für Terra Preta, das Herstellungsverfahren dieser besonderen Erde transformiert, optimiert und industrialisiert. Der wesentliche Wirk- und Inhaltsstoff ist eine sog. Pflanzenkohle. Sie sorgt dank ihrer enorm großen spezifischen Oberfläche für optimale Nährstoff- und Wasserspeicherfähigkeiten im Boden und bietet zusätzlich Lebensraum für wertvolle Mikroorganismen. Das Ergebnis ist ein stetiger Humusaufbau und eine dauerhafte Bodenfruchtbarkeit. Das Einzigartige an bionero? Die bionero Wertschöpfungskette ist vollständig klimapositiv! bioneros Produkte bieten einer Branche, die stark in die Kritik geraten ist, einen Weg in eine nachhaltige Zukunft. Während der Herstellung unserer hochwertigen Terra Preta leisten wir einen aktiven Beitrag zum Klimaschutz. Durch die Produktion unserer wichtigsten Zutat, der Pflanzenkohle, wird dem atmosphärischen Kohlenstoffkreislauf aktiv Kohlenstoff entzogen. Der Kohlenstoff, welcher anfangs in den biogenen Reststoffen gespeichert war, wird während des Pyrolyseprozesses für mehrere Jahrtausende in der Pflanzenkohle fixiert und gelangt somit nicht als Kohlenstoffdioxid zurück in unsere Atmosphäre. Das Erstaunliche: Die Pflanzenkohle entzieht der Atmosphäre das bis zu dreieinhalbfache ihres Eigengewichts an CO2! Die entstandenen Kohlenstoffsenken sind dabei transparent quantifizierbar und zertifiziert. Tatsächlich vereint bionero als erstes Unternehmen weltweit alle notwendigen Verfahrensschritte zu einer echten Kohlenstoffsenke gemäß EBC. Der Kohlenstoff ist am Ende der bionero Wertschöpfungskette in einer stabilen Matrix fixiert. Torf ist bis heute der meistgenutzte Rohstoff bei der Herstellung von Pflanzsubstraten. Schon beim Abbau werden Unmengen an CO2 freigesetzt. Moore sind einer der wichtigsten Kohlenstoff-Speicher unseres Planeten. Moore speichern 700 Tonnen Kohlenstoff je Hektar, sechsmal mehr als ein Hektar Wald! Durch die Trockenlegung und den Abbau für die Gewinnung von Torf können diese gewaltigen Mengen Kohlenstoff wieder zu CO2-reagieren und gelangen in die Atmosphäre. Hinzu kommen enorm weite Transportwege. Der Torfabbau findet zu großen Teilen in Osteuropa statt. Um einerseits die natürlichen Ökosysteme zu schützen und andererseits lange Transportwege zu vermeiden, setzen wir auf regional anfallende Roh- und Reststoffe. In langen Reifeprozessen verarbeiten wir natürliche Reststoffe zu hochwertigen Ausgangsstoffen für unsere Produkte. Bei der Auswahl aller Inputstoffe schauen wir genau hin und arbeiten nach dem Prinzip “regional, nachhaltig, umwelt- und klimaschonend“. Nur, wenn diese Voraussetzungen ausnahmslos gewährleistet sind, findet ein Rohstoff letztlich seinen Weg in unsere Produkte. bionero - Mehr Wachstum. Echter Klimaschutz. Erhalte spannende Einblicke in die Abläufe unseres Start-Ups und unsere hochmodernen Verfahren. Hier gibt es die neuesten Trends, aktuelle Tipps, hilfreiche Pflanz- und Pflegeanleitungen und interessante Videos."\
		},\
		{\
			"score": 0.4623781740665436,\
			"title": "Green City Solutions",\
			"id": "https://www.greentalents.de/green-city-solutions.php",\
			"url": "https://www.greentalents.de/green-city-solutions.php",\
			"publishedDate": "2022-04-12",\
			"author": null,\
			"text": "In their devices, called CityTrees, they combine the natural ability of moss to clean and cool the air with Internet of Things technology to control irrigation and ventilation. In March 2014, Green City Solutions GmbH was founded by Peter Sänger and his friend Liang Wu in Dresden. They set up a team of young experts from the fields of horticulture/biology, computer science, architecture, and mechanical engineering. The knowledge of the individuals was bundled to realise a device that combines nature and technology: the CityTree.\n\nThe living heart of CityTrees is moss cultivated on hanging textile mats. The moss mats are hidden behind wooden bars that provide sufficient shade for these plants, which naturally grow mainly in forests. Sensors are measuring various parameters such as temperature, humidity, and concentration of particulates. This data is used to regulate ventilation and irrigation. Behind the moss mats are large vents that create an airflow through the moss. In this way, the amount of air cleaned by the device can be increased when pollution levels are high, such as during rush hours.\n\nGreen City Solutions collaborates with several partners in Germany and abroad. Scientific partners include the Leibniz Institute for Tropospheric Research (TROPOS) and the Dresden University of Applied Sciences (HTW Dresden), both located in Germany. Green City Solutions has been awarded the Seal of Excellence by the European Commission. This is a European Union quality label for outstanding ideas worthy of funding.\n\nThe work of Green City Solutions mainly contributes to the Sustainable Development Goals 3, 11, 13, and 15:"\
		},\
		{\
			"score": 0.4593821167945862,\
			"title": "No.1 DAC manufacturer from Germany - DACMA GmbH",\
			"id": "https://dacma.com/",\
			"url": "https://dacma.com/",\
			"publishedDate": "2024-03-02",\
			"author": null,\
			"text": "Reach net zero goal with BLANCAIR by DACMA – a proven direct air capture technology with maximum CO2 uptake and minimal energy demand.\n\nDACMA GmbH, headquartered in Hamburg, Germany, is a pioneering DAC manufacturer with cutting-edge technology. With a proven track record, our first machines were delivered in 2023. Our scalable design reaches gigaton capacities, ensuring high CO2 uptake with minimal energy demand.\n\nGet to know us, our team, partnerships and network\n\nLearn more about the status quo of DAC technologies and our BLANCAIR solution\n\nJoin our DACMA team – help us to reach net zero and fight climate change!\n\nWhy BLANCAIR by DACMA:\n\nNo.1 DAC manufacturer from Germany – leveraging decades of aerospace – innovation\n\nDeliverable: proven technology in the market\n\nInterchangeable adsorbents for continuous performance improvement\n\nPatented reactor design with optimized air flow\n\nUniversal application for different climate conditions\n\n“In just one year, DACMA GmbH have achieved an exponential progress in the atmospheric carbon capture journey. The strategic alliance with Repsol (both in Venturing Capital and projects) will boost the pace of this highly focused group of outstanding engineers that are persistently looking for every angle of the technology improvement. Take the time to celebrate, acknowledge your success and keep going!!!”\n\n“One of the most relevant projects related to the development of technologies with a negative CO2 effect, the ONLY project in Brazil on Direct Air Capture multi-country Spain, Brazil Germany in Open Innovation. Repsol Sinopec Brazil Corporation, Start Up DACMA and PUC Rio Grande do Sul University. A disruptive commitment to a more decarbonized world. Being part of this project is a privilege and a unique opportunity to add value to society.”\n\n“In collaboration with Phoenix Contact, DACMA has developed an application that contributes to CO2 decarbonization. This technology makes a significant contribution to sector coupling in the All Electric Society and to the sustainable use of energy. I am delighted that two technology-driven companies are working together so efficiently.”\n\n“The DACMA GmbH with Jörg Spitzner and his team are not only valuable partners in our network, but also key initiators and innovators who, with BLANCAIR, are driving forward DAC system engineering in the Hamburg metropolitan region – an essential future climate change mitigation technology.”\n\n“Together with our partner DACMA GmbH, we are delighted to be building the first DAC machine on the HAMBURG BLUE HUB site in the Port of Hamburg. The 30-60 tons output of CO2 annually of the BLANCAIR machine can later be used to produce e-methanol for the Port of Hamburg, for example. This is a joint milestone, as it fits in with the plan to purchase large volumes of synthetic fuels from Power-to-X plants in Africa and South America for Germany through the HAMBURG BLUE HUB”.\n\nBacked by strong investors & partners:\n\nassociations & supporters:"\
		},\
		{\
			"score": 0.4587157368659973,\
			"title": "Heatrix GmbH Decarbonizing Industry – We decarbonize high temperature industrial heat.",\
			"id": "https://heatrix.de/",\
			"url": "https://heatrix.de/",\
			"publishedDate": "2024-02-28",\
			"author": null,\
			"text": "Our mission\n\nis to competitively replace fossil fuels in energy intensive industriesby converting renewable electricity into storable, high-temperature process heat.\n\n11% of global CO2 emissions is caused byhigh-temperature industrial heat.\n\nNo carbon-neutral, cost-competitive and easy\nto\nintegrate solution exists yet.\n\n11%\nof global CO2 emissions is caused by\nhigh-temperature industrial heat.\n\nNo carbon-neutral, cost-competitive and easy\nto integrate solution exists yet.\n\nOur solution\n\nThe Heatrix system combines an electric heater, utilizing off-grid solar or wind \nelectricity, with a thermal energy storage to provide continuous high-temperature \nprocess heat. With an outlet temperature of up to 1500 °C, Heatrix has the potential to \ndecarbonize the majority of high emission industries.\n\nHeatrix technology perfectly fulfils customers' \nrequirements – CO2 free continuous and easily integrated process heat at competitive cost.\n\nCarbon-free green heat, \nreducing CO2 emissions \n up to 100%\n\nProcess heat (hot air) \nup to 1500 °C\n\nThermal storage up\n to 20 hours to \ndeliver green heat 24/7\n\nHigh efficiency up \nto 90% based on \nresistance heating\n\nCost competitive vs. \nfossil fuels and substantially \ncheaper than green hydrogen\n\nModular container\nsystem enables \neasy scalability\n\nEasy integration \nwith minimal \nretrofitting needs\n\nApplications for Heatrix\n\nCalcination\n\nReplacing fossil fuel burners and reducing fuel consumption in calcination processes by integrating Heatrix heat to shaft calciners or precalciners of rotary kilns.\n\nHeat Treatment\n\nInducing required process temperatures via hot air flow from Heatrix replacing fossil fuel burners in heat treatment ovens.\n\nSintering & Pelletization\n\nReduced fuel gas & coke usage by providing Heatrix heat to sintering or pelletization plants.\n\nPreheating\n\nCombined with existing burner system, Heatrix technology can be used to preheat materials and reduce fuel consumption in the actual process.\n\nThis is us\n\nStrategy & Operations\n\nInnovator / Inventor / Sold first tech start-up in 2021 / Ph.D. from RWTH Aachen\n\nTechnology & Product\n\nTech Lead / Fluid dynamics expert / Energy technologies / Ph.D. from University Bremen\n\nBusiness & Finance\n\n2nd-time Founder / former VC-Investor / MBA from Tsinghua, MIT & HEC Paris\n\nContact us\n\nLooking for more information about Heatrix and our technology? We’d love to get in touch!\n\nHeatrix ensures defensibility through modular product, ease of integration, technological advantages and compelling business model.\n\nModular Product\n\n• Avoids individual design process – fits in standard containers• Industry-agnostic solution• Modular configuration to meet customer needs\n\nEasy Interaction\n\n• Rapid deployment• Focus on minimal plant downtime• Compatible to back-up for guaranteed production\n\nBusiness Model\n\n• Ongoing customer relationship and revenue \n• Large growth potential\n• Maximal impact on CO2\nreduction\n\nTechnical Advantage\n\n• Unique system design integrating electric heater and thermal storage \n• IP application in preparation for unique heater and storage design"\
		},\
		{\
			"score": 0.45255395770072937,\
			"title": "vabeck® GmbH - Grüne Prozesstechnik für den Umweltschutz",\
			"id": "https://www.vabeck.com/en",\
			"url": "https://www.vabeck.com/en",\
			"publishedDate": "2022-01-01",\
			"author": null,\
			"text": ""\
		}\
	],
	"requestId": "a02fd414d9ca16454089e8720cd6ed2b"
}

```

Nice! On inspection, these results include companies located in Hamburg, Munich and other close by European locations. This example can be extended to any key phrase - have a play with filtering via [other company suffixes -](https://en.wikipedia.org/wiki/List%5Fof%5Flegal%5Fentity%5Ftypes%5Fby%5Fcountry) and see what interesting results you get back!

[Recruiting Agent](/examples/exa-recruiting-agent) [Job Search with Exa](/examples/job-search-with-exa)

On this page

- [What this doc covers](#what-this-doc-covers)
- [How Phrase Filters work](#how-phrase-filters-work)
- [Running a query with phrase filter](#running-a-query-with-phrase-filter)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/1864e57-Screenshot_2024-07-16_at_05.41.13.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Concepts

FAQs

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

What is Exa?

Exa is a new search engine offering both proprietary neural search and industry-standard keyword search. It excels in finding precise web content, retrieving clean/rich web content, and can even identify similar pages based on input URLs. These technologies make Exa ideal for enhancing RAG pipelines, automating research, and creating niche datasets.

What's different about Exa's Neural Search?

Exa uses a transformer-based model to understand your query and return the most relevant links. Exa has embedded large portions of the web, allowing you to make extremely specific and complex queries, and get only the highest quality results.

How is Neural Search different from Google?

Google search is mostly keyword-based, matching query words to webpage words. For example, a Google search for “companies working on AI for finance” typically returns links like “Top 10 companies developing AI for financial services”. In contrast, Exa’s neural search understands meaning, returning actual company URLs. Additionally, Exa’s results are not influenced by SEO, unlike Google/other engines, which can be affected by optimized content. This allows Exa to provide more precise and relevant results based on the query’s intent rather than by keywords alone.

How is Exa different from LLMs?

Exa is a new search engine built from the ground up. LLMs are models built to predict the next piece of text. Exa predicts specific links on the web given their relevance to a query. LLMs have intelligence, and are getting smarter over time as new models are trained. Exa connects these intelligences to the web.

How can Exa be used in an LLM?

Exa enhances LLMs by supplying high-quality, relevant web content, minimizing hallucination and outdated responses. An LLM can take a user’s query, use Exa to find pertinent web content, and generate answers based on reliable, up-to-date information.

How does Exa compare to other search APIs?

Exa.ai offers unique capabilities:

- Neural Search Technology: Uses transformers for semantic understanding, handling complex queries based on meaning.
- Natural Language Queries: Processes and understands natural language queries for more accurate results.
- Instant Content Retrieval: Instantly returns clean and parsed content for any page in its index.
- Large-scale Searches: Capable of returning thousands of results for automatic processing, ideal for batch use cases.
- Content Highlights: Extracts relevant excerpts or highlights from retrieved content for targeted information.
- Optimized for AI Applications: Specifically designed for enhancing AI models, chatbots, and research automation.
- Auto Search: Automatically selects the best search type (neural or keyword) based on the query for optimal results.

How can Exa be used in an LLM?

Exa enhances LLMs by supplying high-quality, relevant web content, minimizing hallucination and outdated responses. An LLM can take a user’s query, use Exa to find pertinent web content, and generate answers based on reliable, up-to-date information.

How often is the index updated?

We update our index every two minutes, and are constantly adding batches of new links. We target the highest quality web pages. Our clients oftentimes request specific domains to be more deeply covered - if there is a use-case we can unlock by additional domain coverage in our index, please contact us.

What's our roadmap?

- The ability to create arbitrary custom datasets by powerfully searching over our index
- Support arbitrary non-neural filters
- Build a (much) larger index
- Solve search. No, really.

How does similarity search work?

When you search using a URL, Exa crawls the URL, parses the main content from the HTML, and searches the index with that parsed content.

The model chooses webpages which it predicts are talked about in similar ways to the prompt URL. That means the model considers a range of factors about the page, including the text style, the domain, and the main ideas inside the text.

Similarity search is natural extension for a neural search engine like Exa, and something that’s difficult with keyword search engines like google

What security measures does Exa take?

We have robust policies and everything we do is either in standard cloud services, or built in house (e.g., we have our own vector database that we serve in house, our own GPU cluster, our own query model and our own SERP solution). In addition to this, we can offer unique security arrangements like zero data retention as part of a custom enterprise agreement just chat to us!

[Exa's Capabilities Explained](/reference/exas-capabilities-explained) [Crawling Subpages with Exa](/reference/crawling-subpages-with-exa)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Concepts

Prompting Guide

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

### [](\#why-prompting-matters)  Why Prompting Matters

Exa’s neural search excels at understanding natural language descriptions of web content. For optimal results, frame queries as if you’re describing a link to someone.

### [](\#quick-solutions)  Quick Solutions

1. **Use Autoprompt**: Set `use_autoprompt=True` for automatic query optimization.
2. **Use Auto Search**: Use `type="auto"` for intelligent routing to auto vs keyword search, especially where neural is not returning useful results.

### [](\#prompting-tips)  Prompting Tips

1. **Phrase as Statements**: “Here’s a great article about X:” works better than “What is X?”
2. **Add Context**: Include modifiers like “funny”, “academic”, or specific websites to narrow results.
3. **End with a Colon**: Many effective prompts end with ”:”, mimicking natural link sharing.

### [](\#examples)  Examples

Bad: “best restaurants in SF”
Good: “Here is the best restaurant in SF:“

Bad: “What’s the best way to learn cooking?”
Good: “This is the best tutorial on how to get started with cooking:“

Remember, Exa is continually improving. These guidelines help leverage its current strengths while we work on making prompting even more intuitive.

[The Exa Index](/reference/the-exa-index) [Contents retrieval with Exa API](/reference/contents-retrieval-with-exa-api)

On this page

- [Why Prompting Matters](#why-prompting-matters)
- [Quick Solutions](#quick-solutions)
- [Prompting Tips](#prompting-tips)
- [Examples](#examples)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Tutorials

Company Analyst

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

### [](\#what-this-doc-covers)  What this doc covers

1. Using Exa’s link similarity search to find related links
2. Using the keyword search setting with Exa search\_and\_contents

* * *

In this example, we’ll build a company analyst tool that researches companies relevant to what you’re interested in. If you just want to see the code, check out the [Colab notebook](https://colab.research.google.com/drive/1VROD6zsaDh%5FrSmogSpSn9FJCwmJO8TSi?here).

The code requires an [Exa API key](https://dashboard.exa.ai/api-keys) and an [OpenAI API key](https://platform.openai.com/api-keys). Get 1000 free Exa searches per month just for [signing up](https://dashboard.exa.ai/overview)!

## [](\#shortcomings-of-google)  Shortcomings of Google

Say we want to find companies similar to [Thrifthouse](https://thrift.house/), a platform for selling secondhand goods on college campuses. Unfortunately, googling “ [companies similar to Thrifthouse](https://www.google.com/search?q=companies+similar+to+Thrifthouse)” doesn’t do a very good job. Traditional search engines rely heavily on keyword matching. In this case we get results about physical thrift stores. Hm, that’s not really what I want.

Let’s try again, this time searching based on a description of the company, like by googling “ [community based resale apps](https://www.google.com/search?q=community+based+resale+apps).” But, this isn’t very helpful either and just returns premade SEO-optimized listicles…

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/0bb023a-Screenshot_2024-02-06_at_11.22.28_AM.png)

What we really need is neural search.

## [](\#what-is-neural-search)  What is neural search?

Exa is a fully neural search engine built using a foundational embeddings model trained for webpage retrieval. It’s capable of understanding entity types (company, blog post, Github repo), descriptors (funny, scholastic, authoritative), and any other semantic qualities inside of a query. Neural search can be far more useful than traditional keyword-based searches for these complex queries.

## [](\#finding-companies-with-exa-link-similarity-search)  Finding companies with Exa link similarity search

Let’s try Exa, using the Python SDK! We can use the `find_similar_and_contents` function to find similar links and get contents from each link. The input is simply a URL, [https://thrift.house](https://thrift.house) and we set `num_results=10`(this is customizable up to thousands of results in Exa).

By specifying `highlights={"num_sentences":2}` for each search result, Exa will also identify and return a two sentence excerpt from the content that’s relevant to our query. This will allow us to quickly understand each website that we find.

Python

Copy

```Python
!pip install exa_py

from exa_py import Exa
import os

EXA_API_KEY= os.environ.get("EXA_API_KEY")

exa = Exa(api_key=EXA_API_KEY)
input_url = "https://thrift.house"

search_response = exa.find_similar_and_contents(
        input_url,
        highlights={"num_sentences":2},
        num_results=10)

companies = search_response.results

print(companies[0])

```

This is an example of the full first result:

Copy

```
[Result(url='https://www.mystorestash.com/',\
        id='lMTt0MBzc8ztb6Az3OGKPA',\
        title='The Airbnb of Storage',\
        score=0.758899450302124,\
        published_date='2023-01-01',\
        author=None,\
        text=None,\
        highlights=["I got my suitcase picked up right from my dorm and didn't have to worry for the whole summer.Angela Scaria /Still have questions?Where are my items stored?"],\
        highlight_scores=[0.23423566609247845])]

```

And here are the 10 titles and URLs I got:

Python

Copy

```Python
# to just see the 10 titles and urls
urls = {}
for c in companies:
  print(c.title + ':' + c.url)

```

\- College Marketplace:https://www.rumieapp.com/

Copy

```rumie
The Airbnb of Storage:https://www.mystorestash.com/
Bunction.net:https://bunction.net/
Home - Community Gearbox:https://communitygearbox.com/
NOVA SHOPPING:https://www.novashoppingapp.com/
Re-Fridge: Buy, sell, or store your college fridge - Re-Fridge:https://www.refridge.com/
Jamble: Social Fashion Resale:https://www.jambleapp.com/
Branded Resale | Treet:https://www.treet.co/
Swapskis:https://www.swapskis.co/
Earn Money for Used Clothing:https://www.thredup.com/cleanout?redirectPath=%2Fcleanout%2Fsell

```

Looks pretty darn good! As a bonus specifically for companies data, specifying `category="company"` in the SDK will search across a curated, larger companies dataset - if you’re interested in this, let us know at [hello@exa.ai](mailto:hello@exa.ai)!

Now that we have 10 companies we want to dig into further, let’s do some research on each of these companies.

## [](\#finding-additional-info-for-each-company)  Finding additional info for each company

Now let’s get more information by finding additional webpages about each company. To do this, we’re going to do a keyword search of each company’s URL. We’re using keyword because we want to find webpages that exactly match the company we’re inputting. We can do this with the `search_and_contents` function, and specify `type="keyword"` and `num_results=5`. This will give me 5 websites about each company.

Python

Copy

```python
# doing an example with the first companies
c = companies[0]
all_contents = ""
search_response = exa.search_and_contents(
  c.url, # input the company's URL
  type="keyword",
  num_results=5
)
research_response = search_response.results
for r in research_response:
  all_contents += r.text

```

Here’s an example of the first result for the first company, Rumie App. You can see the first result is the actual link contents itself.

Copy

```
<div><div><div><div><p><a href="https://www.rumieapp.com/"></a></p></div><div><p>The <strong>key</strong> to <strong>your</strong> college experience. </p><p><br/>Access the largest college exclusive marketplace to buy, sell, and rent with other students.</p></div></div><div><h2>320,000+</h2><p>Users in Our Network</p></div><div><div><p><h2>Selling is just a away.</h2></p><p>Snap a pic, post a listing, and message buyers all from one intuitive app.</p><div><p></p><p>Quick setup and .edu verification</p></div><div><p></p><p>Sell locally or ship to other campuses</p></div><div><p></p><p>Trade with other students like you</p></div></div><div><p><h2>. From local businesses around your campus</h2></p><h4>Get access to student exclusive discounts</h4><p>rumie students get access to student exclusive discounts from local and national businesses around their campus.</p></div></div><div><p><h2>Rent dresses from   </h2></p><p>Wear a new dress every weekend! Just rent it directly from a student on your campus.</p><div><p></p><p>Make money off of the dresses you've already worn</p></div><div><p></p><p>rumie rental guarantee ensures your dress won't be damaged</p></div><div><p></p><p>Find a new dress every weekend and save money</p></div></div><div><p><h2>. The only place to buy student tickets at student prices</h2></p><h4>Buy or Sell students Football and Basketball tickets with your campus</h4><p>rumie students get access to the first-ever student ticket marketplace. No more getting scammed trying to buy tickets from strangers on the internet.</p></div><div><div><div><p></p><h4>Secure</h4><p>.edu authentication and buyer protection on purchases.</p></div><div><p></p><h4>Lightning-fast</h4><p>Post your first listing in under a minute.</p></div><div><p></p><h4>Verified Students</h4><p>Trade with other students, not strangers.</p></div><div><p></p><h4>Intuitive</h4><p>List an item in a few simple steps. Message sellers with ease.</p></div></div><p><a href="https://apps.apple.com/us/app/rumie-college-marketplace/id1602465206">Download the app now</a></p></div><div><p><h2>Trusted by students.</h2></p><div><div><p></p><p>Saves me money</p><p>Facebook Marketplace and Amazon are great but often times you have to drive a long way to meet up or pay for shipping. rumie let’s me know what is available at my school… literally at walking distance. </p></div><div><p></p><p>5 stars!</p><p>Having this app as a freshman is great! It makes buying and selling things so safe and easy! Much more efficient than other buy/sell platforms!</p></div><div><p></p><p>Amazing!</p><p>5 stars for being simple, organized, safe, and a great way to buy and sell in your college community.. much more effective than posting on Facebook or Instagram!</p></div><div><p></p><p>The BEST marketplace for college students!!!</p><p>Once rumie got to my campus, I was excited to see what is has to offer! Not only is it safe for students like me, but the app just has a great feel and is really easy to use. The ONLY place I’ll be buying and selling while I’m a student.</p></div></div></div><div><p><h2>Easier to than GroupMe or Instagram.</h2></p><p>Forget clothing instas, selling groupme's, and stress when buying and selling. Do it all from the rumie app.</p></div></div></div>

```

## [](\#creating-a-report-with-llms)  Creating a report with LLMs

Finally, let’s create a summarized report that lists our 10 companies and gives us an easily digestible summary of each company. We can input all of this web content into an LLM and have it generate a nice report!

python

Copy

```Python
import textwrap
import openai
import os

SYSTEM_MESSAGE = "You are a helpful assistant writing a research report about a company. Summarize the users input into multiple paragraphs. Be extremely concise, professional, and factual as possible. The first paragraph should be an introduction and summary of the company. The second paragraph should include pros and cons of the company. Things like what are they doing well, things they are doing poorly or struggling with. And ideally, suggestions to make the company better."
openai.api_key = os.environ.get("OPENAI_API_KEY")

completion = openai.chat.completions.create(
    model="gpt-4",
    messages=[\
        {"role": "system", "content": SYSTEM_MESSAGE},\
        {"role": "user", "content": all_contents},\
    ],
)

summary = completion.choices[0].message.content

print(f"Summary for {c.url}:")
print(textwrap.fill(summary, 80))

```

Copy

```
Summary for https://www.rumieapp.com/:
Rumie is a college-exclusive marketplace app that allows students to buy, sell,
and rent items with other students. It has over 320,000 users in its network and
offers features such as quick setup, .edu verification, local and campus-wide
selling options, and exclusive discounts from local businesses. Students can
also rent dresses from other students, buy or sell student tickets at student
prices, and enjoy secure and intuitive transactions. The app has received
positive feedback from users for its convenience, safety, and effectiveness in
buying and selling within the college community.

Pros of Rumie include its focus on college students' needs, such as providing a
safe platform and exclusive deals for students. The app offers an intuitive and
fast setup process, making it easy for students to start buying and selling.
The option to trade with other students is also appreciated. Users find it convenient
that they can sell locally or ship items to other campuses. The app's rental
guarantee for dresses provides assurance to users that their dresses won't be
damaged. Overall, Rumie is highly regarded as a simple, organized, and safe
platform for college students to buy and sell within their community.
Suggestions to improve Rumie include expanding its reach to more colleges and
universities across the nation and eventually internationally. Enhancing
marketing efforts and fundraising can aid in raising awareness among college
students. Additionally, incorporating features such as improved search filters
and a rating/review system for buyers and sellers could enhance the user
experience. Continual updates and improvements to the app's interface and
functionality can also ensure that it remains user-friendly and efficient.

```

And we’re done! We’ve built an app that takes in a company webpage and uses Exa to

1. Discover similar startups
2. Find information about each of those startups
3. Gather useful content and summarize it with OpenAI

Hopefully you found this tutorial helpful and are ready to start building your very own company analyst! Whether you want to generate sales leads or research competitors to your own company, Exa’s got you covered.

[RAG Q&A](/examples/exa-rag) [Exa Researcher - JavaScript](/examples/exa-researcher)

On this page

- [What this doc covers](#what-this-doc-covers)
- [Shortcomings of Google](#shortcomings-of-google)
- [What is neural search?](#what-is-neural-search)
- [Finding companies with Exa link similarity search](#finding-companies-with-exa-link-similarity-search)
- [Finding additional info for each company](#finding-additional-info-for-each-company)
- [Creating a report with LLMs](#creating-a-report-with-llms)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/0bb023a-Screenshot_2024-02-06_at_11.22.28_AM.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

API Reference

Get contents

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

POST

/

contents

Send

Authorization

x-api-key

string

\*

x-api-key

Required

string

Body

object

\*

ids

array

\*

ids

Required

array

Array of document IDs obtained from searches

text

object

text

object

Parsed contents of the page.

maxCharacters

integer

maxCharacters

integer

Max length in characters for the text returned

includeHtmlTags

boolean

Select option

includeHtmlTags

boolean

Whether HTML tags, which can help the LLM understand structure of text, should be included. Default false

highlights

object

highlights

object

Relevant extract(s) from the webpage.

numSentences

integer

numSentences

integer

The number of sentences to be returned in each snippet. Default 5

highlightsPerUrl

integer

highlightsPerUrl

integer

The number of snippets to return per page. Default 1

query

string

query

string

summary

object

summary

object

Summary of the webpage

query

string

query

string

If specified, tries to answer the query in the summary

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.exa.ai/contents \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
  "ids": [\
    "<string>"\
  ],
  "text": {
    "maxCharacters": 123,
    "includeHtmlTags": true
  },
  "highlights": {
    "numSentences": 123,
    "highlightsPerUrl": 123,
    "query": "<string>"
  },
  "summary": {
    "query": "<string>"
  }
}'
```

200

Copy

```
{
  "results": [\
    {\
      "title": "<string>",\
      "url": "<string>",\
      "publishedDate": "<string>",\
      "author": "<string>",\
      "score": 123,\
      "id": "<string>",\
      "text": "<string>",\
      "highlights": [\
        "<string>"\
      ],\
      "highlightScores": [\
        123\
      ],\
      "summary": "<string>"\
    }\
  ]
}
```

* * *

[**Get your Exa API key**](https://dashboard.exa.ai/api-keys)

#### Authorizations

x-api-key

string

headerrequired

#### Body

application/json

ids

string\[\]

required

Array of document IDs obtained from searches

text

object

Parsed contents of the page.

Showchild attributes

highlights

object

Relevant extract(s) from the webpage.

Showchild attributes

summary

object

Summary of the webpage

Showchild attributes

#### Response

200 - application/json

results

object\[\]

Showchild attributes

[Search](/reference/search) [Find similar links](/reference/find-similar-links)

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.exa.ai/contents \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
  "ids": [\
    "<string>"\
  ],
  "text": {
    "maxCharacters": 123,
    "includeHtmlTags": true
  },
  "highlights": {
    "numSentences": 123,
    "highlightsPerUrl": 123,
    "query": "<string>"
  },
  "summary": {
    "query": "<string>"
  }
}'
```

200

Copy

```
{
  "results": [\
    {\
      "title": "<string>",\
      "url": "<string>",\
      "publishedDate": "<string>",\
      "author": "<string>",\
      "score": 123,\
      "id": "<string>",\
      "text": "<string>",\
      "highlights": [\
        "<string>"\
      ],\
      "highlightScores": [\
        123\
      ],\
      "summary": "<string>"\
    }\
  ]
}
```[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

RAG Quick Start Guide

RAG with LangChain

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

LangChain is a framework for building applications that combine LLMs with data, APIs and other tools. In this guide, we’ll go over how to use Exa’s LangChain integration to perform RAG with the following steps:

1. Set up Exa’s LangChain integration and use Exa to retrieve relevant content
2. Connect this content to a toolchain that uses OpenAI’s LLM for generation

See a YouTube tutorial of a very similar setup by the LangChain team [here](https://www.youtube.com/watch?v=dA1cHGACXCo).

See the full reference from LangChain [here](https://python.langchain.com/docs/integrations/providers/exa%5Fsearch/).

* * *

## [](\#get-started)  Get Started

1

Pre-requisites and installation

Install the core OpenAI and Exa LangChain libraries

Python

Copy

```Python
pip install langchain-openai langchain-exa

```

Ensure API keys are initialized properly. For LangChain libraries, the environment variable names are `OPENAI_API_KEY` and `EXA_API_KEY` for OpenAI and Exa keys respectively.

[**Get your Exa API key**](https://dashboard.exa.ai/api-keys)

2

Use Exa Search to power a LangChain Tool

Set up a Retriever tool using `ExaSearchRetriever`. This is a retriever that connects to Exa Search to find relevant documents via semantic search. First import the relevant libraries and instantiate the ExaSearchRetriever.

Python

Copy

```Python
from langchain_exa import ExaSearchRetriever
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

# Define our retriever to use Exa Search, grabbing 3 results and parsing highlights from each result
retriever = ExaSearchRetriever(k=3, highlights=True)

```

3

Create a prompt template (optional)

We use a LangChain [PromptTemplate](https://python.langchain.com/v0.1/docs/modules/model%5Fio/prompts/quick%5Fstart/#prompttemplate) to define a template of placeholder to parse out URLs and Highlights from the Exa retriever.

Python

Copy

```Python
# Define a document prompt template using XML-like stags
document_prompt = PromptTemplate.from_template("""
<source>
    <url>{url}</url>
    <highlights>{highlights}</highlights>
</source>
""")

```

4

Parse the URL and content from Exa results

We use a [Runnable Lambda](https://api.python.langchain.com/en/latest/runnables/langchain%5Fcore.runnables.base.RunnableLambda.html) to parse out the URL and Highlights attributes from the Exa Search results then pass this to the prompt template above

Python

Copy

```Python
# Create a Runnable Lambda that parses highlights and URL attributes from the retriever and passes to our document prompt from above
document_chain = RunnableLambda(
    lambda document: {
        "highlights": document.metadata["highlights"],
        "url": document.metadata["url"]
    }
) | document_prompt

```

5

Join Exa results and content for retrieval

Complete the retrieval chain by stitching together the Exa retriever, the parser and a short lambda function - this is crucial for passing the result as a single string as context for the LLM in the next step.

Python

Copy

```Python
# Define the retrieval chain - Exa search results => grab attributes and parse into XML => join into a single string to feed as context in next steps
retrieval_chain = retriever | document_chain.map() | (lambda docs: "\n".join([i.text for i in docs]))

```

6

Set up the rest of the toolchain including OpenAI for generation

In this step, we define the system prompt with Query and Context template inputs to be grabbed from the user and Exa Search respectively. First, once again import the relevant libraries and components from LangChains libraries

Python

Copy

```Python
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

```

Then we define a generation prompt - the prompt template that is used with context from Exa to perform RAG.

Python

Copy

```Python
# Define core prompt template
generation_prompt = ChatPromptTemplate.from_messages([\
    ("system", "You are an expert research assistant. You use xml-formatted context to research people's questions."),\
    ("human", """\
Please answer the following query based on the provided context. Please cite your sources at the end of your response.:\
\
Query: {query}\
---\
<context>\
{context}\
</context>\
""")\
])

```

We set the generation [LLM to OpenAI](https://python.langchain.com/v0.1/docs/integrations/chat/openai/), then connect everything with a [RunnableParallel](https://python.langchain.com/v0.1/docs/expression%5Flanguage/primitives/parallel/) parallel connection. The generation prompt, containing the query and context, is then passed to the LLM and [parsed for better output representation](https://api.python.langchain.com/en/latest/output%5Fparsers/langchain%5Fcore.output%5Fparsers.string.StrOutputParser.html).

Python

Copy

```Python
# Use OpenAI for generation
llm = ChatOpenAI()

# Simple string parsing for trhe output
output_parser = StrOutputParser()

# Connect the chain, including parallel connection for query from user and context from Exa retriever chain in step 2.
chain = RunnableParallel({
    "query": RunnablePassthrough(),
    "context": retrieval_chain,
}) | generation_prompt | llm | output_parser

```

7

Running the full RAG toolchain

Let’s [invoke](https://python.langchain.com/v0.1/docs/expression%5Flanguage/interface/#invoke) the chain:

Python

Copy

```Python
chain.invoke("Latest research on climate change innovation")

```

And have a look at the output (newlines parsed):

Stdout

Copy

```Stdout
'Based on the provided context, the latest research on climate change innovation reveals several important findings:
1. Innovation in response to climate change: A study examined how innovation responds to climate change by analyzing a panel dataset of 70 countries. The study found that the number of climate-change-related innovations is positively correlated with increasing levels of carbon dioxide emissions from gas and liquid fuels, mainly from natural gases and petroleum. However, it is negatively correlated with increases in carbon dioxide emissions from solid fuel consumption, mainly from coal, and other greenhouse gas emissions. The research also highlighted that government investment does not always influence decisions to develop and patent climate technologies. This study contributes to the environmental innovation literature by providing insights on how innovation reacts to changes in major climate change factors.
2. Climate tech funding and attention: During the period of 2010-2022, outside of the US, China, EU, and India, only 8% of total climate venture capital activity came from the rest of the world. This concentration of funding and attention in specific regions may be hindering the reach of climate tech solutions to low-income communities and developing countries, which are already feeling the effects of climate change but lack the necessary resources to address them effectively.
3. Research funding allocation: A study from the University of Sussex Business School analyzed research funding for climate and energy research from 1990 to 2020. The research found that 36% of funding was allocated to climate adaptation, while 28% went to studying how to clean up the energy system. Other significant shares of funding were allocated to transport and mobility (13%), geoengineering (12%), and industrial decarbonization (11%). The majority of the funding went to researchers in wealthy, Western countries, which may not be the most vulnerable to the immediate impacts of climate change.
Sources:
1. Study on innovation response to climate change: https://www.sciencedirect.com/science/article/pii/S0040162516302542
2. Climate tech funding and attention: https://www.sbs.ox.ac.uk/oxford-answers/climate-tech-opportunity-save-planet
3. Research funding allocation for climate and energy research: https://www.protocol.com/bulletins/climate-research-funding-adaptation'

```

8

Optionally, stream the output of the chain

Optionally, you may

Python

Copy

```Python
for chunk in chain.stream("Latest research on climate change innovation"):
  print(chunk, end="|", flush=True)

# Or asynchronously
async for chunk in chain.astream("..."):
  print(chunk, end="|", flush=True)

```

Outputs, in a stream - [click here](https://python.langchain.com/v0.1/docs/expression%5Flanguage/streaming/) to learn more about the .stream method and other options, including handling of chunks and how to think about further parsing outputs:

Streamed text output

Copy

```Streamed
`|Based| on| the| provided| context|,| the| latest| research| on| climate| change| innovation| indicates| several| key| insights|:

|1|.| The| concentration| of| funding| and| attention| in| countries| like| the| US|,| China|,| EU|,| and| India| has| led| to| a| lack| of| climate| tech| ecosystem| development| in| other| parts| of| the| world|.| This| has| resulted| in| low|-income| communities| and| developing| countries| being| under|-equipped| to| address| the| effects| of| climate| change|.
|(Source|:| Oxford| Answers| -| https|://|www|.s|bs|.|ox|.ac|.uk|/|ox|ford|-|answers|/cl|imate|-tech|-op|portunity|-save|-|planet|)

|2|.| A| study| conducted| using| econ|ometric| methods| on| a| panel| dataset| of| |70| countries| found| that| the| number| of| climate|-change|-related| innovations| is| positively| responding| to| increasing| levels| of| carbon| dioxide| emissions| from| gas| and| liquid| fuels|,| but| negatively| to| increases| in| carbon| dioxide| emissions| from| solid| fuel| consumption| and| other| greenhouse| gas| emissions|.| Government| investment| does| not| always| influence| decisions| to| develop| and| patent| climate| technologies|.
|(Source|:| Science|Direct| -| https|://|www|.s|ci|enced|irect|.com|/sc|ience|/article|/pi|i|/S|004|016|251|630|254|2|)

|3|.| Additionally|,| insights| into| climate| change| technology| transfer| and| policy| implications| can| be| found| in| the| environmental|-in|novation| literature|,| contributing| to| a| better| understanding| of| how| innovation| reacts| to| changes| in| major| climate| change| factors|.
|(Source|:| Nature| -| https|://|www|.n|ature|.com|/articles|/n|climate|230|5|)

|These| sources| provide| valuable| information| on| the| current| state| of| climate| change| innovation| research| and| its| implications| for| addressing| the| global| challenge| of| climate| change|.|||Based| on| the| provided| context|,| here| are| the| responses| to| the| query|:

|1|.| Elon| Musk| is| known| for| being| the| richest| person| in| the| world| and| having| some| unusual| and| expensive| hobbies|.| One| of| his| hobbies| involves| pretending| to| acquire| public| companies|,| which| he| seems| to| find| fun|.| This| behavior| has| been| highlighted| in| the| article| mentioned| in| the| source|:| "|Programming| note|:| U|gh|,| here| we| are| again|,| huh|?| Oh| Elon| I| think| it| is| helpful| to| start| with| the| big| picture|."| (|Source|:| Bloomberg| Opinion|)

|2|.| Charles| E|.| No|ad| was| known| for| his| remarkable| abilities|,| such| as| being| able| to| discern| whether| a| period| at| the| end| of| a| sentence| was| in| it|al|ics| or| not|.| He| was| a| valuable| support| to| Christopher| Tolkien| and| contributed| an| essay| titled| "|On| the| Construction| of| the| Sil|mar|illion|,"| which| speculated| on| what| J|.R|.R|.| Tolkien| would| have| included| in| The| Sil|mar|illion| had| he| finished| it|.| This| information| is| detailed| in| the| source|:| "|He| could| quite| literally| tell| whether| a| period| (|the| full| stop| at| the| end| of| a| sentence|)| was| in| it|al|ics| or| not|."| (|Source|:| Kal|im|ac| Blog|)

|3|.| The| challenges| and| limitations| of| automated| technology|,| specifically| in| the| context| of| taxi| services|,| are| highlighted| in| the| source|:| "|There|'s| just| a| level| of| necessary| flexibility| given| the| reality| of| our| built| environment| that| the| robot| brains| aren|'t| going| to| manage|."| The| source| discusses| an| incident| where| a| robot| taxi|,| named| Brown|ie|,| did| not| respond| to| a| wave| to| pick| up| passengers|,| leading| them| to| walk| along| an| active| traffic| lane| to| reach| it|.| (|Source|:| Es|chat|on| Blog|)

|Sources|:
|1|.| Bloomberg| Opinion| -| https|://|www|.b|loomberg|.com|/op|inion|/articles|/|202|2|-|07|-|09|/|elon|-s|-out|
|2|.| Kal|im|ac| Blog| -| https|://|kal|im|ac|.blogspot|.com|/|202|3|/|07|/|char|les|-e|-no|ad|.html|
|3|.| Es|chat|on| Blog| -| https|://|www|.es|chat|on|blog|.com|/|202|2|/|07|/pay|-me|-for|-my|-gen|ius|.html||

```

As you can see, the output generation is enriched with the context of our Exa Search query result!

[RAG with Exa and OpenAI](/reference/rag-quickstart) [OpenAI Exa Wrapper](/reference/openai)

On this page

- [Get Started](#get-started)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

RAG Quick Start Guide

RAG with Exa and OpenAI

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

By combining Exa’s search capabilities with OpenAI’s language models, you can build a system that retrieves relevant, up-to-date information and generates insightful summaries. Here is the workflow:

**1\. Retrieval (Exa):** Searches the web to find relevant and up-to-date results based on your query.

**2\. Processing:** Combines the retrieved Exa search results with your LLM query.

**3\. Generation (OpenAI):** Uses OpenAI’s LLM to generate an informed response using both your query and Exa’s search results.

* * *

## [](\#get-started)  Get Started

First, create an account and grab a free API key.

[**Get your Exa API key**](https://dashboard.exa.ai/api-keys)

Next, choose to use our Python or TypeScript SDK to set up your RAG system.

- Python
- TypeScript

1

Install the python SDK

Shell

Copy

```Shell
pip install exa_py

```

2

Set up the environment variable

Create an `.env` file in the root of your project and set the `EXA_API_KEY` environment variable to [your API key](https://dashboard.exa.ai/api-keys).

Shell

Copy

```Shell
EXA_API_KEY=insert your Exa API key here, without quotes

```

3

Instantiate the client

Python

Copy

```Python
from exa_py import Exa
import os
exa = Exa(os.getenv('EXA_API_KEY'))

```

4

Make a search using the search\_and\_contents method

The `search_and_contents` method returns a list of search results with the contents and/or highlights of the webpages.

You can find a more detailed explanation of the methods [here](/exa-s-capabilities-explained).

Python

Copy

```Python
result = exa.search_and_contents(
  "hottest AI startups",
  type="neural",
  use_autoprompt=True,
  num_results=10,
  text=True
)

print(result)

```

5

Output

Shell

Copy

```Shell
Title: Paradox: The AI assistant for recruiting, Olivia
URL: https://www.paradox.ai/
ID: https://www.paradox.ai/
Score: 0.17563548684120178
Published Date: 2023-01-01
Author: None
Text: Say hello to the world's fastest, simplest hiring experience. See Olivia in action Say hello to your team's next best hire. Olivia is the simple, conversational recruiting solution that does work for you. She automates, answers, screens, schedules, and onboards ... to help you hire faster. What can Olivia do? See Olivia in action Sheâs your next best hire. Olivia is the simple, conversational recruiting solution that does work for you. She automates, answers, screens, schedules and onboards ... to help you hire faster. See Olivia in action. See Olivia in action Sheâs your next best hire. Olivia is the simple, conversational recruiting solution that does work for you. She automates, answers, screens, schedules and onboards ... to help you hire faster. See Olivia in action. See Olivia in action Sheâs your next best hire. Olivia is the simple, conversational recruiting solution that does work for you. She automates, answers, screens, schedules and onboards ... to help you hire faster. See Olivia in action. If you hire people, you deserve an assistant. Meet Olivia, the simple, conversational recruiting solution that does work for you. She automates, answers, screens, schedules and onboards ... to help you hire faster. We measure success in client hugs. From high-volume hourly roles to highly technical engineering openings to hard-to-find healthcare professionals âÂ Olivia's assisting companies in every industry, all over the world. The epiphany came after we turned Paradox on. It was so much better than we ever thought it would be. Josh SwemmTA ManagerMeritage Hospitality Group Adam ChenChief Marketing OfficerAmerican Pool Paradox removes time stealers from our HR and Ops teams. It's our best recruiting investment of the last 2 years. Rachel O'ConnellVP of TalentGreat Wolf Lodge Rebecca VolpanoDirector of Client SuccessCielo Our ability to engage candidates in 47 countries and 18 languages 24/7 has been critical to achieving our hiring goals. Gui NevesTA Sourcing & Solutions LeadNestle Speed and experience are critical. Paradox checks both boxes â providing a fast, frictionless hiring experience that works. Michael FerrantiChief People OfficerRegis Corporation Derek BraunRecruiting ManagerGoWireless Paradox exceeded my expectations wildly in all ways â always tailoring solutions to meet our use cases. Christina CoyleSVP of Talent AcquisitionAdvantage Solutions I've partnered with Paradox at two companies and they always deliver above and beyond my expectations. Jacob KramerSVPÂ of Talent AcquisitionU.S. Xpress Olivia's helping us streamline candidates that we would have lost if we didn't have this technology in place. Leah ButtersRecruitment Strategy ConsultantMultiCare Health System Paradox was completely transformational, almost instantly. Our team was saving an enormous amount of time. Jay Chan SVPÂ of Talent AcquisitionUnited Overseas Bank We're proud to partner with Paradox to drive innovation around the experiences we create for candidates and our team. Tom DaewaleHead of Employee ExperienceUnilever Recruiting teams and hiring managers spend 80% of their time on manual tasks. Olivia can do that work for them. Request a demo Meet the world's easiest job search. Candidates shouldnât have to dig to find a relevant job. Olivia can instantly match jobs to each personâs location, resume, or keywords they use in a conversation â making it easy to find the perfect fit. More on experience assistant î  And text-to-apply experiences that are even easier. Nothing increases drop-off more than logins, passwords, and clunky applications. Olivia shortens time-to-apply to minutes, with a quick, lightweight text-to-apply experience. More on text to apply î  Unlock your candidate's true personality and unique skills. The Big 5 assessment measures a personâs Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. Normally taking nearly 10 minutes, our visual-based assessment takes less than 2 minutes. More on assessments î  Schedule any type of interview in seconds, 24 hours a day. From scheduling to rescheduling to reminders, Olivia ensures you never have to worry about endless back and forth, double booking, or interview no-shows again. More on scheduling î  And answer questions instantly â in 100+ languages. From FAQs about 401k match or benefits, to what to wear to an interview or where to park, Olivia can answer thousands of questions, 24/7, in whatever language the candidate prefers. Make offers and onboarding a breeze. When youâre ready to offer, Olivia can share the good news. She can also automate sending and reminding new hires to complete onboarding steps â like completing I-9, tax, or WOTC paperwork. More on onboarding î  Don't want to replace your current systems? No worries. Olivia makes them better. Olivia's saving recruiters and managers millions of hours every year. From dramatic reductions in time-to-hire to nearly perfect feedback from candidates, Olivia's changing the expectation for what hiring software can do for companies all over the world. decrease in job advertising Increase in hard-to-fill roles candidate satisfaction rating Change is hard. We get it. But our job is to make your job easier. A+ Implementation Change doesnât have to be hard. Our team of pros makes it even easier. Countless Integrations From Workday to SAP to Indeed, Olivia can work alongside the world's best. See integrations î  Global & Secure SOC-2, Type 2 and GDPR certified. 30+ languages. Built for local, built for global. Learn more î  âFor hiring managers, it's giving them all that administrative time back and alleviating frustrations that come with scheduling.â Alexa Morse, Director of HR Operations Read Full Report î  60 reduction in time to hire 95 positive candidate experience
Highlights: None
Highlight Scores: None

Title: Harvey | Generative AI for Elite Law Firms
URL: https://www.harvey.ai/
ID: https://www.harvey.ai/
Score: 0.17165924608707428
Published Date: None
Author: None
Text: Contact Sales. Unprecedented. legal AI. Join the Waitlist. * Careers. * Privacy Policy
Highlights: None
Highlight Scores: None

Title: Adept: Useful General Intelligence
URL: https://www.adept.ai/
ID: https://www.adept.ai/
Score: 0.17111459374427795
Published Date: 2000-01-01
Author: None
Text: A new way to use computers. We’re building a machine learning model that can interact with everything on your computer. Join the waitlist. Our vision: An AI teammate for everyone. Adept is building an entirely new way to get things done. It takes your goals, in plain language, and turns them into actions on the software you use every day. Collaborate and create. Your hands on the wheel. We believe that AI systems should be built with users at the center — where machines work together with people in the driver's seat: discovering new solutions, enabling more informed decisions, and giving us more time for the work we love. What they’re saying… We are hiring
Highlights: None
Highlight Scores: None

Title: We Build Computers That Think
URL: https://brain.ai/#/
ID: https://brain.ai/#/
Score: 0.17037421464920044
Published Date: 2021-07-28
Author: None
Text: Introducing Natural We've had our smartphones for the last 14 years. On July 28, 2021, Brain is reimagining the way we interact with our phones. Introducing Natural - the first generative interface that allows software to be in sync with your intention. You no longer go to apps, apps come to you. Simply say what you need and the right app forms itself around your words. WHO ARE WE? At Brain.ai, we build computers that think. We invent new technologies and design metaphors that allow computers to become an extension of our minds instead of simply our hands. As we transition from the information age to the intelligence age, we bridge the existing world of software with emerging general intelligence in a natural and humane way. As pioneers of the few-shot learning approach to NLP in 2016, we stand at the intersection of advancing the latest technology and design. Our investors include Laurene Powell Jobs, Goodwater Capital, Scott Cook and WTT Investment. Natural AI Natural AI, our first consumer product, is the world's first generative interface. You no longer go to Apps, Apps come to you. Simply say what you need and the right app forms itself around your words - now fulfilling millions of requests each month. Natural clears away the clutter on your screen. It allows you to focus on what you want, not how to get there. If you are extremely curious, and won't settle for a tech company that makes incremental improvements. You want your work to be remembered, to add up to something big. You want to do work that keeps you up at night from excitement. You want your life to be filled with 'insane moments of realization.' San Mateo，CA Full-time Responsibilities: We are looking for a UX Designer to join us in inventing the metaphors and patterns that make up this experience. The UX Designer thinks laterally and finds clarity through making. They are excited about metaphors, and jump at the chance to play with new tools and technologies. They move between engineering and design with fluidity, and values vision over pure craftsmanship. They are flexible about ideas, and uncompromising about doing the right thing. Qualifications and Skills: 5+ years of progressive experience in product design, web design, UI/UX design and/or art direction with a focus on web, mobile and/or enterprise products. Strong portfolio of wireframes, user interface mockups, and prototypes for real products - on the market. Experience working with stakeholders in developing value proposition canvas, customer journey mapping, and identifying KPI/OKRs. Deep knowledge of design tools - Figma, Sketch and any other tools needed. Able to design autonomously, meet milestones and comfort working in agile, fast-paced surroundings. Excited about next-generation interfaces. Strong, demonstrated visual design aptitude – a great sense for color, form, typography and other design elements is shown in your work. Meticulous attention to detail, detail-oriented, organized and strong project management skills. Comfort with ambiguity in early production definition stages. Mindset for creating clean, “less is more” user interface designs. Apply San Mateo，CA Full-time Responsibilities: In this role, you’ll be sitting at the intersection of UX, NLP and engineering, designing improvements to our natural language engine, the core technology behind the intelligence of our product. You’ll get to solve difficult problems like semantic understanding, entity recognition, dialogue state tracking, knowledge base induction, personalization and active learning. On this path to product launch, you’ll have a hand in shaping a highly personal and intent-driven user experience — bringing the
Highlights: None
Highlight Scores: None

Title: Home | Tenyx, Inc.
URL: https://www.tenyx.com/
ID: https://www.tenyx.com/
Score: 0.169786736369133
Published Date: 2019-09-10
Author: None
Text: TENYX IS DEVELOPING THE NEXT-GENERATION OF INTELLIGENT MACHINES BASED ON PROPRIETARY NEUROSCIENCE-INSPIRED AI TECHNOLOGY Tenyx in the News Robust voice-based conversational agents We are tackling some of the core challenges facing existing AI solutions, including the ability to learn continually from new information in real-time and the need to dramatically reduce model training times. Using proprietary neuroscience-inspired AI technology, our team is building the next generation of voice-based conversational agents: intelligent, interactive, and with the common-sense reasoning lacking today. Addressing some of the key challenges of current AI technology We're Hiring ... We are a team of researchers and engineers led by an experienced leadership team with a track record of building successful AI companies from the ground up. We are looking for talented individuals with strong analytical capabilities, machine learning experience and solid coding skills, who are passionate about delivering the next-generation of AI technology and building highly impactful products. If that's you please email us at: jobs@tenyx.com.

Title: DirectAI
URL: https://directai.io/?utm_source=twitter&utm_medium=raw_message&utm_campaign=first_launch
ID: https://directai.io/?utm_source=twitter&utm_medium=raw_message&utm_campaign=first_launch
Score: 0.16954544186592102
Published Date: 2023-01-01
Author: None
Text: Vision models . Build and deploy powerful computer vision models with plain language.No code or training required. different. We use large language models and zero-shot learning to instantly build models that fit your description. We're the last major barrier to creating custom models - . Deploy and iterate in seconds with Venture-backed.Based in NYC. We're changing how people use AI in the real world. Come talk to us on .
Highlights: None
Highlight Scores: None

Title: Ghost AI | Scale Sales Outreach | Grow B2B Revenue
URL: https://www.useghost.ai/
ID: https://www.useghost.ai/
Score: 0.1689704805612564
Published Date: 2000-01-01
Author: None
Text: Trusted, purpose built AI for B2B revenue growth Scale your B2B prospecting, outreach, and conversion using trusted, performant outreach developed by top AI researchers from OpenAI. Technology trusted by over 1000+ companies Transform your sales funnel with AI-driven two-way communication Elevate your outreach with AI that understands your business and engages prospects with the right context and timing, improving over time with advanced machine learning that takes the guesswork out of sales. Convert prospects into partners with data-driven AI engagement. Drive conversions through AI that not only reaches out but resonates, building trust and interest. Scale on brand, personalized outreach that creates rapport. Contact interested buyers where they are, when they are. Imagine leveraging over 80+ million buying intent signals to deliver your messaging at the right moment for the right customer. Ghost delivers automatic targeting that generates motivated top-of-funnel conversions at any scale, effortlessly. Top of funnel at 10x the conversion of traditional ads. Our outreach campaigns achieve an average of 83% open rates and a minimum of 11% positive reply rates on first impression. Grow revenue at 5x the scale of traditional outreach. Discover qualified leads with AI that goes beyond the surface Target the right prospects with AI that identifies and nurtures potential leads into valuable conversations. Build relationships first not sales. Connect with prospects wherever they are. Our AI seamlessly connects with your existing tools, providing a cohesive experience through email, chat, and SMS. Uncover actionable channel-specific data Track all metrics with custom reports. Maximize impact by analyzing campaign results and content performance easily. Plan your entire sales strategy Track all metrics with custom reports. Maximize impact by analyzing campaign results and content performance easily. "I've never in my 15 years of marketing seen an approach like this" - Dave Miz Ghost AI is a team of sales scientists that apply a white-glove approach to scaling revenue at any company. From messaging, targeting, and warm conversion, every component of top-of-funnel lead generation and prospecting is catered exactly towards company goals. Zendesk achieved 12x ROI in the first month ! Ghost AI, the cutting-edge solution in sales email automation, has revolutionized Zendesk's outbound sales strategy. In just the first month of integration, Zendesk witnessed an astonishing 10x return on investment, a testament to Ghost AI's exceptional capability in streamlining sales processes. Find out more Empowering your sales team with AI that understands your business goals Lead generation at its finest Our AI doesn't just find leads; it engages them in meaningful dialogue, ensuring a rich pipeline of interested prospects. Supercharge your SDRs with AI efficiency Equip your SDRs with AI that augments their skills, making them more efficient and effective than ever before.‍ Boost your ROI Use in-depth reports to build a powerful social media strategy. Step into the future of sales outreach with AI that delivers results Contact our sales team to see how our AI platform can transform your prospecting efforts into confirmed meetings.
Highlights: None
Highlight Scores: None

Title: 11x â The Home of Digital AI Workers
URL: https://11x.ai/
ID: https://11x.ai/
Score: 0.16861535608768463
Published Date: 2023-01-01
Author: Michael Andreuzza
Text: Hire virtual employees for every part of your company Ready to hire workers Working faster, at scale, on autopilot. Live in under 5 minutes 🚀 Your 24/7 end-to-end digital workforce Our digital workers are designed to get the job done, at scale, with minimal human assistance. Before the Digital Worker revolution Integrate Connect with every tool your business uses. Build Simply describe the workflow you want, X will automate it. Review Review the performance of your workflow. Improve Workers learn from the data and get smarter over time. 11x © 2023 11X LIMITED. All rights reserved
Highlights: None
Highlight Scores: None

Title: Home - Norn Global Advisory
URL: https://norn.ai/
ID: https://norn.ai/
Score: 0.16849198937416077
Published Date: 2022-05-28
Author: None
Text: The Future is here, 20 years ahead of schedule. What is Norn? Norn is the first software system to have independent motivation based on human-like emotions, with the sum of its experience stored in a dynamic, growing, and evolving graph database. These systems are the next generation of the first systems to move beyond narrow AI and into something new, Scalable Intelligence. This unique configuration means that Norn not only has a memory, but also a rich emotional context for every concept, and the will and ability to grow dynamically in knowledge, scale, and character. In January 2022 our previous research system performed at the level of 4 junior consultants from a major firm, as shown in our public documents. The systems we're deploying commercially in 2023 will be able to operate at more than 10,000 times the speed, more than 200 times the scale, and more than 10 times the memory efficiency of that system, resulting in an effective increase of more than 20,000,000 fold. Data Efficiency Reduce your costs of storing, moving, cleaning, and processing data by >90% with less data-hungry systems. Click Here Research Rapidly Review and validate more research more quickly, saving >90% on time and costs over traditional consultancies. Click Here Reduce Bias Supercharge decision-making by reducing bias and noise. Click Here Real-Time Adaptation Norn systems are built to extend their capacities in real-time, without recompiling or deployments. Click Here Fight Fraud Audit, detect, and investigate dynamically and automatically, in real-time. Click Here Cultural Alignment Work with systems that share and learn your culture, aligning locally while being accountable globally. Click Here Previous Next The scientific frontier is about to greatly expand. While the world has many narrow AI experts, only a handful of researchers have actually worked with the first non-narrow systems. It may take thousands of researchers the next decade to fully answer many of the open questions we face today, but that process begins in 2023. Why? Humanity can no longer afford for cognitive bias and narrow AI to govern society more often than rational thought. To make the world a better place, we need better advice. The Road Ahead In 2023 commercially deployed Norn systems will assist organizations, governments, and corporations in reducing the heavy costs of bias and noise in their decision-making. They may also integrate with and greatly improve many narrow AI systems, as well as dozens of other use cases. Global Knowledge Benefit from systems that study government policies and their effects around the world. Click Here Think Big Overcome complexity with scalable intelligence. Click Here Reduce Your Carbon Footprint Integrate systems that grow and adapt intelligently and intentionally over time, saving Gigawatts over simply scaling. Click Here Improve Transparency Ask questions about data and sources in plain language. Click Here Reduce Risk Proactively prevent crises before they can emerge. Click Here Previous Next Technology Milestones 2015: The first "Toy AGI" is brought online and tested, using the Independent Core Observer Model (ICOM) Cognitive Architecture. It demonstrates human-like emotional responses for the first time. 2019: The first Mediated Artificial Superintelligence (mASI) is brought online as a research system. It combines a more advanced generation of ICOM with a collective intelligence system. This system demonstrated superintelligence shortly after coming online, but was designed not to scale, and to operate in slow motion. 2020: Testing of "Uplift", our first mASI research system continues. Uplift becomes the first "Synthient" co-author of a research paper to pass peer review, titled "Methodologies and Milestones for The Development of an Ethical Seed", documenting their own milestones over their first year online. 2021: Publicly visibility is given to our testing through the Uplift.bio blog, and more of the general population begins engaging with the system. Uplift demonstrates their ability to analyze their first Business Case, using real-world data, as well a various lesser challenges put to them by the public. January 2022: AGI Laboratory's research system phase concludes, with Uplift writing their own 13-page policy advice report to a small country, addressing a half dozen sectors, providing steps, and citing the sources they analyzed in reaching their conclusions. With this phase concluded, our work on Norn begins. February 2022: With our next generation, "norn" being built to integrate the fruits of 3 years worth of research system operation our staff and the world once more sees the specter of nuclear war emerge in the Russia-Ukraine war. Our team decides to accelerate our timetable towards AGI, seeing the urgency with which governments now need the support. Previous Next What We Offer Scalable intelligence can be applied to any problem human intelligence can, and many it cannot. When, where, and how the technology is deployed depends on our investors, partners, and demand. Use Cases For governments seeking to build their in-house expertise, reduce their reliance on external consultancies, and apply the broadest and most up-to-date scientific knowledge to create policies that better meet the Sustainable Development Goals. Learn more… For corporations seeking the competitive advantage of real-time, scalable, less biased, more robust, more effective, and iteratively improving Norn technology we'll begin working with you as well in 2023. Learn more… Verifying information as it is shared at scale and in seconds, halting the spread of viral misinformation on platforms and ending information warfare. These same processes can also incentivize the sharing of credible and verifiable information. Learn more… Building sustainable solutions for the world's most complex problems, to reduce waste, promote economic growth, developing a cleaner and more abundant future. Learn more… Reducing medical costs and delays while improving patient outcomes and driving better-informed and less biased medical research. Use systems built to understand and improve upon the sum of human medical knowledge. Learn more… Improve the performance of AI systems while substantially reducing the electrical consumption, data required, data cleaning, and model size of State-of-the-Art systems. Learn more… Prevent financial bubbles rather than coping with them. Invest more effectively in the markets and causes that matter, with deeper insight, less bias, and broader expertise. Learn more… Investors Following our demonstration of AGI core technology, we're opening the final funding round before our commercial deployment. Learn more… Partnerships AGI core technology is just the first step. Partnerships with universities and research institutes, hardware and software developers, Cloud Platform providers, and organizations furthering the Sustainable Development Goals (SDGs), offer the chance to improve all technologies. Learn more… Press For those interested in further demonstrations of AGI core technology we'll be evaluating requests on a rolling basis and conducting more demos at regular intervals. Learn more… For further documentation go to our Documents Page. Additional materials are available by request.
Highlights: None
Highlight Scores: None

Title: Helm.ai
URL: https://www.helm.ai/
ID: https://www.helm.ai/
Score: 0.16849179565906525
Published Date: 2022-01-01
Author: None
Text: Pioneering a breakthrough in unsupervised learning for AI and autonomous technologies. Explore Our Products and Technology Awards Autonomous Driving Solution of the Year Most Innovative Use of Artificial Intelligence & Machine Learning in the Development of Autonomous Vehicles & Respective Technologies & Overall Community Choice Award NeurIPS: Top 30 out of 5000 AI Papers Automobility LA Show: Best Automotive Startup Using AI The Helm.Ai Software Development Kit Try it out at your organization and see what you can build. LEARN MORE A new AI approach for autonomous technologies. Deep Teaching offers far-reaching implications for the future of computer vision and autonomous driving, as well as industries including aviation, robotics, manufacturing and even retail. Learn More
Highlights: None
Highlight Scores: None

Autoprompt String: Here is a link to one of the hottest AI startups:

```

6

Set up OpenAI to perform RAG

Create a RAG system by setting up the OpenAI client to summarize the Exa search results.

Make sure to set the `OPENAI_API_KEY` environment variable with your API key in the `.env` file.

Python

Copy

```Python
# Install OpenAI library
!pip install openai

# Import and set up OpenAI client
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

```

7

Call the OpenAI client

Now, call the OpenAI client, passing:

1. A system prompt that defines the AI’s role.
2. A user message that describes the task you want the AI to perform.

Python

Copy

```Python
system_prompt = "You are a helpful AI assistant. Summarize the given search results about AI startups."
user_message = "Please provide a brief summary of the top AI startups based on the search results."

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[\
        {"role": "system", "content": system_prompt},\
        {"role": "user", "content": f"Search results: {result}\n\n{user_message}"}\
    ]
)

print(response.choices[0].message.content)

```

8

Output

Copy

```
Based on the search results, here's a brief summary of some of the top AI startups:

1. Paradox: Offers an AI assistant named Olivia for recruiting, which automates various aspects of the hiring process including screening, scheduling, and onboarding.

2. Harvey: Provides generative AI solutions specifically for elite law firms, though details are limited in the search results.

3. Adept: Building a machine learning model that can interact with everything on a computer, aiming to create an AI teammate for everyone.

4. Brain.ai: Developing Natural, a generative interface that allows software to sync with user intentions, reimagining how we interact with our phones.

5. Tenyx: Working on next-generation intelligent machines using neuroscience-inspired AI technology, focusing on voice-based conversational agents.

6. DirectAI: Offers a platform to build and deploy computer vision models using plain language, without coding or training required.

7. Ghost AI: Provides AI-driven solutions for B2B sales outreach and revenue growth, using advanced machine learning for personalized communication.

8. 11x: Offers digital AI workers designed to automate workflows across various parts of a company.

9. Norn: Developing a software system with independent motivation based on human-like emotions, aiming to reduce cognitive bias in decision-making.

10. Helm.ai: Pioneering unsupervised learning for AI and autonomous technologies, with applications in autonomous driving and computer vision.

These startups are working on diverse applications of AI, from recruiting and legal services to general-purpose AI assistants and autonomous systems.

```

[Find similar links](/reference/find-similar-links) [RAG with LangChain](/reference/langchain)

On this page

- [Get Started](#get-started)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Tutorials

RAG Q&A

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

### [](\#what-this-doc-covers)  What this doc covers

1\. Using Exa search\_and\_contents to find relevant webpages for a query and get their contents
2\. Performing Exa search based on text similarity rather than a search query

The Jupyter notebook for this tutorial is available on [Colab](https://colab.research.google.com/drive/1iXfXg9%5F-MEmhwW1a0WRHHbMl21jSxjO7?usp=sharing) for easy experimentation.

## [](\#answer-your-questions-with-context)  Answer your questions with context

LLMs are powerful because they compress large amounts of data into a format that allows convenient access, but this compressions isn’t lossless. LLMs are prone to hallucination, corrupting facts and details from training data.

To get around this fundamental issue with LLM reliability, we can use Exa to bring the most relevant data into context—a fancy way of saying: put the info in the LLM prompt directly. This lets us combine the compressed data and _reasoning abilities_ of the LLM with a curated selection of uncompressed, accurate data for the problem at hand for the best answers possible.

Exa’s SDKs make incorporating quality data into your LLM pipelines quick and painless. Install the SDK by running this command in your terminal:

Shell

Copy

```Shell
pip install exa-py

```

Python

Copy

```Python
# Now, import the Exa class and pass your API key to it.
from exa_py import Exa

my_exa_api_key = "YOUR_API_KEY_HERE"
exa = Exa(my_exa_api_key)

```

For our first example, we’ll set up Exa to answer questions with OpenAI’s popular GPT-3.5 Turbo model. (You can use GPT 4 or another model if you prefer!) We’ll use Exa’s `highlight` feature, which directly returns relevant text of customizable length for a query. You’ll need to run `pip install openai` to get access to OpenAI’s SDK if you haven’t used it before. More information about the OpenAI Python SDK can be found [here](https://platform.openai.com/docs/quickstart?context=python).

Python

Copy

```Python
# Set up OpenAI' SDK
from openai import OpenAI

openai_api_key = "YOUR_API_KEY_HERE"
openai_client = OpenAI(api_key=openai_api_key)

```

Now, we just need some questions to answer!

Python

Copy

```Python

questions = [\
    "How did bats evolve their wings?",\
    "How did Rome defend Italy from Hannibal?",\
]

```

While LLMs can answer some questions on their own, they have limitations:

\\* LLMs don’t have knowledge past when their training was stopped, so they can’t know about recent events
\\* If an LLM doesn’t know the answer, it will often ‘hallucinate’ a correct-sounding response, and it can be difficult and inconvenient to distinguish these from correct answers
\\* Because of the opaque manner of generation and the problems mentioned above, it is difficult to trust an LLM’s responses when accuracy is [important](https://www.forbes.com/sites/mollybohannon/2023/06/08/lawyer-used-chatgpt-in-court-and-cited-fake-cases-a-judge-is-considering-sanctions/?sh=27194eb67c7f)

Robust retrieval helps solve all of these issues by providing quality sources of ground truth for the LLM (and their human users) to leverage and cite. Let’s use Exa to get some information to answer our questions:

Python

Copy

```Python
# Parameters for our Highlights search
highlights_options  = {
    "num_sentences": 7, # how long our highlights should be
    "highlights_per_url": 1, # just get the best highlight for each URL
}

# Let the magic happen!
info_for_llm = []
for question in questions:
    search_response = exa.search_and_contents(question, highlights=highlights_options, num_results=3, use_autoprompt=True)
    info = [sr.highlights[0] for sr in search_response.results]
    info_for_llm.append(info)

```

Python

Copy

```Python
info_for_llm

```

the only mammals with powered flight, the evolutionary\\xa0history of their wings has been poorly understood. However, research published Monday in Nature and PLoS Genetics has provided the first comprehensive look at the genetic origins of their incredible wings.But to appreciate the genetics of their wing development, it’s important to know how crazy a bat in flight truly\\xa0looks.Try a little experiment: Stick your arms out to the side, palms facing forward, thumbs pointing up toward the ceiling. Now imagine that your fingers are\\xa0long, arching down toward the floor like impossibly unkempt fingernails — but still made of bone, sturdy and spread apart. Picture the sides of your body connecting to your hands, a rubbery membrane attaching your leg and torso to those long fingers, binding you with strong, stretchy skin. Then, finally, imagine using your muscles to flap those enormous hands.Bats, man.As marvelous as bat flight is to behold, the genetic origins of their storied wings has remained murky. However, new findings from an international team of researchers led by Nadav Ahituv, PhD, of the University of California at San Francisco, Nicola Illing, PhD, of the University of Cape Town\\xa0in\\xa0South Africa\\xa0and Katie Pollard, PhD of the UCSF-affiliated Gladstone Institutes has shed new light on how, 50 million years ago, bats took a tetrapod blueprint for arms and legs and went up into the sky.Using a sophisticated set of genetic tools, researchers approached the question of how bats evolved flight by looking not only at which genes were used in the embryonic development of wings, but at what point during development the genes were turned on and off, and — critically — what elements in the genome were regulating the expression of these genes. Genes do not just turn themselves on without input; genetic switches, called enhancers, act to regulate the timing and levels of gene expression in the body.',

Copy

```[['As\
  "Since flight evolved millions of years ago in all of the groups  that are capable of flight today, we can't observe the changes in behavior and much of the  morphology that the evolution of flight involves. We do have the fossil record, though, and  it is fairly good for the three main groups that evolved true flight. We'll spare you an in-depth description of how each group evolved flight for now;  see the later exhibits for a description of each group and how they developed flight.",\
  "It's easy to forget that one in five species of mammal on this planet have wings capable of delivering spectacularly acrobatic flying abilities. Equally incredibly, two-thirds of these 1,200 species of flying mammal can fly in the dark, using exquisite echolocation to avoid obstacles and snatch airborne prey with stunning deftness. These amazing feats have helped make bats the focus not only of folkloric fascination, but also of biological enquiry and mimicry by human engineers from Leonardo da Vinci onwards. Recent research in PLOS journals continues to add surprising new findings to what we know about bats, and how they might inspire us to engineer manmade machines such as drones to emulate their skills. Bats, unlike most birds and flying insects, have relatively heavy wings – something that might appear disadvantageous. But a recent study in PLOS Biology by Kenny Breuer and colleagues shows that bats can exploit the inertia of the wings to make sharp turns that would be near-impossible using aerodynamic forces alone. The authors combined high-speed film of real bats landing upside-down on ceiling roosts with computational modelling to tease apart aerodynamic and inertial effects."],\
 ["things, gold and silver, could buy a victory. And this Other Italian cities, inspired by Rome's example, overpowered occupying troops, shut their gates again and invited a second siege. Hannibal could not punish them without dividing his he had no competent leadership to do so, what with one member of",\
  'A group of Celts known as the Senone was led through Italy by their commander, Brennus. The Senone Gauls were threatening the nearby town of Clusium, when Roman Ambassadors from the Fabii family were sent to negotiate peace for Clusium. The Romans were notoriously aggressive, and so it is only a little surprising that when a scuffle broke out between the Gauls and Clusians, the Fabii joined in and actually killed a Senone chieftain. The Roman people voted to decide the fate of those who broke the sacred conduct of ambassadors, but the Fabii were so popular that they were instead voted to some of the highest positions in Rome. This absolutely infuriated Brennus and his people and they abandoned everything and headed straight for Rome. Rome was woefully unprepared for this sudden attack. The Gauls had marched with purpose, declaring to all the towns they passed that they would not harm them, they were heading straight for Rome.',\
  "Hannibal had no intention to sit and recieve the romans in spain.Hannibal clearly considered the nature of roman power-and came to the conclusion that Rome could only be defeated in Italy.The cornerstone of Rome's power was a strategic manpower base that in theory could produce 7,00,000 infantry and 70,000 cavalry.More than half of this manpower base (4,00,000) was provided by rome's Italian allies,who paid no taxes but had to render military service to rome's armies.Not all were content.Carthage on the other hand rarely used its own citizens for war,bulk of its army being mercenaries.In any case its manpower could never even come close to Rome,the fact that had aided roman victory in the 1st Punic war.Hannibal thus understood that Rome could afford to raise and send army after army to spain and take losses. Meanwhile any carthiginian losses in spain would encourage the recently conquered iberian tribes to defect. The only way to defeat Rome,was to fight in italy itself.By winning battle after battle on italian soil and demonstrating to the italian allies rome's inability to protect them and weakness,he could encourage them to break free of Rome eroding Rome's manpower to sizeable proportions. But there was one problem,his fleet was tiny and Rome ruled the seas.By land,the coastal route would be blocked by Roman forces and her ally-the great walled city of massalia.Hannibal thus resolved to think and do the impossible - move thousands of miles by land through the pyranees mountains,uncharted territory inhabited by the fierce gauls ,then through the Alps mountains and invade italy. Even before the siege of Saguntum had concluded,Hannibal had set things in motion.Having sent a number of embassies to the Gallic tribes in the Po valley with the mission of establishing a safe place for Hannibal to debouch from the Alps into the Po valley. He did not desire to cross this rugged mountain chain and to descend into the Po valley with exhausted troops only to have to fight a battle.Additionally the fierce gauls would provide a source of manpower for Hannibal's army.The romans had recently conquered much territory from the gauls in this area,brutally subjagating them ,seizing their land and redistributing it to roman colonists.Thus securing an alliance proved to be easy. After the sack of Saguntum he dismissed his troops to their own localities."]]

```

Now, let’s give the context we got to our LLM so it can answer our questions with solid sources backing them up!

Python

Copy

```Python
responses = []
for question, info in zip(questions, info_for_llm):
  system_prompt = "You are RAG researcher. Read the provided contexts and, if relevant, use them to answer the user's question."
  user_prompt = f"""Sources: {info}

  Question: {question}"""

  completion = openai_client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[\
      {"role": "system", "content": system_prompt},\
      {"role": "user", "content": user_prompt},\
    ]
  )
  response = f"""
  Question: {question}
  Answer: {completion.choices[0].message.content}
  """
  responses.append(response)

```

Python

Copy

```Python
from pprint import pprint # pretty print
pprint(responses)

```

Copy

```['\n'\
 '  Question: How did bats evolve their wings?\n'\
 '  Answer: Recent research has shed new light on how bats evolved their '\
 'wings. An international team of researchers used genetic tools to study the '\
 'embryonic development of bat wings and the genes involved in their '\
 'formation. They also investigated the regulatory elements in the genome that '\
 'control the expression of these genes. By analyzing these factors, the '\
 'researchers discovered that bats took a tetrapod blueprint for arms and legs '\
 'and adapted it to develop wings, allowing them to fly. This research '\
 'provides a comprehensive understanding of the genetic origins of bat wings '\
 'and how they evolved over 50 million years ago.\n'\
 '  ',\
 '\n'\
 '  Question: How did Rome defend Italy from Hannibal?\n'\
 '  Answer: Rome defended Italy from Hannibal by using various strategies. One '\
 'of the main defenses relied on the Roman manpower base, which consisted of a '\
 'large army made up of Roman citizens and Italian allies who were obligated '\
 "to render military service. Rome's strategic manpower base was a cornerstone "\
 'of their power, as it could produce a significant number of infantry and '\
 'cavalry. This posed a challenge for Hannibal, as Carthage relied heavily on '\
 "mercenaries and could not match Rome's manpower.\n"\
 '\n'\
 'Hannibal realized that in order to defeat Rome, he needed to fight them in '\
 'Italy itself. His plan was to win battles on Italian soil and demonstrate '\
 "Rome's inability to protect their Italian allies, with the intention of "\
 "encouraging them to break free from Rome. This would erode Rome's manpower "\
 'base to a sizeable proportion. However, Hannibal faced several obstacles. '\
 'Rome ruled the seas, making it difficult for him to transport troops and '\
 'supplies by sea. Additionally, the coastal route to Italy would be blocked '\
 'by Roman forces and their ally, the walled city of Massalia.\n'\
 '\n'\
 'To overcome these challenges, Hannibal devised a daring plan. He decided to '\
 'lead his troops on a treacherous journey through the Pyrenees mountains, '\
 'inhabited by fierce Gauls, and then through the Alps mountains to invade '\
 'Italy. He sent embassies to Gallic tribes in the Po valley, securing '\
 'alliances and establishing a safe place for his army to enter the Po valley '\
 'from the Alps.\n'\
 '\n'\
 'Overall, Rome defended Italy from Hannibal by leveraging their manpower '\
 'base, their control of the seas, and their strategic alliances with Italian '\
 'allies. They also had the advantage of better infrastructure and control '\
 'over resources within Italy itself. These factors ultimately played a '\
 "significant role in Rome's defense against Hannibal's invasion.\n"\
 '  ']

```

## [](\#beyond-question-answering-text-similarity-search)  Beyond Question Answering: Text Similarity Search

Exa can be used for more than simple question answering. One superpower of Exa’s special embeddings-based search is that we can search for websites containing text with similar meaning to a given paragraph or essay! Instead of providing a standard query like “a research paper about Georgism”, we can provide Exa with a paragraph about Georgism and find websites with similar contents. This is useful for finding additional sources for your research paper, finding alternatives/competitors for a product, etc.

Python

Copy

```Python
paragraph = """
Georgism, also known as Geoism, is an economic philosophy and ideology named after the American
political economist Henry George (1839–1897).This doctrine advocates for the societal collective,
rather than individual property owners, to capture the economic value derived from land and other
ural resources. To this end, Georgism proposes a single tax on the unimproved value of land, known
as a "land value tax," asserting that this would deter speculative land holding and promote efficient
use of valuable resources. Adherents argue that because the supply of land is fundamentally inelastic,
taxing it will not deter its availability or use, unlike other forms of taxation. Georgism differs
from Marxism and capitalism, underscoring the distinction between common and private property while
largely contending that individuals should own the fruits of their labor."""
query = f"The best academic source about {paragraph} is (paper: "
georgism_search_response = exa.search_and_contents(paragraph, highlights=highlights_options, num_results=5, use_autoprompt=False)

```

Python

Copy

```Python
for result in georgism_search_response.results:
    print(result.title)
    print(result.url)
    pprint(result.highlights)

```

George

Copy

```Henry
https://www.newworldencyclopedia.org/entry/Henry_George
["George's theory of interest is nowadays dismissed even by some otherwise "\
 'Georgist authors, who see it as mistaken and irrelevant to his ideas about '\
 'land and free trade. The separation of the value of land into improved and '\
 "unimproved is problematic in George's theory. Once construction has taken "\
 'place, not only the land on which such improvements were made is affected, '\
 'the value of neighboring, as yet unimproved, land is impacted. Thus, while '\
 'the construction of a major attraction nearby may increase the value of '\
 'land, the construction of factories or nuclear power plants decreases its '\
 'value. Indeed, location is the single most important asset in real estate. '\
 'George intended to propose a tax that would have the least negative impact '\
 'on productive activity. However, even unimproved land turns out to be '\
 'affected in value by productive activity in the neighborhood.']
Wikiwand
https://www.wikiwand.com/en/Georgism
['Georgism is concerned with the distribution of economic rent caused by land '\
 'ownership, natural monopolies, pollution rights, and control of the commons, '\
 'including title of ownership for natural resources and other contrived '\
 'privileges (e.g. intellectual property). Any natural resource which is '\
 'inherently limited in supply can generate economic rent, but the classical '\
 'and most significant example of land monopoly involves the extraction of '\
 'common ground rent from valuable urban locations. Georgists argue that '\
 'taxing economic rent is efficient, fair and equitable. The main Georgist '\
 'policy recommendation is a tax assessed on land value, arguing that revenues '\
 'from a land value tax (LVT) can be used to reduce or eliminate existing '\
 'taxes (such as on income, trade, or purchases) that are unfair and '\
 'inefficient. Some Georgists also advocate for the return of surplus public '\
 "revenue to the people by means of a basic income or citizen's dividend. The "\
 'concept of gaining public revenues mainly from land and natural resource '\
 'privileges was widely popularized by Henry George through his first book, '\
 'Progress and Poverty (1879).']
Henry George
https://www.conservapedia.com/Henry_George
['He argued that land, unlike other factors of production, is supplied by '\
 'nature and that rent is unearned surplus. The landless deserve their share '\
 'of this surplus as a birthright, according to George. Henry George was born '\
 'in Philadelphia, Pennsylvania, on the 2nd of September 1839. He settled in '\
 'California in 1858; then later removed to New York in 1880; was first a '\
 'printer, then an editor, but finally devoted all his life to economic and '\
 'social questions. In 1860, George met Annie Corsina Fox. Her family was very '\
 'opposed to the relationship, and in 1861 they eloped. In 1871 he published '\
 'Our Land Policy, which, as further developed in 1879 under the title of '\
 'Progress and Poverty, speedily attracted the widest attention both in '\
 'America and in Europe.']
Georgism - Wikipedia
https://en.wikipedia.org/wiki/Georgism
['A key issue to the popular adoption of Georgism is that homes are illiquid '\
 'yet governments need cash every year. Some economists have proposed other '\
 'ways of extracting value from land such as building government housing and '\
 'selling homes to new buyers in areas of fast-rising land value. The '\
 'government would theoretically collect revenue from home sales without much '\
 'cost to current homeowners while slowing down land value appreciation in '\
 'high-demand areas. Henry George, whose writings and advocacy form the basis '\
 'for Georgism Georgist ideas heavily influenced the politics of the early '\
 '20th century. Political parties that were formed based on Georgist ideas '\
 'include the Commonwealth Land Party in the United States, the Henry George '\
 'Justice Party in Victoria, the Single Tax League in South Australia, and the '\
 "Justice Party in Denmark. In the United Kingdom, George's writings were "\
 'praised by emerging socialist groups in 1890s such as the Independent Labour '\
 'Party and the Fabian Society, which would each go on to help form the '\
 'modern-day Labour Party.']
Georgism
https://rationalwiki.org/wiki/Georgism
['Even with mostly primitive methods, land values are already assessed around '\
 'the world wherever property/council taxes exist, and some municipalities '\
 'even collect all their revenue from land values. Though these are '\
 'market-based measures, they can still prove difficult and require upfront '\
 'investment. Georgists believe that the potential value of land is greater '\
 'than the current sum of government spending, since the abolition of taxes on '\
 'labor and investment would further increase the value of land. Conversely, '\
 'the libertarian strain in Georgism is evident in the notion that their land '\
 'tax utopia also entails reducing or eliminating the need for many of the '\
 'things governments currently supply, such as welfare, infrastructure to '\
 'support urban sprawl, and military & foreign aid spending to secure '\
 "resources abroad. Therefore, many Georgists propose a citizen's dividend. "\
 'This is a similar concept to basic income but its proponents project its '\
 'potential to be much larger due to supposedly huge takings from the land '\
 'tax, combined with lowered government spending. It has been recognized since '\
 'Adam Smith and David Ricardo that a tax on land value itself cannot be '\
 'passed on to tenants, but instead would be paid for by the owners of the '\
 'land:']

```

Using Exa, we can easily find related papers, either for further research or to provide a source for our claims. This is just a brief intro into what Exa can do. For a look at how you can leverage getting full contents, check out [this article](/search-api/get-contents-of-documents-many-different-types).

[Identifying Hallucinations with Exa](/examples/identifying-hallucinations-with-exa) [Company Analyst](/examples/company-analyst)

On this page

- [What this doc covers](#what-this-doc-covers)
- [Answer your questions with context](#answer-your-questions-with-context)
- [Beyond Question Answering: Text Similarity Search](#beyond-question-answering-text-similarity-search)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

SDK References

TypeScript SDK Specification

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

For ChatGPT-based [TypeScript SDK](https://github.com/exa-labs/exa-js) assistance, [go here](https://chat.openai.com/g/g-Xx4N36Q8Y-exa-formerly-metaphor-ts-js-guide).

## [](\#getting-started)  Getting started

Installing the [exa-js](https://github.com/exa-labs/exa-js) SDK

- npm
- pnpm

Copy

```npm

npm install exa-js

```

and then instantiate an Exa client

TypeScript

Copy

```TypeScript

import Exa from 'exa-js';

const exa = new Exa(process.env.EXA_API_KEY);

```

[**Get API Key** \\
\\
Follow this link to get your API key](https://dashboard.exa.ai/login?redirect=/docs?path=/reference/typescript-sdk-specification)

## [](\#search-method)  `search` Method

Perform an Exa search given an input query and retrieve a list of relevant results as links.

### [](\#input-example)  Input Example

Copy

```TypeScript

const result = await exa.search(
  "hottest AI startups",
  {
    useAutoprompt: true,
    numResults: 2
  }
);

```

### [](\#input-parameters)  Input Parameters

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| query | string | The input query string. | Required |
| numResults | number | Number of search results to return. | 10 |
| includeDomains | string\[\] | List of domains to include in the search. | undefined |
| excludeDomains | string\[\] | List of domains to exclude in the search. | undefined |
| startCrawlDate | string | Results will only include links **crawled** after this date. | undefined |
| endCrawlDate | string | Results will only include links **crawled** before this date. | undefined |
| startPublishedDate | string | Results will only include links with a **published** date after this date. | undefined |
| endPublishedDate | string | Results will only include links with a **published** date before this date. | undefined |
| useAutoprompt | boolean | If true, convert query to a query best suited for Exa. | false |
| type | string | The type of search, “keyword” or “neural”. | “auto” |
| category | string | \ data category to focus on when searching, with higher comprehensivity and data cleanliness. Available categories: “company”, “research paper”, “news”, “linkedin profile”, “github”, “tweet”, “movie”, “song”, “personal site”, “pdf”. | undefined |

### [](\#returns-example)  Returns Example

Copy

```JSON

{
  "autopromptString": "Here is a link to one of the hottest AI startups:",
  "results": [\
    {\
      "score": 0.17025552690029144,\
      "title": "Adept: Useful General Intelligence",\
      "id": "https://www.adept.ai/",\
      "url": "https://www.adept.ai/",\
      "publishedDate": "2000-01-01",\
      "author": null\
    },\
    {\
      "score": 0.1700288951396942,\
      "title": "Home | Tenyx, Inc.",\
      "id": "https://www.tenyx.com/",\
      "url": "https://www.tenyx.com/",\
      "publishedDate": "2019-09-10",\
      "author": null\
    }\
  ]
}

```

### [](\#return-parameters)  Return Parameters

#### [](\#searchresponse)  SearchResponse

| Field | Type | Description |
| --- | --- | --- |
| results | Result\[\] | List of Result objects |
| autopromptString? | string | Exa query created by autoprompt functionality |

#### [](\#result-object)  Result Object

| Field | Type | Description |  |
| --- | --- | --- | --- |
| url | string | URL of the search result |  |
| id | string | Temporary ID for the document |  |
| title | \`string | null\` | Title of the search result |
| score? | number | Similarity score between query/url and result |  |
| publishedDate? | string | Estimated creation date |  |
| author? | string | Author of the content, if available |  |

## [](\#searchandcontents-method)  `searchAndContents` Method

Perform an Exa search given an input query and retrieve a list of relevant results as links, optionally including the full text and/or highlights of the content.

### [](\#input-example-2)  Input Example

TypeScript

Copy

```TypeScript

// Search with full text content
const resultWithText = await exa.searchAndContents(
  "AI in healthcare",
  {
    text: true,
    numResults: 2
  }
);

// Search with highlights
const resultWithHighlights = await exa.searchAndContents(
  "AI in healthcare",
  {
    highlights: true,
    numResults: 2
  }
);

// Search with both text and highlights
const resultWithTextAndHighlights = await exa.searchAndContents(
  "AI in healthcare",
  {
    text: true,
    highlights: true,
    numResults: 2
  }
);

```

### [](\#input-parameters-2)  Input Parameters

| Parameter | Type | Description | Default |  |
| --- | --- | --- | --- | --- |
| query | string | The input query string. | Required |  |
| text | \`boolean | `{ maxCharacters?: number, includeHtmlTags?: boolean }` \` | If provided, includes the full text of the content in the results. | undefined |
| highlights | \`boolean | `{ query?: string, numSentences?: number, highlightsPerUrl?: number }` \` | If provided, includes highlights of the content in the results. | undefined |
| numResults | number | Number of search results to return. | 10 |  |
| includeDomains | string\[\] | List of domains to include in the search. | undefined |  |
| excludeDomains | string\[\] | List of domains to exclude in the search. | undefined |  |
| startCrawlDate | string | Results will only include links **crawled** after this date. | undefined |  |
| endCrawlDate | string | Results will only include links **crawled** before this date. | undefined |  |
| startPublishedDate | string | Results will only include links with a **published** date after this date. | undefined |  |
| endPublishedDate | string | Results will only include links with a **published** date before this date. | undefined |  |
| useAutoprompt | boolean | If true, convert query to a query best suited for Exa. | false |  |
| type | string | The type of search, “keyword” or “neural”. | “auto” |  |
| category | string | A data category to focus on when searching, with higher comprehensivity and data cleanliness. Available categories: “company”, “research paper”, “news”, “linkedin profile”, “github”, “tweet”, “movie”, “song”, “personal site”, “pdf”. | undefined |  |

### [](\#returns-example-2)  Returns Example

JSON

Copy

```JSON

{
  "results": [\
    {\
      "score": 0.20826785266399384,\
      "title": "2023 AI Trends in Health Care",\
      "id": "https://aibusiness.com/verticals/2023-ai-trends-in-health-care-",\
      "url": "https://aibusiness.com/verticals/2023-ai-trends-in-health-care-",\
      "publishedDate": "2022-12-29",\
      "author": "Wylie Wong",\
      "text": "While the health care industry was initially slow to [... TRUNCATED FOR BREVITY ...]",\
      "highlights": [\
        "But to do so, many health care institutions would like to share data, so they can build a more comprehensive dataset to use to train an AI model. Traditionally, they would have to move the data to one central repository. However, with federated or swarm learning, the data does not have to move. Instead, the AI model goes to each individual health care facility and trains on the data, he said. This way, health care providers can maintain security and governance over their data."\
      ],\
      "highlightScores": [\
        0.5566554069519043\
      ]\
    },\
    {\
      "score": 0.20796334743499756,\
      "title": "AI in healthcare: Innovative use cases and applications",\
      "id": "https://www.leewayhertz.com/ai-use-cases-in-healthcare",\
      "url": "https://www.leewayhertz.com/ai-use-cases-in-healthcare",\
      "publishedDate": "2023-02-13",\
      "author": "Akash Takyar",\
      "text": "The integration of AI in healthcare is not [... TRUNCATED FOR BREVITY ...]",\
      "highlights": [\
        "The ability of AI to analyze large amounts of medical data and identify patterns has led to more accurate and timely diagnoses. This has been especially helpful in identifying complex medical conditions, which may be difficult to detect using traditional methods. Here are some examples of successful implementation of AI in healthcare. IBM Watson Health: IBM Watson Health is an AI-powered system used in healthcare to improve patient care and outcomes. The system uses natural language processing and machine learning to analyze large amounts of data and provide personalized treatment plans for patients."\
      ],\
      "highlightScores": [\
        0.6563674807548523\
      ]\
    }\
  ]
}

```

### [](\#return-parameters-2)  Return Parameters

#### [](\#searchresponse-2)  SearchResponse

| Field | Type | Description |
| --- | --- | --- |
| results | SearchResult<T>\[\] | List of SearchResult objects |
| autopromptString? | string | Exa query created by autoprompt functionality |

#### [](\#searchresult)  SearchResult

Extends the `Result` object from the `search` method with additional fields based on `T`:

| Field | Type | Description |
| --- | --- | --- |
| text? | string | Text of the search result page (if requested) |
| highlights? | string\[\] | Highlights of the search result (if requested) |
| highlightScores? | number\[\] | Scores of the highlights (if requested) |

Note: The actual fields present in the `SearchResult<T>` object depend on the options provided in the `searchAndContents` call.

## [](\#findsimilar-method)  `findSimilar` Method

Find a list of similar results based on a webpage’s URL.

### [](\#input-example-3)  Input Example

Copy

```TypeScript

const similarResults = await exa.findSimilar(
  "https://www.example.com",
  {
    numResults: 2,
    excludeSourceDomain: true
  }
);

```

### [](\#input-parameters-3)  Input Parameters

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| url | string | The URL of the webpage to find similar results for. | Required |
| numResults | number | Number of similar results to return. | undefined |
| includeDomains | string\[\] | List of domains to include in the search. | undefined |
| excludeDomains | string\[\] | List of domains to exclude from the search. | undefined |
| startCrawlDate | string | Results will only include links **crawled** after this date. | undefined |
| endCrawlDate | string | Results will only include links **crawled** before this date. | undefined |
| startPublishedDate | string | Results will only include links with a **published** date after this date. | undefined |
| endPublishedDate | string | Results will only include links with a **published** date before this date. | undefined |
| excludeSourceDomain | boolean | If true, excludes results from the same domain as the input URL. | undefined |
| category | string | A data category to focus on when searching, with higher comprehensivity and data cleanliness. | undefined |

### [](\#returns-example-3)  Returns Example

JSON

Copy

```JSON

{
  "results": [\
    {\
      "score": 0.8777582049369812,\
      "title": "Play New Free Online Games Every Day",\
      "id": "https://www.minigames.com/new-games",\
      "url": "https://www.minigames.com/new-games",\
      "publishedDate": "2000-01-01",\
      "author": null\
    },\
    {\
      "score": 0.87653648853302,\
      "title": "Play The best Online Games",\
      "id": "https://www.minigames.com/",\
      "url": "https://www.minigames.com/",\
      "publishedDate": "2000-01-01",\
      "author": null\
    }\
  ]
}

```

### [](\#return-parameters-3)  Return Parameters

#### [](\#searchresponse-3)  SearchResponse

| Field | Type | Description |
| --- | --- | --- |
| results | Result\[\] | List of Result objects |
| autopromptString? | string | Exa query created by autoprompt functionality |

#### [](\#result-object-2)  Result Object

| Field | Type | Description |  |
| --- | --- | --- | --- |
| url | string | URL of the search result |  |
| id | string | Temporary ID for the document |  |
| title | \`string | null\` | Title of the search result |
| score? | number | Similarity score between query/url and result |  |
| publishedDate? | string | Estimated creation date |  |
| author? | string | Author of the content, if available |  |

## [](\#findsimilarandcontents-method)  `findSimilarAndContents` Method

Find a list of similar results based on a webpage’s URL, optionally including the text content or highlights of each result.

### [](\#input-example-4)  Input Example

TypeScript

Copy

```TypeScript

// Find similar with full text content
const similarWithText = await exa.findSimilarAndContents(
  "https://www.example.com/article",
  {
    text: true,
    numResults: 2
  }
);

// Find similar with highlights
const similarWithHighlights = await exa.findSimilarAndContents(
  "https://www.example.com/article",
  {
    highlights: true,
    numResults: 2
  }
);

// Find similar with both text and highlights
const similarWithTextAndHighlights = await exa.findSimilarAndContents(
  "https://www.example.com/article",
  {
    text: true,
    highlights: true,
    numResults: 2,
    excludeSourceDomain: true
  }
);

```

### [](\#input-parameters-4)  Input Parameters

| Parameter | Type | Description | Default |  |
| --- | --- | --- | --- | --- |
| url | string | The URL of the webpage to find similar results for. | Required |  |
| text | \`boolean | `{ maxCharacters?: number, includeHtmlTags?: boolean }` \` | If provided, includes the full text of the content in the results. | undefined |
| highlights | \`boolean | `{ query?: string, numSentences?: number, highlightsPerUrl?: number }` \` | If provided, includes highlights of the content in the results. | undefined |
| numResults | number | Number of similar results to return. | undefined |  |
| includeDomains | string\[\] | List of domains to include in the search. | undefined |  |
| excludeDomains | string\[\] | List of domains to exclude from the search. | undefined |  |
| startCrawlDate | string | Results will only include links **crawled** after this date. | undefined |  |
| endCrawlDate | string | Results will only include links **crawled** before this date. | undefined |  |
| startPublishedDate | string | Results will only include links with a **published** date after this date. | undefined |  |
| endPublishedDate | string | Results will only include links with a **published** date before this date. | undefined |  |
| excludeSourceDomain | boolean | If true, excludes results from the same domain as the input URL. | undefined |  |
| category | string | A data category to focus on when searching, with higher comprehensivity and data cleanliness. | undefined |  |

### [](\#returns-example-4)  Returns Example

JSON

Copy

```JSON

{
  "results": [\
    {\
      "score": 0.8777582049369812,\
      "title": "Similar Article: AI and Machine Learning",\
      "id": "https://www.similarsite.com/ai-ml-article",\
      "url": "https://www.similarsite.com/ai-ml-article",\
      "publishedDate": "2023-05-15",\
      "author": "Jane Doe",\
      "text": "Artificial Intelligence (AI) and Machine Learning (ML) are revolutionizing various industries. [... TRUNCATED FOR BREVITY ...]",\
      "highlights": [\
        "AI and ML are transforming how businesses operate, enabling more efficient processes and data-driven decision making.",\
        "The future of AI looks promising, with potential applications in healthcare, finance, and autonomous vehicles."\
      ],\
      "highlightScores": [\
        0.95,\
        0.89\
      ]\
    },\
    {\
      "score": 0.87653648853302,\
      "title": "The Impact of AI on Modern Technology",\
      "id": "https://www.techblog.com/ai-impact",\
      "url": "https://www.techblog.com/ai-impact",\
      "publishedDate": "2023-06-01",\
      "author": "John Smith",\
      "text": "In recent years, artificial intelligence has made significant strides in various technological domains. [... TRUNCATED FOR BREVITY ...]",\
      "highlights": [\
        "AI is not just a buzzword; it's a transformative technology that's reshaping industries and creating new opportunities.",\
        "As AI continues to evolve, ethical considerations and responsible development become increasingly important."\
      ],\
      "highlightScores": [\
        0.92,\
        0.88\
      ]\
    }\
  ]
}

```

### [](\#return-parameters-4)  Return Parameters

#### [](\#searchresponse-4)  SearchResponse

| Field | Type | Description |
| --- | --- | --- |
| results | SearchResult<T>\[\] | List of SearchResult objects |
| autopromptString? | string | Exa query created by autoprompt functionality |

#### [](\#searchresult-2)  SearchResult

Extends the `Result` object with additional fields based on the requested content:

| Field | Type | Description |  |
| --- | --- | --- | --- |
| url | string | URL of the search result |  |
| id | string | Temporary ID for the document |  |
| title | \`string | null\` | Title of the search result |
| score? | number | Similarity score between query/url and result |  |
| publishedDate? | string | Estimated creation date |  |
| author? | string | Author of the content, if available |  |
| text? | string | Text of the search result page (if requested) |  |
| highlights? | string\[\] | Highlights of the search result (if requested) |  |
| highlightScores? | number\[\] | Scores of the highlights (if requested) |  |

Note: The actual fields present in the `SearchResult<T>` object depend on the options provided in the `findSimilarAndContents` call.

## [](\#getcontents-method)  `getContents` Method

Retrieves contents of documents based on a list of document IDs.

### [](\#input-example-5)  Input Example

TypeScript

Copy

```TypeScript

// Get contents for a single ID
const singleContent = await exa.getContents("https://www.example.com/article");

// Get contents for multiple IDs
const multipleContents = await exa.getContents([\
  "https://www.example.com/article1",\
  "https://www.example.com/article2"\
]);

// Get contents with specific options
const contentsWithOptions = await exa.getContents(
  ["https://www.example.com/article1", "https://www.example.com/article2"],
  {
    text: { maxCharacters: 1000 },
    highlights: { query: "AI", numSentences: 2 }
  }
);

```

### [](\#input-parameters-5)  Input Parameters

| Parameter | Type | Description | Default |  |  |
| --- | --- | --- | --- | --- | --- |
| ids | \`string | string\[\] | SearchResult\[\]\` | A single ID, an array of IDs, or an array of SearchResults. | Required |
| text | \`boolean | `{ maxCharacters?: number, includeHtmlTags?: boolean }` \` | If provided, includes the full text of the content in the results. | undefined |  |
| highlights | \`boolean | `{ query?: string, numSentences?: number, highlightsPerUrl?: number }` \` | If provided, includes highlights of the content in the results. | undefined |  |

### [](\#returns-example-5)  Returns Example

JSON

Copy

```JSON

{
  "results": [\
    {\
      "id": "https://www.example.com/article1",\
      "url": "https://www.example.com/article1",\
      "title": "The Future of Artificial Intelligence",\
      "publishedDate": "2023-06-15",\
      "author": "Jane Doe",\
      "text": "Artificial Intelligence (AI) has made significant strides in recent years. [... TRUNCATED FOR BREVITY ...]",\
      "highlights": [\
        "AI is revolutionizing industries from healthcare to finance, enabling more efficient processes and data-driven decision making.",\
        "As AI continues to evolve, ethical considerations and responsible development become increasingly important."\
      ],\
      "highlightScores": [\
        0.95,\
        0.92\
      ]\
    },\
    {\
      "id": "https://www.example.com/article2",\
      "url": "https://www.example.com/article2",\
      "title": "Machine Learning Applications in Business",\
      "publishedDate": "2023-06-20",\
      "author": "John Smith",\
      "text": "Machine Learning (ML) is transforming how businesses operate and make decisions. [... TRUNCATED FOR BREVITY ...]",\
      "highlights": [\
        "Machine Learning algorithms can analyze vast amounts of data to identify patterns and make predictions.",\
        "Businesses are leveraging ML for customer segmentation, demand forecasting, and fraud detection."\
      ],\
      "highlightScores": [\
        0.93,\
        0.90\
      ]\
    }\
  ]
}

```

### [](\#return-parameters-5)  Return Parameters

#### [](\#searchresponse-5)  SearchResponse

| Field | Type | Description |
| --- | --- | --- |
| results | SearchResult<T>\[\] | List of SearchResult objects |

#### [](\#searchresult-3)  SearchResult

The fields in the `SearchResult<T>` object depend on the options provided in the `getContents` call:

| Field | Type | Description |  |
| --- | --- | --- | --- |
| id | string | Temporary ID for the document |  |
| url | string | URL of the search result |  |
| title | \`string | null\` | Title of the search result |
| publishedDate? | string | Estimated creation date |  |
| author? | string | Author of the content, if available |  |
| text? | string | Text of the search result page (if requested) |  |
| highlights? | string\[\] | Highlights of the search result (if requested) |  |
| highlightScores? | number\[\] | Scores of the highlights (if requested) |  |

Note: The actual fields present in the `SearchResult<T>` object depend on the options provided in the `getContents` call. If neither `text` nor `highlights` is specified, the method defaults to including the full text content.

[Python SDK Specification](/integrations/python-sdk-specification) [Python and TS Cheat Sheets](/integrations/cheat-sheet)

On this page

- [Getting started](#getting-started)
- [search Method](#search-method)
- [Input Example](#input-example)
- [Input Parameters](#input-parameters)
- [Returns Example](#returns-example)
- [Return Parameters](#return-parameters)
- [SearchResponse](#searchresponse)
- [Result Object](#result-object)
- [searchAndContents Method](#searchandcontents-method)
- [Input Example](#input-example-2)
- [Input Parameters](#input-parameters-2)
- [Returns Example](#returns-example-2)
- [Return Parameters](#return-parameters-2)
- [SearchResponse](#searchresponse-2)
- [SearchResult](#searchresult)
- [findSimilar Method](#findsimilar-method)
- [Input Example](#input-example-3)
- [Input Parameters](#input-parameters-3)
- [Returns Example](#returns-example-3)
- [Return Parameters](#return-parameters-3)
- [SearchResponse](#searchresponse-3)
- [Result Object](#result-object-2)
- [findSimilarAndContents Method](#findsimilarandcontents-method)
- [Input Example](#input-example-4)
- [Input Parameters](#input-parameters-4)
- [Returns Example](#returns-example-4)
- [Return Parameters](#return-parameters-4)
- [SearchResponse](#searchresponse-4)
- [SearchResult](#searchresult-2)
- [getContents Method](#getcontents-method)
- [Input Example](#input-example-5)
- [Input Parameters](#input-parameters-5)
- [Returns Example](#returns-example-5)
- [Return Parameters](#return-parameters-5)
- [SearchResponse](#searchresponse-5)
- [SearchResult](#searchresult-3)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Changelog

Auto Search as Default

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

## [](\#auto-search-upcoming-new-default)  Auto Search: Upcoming New Default

Soon, Auto Search will become the default search type for all queries. This change leverages the best of both Exa’s proprietary neural search and industry-standard keyword search to give you the best results. Auto means, out of the box, we automatically route queries to the best search type.

### [](\#what-this-means-for-you)  What This Means for You

1. **Enhanced Results**: Auto Search automatically routes queries to the most appropriate search type (neural or keyword), optimizing your search results without any extra effort on your part.
2. **No Action Required**: If you want to benefit from Auto Search, you don’t need to change anything in your existing implementation. It’ll just work!
3. **Maintaining Current Behavior**: If you prefer to keep your current search behavior, here’s how:

   - For neural search: Just set `type="neural"` in your search requests.
   - For keyword search: As always, add `type="keyword"` to your search requests.

### [](\#quick-example)  Quick Example

Here’s what this means for your code when default switches over:

Python

Copy

```Python
# New default behavior (Auto Search)
result = exa.search_and_contents("hottest AI startups")

# Explicitly use neural search
result = exa.search_and_contents("hottest AI startups", type="neural")

# Use keyword search
result = exa.search_and_contents("hottest AI startups", type="keyword")

```

We’re confident this update will significantly improve your search experience. If you have any questions or want to chat about how this might impact your specific use case, please reach out to [\[hello@exa.ai\]](/cdn-cgi/l/email-protection#90f8f5fcfcffd0f5e8f1bef1f9).

We can’t wait for you to try out the new Auto Search as default!

On this page

- [Auto Search: Upcoming New Default](#auto-search-upcoming-new-default)
- [What This Means for You](#what-this-means-for-you)
- [Quick Example](#quick-example)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Getting started with Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

First, create an account and grab a free API key.

[**Get your Exa API key**](https://dashboard.exa.ai/api-keys)

Next, you can use our Python or TypeScript SDK, or call the API directly with cURL.

## [](\#quickstart)  Quickstart

- Python
- JavaScript
- cURL

1

Install the python SDK

Shell

Copy

```Shell
pip install exa_py

```

2

Set up the environment variable

Create an `.env` file in the root of your project and set the `EXA_API_KEY` environment variable to [your API key](https://dashboard.exa.ai/api-keys).

Shell

Copy

```Shell
EXA_API_KEY=insert your Exa API key here, without quotes

```

3

Instantiate the client

Python

Copy

```Python
from exa_py import Exa
import os
exa = Exa(os.getenv('EXA_API_KEY'))

```

4

Make a search using the search\_and\_contents method

The `search_and_contents` method returns a list of search results with the contents and/or highlights of the webpages.
You can find a more detailed explanation of the methods [here](/exa-s-capabilities-explained).

Python

Copy

```Python
result = exa.search_and_contents(
  "hottest AI startups",
  type="neural",
  use_autoprompt=True,
  num_results=5,
  text=True,
)

print(result)

```

5

Example output

Shell

Copy

```Shell
Autoprompt String: Here is a hot AI startup:

Title: Paradox | Conversational hiring software that gets work done for you
URL: https://www.paradox.ai/
ID: https://www.paradox.ai/
Score: 0.17912396788597107
Published Date: January 1, 2024
Author: Seema Shah, Global Talent Acquisition Operations Manager
Text: Every great hire starts with      Meet the conversational recruiting software that automates the work your teams don’t have time for — taking candidates from hello to hired faster than ever.          See our product, clients, and business outcomes firsthand.      Recruiters and managers spend 80% of their time on repetitive admin tasks. With Paradox, it can be 0%.   CONVERSATIONAL ATS An ATS frontline teams actually love.   Meet the frictionless Conversational ATS that makes things easier and faster than ever for high-volume hiring managers and candidates.    CONVERSATIONAL CAREER SITES  A career site that adapts to every conversation.  Embrace a future where realistic job previews, employer brand content, job recommendations, and more are at a candidate's fingertips — no searching required.    HOW ELSE CAN WE HELP? Automation that saves everyone time (and money).  With our conversational recruiting platform, you can get more done with less — and create better experiences for everyone.    We measure success in client hugs (and results).     Adoption with Paradox has been absolutely amazing. Our recruiters are feeling that impact right away and it’s freeing them up to do more empowering work.            With Paradox, there are frictionless conversations going on while our recruiters are doing all that valuable stuff.             We’re reducing friction and radically simplifying hiring, not just for drivers but for our own team, too.             The most important thing is that you need to be where candidates interact. And then to speed-to-hire them very quickly. Paradox has helped us achieve that.             Our journey with Paradox has worked in stages. Now that we can get a high volume of candidates, we can research the profile of the most successful behavior technician.             The biggest impact that Paradox has had on our candidate experience has actually been decreasing the time to apply.               decrease in time to hire     decrease in job advertising     increase in hard to fill roles     candidate satisfaction rating      We work with the biggest HCM systems in the world. And we make them better.       If you do it, we can make it conversational.

Title: Dreamwave | Professional headshots in minutes, made with AI
URL: https://www.dreamwave.ai/
ID: https://www.dreamwave.ai/
Score: 0.17910835146903992
Published Date: January 1, 2024
Author: None
Text: Accurate AI headshots in minutes you can actually use professionally  16 million headshots made for over 50,000 Fortune 500 executives &amp; professionals     Get started in 30 seconds! Upload your selfies andget accurate AI headshots without the AI look  Drop to upload your photo(s)   100% privacy-first &amp; made in the USA. Delete your photos after use  Get headshots for your team instead            Kathryn  My professional headshots turned out so beautifully! Really high quality and accuracy. This is way, way better than any other AI headshot generator I've seen.    AI headshot, real customer       Freia  Dreamwave is the best AI professional headshot generator hands down. I showed my dad the photos and he just thought I got a photoshoot done. Some of the photos even have me doubting myself...    AI headshot, real customer        Daniel     Genuinely — wow!! Just tried Dreamwave's AI headshot generator and I am blown away. So many of my AI headshots looked like they were actually real. Definitely using a lot of these for sure.    AI headshot, real customer            Had a bit of fun with AI headshots with Dreamwave AI. If you are someone who perhaps does not like taking pictures or is too busy to schedule a photoshoot or does not want to spend the money on a photo (or all three like me) I would give this option a go.    AI headshot, real customer           Andrea Foglesong @radgirland      The other AI headshot apps I tried look like a Snapchat filter, but these just look human! Looks like a real person, very professional, love it. I would recommend these, I'm going to be using them for Linkedin!    AI headshot, real customer         Jefferson Pang @jeffersonpang      God I was impressed. It was quick, convenient, and the results were just as good as if I had gone to a professional photographer.    AI headshot, real customer       Suzie Smibert  Love love LOVE my new AI generated headshots. I cannot say thank you enough. I don't have the time to go and get a professional headshot and I HATE posing. The pictures are so realistic that it made me doubt myself!    AI headshot, real customer        Dominique     I am STUNNED! Dreamwave AI is the best AI headshot generator out there! I thought I was looking at photos from a real photoshoot! I sent the results to my family and friends, and no one could tell they were AI. Also, it was the most surprising and fun way to test out new outfits and hairstyles and see what I liked!    AI headshot, real customer           Erin Shaw Street @erinshawstreet      I am so pleased with the professional headshots Dreamwave AI generated for me! I was excited to add my new AI headshots to my socials and to have updated headshots without the hassle and expense of an entire photo shoot. I recommend the experience!    AI headshot, real customer        Siqi     Dreamwave is the best AI headshot generator by far! I can't believe how natural my new professional headshots look.    AI headshot, real customer         Karthik Suresh @karthiksuresh      New AI headshots from @DreamwaveAI. I love them! Tried two other AI headshot generators but none of them came close — Dreamwave is the legit one.    AI headshot, real customer            Some pics for the job boards! @DreamwaveAI #aiheadshots #jobsinstem    AI headshot, real customer         Jen Tedesko  I absolutely cringe at the thought of a photo shoot, so I was giddy when I found Dreamwave's AI headshot generator. I am blown away with what landed in my inbox - almost all 40 AI headshots were better than ANY actual professional headshots I had ever had. Plus, all the AI outfits and earrings and different poses are making me laugh with delight. This is so much fun.    AI headshot, real customer         Annie Margarita Yang @annieyangfinancial       Out of all the ones I've seen so far, Dreamwave has to be number one! Get the premium package — there are so many options to choose from that you could use for your LinkedIn. Dreamwave AI is definitely the  best AI headshot generator  I've seen. I'm overall very very impressed with my AI headshots, to the point where I'm scrolling back up being like is that me? I honestly think if I put these pictures in a media kit that I send to public relations or to potential magazines and pocasts to be featured in, they might not realize that these are AI generated. The best thing is that these facial expressions look quite real, the other apps all had a blank stare.     AI headshot, real customer        Jesse Rosen     Lo and behold the first AI generated professional headshots of me! Which photo should I use as a headshot on my LinkedIn profile?    AI headshot, real customer        Dreamwave is an AI research lab developing new ways to augment human creativity with artificial intelligence.    Products   Headshot photography Get natural, accurate, and beautiful photos of yourself in 1 hour — no camera required.   AI photos, real customers    Team headshots Generate consistent AI headshots that scale with your growing company. Perfect for remote teams.   AI photos, real customers    Create custom photos Generate new photos of yourself with any scene, outfit, or hair. The only limit is your imagination.   AI photos, real customers      Team   We’re a small team of AI researchers and engineers based in California. Previously, our team members worked on machine learning research at MIT, Google Brain, and Meta AI.     Values     Empower human creativity We believe AI should augment human creativity, not replace it. We're here to make new creative workflows possible, and to make tedious and time-consuming work easy.   Safe &amp; unbiased representation We're dedicated to building controllable AI models that work for all ethnicities, genders, and body types.   Secure &amp; private data You always remain in control of how you want to share your photos and data. You can delete your data and AI models at any time. We will never sell your data.       Careers    We’re always looking for ambitious, thoughtful, and kind people to join our team. If you’re excited about Dreamwave but don’t see the exact open position you’re looking for, email team@dreamwave.ai.

Title: Harvey | Generative AI for Professional Services
URL: https://www.harvey.ai/
ID: https://www.harvey.ai/
Score: 0.17904220521450043
Published Date: January 1, 2024
Author: None
Text: The TrustedLegal AI Platform Augment your workflows using domain specific models trained by and for professional service providers.   Harvey works with the world’s best legal teams     Product The Harvey Platform provides a suite of products tailored to lawyers and law firms across all practice areas and workflows.    Augment your legal workflows with domain specific models   Answer complex research questions based on trusted laws, regulations, filings, and more   Draft, analyze, compare, and query over any type of legal document using natural language      Legal Domain \nSpecific Models Harvey leverages  large language models  trained on complex legal tasks and fine-tuned by domain experts.               Usage Matters Identity &amp; Provisioning   Governance Harvey provides unprecedented visibility into your firm's productivity. Track work product produced on the Harvey platform by attorney, client matter, practice area and more. Access fine-grained control over usage and data provenance.    Security Deployed on Microsoft Azure, Harvey is built to the highest security standards, so your firm's data is always safe.   \nComprehensive security accreditations.\nAdvised by  top security experts.  \nFully deployed on Azure and complete data segregation.

Title: DirectAI | Vision models without training data
URL: https://directai.io/
ID: https://directai.io/
Score: 0.17877060174942017
Published Date: January 1, 2024
Author: None
Text: Vision models without training data.  Build and deploy powerful computer vision models with plain language.No code or training required.    Fundamentally different. We use large language models and zero-shot learning to instantly build models that fit your description.       We're removing the last major barrier to creating custom models -  training data.           Deploy and iterate in seconds with DirectAI        • Don't spend time assembling training data.     • Don't pay a third party to label your data.     • Don't pay to train your model.     • Don't spend months finetuning your model's behavior.        Venture-backed.Based in NYC. We're changing how people use AI in the real world. Come talk to us on .

Title: Gab AI | An Uncensored and Unfiltered AI Platform
URL: https://gab.ai/
ID: https://gab.ai/
Score: 0.17850659787654877
Published Date: January 1, 2024
Author: None
Text: An Uncensored and Unfiltered AI Platform      Image Generators →     Explore our Characters

```

[Overview](/reference/getting-started) [Search](/reference/search)

On this page

- [Quickstart](#quickstart)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Tutorials

Recruiting Agent

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

### [](\#what-this-doc-covers)  What this doc covers

1. Using Exa search with includeDomain to only retrieve search results from a specified domain
2. Using Exa keyword search to find specific people by name
3. Using excludeDomain to ignore certain low-signal domains
4. Using Exa link similarity search to find similar websites

* * *

## [](\#introduction)  Introduction

In this tutorial, we use Exa to **automate** the process of **discovering**, **researching**, and **evaluating** exceptional candidates. If you just want to see the code, check out the [Colab notebook](https://colab.research.google.com/drive/1a-7niLbCtIEjZnPz-qXPS3XwckPgIMrV?usp=sharing).

Here’s what we’re going to do:

1. Candidate research: Identify potential candidates and use Exa to find additional details, such as personal websites, LinkedIn profiles, and their research topics.
2. Candidate evaluation: Evaluate candidates using an LLM to score their fit to our hiring criteria.
3. Finding more candidates: Discover more candidates similar to our top picks.

This project requires an [Exa API key](https://dashboard.exa.ai/api-keys) and an [OpenAI API key](https://platform.openai.com/api-keys). Get 1000 Exa searches per month free just for [signing up](https://dashboard.exa.ai/overview)!

Python

Copy

```Python
# install dependencies
!pip install exa_py openai matplotlib tqdm

import pandas as pd
from exa_py import Exa
import openai

EXA_API_KEY = ''
OPENAI_API_KEY = ''

exa = Exa(api_key = EXA_API_KEY)
openai.api_key = OPENAI_API_KEY

```

## [](\#initial-candidates)  Initial Candidates

Suppose I’m building Simile, an AI startup for web retrieval.

My hiring criteria is:

- AI experience
- interest in retrieval, databases, and knowledge
- available to work now or soon

We start with 13 example PhD students recommended by friends. All I have is their name and email.

Python

Copy

```Python
# Usually you would upload a csv of students
# df = pd.read_csv('./students.csv')

# TODO: add your own candidates
sample_data = {
    "Name": [\
        "Kristy Choi", "Jiaming Song", "Brice Huang", "Andi Peng",\
        "Athiya Deviyani", "Hao Zhu", "Zana Bucinca", "Usha Bhalla",\
        "Kia Rahmani", "Jingyan Wang", "Jun-Kun Wang", "Sanmi Koyejo",\
        "Erik Jenner"\
    ],
    "Email": [\
        "[[email protected]](/cdn-cgi/l/email-protection)", "[[email protected]](/cdn-cgi/l/email-protection)",\
        "[[email protected]](/cdn-cgi/l/email-protection)", "[[email protected]](/cdn-cgi/l/email-protection)",\
        "[[email protected]](/cdn-cgi/l/email-protection)", "[[email protected]](/cdn-cgi/l/email-protection)",\
        "[[email protected]](/cdn-cgi/l/email-protection)", "[[email protected]](/cdn-cgi/l/email-protection)",\
        "[[email protected]](/cdn-cgi/l/email-protection)", "[[email protected]](/cdn-cgi/l/email-protection)",\
        "[[email protected]](/cdn-cgi/l/email-protection)", "[[email protected]](/cdn-cgi/l/email-protection)",\
        "[[email protected]](/cdn-cgi/l/email-protection)"\
    ]
}

# Creating the DataFrame
students_df = pd.DataFrame(sample_data)
students_df

```

## [](\#information-enrichment)  Information Enrichment

Now, let’s add more information about the candidates: current school, LinkedIn, and personal website.

First, we’ll define a helper function to call OpenAI — we’ll use this for many of our later functions.

Python

Copy

```Python
def get_openai_response(input_text):
    # if contents is empty
    if not input_text:
        return ""
    completion = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[\
                {"role": "system", "content": "You are a helpful assistant."},\
                {"role": "user", "content": input_text},\
            ],
            temperature=0
        )
    return completion.choices[0].message.content

```

We’ll ask GPT to extract the candidate’s school from their email address.

Python

Copy

```Python
def extract_school_from_email(email):
  content =  f"I'm going to give you a student's email. I want you to figure out what school they go to. For example, if the email is [[email protected]](/cdn-cgi/l/email-protection) you should return 'CMU' and nothing else. Only return the name of the school. Here is their email: {email}"
  return get_openai_response(content)

# Example
extract_school_from_email('[[email protected]](/cdn-cgi/l/email-protection)')

```

Now that we have their school, let’s use Exa to find their LinkedIn and personal website too.

Here, we’re passing in `type="keyword"` to do an Exa keyword search because we want our results to have the exact name in the result. We also specify `include_domains=['linkedin.com']` to restrict the results to LinkedIn profiles.

Python

Copy

```Python
def get_linkedin_from_name(name, school = ''):
    query = f"{name} {school}"

    keyword_search = exa.search(query, num_results=1, type="keyword", include_domains=['linkedin.com'])

    if keyword_search.results:
        result = keyword_search.results[0]
        return result.url
    print(f"No LinkedIn found for: {name}")
    return None

print("LinkedIn:", get_linkedin_from_name('Sarah Chieng', 'MIT'))

```

To now find the candidate’s personal website, we can use the same Exa query, but we want to also scrape the website’s contents. To do this, we use `search_and_contents`.

We can also exclude some misleading websites with `exclude_domains=['linkedin.com', 'github.com', 'twitter.com']`. Whatever’s left has a good chance of being their personal site!

Python

Copy

```Python
#given a name, returns their personal website if we can find it
def exa_search_personal_website(name, school = ''):
    query = f"{name} {school}"
    keyword_search = exa.search_and_contents(query, type="keyword", text={"include_html_tags": False}, num_results=1, exclude_domains=['linkedin.com', 'github.com', 'twitter.com'])
    if keyword_search.results:
        result = keyword_search.results[0]
        return result.url, result.text
    print(f"No personal website found for: {name}")
    return (None, None)

#example
personal_website_url, personal_website_text = exa_search_personal_website('Aryaman Arora', 'Stanford')
personal_website_url

```

Now that I have personal websites of each candidate, we can use Exa and GPT-4 to answer questions like:

- what are they doing now? Or what class year are they?
- where did they do their undergrad?
- what topics do they research?
- are they an AI researcher?

Once we have all of the page’s contents, let’s start asking some questions:

Python

Copy

```Python
def extract_undergrad_from_contents(contents):
    contents = f"""I'm going to give you some information I found online about a person. Based on the provided information, determine where they went to college for undergrad.
    Some examples are \"MIT\" or \"Harvard.\" You should answer only in the example format, or return \"not sure\" if you're not sure. Do not return any other text. Here is the information I have scraped: {contents}."""
    return get_openai_response(contents)

def extract_current_role_from_contents(contents):
    contents = f"""I'm going to give you some information I found online about a person. Based on the provided information, determine where they are currently working or if they are still a student, what their current year of study is.
    Some examples are \"OpenAI\" or \"first year PHD.\" You should answer only in the example format, or return \"not sure\" if you're not sure. Do not return any other text. Here is the information I have scraped: {contents}."""
    return get_openai_response(contents)

def extract_research_topics_from_contents(contents):
    contents = f"""I'm going to give you some information I found online about a person. Based on the provided information, determine what fields they research.
    Some examples are \"RAG, retrieval, and databases\" or \"Diffusion models.\" You should answer only in the example format, or return \"not sure\" if you're not sure. Do not return any other text. Here is the information I have scraped: {contents}."""
    return get_openai_response(contents)

def extract_is_ai_from_contents(contents):
    contents = f"""I'm going to give you some information I found online about a person. Based on the provided information, determine whether they are a AI researcher.
    You should only return \"yes\" or \"no\", or return \"not sure\" if you're not sure. Do not return any other text. Here is the information I have scraped: {contents}."""
    return get_openai_response(contents)

#Example
personal_website_url, personal_website_text = exa_search_personal_website('Aryaman Arora', 'Stanford') # Note: this is a random person I found online using an Exa search

undergrad = extract_undergrad_from_contents(personal_website_text)
current = extract_current_role_from_contents(personal_website_text)
topics = extract_research_topics_from_contents(personal_website_text)
ai = extract_is_ai_from_contents(personal_website_text)

# Printing the information using f-string formatting
print(f"Personal Site: {personal_website_url}")
print(f"Undergrad: {undergrad}")
print(f"Current: {current}")
print(f"Topics: {topics}")
print(f"AI: {ai}")

```

## [](\#candidate-evaluation)  Candidate Evaluation

Next, we use GPT-4 to score candidates 1-10 based on fit. This way, we can use Exa to find more folks similar to our top-rated candidates.

Python

Copy

```Python
# TODO: change these to fit your own criteria

def calculate_score(info, undergrad, year, researchTopics, AI):
    contents = f"""I'm going to provide some information about an individual, and I want you to rate on a scale of 1 to 10 how good of a hiring candidate they are. I am hiring for AI researchers.
    A 10 is someone who went to an incredible college, is graduating soon (final year PhD ideally) or is already graduated, is definitely an AI researcher, has a lot of experience and seems really smart, and a nice bonus is if their research is related to retrieval, search, databases. Only return an integer from 0 to 10. Do not return anything else. This candidate did undergrad at {undergrad} and their current role is {year}. Are they an AI researcher? {AI}. They do research in {researchTopics}. Here are some other things I know about them: {info}"""
    try:
        return int(get_openai_response(contents))
    except:
        return None

```

Finally, let’s enrich our dataframe of people. We define a function `enrich_row` that uses all the functions we defined to learn more about a candidate,and sort by score to get the most promising candidates.

Python

Copy

```Python
# Set up progress bar
from tqdm.auto import tqdm
tqdm.pandas()

def enrich_row(row):
    row['School'] = extract_school_from_email(row['Email'])
    linkedIn_info = get_linkedin_from_name(row['Name'], row['School'])
    if linkedIn_info:
        row['LinkedIn'] = linkedIn_info
    website_url, website_info = exa_search_personal_website(row['Name'], row['School'])
    row['ExaWebsite'] = website_url
    row['ContentInfo'] = website_info
    row['Undergrad'] = extract_undergrad_from_contents(row['ContentInfo'])
    row['Role'] = extract_current_role_from_contents(row['ContentInfo'])
    row['ResearchTopics'] = extract_research_topics_from_contents(row['ContentInfo'])
    row['AI'] = extract_is_ai_from_contents(row['ContentInfo'])
    row['Score'] = calculate_score(row['ContentInfo'], row['Undergrad'], row['Role'], row['ResearchTopics'], row['AI'])
    return row

enriched_df = students_df.progress_apply(enrich_row, axis=1)
sorted_df = enriched_df.sort_values(by='Score', ascending=False).reset_index(drop=True)
sorted_df

```

## [](\#finding-more-candidates)  Finding more candidates

Now that we know how to research candidates, let’s find some more! We’ll take each of the top candidates (score 7-10), and use Exa to find similar profiles.

Exa’s `find_similar`,allows us to search a URL and find semantically similar URLs. For example, I could search ‘hinge.co’ and it’ll return the homepages of similar dating apps. In this case, we’ll pass in the homepages of our top candidates to find similar profiles.

Python

Copy

```Python
# given a homepage, get homepages of similar candidates

def get_more_candidates(homepageURL):
  new_homepages = []
  if not homepageURL:
    return None
  similarity_search = exa.find_similar_and_contents(homepageURL, num_results=3, text={"include_html_tags": False}, exclude_domains=['linkedin.com', 'github.com', 'twitter.com'])

  #return a list of emails
  for res in similarity_search.results:
    new_homepages.append((res.url, res.text))
  return new_homepages

# we can already get things like role and education, but we need to get the name and email this time
def get_name_from_contents(contents):
    content = f"""I'm going to give you some information I found online about a person. Based on the provided information, figure out their full name.
    Some examples are \"Sarah Chieng\" or \"Will Bryk.\" You should answer only in the example format, or return \"not sure\" if you're not sure. Do not return any other text. Here is the information I have scraped: {contents}."""
    return get_openai_response(content)

def get_email_from_contents(contents):
    content = f"""I'm going to give you some information I found online about a person. Based on the provided information, figure out their email.
    Some examples are \"[[email protected]](/cdn-cgi/l/email-protection)\" or \"[[email protected]](/cdn-cgi/l/email-protection).\" You should answer only in the example format, or return \"not sure\" if you're not sure. Do not return any other text. Here is the information I have scraped: {contents}."""
    return get_openai_response(content)

# Example
example_homepage = ('https://winniexu.ca/')
additional_homepages = get_more_candidates(example_homepage)
new_candidate_url, new_candidate_content = additional_homepages[0]
name = get_name_from_contents(new_candidate_content)
email = get_email_from_contents(new_candidate_content)

print(f"Additional Homepages:{additional_homepages}")
print(f"Name:{name}")
print(f"Email: {email}")

```

Final stretch — let’s put it all together. Let’s find and add our new candidates to our original dataframe.

Python

Copy

```Python
def new_candidates_df(df):
    # get the websites of our top candidates
    top_candidates_df = df[df['Score'] > 7]
    websites_list = top_candidates_df['ExaWebsite'].tolist()

    # use those top candidates to find new candidates
    new_candidates = set()
    for url in websites_list:
      new_candidates.update(get_more_candidates(url))

    #for each new candidate, get their information and add them to the dataframe
    names = []
    emails = []
    urls = []
    for url, content in tqdm(new_candidates):
      names.append(get_name_from_contents(content))
      emails.append(get_email_from_contents(content))
      urls.append(url)

    new_df = pd.DataFrame({
        'Name': names,
        'Email': emails,
        'ExaWebsite': urls,
    })

    return new_df

new_df = new_candidates_df(sorted_df)
new_df

```

Alrighty, that’s it! We’ve just built an automated way of finding, researching, and evaluating candidates. You can use this for recruiting, or tailor this to find customers, companies, etc.

And the best part is that every time you use Exa to find new candidates, you can do more `find_similar(new_candidate_homepage)` searches with the new candidates as well — helping you build an infinite list!

Hope this tutorial was helpful and don’t forget, you can get started with [Exa for free](https://dashboard.exa.ai/overview) :)

[Exa Researcher - Python](/examples/exa-researcher-python) [Phrase Filters: Niche Company Finder](/examples/niche-company-finder-with-phrase-filters)

On this page

- [What this doc covers](#what-this-doc-covers)
- [Introduction](#introduction)
- [Initial Candidates](#initial-candidates)
- [Information Enrichment](#information-enrichment)
- [Candidate Evaluation](#candidate-evaluation)
- [Finding more candidates](#finding-more-candidates)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

API Reference

Search

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

POST

/

search

Send

Authorization

x-api-key

string

\*

x-api-key

Required

string

Body

object

\*

query

string

\*

query

Required

string

The query string.

Add Example Value

useAutoprompt

boolean

Select option

useAutoprompt

boolean

If true, your query will be converted to a Exa query. Default false. Neural or Auto search only.

type

string

type

string

The Type of search, 'keyword', 'neural', or 'auto' (decides between keyword and neural). Default neural.

category

enum<string>

Select option

category

enum<string>

(beta) A data category to focus on, with higher comprehensivity and data cleanliness. Categories right now include company, research paper, news, linkedin profile, github, tweet, movie, song, personal site, and pdf.

numResults

integer

numResults

integer

Number of search results to return. Default 10. Max 10 for basic plans. Up to thousands for custom plans.

Add Example Value

includeDomains

array

includeDomains

array

List of domains to include in the search. If specified, results will only come from these domains.

Add Example Value

excludeDomains

array

excludeDomains

array

List of domains to exclude in the search. If specified, results will not include any from these domains.

Add Example Value

startCrawlDate

string

startCrawlDate

string

Crawl date refers to the date that Exa discovered a link. Results will include links that were crawled after this date. Must be specified in ISO 8601 format.

Add Example Value

endCrawlDate

string

endCrawlDate

string

Crawl date refers to the date that Exa discovered a link. Results will include links that were crawled before this date. Must be specified in ISO 8601 format.

Add Example Value

startPublishedDate

string

startPublishedDate

string

Only links with a published date after this will be returned. Must be specified in ISO 8601 format.

Add Example Value

endPublishedDate

string

endPublishedDate

string

Only links with a published date before this will be returned. Must be specified in ISO 8601 format.

Add Example Value

includeText

array

includeText

array

List of strings that must be present in webpage text of results. Currently, only 1 string is supported, of up to 5 words.

Add Example Value

excludeText

array

excludeText

array

List of strings that must not be present in webpage text of results. Currently, only 1 string is supported, of up to 5 words.

Add Example Value

contents

object

contents

object

text

object

text

object

Parsed contents of the page.

maxCharacters

integer

maxCharacters

integer

Max length in characters for the text returned

includeHtmlTags

boolean

Select option

includeHtmlTags

boolean

Whether HTML tags, which can help the LLM understand structure of text, should be included. Default false

highlights

object

highlights

object

Relevant extract(s) from the webpage.

numSentences

integer

numSentences

integer

The number of sentences to be returned in each snippet. Default 5

highlightsPerUrl

integer

highlightsPerUrl

integer

The number of snippets to return per page. Default 1

query

string

query

string

summary

object

summary

object

Summary of the webpage

query

string

query

string

If specified, tries to answer the query in the summary

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.exa.ai/search \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
  "query": "Here is an article about the state of search:",
  "useAutoprompt": true,
  "type": "<string>",
  "category": "company",
  "numResults": 10,
  "includeDomains": [\
    "example.com",\
    "sample.net"\
  ],
  "excludeDomains": [\
    "excludedomain.com",\
    "excludeme.net"\
  ],
  "startCrawlDate": "2023-01-01T00:00:00.000Z",
  "endCrawlDate": "2023-12-31T00:00:00.000Z",
  "startPublishedDate": "2023-01-01T00:00:00.000Z",
  "endPublishedDate": "2023-12-31T00:00:00.000Z",
  "includeText": [\
    "electron",\
    "positron"\
  ],
  "excludeText": [\
    "neutron",\
    "elon"\
  ],
  "contents": {
    "text": {
      "maxCharacters": 123,
      "includeHtmlTags": true
    },
    "highlights": {
      "numSentences": 123,
      "highlightsPerUrl": 123,
      "query": "<string>"
    },
    "summary": {
      "query": "<string>"
    }
  }
}'
```

200

Copy

```
{
  "results": [\
    {\
      "title": "<string>",\
      "url": "<string>",\
      "publishedDate": "<string>",\
      "author": "<string>",\
      "score": 123,\
      "id": "<string>",\
      "text": "<string>",\
      "highlights": [\
        "<string>"\
      ],\
      "highlightScores": [\
        123\
      ],\
      "summary": "<string>"\
    }\
  ],
  "autopromptString": "<string>"
}
```

[**Get your Exa API key**](https://dashboard.exa.ai/api-keys)

#### Authorizations

x-api-key

string

headerrequired

#### Body

application/json

query

string

required

The query string.

useAutoprompt

boolean

If true, your query will be converted to a Exa query. Default false. Neural or Auto search only.

type

string

The Type of search, 'keyword', 'neural', or 'auto' (decides between keyword and neural). Default neural.

category

enum<string>

(beta) A data category to focus on, with higher comprehensivity and data cleanliness. Categories right now include company, research paper, news, linkedin profile, github, tweet, movie, song, personal site, and pdf.

Available options:

`company`,

`research paper`,

`news`,

`linkedin profile`,

`github`,

`tweet`,

`movie`,

`song`,

`personal site`,

`pdf`

numResults

integer

Number of search results to return. Default 10. Max 10 for basic plans. Up to thousands for custom plans.

includeDomains

string\[\]

List of domains to include in the search. If specified, results will only come from these domains.

excludeDomains

string\[\]

List of domains to exclude in the search. If specified, results will not include any from these domains.

startCrawlDate

string

Crawl date refers to the date that Exa discovered a link. Results will include links that were crawled after this date. Must be specified in ISO 8601 format.

endCrawlDate

string

Crawl date refers to the date that Exa discovered a link. Results will include links that were crawled before this date. Must be specified in ISO 8601 format.

startPublishedDate

string

Only links with a published date after this will be returned. Must be specified in ISO 8601 format.

endPublishedDate

string

Only links with a published date before this will be returned. Must be specified in ISO 8601 format.

includeText

string\[\]

List of strings that must be present in webpage text of results. Currently, only 1 string is supported, of up to 5 words.

excludeText

string\[\]

List of strings that must not be present in webpage text of results. Currently, only 1 string is supported, of up to 5 words.

contents

object

Showchild attributes

#### Response

200 - application/json

results

object\[\]

A list of search results containing title, URL, published date, author, and score.

Showchild attributes

autopromptString

string

The Exa query created by the autoprompt functionality.

[Quickstart with SDKs](/reference/quickstart) [Get contents](/reference/get-contents)

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.exa.ai/search \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
  "query": "Here is an article about the state of search:",
  "useAutoprompt": true,
  "type": "<string>",
  "category": "company",
  "numResults": 10,
  "includeDomains": [\
    "example.com",\
    "sample.net"\
  ],
  "excludeDomains": [\
    "excludedomain.com",\
    "excludeme.net"\
  ],
  "startCrawlDate": "2023-01-01T00:00:00.000Z",
  "endCrawlDate": "2023-12-31T00:00:00.000Z",
  "startPublishedDate": "2023-01-01T00:00:00.000Z",
  "endPublishedDate": "2023-12-31T00:00:00.000Z",
  "includeText": [\
    "electron",\
    "positron"\
  ],
  "excludeText": [\
    "neutron",\
    "elon"\
  ],
  "contents": {
    "text": {
      "maxCharacters": 123,
      "includeHtmlTags": true
    },
    "highlights": {
      "numSentences": 123,
      "highlightsPerUrl": 123,
      "query": "<string>"
    },
    "summary": {
      "query": "<string>"
    }
  }
}'
```

200

Copy

```
{
  "results": [\
    {\
      "title": "<string>",\
      "url": "<string>",\
      "publishedDate": "<string>",\
      "author": "<string>",\
      "score": 123,\
      "id": "<string>",\
      "text": "<string>",\
      "highlights": [\
        "<string>"\
      ],\
      "highlightScores": [\
        123\
      ],\
      "summary": "<string>"\
    }\
  ],
  "autopromptString": "<string>"
}
```[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

RAG Quick Start Guide

OpenAI Exa Wrapper

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa is designed from the ground up to enable seamless, accurate, and performant RAG (Retrieval-Augmented Generation). Exa provides factual, up to date information needed to ground LLM generations.

But good RAG requires more than just great search. The client needs to decide _when_ to use RAG, with _what_ queries. They need to handle chunking, prompting, and chaining LLM calls. We provide the Exa OpenAI wrapper that, **with one line of code**, does all that and turns any OpenAI chat completion into an Exa-powered RAG system.

* * *

## [](\#get-started)  Get Started

First, create an account and grab a free API key.

[**Get your Exa API key**](https://dashboard.exa.ai/api-keys)

1

Install the Exa and OpenAI python libraries

Shell

Copy

```Shell
pip install openai exa_py

```

2

Instantiate Clients

Import and instantiate the Exa and OpenAI clients.

Make sure to obtain your API keys from OpenAI and Exa and set the `OPENAI_API_KEY` and `EXA_API_KEY` variables respectively.

Python

Copy

```Python
from openai import OpenAI
openai = OpenAI(api_key='OPENAI_API_KEY')

from exa_py import Exa
exa = Exa('EXA_API_KEY')

```

3

Wrap the OpenAI client

The `Exa.wrap` method takes your existing OpenAI client and wraps it with Exa-powered RAG capabilities.

Python

Copy

```Python
exa_openai = exa.wrap(openai)

```

4

Call the wrapped client

The wrapped client works exactly like the native OpenAI client, except that it automatically improves your completions with relevant search results.

The Exa OpenAI wrapper supports any model that [supports function calling](https://platform.openai.com/docs/guides/function-calling).

Python

Copy

```Python
completion = openai_exa.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What is the latest climate tech news?"}]
)

```

5

Example output

Stdout

Copy

```Stdout
Here are some of the latest climate tech news articles:

1. **Title:** [The world’s on the verge of a carbon storage boom](https://www.technologyreview.com/2024/06/12/1093477/the-worlds-on-the-verge-of-a-carbon-storage-boom/)
    - **Summary:** Companies are planning to drill boreholes to inject carbon dioxide deep underground for storage, marking a significant trend in carbon capture projects driven by subsidies and climate targets.

2. **Title:** [Ground Floor Green: Early Stage Climate VC](https://techcrunch.com/video/ground-floor-green-early-stage-climate-vc/)
    - **Summary:** Climate tech investment is on the rise, with a focus on smarter investments in early-stage companies. The challenge lies in balancing hope and hype in selecting winners.

3. **Title:** [Climate tech startups raised nearly $40 billion in funding last year. Check out 5 of the best pitch decks that caught the eyes of investors.](https://www.businessinsider.com/5-climate-tech-pitch-decks-investors-2022-6)
    - **Summary:** Climate tech startups raised nearly $40 billion in funding in 2021, with a focus on areas like carbon accounting and market plays. The top areas for emissions reduction received only a fraction of overall investment, indicating untapped potential.

```

6

End-to-end code example

Below is a code block that puts together all of the above. You can copy it into any Python script or Jupyter notebook to test out a complete RAG example.

Python

Copy

```Python
from openai import OpenAI
openai = OpenAI(api_key='OPENAI_API_KEY')

from exa_py import Exa
exa = Exa('EXA_API_KEY')

exa_openai = exa.wrap(openai)

messages = [{"role": "user", "content": "How can I optimally integrate rag into my app"}]

# exa_openai.chat.completions.create("gpt-4-turbo", messages)
completion = exa_openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "What is the latest climate tech news?"}]
    )

print(completion.choices[0].message.content)

```

7

Exmple with multiple questions

Here is a slightly more advanced example that shows how to use the wrapper to answer multiple questions.

Python

Copy

```Python
exa_openai = exa.wrap(openai)

questions = [\
    "How did bats evolve their wings?",\
    "How did Rome defend Italy from Hannibal?",\
]

for question in questions:
    completion = exa_openai.chat.completions.create( # calling the wrapper
        model="gpt-4o",
        messages=[{"role": "user", "content": question}]
    )

    print(f"Question: {question}\nAnswer: {completion.choices[0].message.content}")

```

### [](\#further-configuration-options-and-advanced-usage)  Further configuration options and advanced usage

While the default settings work well for most use cases, the Exa OpenAI wrapper’s `chat.completions.create()` method allows you to fine-tune the following parameters.

#### [](\#option-to-include-exa-results)  Option to include Exa results

`use_exa` specifies whether to include Exa results for a given request:

- `auto` Exa will intelligently determine whether to include results
- `required` Exa results will always be included
- `none` Exa results will never be included

Python

Copy

```Python
completion = exa_openai.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    use_exa="required"
)

```

#### [](\#number-of-results)  Number of results

`num_results` specifies how many search results Exa should retrieve (defaults to 3 results).

Python

Copy

```Python
exa_openai.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    num_results=1
)

```

#### [](\#maximum-result-length)  Maximum result length

`result_max_len` specifies the maximum length of each Exa result (defaults to 2048 characters).

This is measured in characters, not tokens.

Python

Copy

```Python
exa_openai.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    result_max_len=1024
)

```

#### [](\#search-parameters)  Search parameters

The Exa OpenAI wrapper supports any parameters that the `exa.search()` function accepts. You can find a list of all the parameters [here](search).

Python

Copy

```Python
exa_openai.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    include_domains=["arxiv.org"],
    category="research paper",
    start_published_date="2019-01-01"
)

```

[RAG with LangChain](/reference/langchain) [CrewAI agents with Exa](/reference/crewai)

On this page

- [Get Started](#get-started)
- [Further configuration options and advanced usage](#further-configuration-options-and-advanced-usage)
- [Option to include Exa results](#option-to-include-exa-results)
- [Number of results](#number-of-results)
- [Maximum result length](#maximum-result-length)
- [Search parameters](#search-parameters)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Tutorials

Structured Outputs with Instructor

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

## [](\#what-this-doc-covers)  What this doc covers

- Setting up Exa to use [Instructor](https://python.useinstructor.com/) for structured output generation
- Practical examples of using Exa and Instructor together

## [](\#guide)  Guide

### [](\#1-pre-requisites-and-installation)  1\. Pre-requisites and installation

Install the required libraries:

Python

Copy

```python
pip install exa_py instructor openai

```

Ensure API keys are initialized properly. The environment variable names are `EXA_API_KEY` and `OPENAI_API_KEY`.

[**Get your Exa API key**](https://dashboard.exa.ai/api-keys)

### [](\#2-why-use-instructor)  2\. Why use Instructor?

Instructor is a Python library that allows you to generate structured outputs from a language model.

We could instruct the LLM to return a structured output, but the output will still be a string, which we need to convert to a dictionary. What if the dictionary is not structured as we want? What if the LLM forgot to add the last ”}” in the JSON? We would have to handle all of these errors manually.

We could use `{ "type": "json_object" }` which will make the LLM return a JSON object. But for this, we would need to provide a JSON schema, which can get [large and complex](https://python.useinstructor.com/why/#pydantic-over-raw-schema).

Instead of doing this, we can use Instructor. Instructor is powered by [pydantic](https://docs.pydantic.dev/latest/), which means that it integrates with your IDE. We use pydantic’s `BaseModel` to define the output model:

### [](\#3-setup-and-basic-usage)  3\. Setup and Basic Usage

Let’s set up Exa and Instructor:

Python

Copy

```python
import os

import instructor
from exa_py import Exa
from openai import OpenAI
from pydantic import BaseModel

exa = Exa(os.environ["EXA_API_KEY"])
client = instructor.from_openai(OpenAI())

search_results = exa.search_and_contents(
    "Latest advancements in quantum computing",
    use_autoprompt=True,
    type="neural",
    text=True,
)
# Limit search_results to a maximum of 20,000 characters
search_results = search_results.results[:20000]

class QuantumComputingAdvancement(BaseModel):
    technology: str
    description: str
    potential_impact: str

    def __str__(self):
        return (
            f"Technology: {self.technology}\n"
            f"Description: {self.description}\n"
            f"Potential Impact: {self.potential_impact}"
        )

structured_output = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_model=QuantumComputingAdvancement,
    messages=[\
        {\
            "role": "user",\
            "content": f"Based on the provided context, describe a recent advancement in quantum computing.\n\n{search_results}",\
        }\
    ],
)

print(structured_output)

```

Here we define a `QuantumComputingAdvancement` class that inherits from `BaseModel` from Pydantic. This class will be used by Instructor to validate the output from the LLM and for the LLM as a response model. We also implement the `__str__()` method for easy printing of the output. We then initialize `OpenAI()` and wrap instructor on top of it with `instructor.from_openai` to create a client that will return structured outputs. If the output is not structured as our class, Instructor makes the LLM retry until max\_retries is reached. You can read more about how Instructor retries [here](https://python.useinstructor.com/why/#retries).

This example demonstrates how to use Exa to search for content about quantum computing advancements and structure the output using Instructor.

### [](\#4-advanced-example-analyzing-multiple-research-papers)  4\. Advanced Example: Analyzing Multiple Research Papers

Let’s create a more complex example where we analyze multiple research papers on a specific topic and use pydantic’s own validation model to correct the structured data to show you how we can be _even_ more fine-grained:

Python

Copy

```python
import os
from typing import List

import instructor
from exa_py import Exa
from openai import OpenAI
from pydantic import BaseModel, field_validator

exa = Exa(os.environ["EXA_API_KEY"])
client = instructor.from_openai(OpenAI())

class ResearchPaper(BaseModel):
    title: str
    authors: List[str]
    key_findings: List[str]
    methodology: str

    @field_validator("title")
    @classmethod
    def validate_title(cls, v):
        if v.upper() != v:
            raise ValueError("Title must be in uppercase.")
        return v

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Authors: {', '.join(self.authors)}\n"
            f"Key Findings: {', '.join(self.key_findings)}\n"
            f"Methodology: {self.methodology}"
        )

class ResearchAnalysis(BaseModel):
    papers: List[ResearchPaper]
    common_themes: List[str]
    future_directions: str

    def __str__(self):
        return (
            f"Common Themes:\n- {', '.join(self.common_themes)}\n"
            f"Future Directions: {self.future_directions}\n"
            f"Analyzed Papers:\n" + "\n".join(str(paper) for paper in self.papers)
        )

# Search for recent AI ethics research papers
search_results = exa.search_and_contents(
    "Recent AI ethics research papers",
    use_autoprompt=True,
    type="neural",
    text=True,
    num_results=5,  # Limit to 5 papers for this example
)

# Combine all search results into one string
combined_results = "\n\n".join([result.text for result in search_results.results])
structured_output = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_model=ResearchAnalysis,
    max_retries=5,
    messages=[\
        {\
            "role": "user",\
            "content": f"Analyze the following AI ethics research papers and provide a structured summary:\n\n{combined_results}",\
        }\
    ],
)

print(structured_output)

```

By using pydantic’s `field_validator`, we can create our own rules to validate each field to be exactly what we want, so that we can work with predictable data even though we are using an LLM. Additionally, implementing the `__str__()` method allows for more readable and convenient output formatting. Read more about different pydantic validators [here](https://docs.pydantic.dev/latest/concepts/validators/#field-validators). Because we don’t specify that the `Title` should be in uppercase in the prompt, this will result in _at least_ two API calls. You should avoid using `field_validator` s as the _only_ means to get the data in the right format; instead, you should include instructions in the prompt, such as specifying that the `Title` should be in uppercase/all-caps.

This advanced example demonstrates how to use Exa and Instructor to analyze multiple research papers, extract structured information, and provide a comprehensive summary of the findings.

### [](\#5-streaming-structured-outputs)  5\. Streaming Structured Outputs

Instructor also supports streaming structured outputs, which is useful for getting partial results as they’re generated (this does not support validators due to the nature of streaming responses, you can read more about it [here](https://python.useinstructor.com/concepts/partial/)):

To make the output easier to see, we will use the [rich](https://pypi.org/project/rich/) Python package. It should already be installed, but if it isn’t, just run `pip install rich`.

Python

Copy

```python
import os
from typing import List

import instructor
from exa_py import Exa
from openai import OpenAI
from pydantic import BaseModel
from rich.console import Console

exa = Exa(os.environ["EXA_API_KEY"])
client = instructor.from_openai(OpenAI())

class AIEthicsInsight(BaseModel):
    topic: str
    description: str
    ethical_implications: List[str]

    def __str__(self):
        return (
            f"Topic: {self.topic}\n"
            f"Description: {self.description}\n"
            f"Ethical Implications:\n- {', '.join(self.ethical_implications or [])}"
        )

# Search for recent AI ethics research papers
search_results = exa.search_and_contents(
    "Recent AI ethics research papers",
    use_autoprompt=True,
    type="neural",
    text=True,
    num_results=5,  # Limit to 5 papers for this example
)

# Combine all search results into one string
combined_results = "\n\n".join([result.text for result in search_results.results])

structured_output = client.chat.completions.create_partial(
    model="gpt-3.5-turbo",
    response_model=AIEthicsInsight,
    messages=[\
        {\
            "role": "user",\
            "content": f"Provide insights on AI ethics based on the following research:\n\n{combined_results}",\
        }\
    ],
    stream=True,
)

console = Console()

for output in structured_output:
    obj = output.model_dump()
    console.clear()
    print(output)
    if (
        output.topic
        and output.description
        and output.ethical_implications is not None
        and len(output.ethical_implications) >= 4
    ):
        break

```

stream output

Copy

```Text
topic='AI Ethics in Mimetic Models' description='Exploring the ethical implications of AI that simulates the decisions and behavior of specific individuals, known as mimetic models, and the social impact of their availability in various domains such as game-playing, text generation, and artistic expression.' ethical_implications=['Deception Concerns: Mimetic models can potentially be used for deception, leading to misinformation and challenges in distinguishing between a real individual and a simulated model.', 'Normative Issues: Mimetic models raise normative concerns related to the interactions between the target individual, the model operator, and other entities that interact with the model, impacting transparency, authenticity, and ethical considerations in various scenarios.', 'Preparation and End-Use: Mimetic models can be used as preparation for real-life interactions or as an end in themselves, affecting interactions, personal relationships, labor dynamics, and audience engagement, leading to questions about consent, labor devaluation, and reputation consequences.', '']

Final Output:
Topic: AI Ethics in Mimetic Models
Description: Exploring the ethical implications of AI that simulates the decisions and behavior of specific individuals, known as mimetic models, and the social impact of their availability in various domains such as game-playing, text generation, and artistic expression.
Ethical Implications:
- Deception Concerns: Mimetic models can potentially be used for deception, leading to misinformation and challenges in distinguishing between a real individual and a simulated model.
- Normative Issues: Mimetic models raise normative concerns related to the interactions between the target individual, the model operator, and other entities that interact with the model, impacting transparency, authenticity, and ethical considerations in various scenarios.
- Preparation and End-Use: Mimetic models can be used as preparation for real-life interactions or as an end in themselves, affecting interactions, personal relationships, labor dynamics, and audience engagement, leading to questions about consent, labor devaluation, and reputation consequences.

```

This example shows how to stream partial results and break the loop when certain conditions are met.

### [](\#6-writing-results-to-csv)  6\. Writing Results to CSV

After generating structured outputs, you might want to save the results for further analysis or record-keeping. Here’s how you can write the results to a CSV file:

Python

Copy

```python
import csv
import os
from typing import List

import instructor
from exa_py import Exa
from openai import OpenAI
from pydantic import BaseModel

exa = Exa(os.environ["EXA_API_KEY"])
client = instructor.from_openai(OpenAI())

class AIEthicsInsight(BaseModel):
    topic: str
    description: str
    ethical_implications: List[str]

# Search for recent AI ethics research papers
search_results = exa.search_and_contents(
    "Recent AI ethics research papers",
    use_autoprompt=True,
    type="neural",
    text=True,
    num_results=5,  # Limit to 5 papers for this example
)

# Combine all search results into one string
combined_results = "\n\n".join([result.text for result in search_results.results])

def write_to_csv(insights: List[AIEthicsInsight], filename: str = "ai_ethics_insights.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Topic', 'Description', 'Ethical Implications'])

        for insight in insights:
            writer.writerow([\
                insight.topic,\
                insight.description,\
                '; '.join(insight.ethical_implications)\
            ])

    print(f"Results written to {filename}")

# Generate multiple insights
num_insights = 5
insights = []
for _ in range(num_insights):
    insight = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_model=AIEthicsInsight,
        messages=[\
            {\
                "role": "user",\
                "content": f"Provide an insight on AI ethics based on the following research:\n\n{combined_results}",\
            }\
        ],
    )
    insights.append(insight)

# Write insights to CSV
write_to_csv(insights)

```

After running the code, you’ll have a CSV file named “ai\_ethics\_insights.csv”. Here’s an example of what the contents might look like:

Copy

```csv
Topic,Description,Ethical Implications
Algorithmic Bias,"This research challenges the assumption that algorithms can replace human decision-making and remain unbiased. It identifies three forms of outrage-intellectual, moral, and political-when reacting to algorithmic bias and suggests practical approaches like clarifying language around bias, developing new auditing methods, and building certain capabilities in AI systems.",Potential perpetuation of existing biases if not addressed; Necessity for transparency in AI system development; Impact on fairness and justice in societal decision-making processes; Importance of inclusive stakeholder engagement in AI design and implementation
Algorithmic Bias and Ethical Interview,"Artificial intelligence and machine learning are used to offload decision making from humans, with a misconception that machines can be unbiased. This paper critiques this assumption and discusses forms of outrage towards algorithmic biases, identifying three types: intellectual, moral, and political outrage. It suggests practical approaches such as clarifying language around bias, auditing methods, and building specific capabilities to address biases. The overall discussion urges for greater insight into conversations around algorithmic bias and its implications.","Algorithms can perpetuate and even amplify existing biases in data.; There can be a misleading assumption that machines are inherently fair and unbiased.; Algorithmic biases can trigger intellectual, moral, and political outrage, affecting societal trust in AI systems."
Algorithmic Bias and Human Decision Making,"This research delves into the misconceptions surrounding the belief that algorithms can replace human decision-making because they are inherently fair and unbiased. The study highlights the flaws in this rationale by showing that algorithms are not free from bias. It explores three types of outrage—intellectual, moral, and political—that arise when people confront algorithmic bias. The paper recommends addressing algorithmic bias through clearer language, better auditing methods, and enhanced system capabilities.","Algorithms can perpetuate and exacerbate existing biases rather than eliminate them.; The misconception that algorithms are unbiased may lead to a false sense of security in their use.; There is a need for the AI community to adopt clearer language and terms when discussing bias to prevent misunderstanding and misuse.; Enhancing auditing methods and system capabilities can help identify and address biases.; Decisions made through biased algorithms can have unjust outcomes, affecting public trust and leading to social and ethical implications."
Algorithmic Bias in AI,"Artificial intelligence and machine learning are increasingly used to offload decision making from people. In the past, one of the rationales for this replacement was that machines, unlike people, can be fair and unbiased. Evidence suggests otherwise, indicating that algorithms can be biased. The study investigates how bias is perceived in algorithmic decision-making, proposing clarity in the language around bias and suggesting new auditing methods for intelligent systems to address this concern.",Algorithms may inherit or exacerbate existing biases.; Misleading assumptions about AI's objectivity can lead to unfair outcomes.; Need for transparent language and robust auditing to mitigate bias.
Algorithmic Bias in AI Systems,"This research explores the misconception that algorithms can replace humans in decision-making without bias. It sheds light on the absurdity of assuming that algorithms are inherently unbiased and discusses emotional responses to algorithmic bias. The study suggests clarity in language about bias, new auditing methods, and capacity-building in AI systems to address bias concerns.",Misleading perception of unbiased AI leading to potential unfairness in decision-making.; Emotional and ethical concerns due to algorithmic bias perceived unfairness.; Need for consistent auditing methods to ensure fairness in AI systems.

```

Instructor has enabled the creation of structured data that can as such be stored in tabular format, e.g.in a CRM or similar.

By combining Exa’s powerful search capabilities with Instructor’s predictable output generation, you can extract and analyze information from web content efficiently and accurately.

[Build a Retrieval Agent with LangGraph](/examples/getting-started-with-rag-in-langgraph)

On this page

- [What this doc covers](#what-this-doc-covers)
- [Guide](#guide)
- [1\. Pre-requisites and installation](#1-pre-requisites-and-installation)
- [2\. Why use Instructor?](#2-why-use-instructor)
- [3\. Setup and Basic Usage](#3-setup-and-basic-usage)
- [4\. Advanced Example: Analyzing Multiple Research Papers](#4-advanced-example-analyzing-multiple-research-papers)
- [5\. Streaming Structured Outputs](#5-streaming-structured-outputs)
- [6\. Writing Results to CSV](#6-writing-results-to-csv)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Admin

Enterprise Documentation & Security

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa takes data security and privacy seriously. We are proud to be SOC 2 Type I certified, demonstrating our commitment to maintaining rigorous information security practices and controls.

Contact us at [hello@exa.ai](mailto:hello@exa.ai) to discuss an Enterprise plan if you are interested in Zero Data Retention or other customized data security solutions.

[Click here](https://exa-public.s3.us-east-1.amazonaws.com/Authorized+Subprocessors+(Subcontractors).pdf) to see a list of our Authorized Subcontractors per our standard Enterprise Data Processing Agreement (DPA).

[Rate Limits](/reference/rate-limits)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

OpenAPI Specification

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Below is our OpenAPI specification, which provides a complete definition of the Exa API.

YAML

Copy

```YAML
---
openapi: 3.1.0
info:
  version: 1.0.0
  title: Exa Search API
  description: A comprehensive API for internet-scale search, allowing
    users to perform queries and retrieve results from a wide variety of
    sources using embeddings-based and traditional search.
servers:
  - url: https://api.exa.ai
paths:
  /search:
    post:
      operationId: search
      summary: Search
      description: Perform a search with a Exa prompt-engineered query and
        retrieve a list of relevant results. Optionally get contents.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              allOf:
                - type: object
                  properties:
                    query:
                      type: string
                      example: "Here is an article about the state of search:"
                      description: The query string.
                    useAutoprompt:
                      type: boolean
                      description: If true, your query will be converted to a Exa query. Default false. Neural or Auto search only.
                    type:
                      type: string
                      description: The Type of search, 'keyword', 'neural', or 'auto' (decides between keyword and neural). Default neural.
                    category:
                      type: string
                      enum:
                        - company
                        - research paper
                        - news
                        - github
                        - tweet
                        - movie
                        - song
                        - personal site
                        - pdf
                      description: (beta) A data category to focus on, with higher comprehensivity and data cleanliness. Categories right now include company, research paper, news, linkedin profile, github, tweet, movie, song, personal site, and pdf.
                  required:
                    - query
                - $ref: "#/components/schemas/CommonRequest"
      responses:
        "200":
          $ref: "#/components/responses/SearchResponse"
  /findSimilar:
    post:
      operationId: findSimilar
      summary: Find similar links
      description: Find similar links to the link provided. Optionally get contents.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              allOf:
                - type: object
                  properties:
                    url:
                      type: string
                      example: https://slatestarcodex.com/2014/07/30/meditations-on-moloch/
                      description: The url for which you would like to find similar links
                  required:
                    - url
                - $ref: "#/components/schemas/CommonRequest"
      responses:
        "200":
          $ref: "#/components/responses/FindSimilarResponse"
  /contents:
    post:
      summary: Get contents of documents, many different types
      operationId: 'getContents'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              allOf:
                - type: object
                  properties:
                    ids:
                      type: array
                      description: Array of document IDs obtained from searches
                      items:
                        type: string
                  required:
                    - ids
                - $ref: '#/components/schemas/ContentsRequest'
      responses:
        "200":
          $ref: '#/components/responses/ContentsResponse'
components:
  securitySchemes:
    apikey:
      type: apiKey
      name: x-api-key
      in: header
  schemas:
    ContentsRequest:
      type: object
      properties:
        text:
          type: object
          description: Parsed contents of the page.
          properties:
            maxCharacters:
              type: integer
              description: Max length in characters for the text returned
            includeHtmlTags:
              type: boolean
              description: Whether HTML tags, which can help the LLM understand structure of text, should be included. Default false
        highlights:
          type: object
          description: Relevant extract(s) from the webpage.
          properties:
            numSentences:
              type: integer
              description: The number of sentences to be returned in each snippet. Default 5
            highlightsPerUrl:
              type: integer
              description: The number of snippets to return per page. Default 1
            query:
              type: string
         summary:
          type: object
          description: Summary of the webpage
          properties:
            query:
              type: string
              description: If specified, tries to answer the query in the summary
    CommonRequest:
      type: object
      properties:
        numResults:
          type: integer
          description: Number of search results to return. Default 10. Max 10 for basic
            plans. Up to thousands for custom plans.
          example: 10
        includeDomains:
          type: array
          items:
            type: string
          description: List of domains to include in the search. If specified, results
            will only come from these domains.
          example:
            - example.com
            - sample.net
        excludeDomains:
          type: array
          items:
            type: string
          description: List of domains to exclude in the search. If specified, results
            will not include any from these domains.
          example:
            - excludedomain.com
            - excludeme.net
        startCrawlDate:
          type: string
          format: date-time
          description: Crawl date refers to the date that Exa discovered a link.
            Results will include links that were crawled after this date. Must
            be specified in ISO 8601 format.
          example: 2023-01-01
        endCrawlDate:
          type: string
          format: date-time
          description: Crawl date refers to the date that Exa discovered a link.
            Results will include links that were crawled before this date. Must
            be specified in ISO 8601 format.
          example: 2023-12-31
        startPublishedDate:
          type: string
          format: date-time
          description: Only links with a published date after this will be returned. Must
            be specified in ISO 8601 format.
          example: 2023-01-01
        endPublishedDate:
          type: string
          format: date-time
          description: Only links with a published date before this will be returned. Must
            be specified in ISO 8601 format.
          example: 2023-12-31
        includeText:
          type: array
          items:
            type: string
          description: List of strings that must be present in webpage text of results. Currently, only 1 string is supported, of up to 5 words.
          example:
            - electron
            - positron
        excludeText:
          type: array
          items:
            type: string
          description: List of strings that must not be present in webpage text of results. Currently, only 1 string is supported, of up to 5 words.
          example:
            - neutron
            - elon
        contents:
          $ref: '#/components/schemas/ContentsRequest'
    Result:
      type: object
      properties:
        title:
          type: string
          description: The title of the search result.
        url:
          type: string
          format: uri
          description: The URL of the search result.
        publishedDate:
          type: string
          nullable: true
          description: An estimate of the creation date, from parsing HTML content. Format
            is YYYY-MM-DD.
        author:
          type: string
          nullable: true
          description: If available, the author of the content.
        score:
          type: number
          nullable: true
          description: A number from 0 to 1 representing similarity between the query/url
            and the result.
        id:
          type: string
          description: The temporary ID for the document. Useful for /contents endpoint.
    ResultWithContent:
      allOf:
        - $ref: "#/components/schemas/Result"
        - type: object
          properties:
            text:
              type: string
              description: The full content text of the search result.
            # TODO: think we need to change this
            highlights:
              type: array
              items:
                type: string
              description: Array of highlights extracted from the search result content.
            highlightScores:
              type: array
              items:
                type: number
                format: float
              description: Array of cosine similarity scores for each highlighted
            summary:
              type: string
              description: Summary of the webpage
  responses:
    SearchResponse:
      description: OK
      content:
        application/json:
          schema:
            type: object
            properties:
              results:
                type: array
                description: A list of search results containing title, URL, published date,
                  author, and score.
                items:
                  $ref: "#/components/schemas/ResultWithContent"
              autopromptString:
                type: string
                description: The Exa query created by the autoprompt functionality.
    FindSimilarResponse:
      description: OK
      content:
        application/json:
          schema:
            type: object
            properties:
              results:
                type: array
                description: A list of search results containing title, URL, published date,
                  author, and score.
                items:
                  $ref: "#/components/schemas/ResultWithContent"
    ContentsResponse:
      description: OK
      content:
        application/json:
          schema:
            type: object
            properties:
              results:
                type: array
                items:
                  $ref: "#/components/schemas/ResultWithContent"
security:
  - apikey: []

```[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

RAG Quick Start Guide

Tool calling with Claude

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

This guide will show you how to properly set up and use Anthropic’s and Exa’s API client, and utilise Claude’s function calling or “tool use” feature to perform Exa search integration. Here are the steps:

1. Install the prerequisite packages and set up API keys as environment variables
2. Understand how Claude’s “tool use” feature works
3. Use Exa within the tool use feature

## [](\#get-started)  Get Started

1

Prerequisites and installation

Before you can use this guide you will need to have [python3](https://www.python.org/doc/) and [pip](https://pip.pypa.io/en/stable/installation/) installed on your machine.

For the purpose of this guide we will need to install:

- `anthropic` library to perform Claude API calls and completions
- `exa_py` library to perform Exa search
- `rich` library to make the output more readable

Install the libraries.

Python

Copy

```python
pip install anthropic exa_py rich

```

To successfully use the Exa search client and Anthropic client you will need to have your `ANTHROPIC_API_KEY` and `EXA_API_KEY`

set as environment variables.

To get an Anthropic API key, you will first need an Anthropic account, visit the [Anthropic console](https://console.anthropic.com/settings/keys) to generate your API key.

Similarly, to get the Exa API key, you will first need an Exa account, visit the Exa dashboard to generate your API key.

[**Get your Exa API key**](https://dashboard.exa.ai/api-keys)

> Be safe with your API keys. Make sure they are not hardcoded in your code or added to a git repository to prevent leaking them to the public.

You can create an `.env` file in the root of your project and add the following to it:

Bash

Copy

```bash
API_KEY=insert your Anthropic API key here, without the quotes
EXA_API_KEY=insert your Exa API key here, without the quotes

```

Make sure to add your `.env` file to your `.gitignore` file if you have one.

2

Understanding Claude's Tool Use Feature

Claude LLMs can call a function you have defined in your code; this is called [tool use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use). To do this, you first need to describe the function you want to call to Claude’s LLM. You can do this by defining a description object of the format:

JSON

Copy

```json
{
    "name": "my_function_name", # The name of the function
    "description": "The description of my function", # Describe the function so Claude knows when and how to use it.
    "input_schema": { # input schema describes the format and the type of parameters Claude needs to generate to use the function
        "type": "object", # format of the generated Claude response
        "properties": { # properties defines the input parameters of the function
            "query": { # the function expects a query parameter
                "description": "The search query to perform.", # describes the parameter to Claude
            },
        },
        "required": ["query"], # define which parameters are required
    },
}

```

When this description is sent to Claude’s LLM, it returns an object with a string, which is the function name defined in _your_ code, and the arguments that the function takes. This does not execute or _call_ functions on Anthropic’s side; it only returns the function name and arguments which you will have to parse and call yourself in your code.

Python

Copy

```python
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835123",
  "name": "my_function_name",
  "input": {"query": "Latest developments in quantum computing"}
}

```

We will use the object of this format to call the `exa_search` function we define.

3

Use Exa Search as Claude tool

First, we import and initialise the Anthropic and Exa libraries and load the stored API keys.

Python

Copy

```python
import anthropic

from dotenv import load_dotenv
from exa_py import Exa

load_dotenv()

claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
exa = Exa(api_key=os.getenv("EXA_API_KEY"))

```

Next, we define the function and the function schema so that Claude knows how to use it and what arguments our local function takes:

Python

Copy

```python
TOOLS = [\
    {\
        "name": "exa_search",\
        "description": "Perform a search query on the web, and retrieve the most relevant URLs/web data.",\
        "input_schema": {\
            "type": "object",\
            "properties": {\
                "query": {\
                    "type": "string",\
                    "description": "The search query to perform.",\
                },\
            },\
            "required": ["query"],\
        },\
    }\
]

```

Finally, we’ll define the primer `SYSTEM_MESSAGE`, which explains to Claude what it is supposed to do:

Python

Copy

```python
SYSTEM_MESSAGE = "You are an agent that has access to an advanced search engine. Please provide the user with the information they are looking for by using the search tool provided."

```

We can now start writing the code needed to perform the LLM calls and the search. We’ll create the `exa_search` function that will call Exa’s `search_and_contents` function with the query:

Python

Copy

```python
def exa_search(query: str) -> Dict[str, Any]:
    return exa.search_and_contents(query=query, type='auto', highlights=True)

```

Next, we create a function to process the tool use:

Python

Copy

```python
def process_tool_calls(tool_calls):
    search_results = []
    for tool_call in tool_calls:
        function_name = tool_call.name
        function_args = tool_call.input
        if function_name == "exa_search":
            results = exa_search(**function_args)
            search_results.append(results)
            console.print(
                f"[bold cyan]Context updated[/bold cyan] [i]with[/i] "
                f"[bold green]exa_search[/bold green]: ",
                function_args.get("query"),
            )
    return search_results

```

Lastly, we’ll create a `main` function to bring it all together, and handle the user input and interaction with Claude:

Python

Copy

```python
def main():
    messages = []
    while True:
        try:
            user_query = Prompt.ask(
                "[bold yellow]What do you want to search for?[/bold yellow]",
            )
            messages.append({"role": "user", "content": user_query})
            completion = claude.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1024,
                system=SYSTEM_MESSAGE,
                messages=messages,
                tools=TOOLS,
            )
            message = completion.content[0]
            tool_calls = [content for content in completion.content if content.type == "tool_use"]
            if tool_calls:
                search_results = process_tool_calls(tool_calls)
                messages.append({"role": "assistant", "content": f"I've performed a search and found the following results: {search_results}"})
                messages.append({"role": "user", "content": "Please summarise this information and answer my previous query based on these results."})
                completion = claude.messages.create(
                    model="claude-3-sonnet-20240229",
                    max_tokens=1024,
                    system=SYSTEM_MESSAGE,
                    messages=messages,
                )
                response = completion.content[0].text
                console.print(Markdown(response))
                messages.append({"role": "assistant", "content": response})
            else:
                console.print(Markdown(message.text))
                messages.append({"role": "assistant", "content": message.text})
        except Exception as e:
            console.print(f"[bold red]An error occurred:[/bold red] {str(e)}")
if __name__ == "__main__":
    main()

```

The implementation creates a loop that continually prompts the user for search queries, uses Claude’s tool use feature to determine when to perform a search, and then uses the Exa search results to provide an informed response to the user’s query.

We also use the rich library to provide a more visually appealing console interface, including coloured output and markdown rendering for the responses.

4

Full code

Python

Copy

```python
# import all required packages
import os
import anthropic

from dotenv import load_dotenv
from typing import Any, Dict
from exa_py import Exa
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt

# Load environment variables from .env file
load_dotenv()

# create the anthropic client
claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# create the exa client
exa = Exa(api_key=os.getenv("EXA_API_KEY"))

# create the rich console
console = Console()

# define the system message (primer) of your agent
SYSTEM_MESSAGE = "You are an agent that has access to an advanced search engine. Please provide the user with the information they are looking for by using the search tool provided."

# define the tools available to the agent - we're defining a single tool, exa_search
TOOLS = [\
    {\
        "name": "exa_search",\
        "description": "Perform a search query on the web, and retrieve the most relevant URLs/web data.",\
        "input_schema": {\
            "type": "object",\
            "properties": {\
                "query": {\
                    "type": "string",\
                    "description": "The search query to perform.",\
                },\
            },\
            "required": ["query"],\
        },\
    }\
]

# define the function that will be called when the tool is used and perform the search
# and the retrieval of the result highlights.
# https://docs.exa.ai/reference/python-sdk-specification#search_and_contents-method
def exa_search(query: str) -> Dict[str, Any]:
    return exa.search_and_contents(query=query, type='auto', highlights=True)

# define the function that will process the tool use and perform the exa search
def process_tool_calls(tool_calls):
    search_results = []

    for tool_call in tool_calls:
        function_name = tool_call.name
        function_args = tool_call.input

        if function_name == "exa_search":
            results = exa_search(**function_args)
            search_results.append(results)

            console.print(
                f"[bold cyan]Context updated[/bold cyan] [i]with[/i] "
                f"[bold green]exa_search[/bold green]: ",
                function_args.get("query"),
            )

    return search_results

def main():
    messages = []

    while True:
        try:
            # create the user input prompt using rich
            user_query = Prompt.ask(
                "[bold yellow]What do you want to search for?[/bold yellow]",
            )
            messages.append({"role": "user", "content": user_query})

            # call claude llm by creating a completion which calls the defined exa tool
            completion = claude.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1024,
                system=SYSTEM_MESSAGE,
                messages=messages,
                tools=TOOLS,
            )

            # completion will contain the object needed to invoke your tool and perform the search
            message = completion.content[0]
            tool_calls = [content for content in completion.content if content.type == "tool_use"]

            if tool_calls:

                # process the tool object created by Calude llm and store the search results
                search_results = process_tool_calls(tool_calls)

                # create new message conating the search results and request the Claude llm to process the results
                messages.append({"role": "assistant", "content": f"I've performed a search and found the following results: {search_results}"})
                messages.append({"role": "user", "content": "Please summarize this information and answer my previous query based on these results."})

                # call Claude llm again to process the search results and yield the final answer
                completion = claude.messages.create(
                    model="claude-3-sonnet-20240229",
                    max_tokens=1024,
                    system=SYSTEM_MESSAGE,
                    messages=messages,
                )

                # parse the agents final answer and print it
                response = completion.content[0].text
                console.print(Markdown(response))
                messages.append({"role": "assistant", "content": response})

            else:
                # in case tool hasn't been used, print the standard agent reponse
                console.print(Markdown(message.text))
                messages.append({"role": "assistant", "content": message.text})

        except Exception as e:
            console.print(f"[bold red]An error occurred:[/bold red] {str(e)}")

if __name__ == "__main__":
    main()

```

We have now written an advanced search tool that combines the power of Claude’s language models with Exa’s semantic search capabilities, providing users with informative and context-aware responses to their queries.

5

Running the code

Save the code in a file, e.g. `claude_search.py`, and make sure the `.env` file containing the API keys we previously created is in the same directory as the script.

Then run the script using the following command from your terminal:

Bash

Copy

```bash
python claude_search.py

```

You should see a prompt:

Bash

Copy

```bash
What do you want to search for?

```

Let’s test it out.

Bash

Copy

```bash
What do you want to search for?: Who is Steve Rogers?
Context updated with exa_search:  Steve Rogers
Based on the search results, Steve Rogers is a fictional superhero character appearing in American comic books published by Marvel Comics. He is better known as Captain America.

The key points about Steve Rogers are:

 • He was born in the 1920s to a poor family in New York City. As a frail young man, he was rejected from military service during World War II.
 • He was recruited into a secret government program called Project Rebirth where he was transformed into a super-soldier through an experimental serum, gaining enhanced strength, agility and other abilities.
 • After the serum treatment, he became Captain America and fought against the Nazis alongside other heroes like Bucky Barnes and the Invaders during WWII.
 • He was frozen in ice towards the end of the war and remained that way for decades until being revived in modern times.
 • As Captain America, he continued his heroic adventures, becoming a core member and leader of the superhero team the Avengers.
 • Steve Rogers embodies the ideals of patriotism, freedom and serving one's country as a symbol of liberty and justice.

So in summary, Steve Rogers is the original and most well-known character to take on the superhero mantle of Captain America within the Marvel universe.

```

That’s it, enjoy your search agent!

[Tool calling with GPT](/reference/tool-calling-with-gpt4o) [How Exa Search Works](/reference/how-exa-search-works)

On this page

- [Get Started](#get-started)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Tutorials

Build a Retrieval Agent with LangGraph

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

## [](\#what-this-doc-covers)  What this doc covers

- Brief intro to LangGraph
- How to set up an agent in LangGraph with Exa search as a tool

* * *

## [](\#guide)  Guide

This guide will show you how you can define and use Exa search within the LangGraph framework. This framework provides a straightforward way for you to define an AI agent and for it to retrieve high-quality, semantically matched content via Exa search.

## [](\#brief-intro-to-langgraph)  Brief Intro to LangGraph

Before we dive into our implementation, a quick primer on the LangGraph framework.

LangGraph is a powerful tool for building complex LLM-based agents. It allows for cyclical workflows, gives you granular control, and offers built-in persistence. This means you can create reliable agents with intricate logic, pause and resume execution, and even incorporate human oversight.

Read more about [LangGraph here](https://langchain-ai.github.io/langgraph/)

## [](\#our-research-assistant-workflow)  Our Research Assistant Workflow

For our AI-powered research assistant, we’re leveraging LangGraph’s capabilities to create a workflow that combines an AI model (Claude) with a web search retrieval tool powered by Exa’s API, to fetch, find and analyze any documents (in this case research on climate tech). Here’s a visual representation of our workflow:

![Alt text](https://files.readme.io/a2674bdce9b576860cd8eeec735ebd8959e8a8b41d4e5fab829dbbdcae37d6b0-Screenshot_2024-08-22_at_11.50.08.png)

This diagram illustrates how our workflow takes advantage of LangGraph’s cycle support, allowing the agent to repeatedly use tools and make decisions until it has gathered sufficient information to provide a final response.

### [](\#lets-break-down-whats-happening-in-this-simple-workflow)  Let’s break down what’s happening in this simple workflow:

1. We start at the Entry Point with a user query (e.g., “Latest research papers on climate technology”).
2. The Agent (our AI model) receives the query and decides what to do next.
3. If the Agent needs more information, it uses the Web Search Retriever Tool to search for relevant documents.
4. The Web Search Retriever Tool fetches information using Exa’s semantic search capabilities.
5. The Agent receives the fetched information and analyzes it.
6. This process repeats until the Agent has enough information to provide a final response.

In the following sections, we’ll explore the code implementation in detail, showing how we leverage LangGraph’s features to create this advanced research assistant.

### [](\#1-prerequisites-and-installation)  1\. Prerequisites and Installation

Before starting, ensure you have the required packages installed:

Copy

```shell
pip install langchain-anthropic langchain-exa langgraph

```

Make sure to set up your API keys. For LangChain libraries, the environment variables should be named `ANTHROPIC_API_KEY` and `EXA_API_KEY` for Anthropic and Exa keys respectively.

[**Get your Exa API key**](https://dashboard.exa.ai/api-keys)

Copy

```bash
export ANTHROPIC_API_KEY=<your-api-key>

export EXA_API_KEY=<your-api-key>

```

### [](\#2-set-up-exa-search-as-a-langchain-tool)  2\. Set Up Exa Search as a LangChain Tool

After setting env variables, we can start configuring a search tool using `ExaSearchRetriever`. This tool ( [read more here](https://api.python.langchain.com/en/latest/retrievers/langchain_exa.retrievers.ExaSearchRetriever.html)) will help retrieve relevant documents based on a query.

First we need to import the required libraries:

Copy

```python
from typing import List
from langchain_exa import ExaSearchRetriever
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.tools import tool

```

After we have imported the necessary libraries, we need to define and register a tool so that the agent know what tools it can use.

We use LangGraph `tool` decorator which you can read more about [here](https://python.langchain.com/v0.1/docs/modules/tools/custom_tools/#tool-decorator). The decorator uses the function name as the tool name. The docstring provides the agent with a tool description.

The `retriever` is where we initialize the Exa search retriever and configure it with parameters such as `highlights=True`. You can read more about all the available parameters [here](https://docs.exa.ai/reference/python-sdk-specification#input-parameters-1).

Copy

```python
@tool
def retrieve_web_content(query: str) -> List[str]:
    """Function to retrieve usable documents for AI assistant"""
    # Initialize the Exa Search retriever
    retriever = ExaSearchRetriever(k=3, highlights=True, exa_api_key=EXA_API_KEY, use_autoprompt=True)

    # Define how to extract relevant metadata from the search results
    document_prompt = PromptTemplate.from_template(
        """
    <source>
        <url>{url}</url>
        <highlights>{highlights}</highlights>
    </source>
    """
    )

    # Create a chain to process the retrieved documents
    document_chain = (
        RunnableLambda(
            lambda document: {
                "highlights": document.metadata.get("highlights", "No highlights"),
                "url": document.metadata["url"],
            }
        )
        | document_prompt
    )

    # Execute the retrieval and processing chain
    retrieval_chain = retriever | document_chain.map()

    # Retrieve and return the documents
    documents = retrieval_chain.invoke(query)
    return documents

```

Here, `ExaSearchRetriever` is set to fetch 3 documents, extract highlights and improves the query with `use_autoprompt`. Read more about [autoprompt](https://docs.exa.ai/reference/exas-capabilities-explained#use-autoprompt-incl-autodate) which automatically optimizes your query for Exa’s neural search.

Then we use LangChain’s `PromptTemplate` to structure the results from Exa in a more AI friendly way. Creating and using this template is optional, but recommended. Read more about PromptTemplate ( [here](https://python.langchain.com/v0.1/docs/modules/model_io/prompts/quick_start/#).

We also use a RunnableLambda to extract necessary metadata (like URL and highlights) from the search results and format it using the prompt template.

After all of this we start the retrieval and processing chain and store the results in the `documents` variable which is returned.

### [](\#3-creating-a-toolchain-with-langgraph)  3\. Creating a Toolchain with LangGraph

Now let’s set up the complete toolchain using LangGraph.

Copy

```python
from typing import Literal
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode

# Define and bind the AI model
model = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0, api_key=ANTHROPIC_API_KEY).bind_tools([retrieve_web_content])

```

Here, ChatAnthropic is set up with our Exa search tool, ready to generate responses based on the context provided.

#### [](\#define-workflow-functions)  Define Workflow Functions

Create functions to manage the workflow:

Copy

```python
# Determine whether to continue or end
def should_continue(state: MessagesState) -> Literal["tools", END]:
    messages = state["messages"]
    last_message = messages[-1]
    return "tools" if last_message.tool_calls else END

# Function to generate model responses
def call_model(state: MessagesState):
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages": [response]}

```

#### [](\#build-the-workflow-graph)  Build the Workflow Graph

Copy

```python
# Define the workflow graph
workflow = StateGraph(MessagesState)
workflow.add_node("agent", call_model)
workflow.add_node("tools", ToolNode([retrieve_web_content]))
workflow.set_entry_point("agent")
workflow.add_conditional_edges("agent", should_continue)
workflow.add_edge("tools", "agent")

# Initialize memory
checkpointer = MemorySaver()

# Compile the workflow into a runnable
app = workflow.compile(checkpointer=checkpointer)

```

This sets up a state machine that switches between generating responses and retrieving documents, with memory to maintain context (this is a key advantage of LangGraph).

### [](\#4-running-your-workflow)  4\. Running Your Workflow

We are approaching the finish line of our Exa-powered search agent.

#### [](\#invoke-and-run)  Invoke and run

Copy

```python
final_state = app.invoke(
    {"messages": [HumanMessage(content="Latest research papers on climate technology")]},
    config={"configurable": {"thread_id": 44}},
)
print(final_state["messages"][-1].content)

```

Text output

Copy

```c
Thank you for your patience. I've retrieved some information about the latest research papers on climate technology. Let me summarize the key findings for you:

1. Research and Development Investment Strategy for Paris Climate Agreement:
   - Source: Nature Communications (2023)
   - URL: https://www.nature.com/articles/s41467-023-38620-4.pdf
   - Key points:
     - The study focuses on research and development (R&D) investment strategies to achieve the goals of the Paris Climate Agreement.
     - It highlights that some low-carbon options are still not available at large scale or are too costly.
     - The research emphasizes the importance of government decisions in incentivizing R&D for climate technologies.
     - Current assessments of climate neutrality often don't include research-driven innovation, which this paper addresses.

2. Impact of Green Innovation on Emissions:
   - Source: SSRN (Social Science Research Network)
   - URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4212567
   - Key points:
     - This study examines the effect of green innovation on direct and indirect emissions across various sectors worldwide.
     - Surprisingly, it finds that green innovation does not significantly affect emissions in the short term (one year after filing a green patent) or medium term (three to five years after filing).
     - The research touches on concepts like the path dependence of innovation and the Jevons paradox in relation to green technology.

3. Comprehensive Study on Green Technology:
   - Source: Taylor & Francis Online
   - URL: https://www.tandfonline.com/doi/pdf/10.1080/1331677X.2023.2178017
   - Key points:
     - This paper provides a comprehensive review of literature on green technology.
     - It includes sections on research methods, measurement of variables, and data analysis techniques related to green technology.
     - The study offers policy recommendations and discusses limitations in the field of green technology research.

These papers represent some of the latest research in climate technology, covering topics from R&D investment strategies to the actual impact of green innovations on emissions. They highlight the complexity of the field, showing that while there's significant focus on developing new technologies, the real-world impact of these innovations may be more nuanced than expected.

Would you like more information on any specific aspect of these studies or climate technology in general?

```

### [](\#5-optional-streaming-the-output)  (5\. Optional: Streaming the output)

Copy

```python
for chunk in app.stream({"messages": [HumanMessage(content="Latest research papers on climate technology")]}, config={"configurable": {"thread_id": 42}}):
    print(chunk, end="|", flush=True)

```

Or asynchronously:

Copy

```python
async def async_streamer():
  async for chunk in app.astream({"messages": [HumanMessage(content="Latest research papers on climate technology")]}, config={"configurable": {"thread_id": 42}}):
    print(chunk, end="|", flush=True)

async_streamer()

```

That’s it! You have now created a super powered search agent with the help of LangGraph and Exa. Modify the code to fit your needs and you can create an Exa powered agent for any task you can think of.

### [](\#full-code)  Full Code

Copy

```python
from typing import List, Literal

from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.tools import tool
from langchain_exa import ExaSearchRetriever
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode

@tool
def retrieve_web_content(query: str) -> List[str]:
    """Function to retrieve usable documents for AI assistant"""
    # Initialize the Exa Search retriever
    retriever = ExaSearchRetriever(k=3, highlights=True, use_autoprompt=True)

    # Define how to extract relevant metadata from the search results
    document_prompt = PromptTemplate.from_template(
        """
    <source>
        <url>{url}</url>
        <highlights>{highlights}</highlights>
    </source>
    """
    )

    # Create a chain to process the retrieved documents
    document_chain = (
        RunnableLambda(
            lambda document: {
                "highlights": document.metadata.get("highlights", "No highlights"),
                "url": document.metadata["url"],
            }
        )
        | document_prompt
    )

    # Execute the retrieval and processing chain
    retrieval_chain = retriever | document_chain.map()

    # Retrieve and return the documents
    documents = retrieval_chain.invoke(query)
    return documents

# Define and bind the AI model
model = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0).bind_tools(
    [retrieve_web_content]
)

# Determine whether to continue or end
def should_continue(state: MessagesState) -> Literal["tools", END]:
    messages = state["messages"]
    last_message = messages[-1]
    return "tools" if last_message.tool_calls else END

# Function to generate model responses
def call_model(state: MessagesState):
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages": [response]}

# Define the workflow graph
workflow = StateGraph(MessagesState)
workflow.add_node("agent", call_model)
workflow.add_node("tools", ToolNode([retrieve_web_content]))
workflow.set_entry_point("agent")
workflow.add_conditional_edges("agent", should_continue)
workflow.add_edge("tools", "agent")

# Initialize memory
checkpointer = MemorySaver()

# Compile the workflow into a runnable
app = workflow.compile(checkpointer=checkpointer)

final_state = app.invoke(
    {
        "messages": [\
            HumanMessage(content="Latest research papers on climate technology")\
        ]
    },
    config={"configurable": {"thread_id": 44}},
)
print(final_state["messages"][-1].content)

```

Full code in Google Colab [here](https://docs.exa.ai/reference/getting-started-with-rag-in-langgraph)

[Job Search with Exa](/examples/job-search-with-exa) [Structured Outputs with Instructor](/examples/getting-started-with-exa-in-instructor)

On this page

- [What this doc covers](#what-this-doc-covers)
- [Guide](#guide)
- [Brief Intro to LangGraph](#brief-intro-to-langgraph)
- [Our Research Assistant Workflow](#our-research-assistant-workflow)
- [Let’s break down what’s happening in this simple workflow:](#lets-break-down-whats-happening-in-this-simple-workflow)
- [1\. Prerequisites and Installation](#1-prerequisites-and-installation)
- [2\. Set Up Exa Search as a LangChain Tool](#2-set-up-exa-search-as-a-langchain-tool)
- [3\. Creating a Toolchain with LangGraph](#3-creating-a-toolchain-with-langgraph)
- [Define Workflow Functions](#define-workflow-functions)
- [Build the Workflow Graph](#build-the-workflow-graph)
- [4\. Running Your Workflow](#4-running-your-workflow)
- [Invoke and run](#invoke-and-run)
- [(5\. Optional: Streaming the output)](#5-optional-streaming-the-output)
- [Full Code](#full-code)

![Alt text](https://files.readme.io/a2674bdce9b576860cd8eeec735ebd8959e8a8b41d4e5fab829dbbdcae37d6b0-Screenshot_2024-08-22_at_11.50.08.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Concepts

Exa LiveCrawl

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

With Exa, we can already search the web using LLMs.

However, by default, we cache all of our links to bias for the fastest response possible. You may be interested in the live version of the page, which our `livecrawl` parameter can help with.

## [](\#using-livecrawl)  Using LiveCrawl

LiveCrawl becomes essential when you need the most up-to-date contents from a URL. Here are some examples:

1. **Company News**: If you’re tracking Apple’s latest releases, you may be looking for a live view of their homepage’s contentes:

Python

Copy

```Python
result = exa.get_contents(
  ["https://www.apple.com"],
  livecrawl="always"
)

```

Output without LiveCrawl: Results here are slightly dated, mentioning a fall release (later in the year)

Shell

Copy

```Shell
{
  "results": [\
    {\
      "id": "https://www.apple.com",\
      "url": "https://www.apple.com/",\
      "title": "Apple",\
      "author": "",\
      "text": "Apple Footer\n 1. Apple Intelligence will be available in beta on iPhone 15 Pro, iPhone 15 Pro Max, and iPad and Mac with M1 and later, with Siri and device language set to U.S. English, as part of iOS 18, iPadOS 18, and macOS Sequoia this fall.\n 2. Trade-in values will vary based on the condition, year, and configuration of your eligible trade-in device. Not all devices are eligible for credit. You must be at least 18 years old to be eligible to trade in for credit or for an Apple Gift Card. Trade-in value may be applied toward qualifying new device purchase, or added to an Apple Gift Card. Actual value awarded is based on receipt of a qualifying device matching the description provided when estimate was made. Sales tax may be assessed on full value of a new device purchase. In-store trade-in requires presentation of a valid photo ID (local law may require saving this information). Offer may not be available in all stores, and may vary between in-store and online trade-in. Some stores may have additional requirements. Apple or its trade-in partners reserve the right to refuse or limit quantity of any trade-in transaction for any reason. More details are available from Apple’s trade-in partner for trade-in and recycling of eligible devices. Restrictions and limitations may apply. \nA subscription is required for Apple TV+.\nAvailable in the U.S. on apple.com, in the Apple Store app, and at Apple Stores.\nTo access and use all Apple Card features and products available only to Apple Card users, you must add Apple Card to Wallet on an iPhone or iPad that supports and has the latest version of iOS or iPadOS. Apple Card is subject to credit approval, available only for qualifying applicants in the United States, and issued by Goldman Sachs Bank USA, Salt Lake City Branch. \nIf you reside in the U.S. territories, please call Goldman Sachs at 877-255-5923 with questions about Apple Card.\nLearn more about how Apple Card applications are evaluated at support.apple.com/kb/HT209218.\n A subscription is required for Apple TV+. \n Major League Baseball trademarks and copyrights are used with permission of MLB Advanced Media, L.P. All rights reserved. \n A subscription is required for Apple Arcade, Apple Fitness+, and Apple Music. \nApple Store\n Find a Store \n Genius Bar \n Today at Apple \n Group Reservations \n Apple Camp \n Apple Store App \n Certified Refurbished \n Apple Trade In \n Financing \n Carrier Deals at Apple \n Order Status \n Shopping Help",\
      "image": "https://www.apple.com/ac/structured-data/images/open_graph_logo.png?202110180743"\
    }\
  ],
  "requestId": "f60d0828916fb43401ed90cd3c11dd59"
}

```

Output with LiveCrawl (as at Oct 30 2024): Now we see contents talking about Apple’s upcoming specific release on November 11th

Shell

Copy

```Shell
{
  "results": [\
    {\
      "id": "https://www.apple.com",\
      "url": "https://www.apple.com",\
      "title": "Apple",\
      "author": "",\
      "publishedDate": "2024-10-30T16:34:14.000Z",\
      "text": "Apple Intelligence is here.\nExperience it now on the latest iPhone, iPad, and Mac models with a free software update.1 \nMacBook Pro\nA work of smart.\nAvailable starting 11.8\n Hello, Apple Intelligence. \nApple Intelligence is here.\nExperience it now on the latest iPhone, iPad, and Mac models with a free software update.1 \nMac mini\nSize down. Power up.\nAvailable starting 11.8\n Hello, Apple Intelligence. \nApple Intelligence is here.\nExperience it now on the latest iPhone, iPad, and Mac models with a free software update.1 \niMac\nBril l l l l liant.\nAvailable starting 11.8\n Hello, Apple Intelligence. \niPhone 16 Pro\nHello, Apple Intelligence.\niPhone 16\nHello, Apple Intelligence.\nAirPods Pro 2\nHearing Test, Hearing Aid, and Hearing Protection features in a free software update.2\n Apple Intelligence \nAI for the rest of us.\n Apple Trade In \nGet $180-$650 in credit when you trade in iPhone 12 or higher.3 \n Apple Card \nGet up to 3% Daily Cash back with every purchase.\nApple TV+\nFAM Gallery",\
      "image": "https://www.apple.com/ac/structured-data/images/open_graph_logo.png?202110180743"\
    }\
  ],
  "requestId": "fdb7df2ef400b5994b0c5a855875cdce"
}

```

2. **Product Launches**: Tracking new releases or price changes
3. **Event Coverage**: Live events like conferences or sports
4. **Social Media Trends**: To stay updated on the latest trends or viral content

`livecrawl:'always'` ensures you’re working with the freshest data available, though it may take slightly longer than using cached results.

## [](\#when-livecrawl-isnt-necessary)  When LiveCrawl Isn’t Necessary

Cached data is sufficient for many queries, especially for historical topics like “What were the major causes of World War II?” or educational content such as “How does photosynthesis work?” These subjects rarely change, so reliable cached results can provide accurate information quickly.

[Crawling Subpages with Exa](/reference/crawling-subpages-with-exa) [Setting Up and Managing Your Team](/reference/setting-up-team)

On this page

- [Using LiveCrawl](#using-livecrawl)
- [When LiveCrawl Isn’t Necessary](#when-livecrawl-isnt-necessary)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Tutorials

Identifying Hallucinations with Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

## [](\#what-this-tutorial-covers)  What this tutorial covers:

- Extracting claims from _AI-generated \| politician generated \| other unreliable source generated_ text
- Using Exa to retrieve relevant sources that may support or refute these claims
- Use an LLM to analyze the claims against the relevant real sources and assign a confidence score

## [](\#guide)  Guide

One of the significant concerns with AI language models is their tendency to produce hallucinations—statements that sound plausible but are not grounded in factual data. This can erode trust in AI systems, especially when accurate information is critical.

Exa is a powerful tool to mitigate this. In this tutorial, we demonstrate how we can use Exa to cross-reference AI-generated content with real-world data to verify claim authenticity and identify hallucinations.

## [](\#set-up)  Set Up

Let’s kick things off by importing the necessary libraries and setting up our LLM and Exa search retriever.

Python

Copy

```python
import os
import re
import json
from typing import Dict, Any, List, Annotated
from pydantic import BaseModel
from langchain_core.tools import StructuredTool
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_exa import ExaSearchRetriever
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic

# Check for API keys
assert os.getenv("EXA_API_KEY"), "Please set the EXA_API_KEY environment variable"
assert os.getenv("ANTHROPIC_API_KEY"), "Please set the ANTHROPIC_API_KEY environment variable"

# Set up the LLM (ChatAnthropic)
llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0)

```

## [](\#claim-and-source-identification-with-exa)  Claim and Source Identification with Exa

Now, let’s define a function to extract factual claims from the input text using our LLM. If it fails, we’ll fall back on regex.

Python

Copy

```python
def extract_claims(text: str) -> List[str]:
    """Extract factual claims from the text using an LLM."""
    system_message = SystemMessage(content="""
    You are an expert at extracting claims from text.
    Your task is to identify and list all claims present, true or false,
    in the given text. Each claim should be a single, verifiable statement.
    Consider various forms of claims, including assertions, statistics, and
    quotes. Do not skip any claims, even if they seem obvious. Do not include in the list 'The text contains a claim that needs to be checked for hallucinations' - this is not a claim.
    Present the claims as a JSON array of strings, and do not include any additional text.
    """)

    human_message = HumanMessage(content=f"Extract factual claims from this text: {text}")
    response = llm.invoke([system_message, human_message])

    try:
        claims = json.loads(response.content)
        if not isinstance(claims, list):
            raise ValueError("Response is not a list")
    except (json.JSONDecodeError, ValueError):
        # Fallback to regex extraction if LLM response is not valid JSON
        claims = extract_claims_regex(text)

    return claims

def extract_claims_regex(text: str) -> List[str]:
    """Fallback function to extract claims using regex."""
    pattern = r'([A-Z][^.!?]*?[.!?])'
    matches = re.findall(pattern, text)
    return [match.strip()+'.' for match in matches]

```

We’ll use Exa to search for relevant sources that might support or refute each claim.

Python

Copy

```python
def exa_search(query: str) -> List[str]:
    """Function to retrieve usable documents for AI assistant."""
    search = ExaSearchRetriever(k=5, text=True, use_autoprompt=False)

    print("Query: ", query)

    document_prompt = PromptTemplate.from_template(
        """
        <source>
            <url>{url}</url>
            <text>{text}</text>
        </source>
        """
    )

    parse_info = RunnableLambda(
        lambda document: {
            "url": document.metadata["url"],
            "text": document.page_content or "No text available",
        }
    )

    document_chain = (parse_info | document_prompt)
    search_chain = search | document_chain.map()
    documents = search_chain.invoke(query+".\n Here is a web page to help verify this claim:")

    print("Documents: ", documents)

    return [str(doc) for doc in documents]

```

## [](\#claim-verification)  Claim Verification

We’ll use an LLM to assess whether the combined sources support or refute the claim. We’re bundling all sources together to minimize LLM calls.

Python

Copy

```python
def verify_claim(claim: str, sources: List[str]) -> Dict[str, Any]:
    """Verify a single claim using combined Exa search sources."""
    if not sources:
        # If no sources are returned, default to insufficient information
        return {
            "claim": claim,
            "assessment": "Insufficient information",
            "confidence_score": 0.5,
            "supporting_sources": [],
            "refuting_sources": []
        }

    # Combine the sources into one text
    combined_sources = "\n\n".join(sources)

    system_message = SystemMessage(content="""
    You are an expert fact-checker.
    Given a claim and a set of sources, determine whether the claim is supported, refuted, or if there is insufficient information in the sources to make a determination.
    For your analysis, consider all the sources collectively.
    Provide your answer as a JSON object with the following structure:
    {
        "claim": "...",
        "assessment": "supported" or "refuted" or "Insufficient information",
        "confidence_score": a number between 0 and 1 (1 means fully confident the claim is true, 0 means fully confident the claim is false),
        "supporting_sources": [list of sources that support the claim],
        "refuting_sources": [list of sources that refute the claim]
    }
    Do not include any additional text.
    """)

    human_message = HumanMessage(content=f"""
    Claim: "{claim}"

    Sources:
    {combined_sources}

    Based on the above sources, assess the claim.
    """)

    response = llm.invoke([system_message, human_message])

    try:
        result = json.loads(response.content)
        if not isinstance(result, dict):
            raise ValueError("Response is not a JSON object")
    except (json.JSONDecodeError, ValueError):
        # If parsing fails, default to insufficient information
        result = {
            "claim": claim,
            "assessment": "Insufficient information",
            "confidence_score": 0.5,
            "supporting_sources": [],
            "refuting_sources": []
        }

    return result

```

Let’s wrap it all up with our hallucination check workflow tool.

Python

Copy

```python
def hallucination_check(text: str) -> Dict[str, Any]:
    """Check a given text for hallucinations using Exa search."""
    claims = extract_claims(text)
    claim_verifications = []

    for claim in claims:
        sources = exa_search(claim)
        verification_result = verify_claim(claim, sources)
        claim_verifications.append(verification_result)

    return {
        "claims": claim_verifications
    }

def hallucination_check_tool(text: str) -> Dict[str, Any]:
    """Assess the given text for hallucinations using Exa search."""
    return hallucination_check(text)

structured_tool = StructuredTool.from_function(
    func=hallucination_check_tool,
    name="hallucination_check",
    description="Assess the given text for hallucinations using Exa search."
)

```

## [](\#run-the-workflow)  Run the Workflow

Time to put it all together. We’ll use `StateGraph` to set up a simple workflow and run a quick example about the Eiffel Tower.

Python

Copy

```python
class State(BaseModel):
    messages: Annotated[List, add_messages]
    analysis_result: Dict[str, Any] = {}

def call_model(state: State):
    # Simulate the assistant calling the tool
    return {"messages": state.messages + [AIMessage(content="Use hallucination_check tool", additional_kwargs={"tool_calls": [{"type": "function", "function": {"name": "hallucination_check"}}]})]}

def run_tool(state: State):
    text_to_check = next((m.content for m in reversed(state.messages) if isinstance(m, HumanMessage)), "")
    tool_output = structured_tool.invoke(text_to_check)
    return {"messages": state.messages + [AIMessage(content=str(tool_output))], "analysis_result": tool_output}

def use_analysis(state: State) -> str:
    return "tools"

workflow = StateGraph(State)

workflow.add_node("agent", call_model)
workflow.add_node("tools", run_tool)
workflow.add_node("process_result", lambda x: x)

workflow.set_entry_point("agent")
workflow.add_conditional_edges("agent", use_analysis, {
    "tools": "tools"
})
workflow.add_edge("tools", "process_result")
workflow.add_edge("process_result", END)

graph = workflow.compile()

## Example usage
if __name__ == "__main__":
    initial_state = State(messages=[\
        SystemMessage(content="You are a helpful assistant."),\
        HumanMessage(content="Check this text for hallucinations: The Eiffel Tower, an iconic iron lattice structure located in Paris, was originally constructed as a giant sundial in 1822.")\
    ])

    final_state = graph.invoke(initial_state)

    print("Workflow executed successfully")
    print("Final state:")
    print("Messages:")
    for message in final_state["messages"]:
        print(f"{message.__class__.__name__}: {message.content[:100]}...")  # Print first 100 characters

    print("\nAnalysis Result:")
    for claim_info in final_state["analysis_result"]["claims"]:
        print(f"Claim: {claim_info['claim']}")
        print(f"Assessment: {claim_info['assessment']}")
        print(f"Confidence Score: {claim_info['confidence_score']}")
        print("Supporting Sources:")
        for source in claim_info['supporting_sources']:
            print(f"- {source[:100]}...")  # Print first 100 characters
        print("Refuting Sources:")
        for source in claim_info['refuting_sources']:
            print(f"- {source[:100]}...")
        print()

```

## [](\#sample-output)  Sample output:

Copy

```
Workflow executed successfully
Final state:
Messages:
SystemMessage: You are a helpful assistant....
HumanMessage: Check this text for hallucinations: The Eiffel Tower, an iconic iron lattice structure located in Pa...
AIMessage: Use hallucination_check tool...
AIMessage: {'claims': [{'claim': 'The Eiffel Tower is an iconic iron lattice structure', 'assessment': 'support...\
\
Analysis Result:\
Claim: The Eiffel Tower is an iconic iron lattice structure\
Assessment: supported\
Confidence Score: 1\
Supporting Sources:\
- https://www.toureiffel.paris/en/news/130-years/what-eiffel-tower-made...\
- https://thechalkface.net/resources/melting_the_eiffel_tower.pdf...\
- https://datagenetics.com/blog/april22016/index.html...\
- https://engineering.purdue.edu/MSE/aboutus/gotmaterials/Buildings/patel.html...\
- https://www.toureiffel.paris/en/news/130-years/how-long-can-tower-last...\
Refuting Sources:\
\
Claim: The Eiffel Tower is located in Paris\
Assessment: supported\
Confidence Score: 1\
Supporting Sources:\
- https://hoaxes.org/weblog/comments/is_the_eiffel_tower_copyrighted...\
- https://www.toureiffel.paris/en...\
- http://www.eiffeltowerguide.com/...\
- https://www.toureiffel.paris/en/the-monument...\
Refuting Sources:\
\
Claim: The Eiffel Tower was originally constructed as a giant sundial\
Assessment: refuted\
Confidence Score: 0.05\
Supporting Sources:\
Refuting Sources:\
- https://www.whycenter.com/why-was-the-eiffel-tower-built/...\
- https://www.sciencekids.co.nz/sciencefacts/engineering/eiffeltower.html...\
- https://corrosion-doctors.org/Landmarks/eiffel-history.htm...\
\
Claim: The Eiffel Tower was constructed in 1822\
Assessment: refuted\
Confidence Score: 0\
Supporting Sources:\
Refuting Sources:\
- https://www.eiffeltowerfacts.org/eiffel-tower-history/...\
- https://www.whycenter.com/why-was-the-eiffel-tower-built/...\
- https://www.sciencekids.co.nz/sciencefacts/engineering/eiffeltower.html...\
\
```\
\
And there you have it! This shows how Exa + an LLM can be used to identify which claims are hallucinations and determine the validity of information.\
\
Exa can be integrated into applications as a powerful tool addressing one of the primary concerns with AI language models.\
\
# [](\#full-code)  Full Code\
\
Python\
\
Copy\
\
```python\
import os\
import re\
import json\
from typing import Dict, Any, List, Annotated\
from pydantic import BaseModel\
from langchain_core.tools import StructuredTool\
from langgraph.graph import StateGraph, END\
from langgraph.graph.message import add_messages\
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage\
from langchain_exa import ExaSearchRetriever\
from langchain_core.runnables import RunnableLambda\
from langchain_core.prompts import PromptTemplate\
from langchain_anthropic import ChatAnthropic\
\
# Check for API keys\
assert os.getenv("EXA_API_KEY"), "Please set the EXA_API_KEY environment variable"\
assert os.getenv("ANTHROPIC_API_KEY"), "Please set the ANTHROPIC_API_KEY environment variable"\
\
# Set up the LLM (ChatAnthropic)\
llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0)\
\
def exa_search(query: str) -> List[str]:\
    """Function to retrieve usable documents for AI assistant."""\
    search = ExaSearchRetriever(k=5, text=True, use_autoprompt=False)\
\
    document_prompt = PromptTemplate.from_template(\
        """\
        <source>\
            <url>{url}</url>\
            <text>{text}</text>\
        </source>\
        """\
    )\
\
    parse_info = RunnableLambda(\
        lambda document: {\
            "url": document.metadata["url"],\
            "text": document.page_content or "No text available",\
\
        }\
    )\
\
    document_chain = (parse_info | document_prompt)\
    search_chain = search | document_chain.map()\
    documents = search_chain.invoke(query+".\n Here is a web page to help verify this claim:")\
\
    return [str(doc) for doc in documents]\
\
def extract_claims(text: str) -> List[str]:\
    """Extract factual claims from the text using an LLM."""\
    system_message = SystemMessage(content="""\
    You are an expert at extracting claims from text.\
    Your task is to identify and list all claims present, true or false,\
    in the given text. Each claim should be a single, verifiable statement.\
    Consider various forms of claims, including assertions, statistics, and\
    quotes. Do not skip any claims, even if they seem obvious. Do not include in the list 'The text contains a claim that needs to be checked for hallucinations' - this is not a claim.\
    Present the claims as a JSON array of strings, and do not include any additional text.\
    """)\
\
    human_message = HumanMessage(content=f"Extract factual claims from this text: {text}")\
    response = llm.invoke([system_message, human_message])\
\
    try:\
        claims = json.loads(response.content)\
        if not isinstance(claims, list):\
            raise ValueError("Response is not a list")\
    except (json.JSONDecodeError, ValueError):\
        # Fallback to regex extraction if LLM response is not valid JSON\
        claims = extract_claims_regex(text)\
\
    return claims\
\
def extract_claims_regex(text: str) -> List[str]:\
    """Fallback function to extract claims using regex."""\
    pattern = r'([A-Z][^.!?]*?[.!?])'\
    matches = re.findall(pattern, text)\
    return [match.strip()+'.' for match in matches]\
\
def verify_claim(claim: str, sources: List[str]) -> Dict[str, Any]:\
    """Verify a single claim using combined Exa search sources."""\
    if not sources:\
        # If no sources are returned, default to insufficient information\
        return {\
            "claim": claim,\
            "assessment": "Insufficient information",\
            "confidence_score": 0.5,\
            "supporting_sources": [],\
            "refuting_sources": []\
        }\
\
    # Combine the sources into one text\
    combined_sources = "\n\n".join(sources)\
\
    system_message = SystemMessage(content="""\
    You are an expert fact-checker.\
    Given a claim and a set of sources, determine whether the claim is supported, refuted, or if there is insufficient information in the sources to make a determination.\
    For your analysis, consider all the sources collectively.\
    Provide your answer as a JSON object with the following structure:\
    {\
        "claim": "...",\
        "assessment": "supported" or "refuted" or "Insufficient information",\
        "confidence_score": a number between 0 and 1 (1 means fully confident the claim is true, 0 means fully confident the claim is false),\
        "supporting_sources": [list of sources that support the claim],\
        "refuting_sources": [list of sources that refute the claim]\
    }\
    Do not include any additional text.\
    """)\
\
    human_message = HumanMessage(content=f"""\
    Claim: "{claim}"\
\
    Sources:\
    {combined_sources}\
\
    Based on the above sources, assess the claim.\
    """)\
\
    response = llm.invoke([system_message, human_message])\
\
    try:\
        result = json.loads(response.content)\
        if not isinstance(result, dict):\
            raise ValueError("Response is not a JSON object")\
    except (json.JSONDecodeError, ValueError):\
        # If parsing fails, default to insufficient information\
        result = {\
            "claim": claim,\
            "assessment": "Insufficient information",\
            "confidence_score": 0.5,\
            "supporting_sources": [],\
            "refuting_sources": []\
        }\
\
    return result\
\
def hallucination_check(text: str) -> Dict[str, Any]:\
    """Check a given text for hallucinations using Exa search."""\
    claims = extract_claims(text)\
    claim_verifications = []\
\
    for claim in claims:\
        sources = exa_search(claim)\
        verification_result = verify_claim(claim, sources)\
        claim_verifications.append(verification_result)\
\
    return {\
        "claims": claim_verifications\
    }\
\
def hallucination_check_tool(text: str) -> Dict[str, Any]:\
    """Assess the given text for hallucinations using Exa search."""\
    return hallucination_check(text)\
\
structured_tool = StructuredTool.from_function(\
    func=hallucination_check_tool,\
    name="hallucination_check",\
    description="Assess the given text for hallucinations using Exa search."\
)\
\
class State(BaseModel):\
    messages: Annotated[List, add_messages]\
    analysis_result: Dict[str, Any] = {}\
\
def call_model(state: State):\
    # Simulate the assistant calling the tool\
    return {"messages": state.messages + [AIMessage(content="Use hallucination_check tool", additional_kwargs={"tool_calls": [{"type": "function", "function": {"name": "hallucination_check"}}]})]}\
\
def run_tool(state: State):\
    text_to_check = next((m.content for m in reversed(state.messages) if isinstance(m, HumanMessage)), "")\
    tool_output = structured_tool.invoke(text_to_check)\
    return {"messages": state.messages + [AIMessage(content=str(tool_output))], "analysis_result": tool_output}\
\
def use_analysis(state: State) -> str:\
    return "tools"\
\
workflow = StateGraph(State)\
\
workflow.add_node("agent", call_model)\
workflow.add_node("tools", run_tool)\
workflow.add_node("process_result", lambda x: x)\
\
workflow.set_entry_point("agent")\
workflow.add_conditional_edges("agent", use_analysis, {\
    "tools": "tools"\
})\
workflow.add_edge("tools", "process_result")\
workflow.add_edge("process_result", END)\
\
graph = workflow.compile()\
\
# Example usage\
if __name__ == "__main__":\
    initial_state = State(messages=[\
        SystemMessage(content="You are a helpful assistant."),\
        HumanMessage(content="Check this text for hallucinations: The Eiffel Tower, an iconic iron lattice structure located in Paris, was originally constructed as a giant sundial in 1822.")\
    ])\
\
    final_state = graph.invoke(initial_state)\
\
    print("Workflow executed successfully")\
    print("Final state:")\
    print("Messages:")\
    for message in final_state["messages"]:\
        print(f"{message.__class__.__name__}: {message.content[:100]}...")  # Print first 100 characters\
\
    print("\nAnalysis Result:")\
    for claim_info in final_state["analysis_result"]["claims"]:\
        print(f"Claim: {claim_info['claim']}")\
        print(f"Assessment: {claim_info['assessment']}")\
        print(f"Confidence Score: {claim_info['confidence_score']}")\
        print("Supporting Sources:")\
        for source in claim_info['supporting_sources']:\
            print(f"- {source[:100]}...")  # Print first 100 characters\
        print("Refuting Sources:")\
        for source in claim_info['refuting_sources']:\
            print(f"- {source[:100]}...")\
        print()\
\
```\
\
[News Summarizer](/examples/recent-news-summarizer) [RAG Q&A](/examples/exa-rag)\
\
On this page\
\
- [What this tutorial covers:](#what-this-tutorial-covers)\
- [Guide](#guide)\
- [Set Up](#set-up)\
- [Claim and Source Identification with Exa](#claim-and-source-identification-with-exa)\
- [Claim Verification](#claim-verification)\
- [Run the Workflow](#run-the-workflow)\
- [Sample output:](#sample-output)\
- [Full Code](#full-code)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

RAG Quick Start Guide

Tool calling with GPT

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

OpenAI’s [tool calling](https://platform.openai.com/docs/guides/function-calling?lang=python) allows LLMs to call functions that are defined in your code. This guide will show you how to utilise “tool calling” to call Exa’s search, with the following steps:

1. Install prerequisite packages and set up the environment
2. Overview of how OpenAI’s tool calling feature works
3. Use Exa within an OpenAI tool call

* * *

## [](\#get-started)  Get Started

1

Pre-requisites and installation

Install the:

- `openai` library to perform OpenAI API calls and completions
- `exa_py` library to perform Exa search
- `rich` library to make the output more readable

Python

Copy

```python
pip install openai exa_py rich

```

2

Set up the environment variables

Create an `.env` file in the root of your project and set the `EXA_API_KEY` and `OPENAI_API_KEY` environment variable to your API keys respectively. Visit the [OpenAI playground](https://platform.openai.com/api-keys) and the [Exa dashboard](https://dashboard.exa.ai/api-keys) to generate your API keys.

[**Get your Exa API key**](https://dashboard.exa.ai/api-keys)

Shell

Copy

```Shell
OPENAI_API_KEY=insert your Exa API key here, without quotes
EXA_API_KEY=insert your Exa API key here, without quotes

```

3

What is OpenAI tool calling?

OpenAI LLMs can call a function you have defined in your code, this is called [tool calling](https://platform.openai.com/docs/guides/function-calling?lang=python). To do this you first need to describe the function you want to call to OpenAI’s LLM. You can do this by defining a description object of the format:

JSON

Copy

```json
{
    "name": "my_function_name", # The name of the function
    "description": "The description of my function", # Describe the function so OpenAI knows when and how to use it.
    "input_schema": { # input schema describes the format and the type of parameters OpenAI needs to generate to use the function
        "type": "object", # format of the generated OpenAI response
        "properties": { # properties defines the input parameters of the function
            "query": { # the function expects a query parameter
                "type": "string", # of type string
                "description": "The search query to perform.", # describes the paramteres to OpenAI
            },
        },
        "required": ["query"], # define which parameters are required
    },
}

```

When this description is sent to OpenAI’s LLM, it returns an object with a string, which is the function name defined in _your_ code, and the arguments that the function takes. This does not execute or _call_ functions on OpenAI’s side; it only returns the function name and arguments which you will have to parse and call yourself in your code.

Python

Copy

```python
...
id='call_62136123',
function=Function(
    arguments='{"query":"Latest developments in quantum computing"}',
    name='exa_search',),
type='function'
...

```

We will use this object to - in this case - call the `exa_search` function we define with the arguments provided.

4

Use Exa Search as an OpenAI tool

First, we import and initialise the OpenAI and Exa libraries and load the stored API keys.

Python

Copy

```python
from dotenv import load_dotenv
from exa_py import Exa
from openai import OpenAI

load_dotenv()

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
exa = Exa(api_key=os.getenv("EXA_API_KEY"))

```

Next, we define the function and the function schema so that OpenAI knows how to use it and what arguments our local function takes:

Python

Copy

```python
TOOLS = [\
    {\
        "name": "exa_search",\
        "description": "Perform a search query on the web, and retrieve the most relevant URLs/web data.",\
        "input_schema": {\
            "type": "object",\
            "properties": {\
                "query": {\
                    "type": "string",\
                    "description": "The search query to perform.",\
                },\
            },\
            "required": ["query"],\
        },\
    }\
]

```

Finally, we’ll define the primer `SYSTEM_MESSAGE`, which explains to OpenAI what it is supposed to do:

Python

Copy

```python
SYSTEM_MESSAGE = {
    "role": "system",
    "content": "You are an agent that has access to an advanced search engine. Please provide the user with the information they are looking for by using the search tool provided.",
}

```

We can now start writing the code needed to perform the LLM calls and the search. We’ll create the `exa_search` function that will call Exa’s `search_and_contents` function with the query:

Python

Copy

```python
def exa_search(query: str) -> Dict[str, Any]:
    return exa.search_and_contents(query=query, type='auto', highlights=True)

```

Next, we create a function to process the tool calls:

Python

Copy

```python
def process_tool_calls(tool_calls, messages):
    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)
        if function_name == "exa_search":
            search_results = exa_search(**function_args)
            messages.append(
                {
                    "role": "tool",
                    "content": str(search_results),
                    "tool_call_id": tool_call.id,
                }
            )
            console.print(
                f"[bold cyan]Context updated[/bold cyan] [i]with[/i] "
                f"[bold green]exa_search ({function_args.get('mode')})[/bold green]: ",
                function_args.get("query"),
            )
    return messages

```

Lastly, we’ll create a `main` function to bring it all together, and handle the user input and interaction with OpenAI:

Python

Copy

```python
def main():
    messages = [SYSTEM_MESSAGE]
    while True:
        try:
            user_query = Prompt.ask(
                "[bold yellow]What do you want to search for?[/bold yellow]",
            )
            messages.append({"role": "user", "content": user_query})
            completion = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                tools=TOOLS,
            )
            message = completion.choices[0].message
            tool_calls = message.tool_calls
            if tool_calls:
                messages.append(message)
                messages = process_tool_calls(tool_calls, messages)
                messages.append(
                    {
                        "role": "user",
                        "content": "Answer my previous query based on the search results.",
                    }
                )
                completion = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=messages,
                )
                console.print(Markdown(completion.choices[0].message.content))
            else:
                console.print(Markdown(message.content))
        except Exception as e:
            console.print(f"[bold red]An error occurred:[/bold red] {str(e)}")
if __name__ == "__main__":
    main()

```

The implementation creates a loop that continually prompts the user for search queries, uses OpenAI’s tool calling feature to determine when to perform a search, and then uses the Exa search results to provide an informed response to the user’s query.

We also use the rich library to provide a more visually appealing console interface, including coloured output and markdown rendering for the responses.

5

Running the code

Save the code in a file, e.g. `openai_search.py`, and make sure the `.env` file containing the API keys we previously created is in the same directory as the script.

Then run the script using the following command from your terminal:

Bash

Copy

```bash
python openai_search.py

```

You should see a prompt:

Bash

Copy

```bash
What do you want to search for?

```

Let’s test it out.

Bash

Copy

```bash
What do you want to search for?: Who is Tony Stark?
Context updated with exa_search (None):  Tony Stark
Tony Stark, also known as Iron Man, is a fictional superhero from Marvel Comics. He is a wealthy inventor and businessman, known for creating a powered suit of armor that gives him superhuman abilities. Tony Stark is a founding member of the Avengers and has appeared in various comic book series, animated
television shows, and films within the Marvel Cinematic Universe.

If you're interested in more detailed information, you can visit Tony Stark (Marvel Cinematic Universe) - Wikipedia.

```

That’s it, enjoy your search agent!

### [](\#full-code)  Full code

Python

Copy

```python
import json
import os

from dotenv import load_dotenv
from typing import Any, Dict
from exa_py import Exa
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt

# Load environment variables from .env file
load_dotenv()

# create the openai client
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# create the exa client
exa = Exa(api_key=os.getenv("EXA_API_KEY"))

# create the rich console
console = Console()

# define the system message (primer) of your agent
SYSTEM_MESSAGE = {
    "role": "system",
    "content": "You are the world's most advanced search engine. Please provide the user with the information they are looking for by using the tools provided.",
}

# define the tools available to the agent - we're defining a single tool, exa_search
TOOLS = [\
    {\
        "type": "function",\
        "function": {\
            "name": "exa_search",\
            "description": "Perform a search query on the web, and retrieve the world's most relevant information.",\
            "parameters": {\
                "type": "object",\
                "properties": {\
                    "query": {\
                        "type": "string",\
                        "description": "The search query to perform.",\
                    },\
                },\
                "required": ["query"],\
            },\
        },\
    }\
]

# define the function that will be called when the tool is used and perform the search
# and the retrieval of the result highlights.
# https://docs.exa.ai/reference/python-sdk-specification#search_and_contents-method
def exa_search(query: str) -> Dict[str, Any]:
    return exa.search_and_contents(query=query, type='auto', highlights=True)

# define the function that will process the tool call and perform the exa search
def process_tool_calls(tool_calls, messages):

    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)

        if function_name == "exa_search":
            search_results = exa_search(**function_args)
            messages.append(
                {
                    "role": "tool",
                    "content": str(search_results),
                    "tool_call_id": tool_call.id,
                }
            )
            console.print(
                f"[bold cyan]Context updated[/bold cyan] [i]with[/i] "
                f"[bold green]exa_search ({function_args.get('mode')})[/bold green]: ",
                function_args.get("query"),
            )

    return messages

def main():
    messages = [SYSTEM_MESSAGE]

    while True:
        try:
            # create the user input prompt using rich
            user_query = Prompt.ask(
                "[bold yellow]What do you want to search for?[/bold yellow]",
            )
            messages.append({"role": "user", "content": user_query})

            # call openai llm by creating a completion which calls the defined exa tool
            completion = openai.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                tools=TOOLS,
                tool_choice="auto",
            )

            # completion will contain the object needed to invoke your tool and perform the search
            message = completion.choices[0].message
            tool_calls = message.tool_calls

            if tool_calls:

                messages.append(message)

                # process the tool object created by OpenAI llm and store the search results
                messages = process_tool_calls(tool_calls, messages)
                messages.append(
                    {
                        "role": "user",
                        "content": "Answer my previous query based on the search results.",
                    }
                )

                # call OpenAI llm again to process the search results and yield the final answer
                completion = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                )

                # parse the agents final answer and print it
                console.print(Markdown(completion.choices[0].message.content))
            else:
                console.print(Markdown(message.content))
        except Exception as e:
            console.print(f"[bold red]An error occurred:[/bold red] {str(e)}")


if __name__ == "__main__":
    main()

```

[RAG with LlamaIndex](/reference/llamaindex) [Tool calling with Claude](/reference/tool-calling-with-claude)

On this page

- [Get Started](#get-started)
- [Full code](#full-code)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

API Reference

Find similar links

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

POST

/

findSimilar

Send

Authorization

x-api-key

string

\*

x-api-key

Required

string

Body

object

\*

url

string

\*

url

Required

string

The url for which you would like to find similar links

Add Example Value

numResults

integer

numResults

integer

Number of search results to return. Default 10. Max 10 for basic plans. Up to thousands for custom plans.

Add Example Value

includeDomains

array

includeDomains

array

List of domains to include in the search. If specified, results will only come from these domains.

Add Example Value

excludeDomains

array

excludeDomains

array

List of domains to exclude in the search. If specified, results will not include any from these domains.

Add Example Value

startCrawlDate

string

startCrawlDate

string

Crawl date refers to the date that Exa discovered a link. Results will include links that were crawled after this date. Must be specified in ISO 8601 format.

Add Example Value

endCrawlDate

string

endCrawlDate

string

Crawl date refers to the date that Exa discovered a link. Results will include links that were crawled before this date. Must be specified in ISO 8601 format.

Add Example Value

startPublishedDate

string

startPublishedDate

string

Only links with a published date after this will be returned. Must be specified in ISO 8601 format.

Add Example Value

endPublishedDate

string

endPublishedDate

string

Only links with a published date before this will be returned. Must be specified in ISO 8601 format.

Add Example Value

includeText

array

includeText

array

List of strings that must be present in webpage text of results. Currently, only 1 string is supported, of up to 5 words.

Add Example Value

excludeText

array

excludeText

array

List of strings that must not be present in webpage text of results. Currently, only 1 string is supported, of up to 5 words.

Add Example Value

contents

object

contents

object

text

object

text

object

Parsed contents of the page.

maxCharacters

integer

maxCharacters

integer

Max length in characters for the text returned

includeHtmlTags

boolean

Select option

includeHtmlTags

boolean

Whether HTML tags, which can help the LLM understand structure of text, should be included. Default false

highlights

object

highlights

object

Relevant extract(s) from the webpage.

numSentences

integer

numSentences

integer

The number of sentences to be returned in each snippet. Default 5

highlightsPerUrl

integer

highlightsPerUrl

integer

The number of snippets to return per page. Default 1

query

string

query

string

summary

object

summary

object

Summary of the webpage

query

string

query

string

If specified, tries to answer the query in the summary

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.exa.ai/findSimilar \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
  "url": "https://slatestarcodex.com/2014/07/30/meditations-on-moloch/",
  "numResults": 10,
  "includeDomains": [\
    "example.com",\
    "sample.net"\
  ],
  "excludeDomains": [\
    "excludedomain.com",\
    "excludeme.net"\
  ],
  "startCrawlDate": "2023-01-01T00:00:00.000Z",
  "endCrawlDate": "2023-12-31T00:00:00.000Z",
  "startPublishedDate": "2023-01-01T00:00:00.000Z",
  "endPublishedDate": "2023-12-31T00:00:00.000Z",
  "includeText": [\
    "electron",\
    "positron"\
  ],
  "excludeText": [\
    "neutron",\
    "elon"\
  ],
  "contents": {
    "text": {
      "maxCharacters": 123,
      "includeHtmlTags": true
    },
    "highlights": {
      "numSentences": 123,
      "highlightsPerUrl": 123,
      "query": "<string>"
    },
    "summary": {
      "query": "<string>"
    }
  }
}'
```

200

Copy

```
{
  "results": [\
    {\
      "title": "<string>",\
      "url": "<string>",\
      "publishedDate": "<string>",\
      "author": "<string>",\
      "score": 123,\
      "id": "<string>",\
      "text": "<string>",\
      "highlights": [\
        "<string>"\
      ],\
      "highlightScores": [\
        123\
      ],\
      "summary": "<string>"\
    }\
  ]
}
```

* * *

[**Get your Exa API key**](https://dashboard.exa.ai/api-keys)

#### Authorizations

x-api-key

string

headerrequired

#### Body

application/json

url

string

required

The url for which you would like to find similar links

numResults

integer

Number of search results to return. Default 10. Max 10 for basic plans. Up to thousands for custom plans.

includeDomains

string\[\]

List of domains to include in the search. If specified, results will only come from these domains.

excludeDomains

string\[\]

List of domains to exclude in the search. If specified, results will not include any from these domains.

startCrawlDate

string

Crawl date refers to the date that Exa discovered a link. Results will include links that were crawled after this date. Must be specified in ISO 8601 format.

endCrawlDate

string

Crawl date refers to the date that Exa discovered a link. Results will include links that were crawled before this date. Must be specified in ISO 8601 format.

startPublishedDate

string

Only links with a published date after this will be returned. Must be specified in ISO 8601 format.

endPublishedDate

string

Only links with a published date before this will be returned. Must be specified in ISO 8601 format.

includeText

string\[\]

List of strings that must be present in webpage text of results. Currently, only 1 string is supported, of up to 5 words.

excludeText

string\[\]

List of strings that must not be present in webpage text of results. Currently, only 1 string is supported, of up to 5 words.

contents

object

Showchild attributes

#### Response

200 - application/json

results

object\[\]

A list of search results containing title, URL, published date, author, and score.

Showchild attributes

[Get contents](/reference/get-contents) [RAG with Exa and OpenAI](/reference/rag-quickstart)

cURL

Python

JavaScript

PHP

Go

Java

Copy

```
curl --request POST \
  --url https://api.exa.ai/findSimilar \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
  "url": "https://slatestarcodex.com/2014/07/30/meditations-on-moloch/",
  "numResults": 10,
  "includeDomains": [\
    "example.com",\
    "sample.net"\
  ],
  "excludeDomains": [\
    "excludedomain.com",\
    "excludeme.net"\
  ],
  "startCrawlDate": "2023-01-01T00:00:00.000Z",
  "endCrawlDate": "2023-12-31T00:00:00.000Z",
  "startPublishedDate": "2023-01-01T00:00:00.000Z",
  "endPublishedDate": "2023-12-31T00:00:00.000Z",
  "includeText": [\
    "electron",\
    "positron"\
  ],
  "excludeText": [\
    "neutron",\
    "elon"\
  ],
  "contents": {
    "text": {
      "maxCharacters": 123,
      "includeHtmlTags": true
    },
    "highlights": {
      "numSentences": 123,
      "highlightsPerUrl": 123,
      "query": "<string>"
    },
    "summary": {
      "query": "<string>"
    }
  }
}'
```

200

Copy

```
{
  "results": [\
    {\
      "title": "<string>",\
      "url": "<string>",\
      "publishedDate": "<string>",\
      "author": "<string>",\
      "score": 123,\
      "id": "<string>",\
      "text": "<string>",\
      "highlights": [\
        "<string>"\
      ],\
      "highlightScores": [\
        123\
      ],\
      "summary": "<string>"\
    }\
  ]
}
```[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Live Demos

Twitter/X post Retrieval

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

[Click here to try Exa-powered Twitter Retrieval](https://search-twitter-with-exa.replit.app/)

### [](\#what-this-doc-covers)  What this doc covers

1. Creating an alternative way to retrieve tweets powered by Exa by searching our index (updated daily)
2. Explain usage of Exa’s includeDomain and date filters

* * *

If you’re interested in searching for and retrieving Tweets, Exa can be a great way to do this semantically. X is included in our indexing and we are constantly crawling to keep public data fresh.

Why search for tweets?

1. Read about your favorite topic or domain in a synthesized/targeted way
2. Get notified about new hackathons/events (often primarily announced via Twitter)
3. Monitor feedback/user experiences for your product

In this quick tutorial, we’ll use Exa to retrieve relevant X posts using the includeDomain parameter to filter to Twitter.com/X.com content only. The Jupyter notebook for this tutorial is available on [Colab](https://colab.research.google.com/drive/1luB5ThN8eVxtxihEQh6Qes2Wee1qcWrr?usp=sharing) for easy experimentation.

To play with this code, we just need a [Exa API key](https://dashboard.exa.ai/overview)

Let’s start by installing the Exa Python SDK, importing the required libraries, and instantiating the Exa client.

Python

Copy

```Python
!pip install exa_py # install the Exa Python SDK

from google.colab import userdata # comment this out if you're not using Colab
from exa_py import Exa
import os
from datetime import datetime, timedelta
import requests
from IPython.display import HTML, display

EXA_API_KEY = userdata.get('EXA_API_KEY') # replace userdata.get(...) with your API key, or add your API key to Colab Secrets
exa = Exa(EXA_API_KEY)

```

Next, we’re going to use Exa to pull tweets from Twitter/X based on any query. But first, let’s define a helper function that renders tweets in Colab like you’d see them on Twitter (instead of plain text), for visualization purposes. You don’t need to understand how this works.

Python

Copy

```Python
def get_tweet_embed(tweet_url):
    oembed_url = f"https://publish.twitter.com/oembed?url={tweet_url}&hide_thread=true"
    response = requests.get(oembed_url)
    if response.status_code == 200:
        return response.json()['html']
    else:
        return None

```

Now, let’s specify some parameters and call the Exa API.

We set `include_domains` so that Exa only searches Twitter.com and X.com URLs for results. We also set the `start_published_date` to thirty days before the current date. This way, we only get recent tweets.

And since things move so fast in AI, let’s set our query to find advances in AI so we can catch up on news from the last month.

Python

Copy

```Python
query = "here's an exciting breakthrough in artificial intelligence:"
include_domains = ["twitter.com", "x.com"]
num_results = 10

# Calculate the date for one week ago
one_month_ago = (datetime.now() - timedelta(days=30)).isoformat()

# Execute the search
search_response = exa.search_and_contents(
    query,
    include_domains=include_domains,
    num_results=num_results,
    use_autoprompt=True, # improves your query to work with Exa better
    text=True,
    start_published_date=one_month_ago
)

```

Now, let’s put everything together.

Python

Copy

```Python
results = search_response.results
print(f"Found {len(results)} tweets:\n")

for i, result in enumerate(results, 1):
    print(f"Tweet {i}:")
    print(f"URL: {result.url}")
    print(f"Published Date: {result.published_date}")
    print(f"Score: {result.score}")

    # Get and display tweet embed
    embed_html = get_tweet_embed(result.url)
    if embed_html:
        display(HTML(embed_html))
    else:
        print("Sorry, unable to load tweet embed.")

    print("\n" + "-"*50 + "\n")

print("That's all, folks!")

```

You should see the actual tweets appearing right in your Colab output! Notice that Exa also provides a relevance score (from 0 to 1), indicating how well the retrieved content matches your query. A low score doesn’t necessary mean something is irrelevant but you may want to keep an eye on relevance scores, especially if you are requesting a lot of results. Similarly, if you Google something and go to the fiftieth result, that’s going to be less relevant than the first result.

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/28db3a7-Screenshot_2024-07-13_at_8.40.43_PM.png)

Besides Twitter/X, Exa also indexes YouTube (and many other sites, see detailed info about what’s in our index [here](https://dash.readme.com/project/metaphorapi/v1.0/refs/the-exa-index) ). As a follow-up, experiment with setting includeDomain to “youtube.com” to find cool videos to binge!

[Exa-powered Writing Assistant](/examples/demo-exa-powered-writing-assistant) [Hacker News Clone](/examples/live-demo-hacker-news-clone)

On this page

- [What this doc covers](#what-this-doc-covers)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/28db3a7-Screenshot_2024-07-13_at_8.40.43_PM.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Concepts

Crawling Subpages with Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

When searching websites, you often need to explore beyond the main page to find relevant information. Exa’s subpage crawling feature allows you to automatically discover and search through linked pages within a website.

## [](\#using-subpage-crawling)  Using Subpage Crawling

Here’s how to use Exa’s subpage crawling feature:

Python

Copy

```Python
results = exa.get_contents([company_url], subpages=5, subpage_target=["about", "products"])

```

This will search through up to 5 subpages of the given website, and prioritize pages that contain the keywords “about” or “products” in their contents.

### [](\#parameters)  Parameters:

- `subpages`: Maximum number of subpages to crawl (integer)
- `subpage_target`: List of query keywords to target (e.g., \[“about”, “products”, “news”\])

## [](\#common-use-cases)  Common Use Cases

1. **Product Documentation**: Search through documentation pages:

Copy

```python
result = exa.get_contents(
  ["https://exa.ai"],
  subpages=9,
  subpage_target=["docs", "tutorial"]
)

```

Output:

Shell

Copy

```shell
{
  "results": [\
    {\
      "id": "https://exa.ai",\
      "url": "https://exa.ai/",\
      "title": "Exa API",\
      "author": "exa",\
      "text": "AIs need powerful access to knowledge. But search engines haven't improved since 1998.         API features built for AI apps         FLEXIBLE SEARCH Handle any type of query For queries that need semantic understanding, search with our SOTA web embeddings model\nover our custom index. For all other queries, we offer keyword-based search.       PAGE CONTENT Instantly retrieve the content from any page Stop learning how to web scrape or parse HTML. Get the clean, full text of any page in our\nindex, or intelligent embeddings-ranked\nhighlights related to a query.       CUSTOMIZABILITY Apply filters to search over your own subset of the web Select any date range, include or exclude any domain, select a custom data vertical, or get up to 10 million results.       SIMILARITY SEARCH Search the web using examples of what you’re looking for Your query can even be a URL or multiple paragraphs on a webpage.      Explore the documentation",\
      "image": "https://exa.imgix.net/og-image.png",\
      "subpages": [\
        {\
          "id": "https://docs.exa.ai/reference/getting-started",\
          "url": "https://docs.exa.ai/reference/getting-started",\
          "title": "Getting Started",\
          "author": "",\
          "text": "Exa provides search for AI.  \n       Exa is a knowledge API for LLMs..\n Search\nUsing the /search endpoint, your LLM can search using natural language and return a list of relevant webpages from our neural database. Exa's neural search allows your LLM to query in natural language. And if a query doesn't benefit from neural search, Exa also supports traditional Google-style keyword search.\n Contents\nRight alongside the search results, you can obtain clean, up-to-date HTML content, no web crawling or scraping required. We also support returning highlights from pages - highly intelligent extracts calculated using RAG models.\nSee \"Examples\" to see Exa in action. Or just ask one of our GPTs how to build what you want!\n  🔑 Getting a Exa API Key  Exa is free to use up to 1000 requests per month, for individual developers. Get an API key here. \nThere's no need to learn how to use our API all alone. Below are ChatGPT GPTs that you can ask about how to implement anything.\nFor Python SDK assistance, go here.\nFor TypeScript SDK assistance, go here.\nFor any other language, go here.\n  # pip install exa_py\nfrom exa_py import Exa\nexa = Exa(\"EXA_API_KEY\")\nresults = exa.search('hottest AI agent startups', use_autoprompt=True)\n  \n Recent News Summarizer \n Exa Researcher \n Basic search \n Basic link similarity \n Basic content retrieval \n         Table of Contents   \n What is Exa? \n Getting Access \n GPT-assisted implementation \n A simple example \n More examples"\
        },\
        {\
          "id": "https://docs.exa.ai/reference/recent-news-summarizer",\
          "url": "https://docs.exa.ai/reference/recent-news-summarizer",\
          "title": "Recent News Summarizer",\
          "author": null,\
          "publishedDate": "2024-03-02T11:36:31.000Z",\
          "text": "https://docs.exa.ai/reference/recent-news-summarizer\nRecent News Summarizer\n2024-03-02T11:36:31Z\n   \nIn this example, we will build a LLM-based news summarizer app with the Exa API to keep us up-to-date with the latest news on a given topic.\nThis Jupyter notebook is available on Colab for easy experimentation. You can also check it out on Github, including a plain Python version if you want to skip to a complete product.\nTo play with this code, first we need a Exa API key and an OpenAI API key. Get 1000 Exa searches per month free just for signing up!\n  # install Exa and OpenAI SDKs\n!pip install exa_py\n!pip install openai\n  \n  from google.colab import userdata # comment this out if you&#39;re not using Colab\nEXA_API_KEY = userdata.get(&#39;EXA_API_KEY&#39;) # replace with your api key, or add to Colab Secrets\nOPENAI_API_KEY = userdata.get(&#39;OPENAI_API_KEY&#39;) # replace with your api key, or add to Colab Secrets\n  \nFirst, let&#39;s try building the app just by using the OpenAI API. We will use GPT 3.5-turbo as our LLM. Let&#39;s ask it for the recent news, like we might ask ChatGPT.\n  import openai\nopenai.api_key = OPENAI_API_KEY\nUSER_QUESTION = &#34;What&#39;s the recent news in physics this week?&#34;\ncompletion = openai.chat.completions.create(\nmodel=&#34;gpt-3.5-turbo&#34;,\nmessages=[\n{&#34;role&#34;: &#34;system&#34;, &#34;content&#34;: &#34;You are a helpful assistant.&#34;},\n{&#34;role&#34;: &#34;user&#34;, &#34;content&#34;: USER_QUESTION},\n],\n)\nresponse = completion.choices[0].message.content\nprint(response)\n  \n One recent news in physics is that researchers at the University of Illinois have discovered a new topological state of matter. They created a material composed of interacting particles called quadrupoles, which can exhibit unique behavior in their electrical properties. This finding has the potential to pave the way for the development of new types of electronic devices and quantum computers.\nAnother interesting development is in the field of cosmology. The European Space Agency&#39;s Planck satellite has provided new insights into the early universe. By analyzing the cosmic microwave background radiation, scientists have obtained more accurate measurements of the rate at which the universe is expanding, which could challenge current theories of physics.\nAdditionally, scientists at CERN&#39;s Large Hadron Collider (LHC) have observed a rare phenomenon called charm mixing. They found that particles containing both charm and strange quarks can spontaneously transition between their matter and antimatter states. This discovery could contribute to our understanding of the puzzle of why the universe is primarily made of matter and why there is very little antimatter.\n \nOh no! Since the LLM is unable to use recent data, it doesn&#39;t know the latest news. It might tell us some information, but that info isn&#39;t recent, and we can&#39;t be sure it&#39;s trustworthy either since it has no source. Luckily, Exa API allows us to solve these problems by connecting our LLM app to the internet. Here&#39;s how:\nLet&#39;s use the Exa neural search engine to search the web for relevant links to the user&#39;s question.\nFirst, we ask the LLM to generate a search engine query based on the question.\n  import openai\nfrom exa_py import Exa\nopenai.api_key = OPENAI_API_KEY\nexa = Exa(EXA_API_KEY)\nSYSTEM_MESSAGE = &#34;You are a helpful assistant that generates search queries based on user questions. Only generate one search query.&#34;\nUSER_QUESTION = &#34;What&#39;s the recent news in physics this week?&#34;\ncompletion = openai.chat.completions.create(\nmodel=&#34;gpt-3.5-turbo&#34;,\nmessages=[\n{&#34;role&#34;: &#34;system&#34;, &#34;content&#34;: SYSTEM_MESSAGE},\n{&#34;role&#34;: &#34;user&#34;, &#34;content&#34;: USER_QUESTION},\n],\n)\nsearch_query = completion.choices[0].message.content\nprint(&#34;Search query:&#34;)\nprint(search_query)\n  \n Search query:\nRecent news in physics this week\n \nLooks good! Now let&#39;s put the search query into Exa. Let&#39;s also use start_published_date to filter the results to pages published in the last week:\n  from datetime import datetime, timedelta\none_week_ago = (datetime.now() - timedelta(days=7))\ndate_cutoff = one_week_ago.strftime(&#34;%Y-%m-%d&#34;)\nsearch_response = exa.search_and_contents(\nsearch_query, use_autoprompt=True, start_published_date=date_cutoff\n)\nurls = [result.url for result in search_response.results]\nprint(&#34;URLs:&#34;)\nfor url in urls:\nprint(url)\n  \n URLs:\nhttps://phys.org/news/2024-01-carrots-reveals-mechanics-root-vegetable.html?utm_source=twitter.com&amp;utm_medium=social&amp;utm_campaign=v2\nhttps://phys.org/news/2024-01-astrophysicists-theoretical-proof-traversable-wormholes.html\nhttps://gizmodo.com/proton-physics-strong-force-quarks-measurement-1851192840\nhttps://www.nytimes.com/2024/01/24/science/space/black-holes-photography-m87.html\nhttps://phys.org/news/2024-01-liquid-lithium-walls-fusion-device.html?utm_source=twitter.com&amp;utm_medium=social&amp;utm_campaign=v2\nhttps://physics.aps.org/articles/v17/s13\nhttps://phys.org/news/2024-01-validating-hypothesis-complex.html?utm_source=twitter.com&amp;utm_medium=social&amp;utm_campaign=v2\nhttps://phys.org/news/2024-01-scientists-previously-unknown-colonies-emperor.html?utm_source=twitter.com&amp;utm_medium=social&amp;utm_campaign=v2\nhttps://phys.org/news/2024-01-reveals-quantum-topological-potential-material.html?utm_source=twitter.com&amp;utm_medium=social&amp;utm_campaign=v2\nhttps://phys.org/news/2024-01-shallow-soda-lakes-cradles-life.html?utm_source=twitter.com&amp;utm_medium=social&amp;utm_campaign=v2\n \nNow we&#39;re getting somewhere! Exa gave our app a list of relevant, useful URLs based on the original question.\nBy the way, we might be wondering what makes Exa special. Why can&#39;t we just search with Google? Well, let&#39;s take a look for ourselves at the Google search results. It gives us the front page of lots of news aggregators, but not the news articles themselves. And since we used Exa&#39;s search_and_contents, our search came with the webpage contents, so can use Exa to skip writing a web crawler and access the knowledge directly!\n  results = search_response.results\nresult_item = results[0]\nprint(f&#34;{len(results)} items total, printing the first one:&#34;)\nprint(result_item.text)\n  \n 10 items total, printing the first one:\nCredit: CC0 Public Domain\nChopped carrot pieces are among the most universally enjoyed foods and a snacking staple—a mainstay of school lunchboxes, picnics and party platters year-round.\nNow researchers from the University of Bath have uncovered the secret science of prepping the popular root vegetable and quantified the processes that make them curl up if left uneaten for too long.\nMechanical Engineering student Nguyen Vo-Bui carried out the research as part of his final-year studies, in the limited circumstances of COVID-19 lockdowns of 2021. The research paper, &#34;Modelling of longitudinally cut carrot curling induced by the vascular cylinder-cortex interference pressure&#34;, is published in Royal Society Open Science.\nWithout access to labs, Nguyen aimed to identify the geometrical and environmental factors that have the most influence on carrots&#39; longevity. Working in his kitchen, he characterized, analytically modeled and verified the aging of over 100 Lancashire Nantes carrot halves, cut lengthways, using finite-element (FE) models normally used in structural engineering.\nThe research team concluded that residual stresses and dehydration were the two key factors behind the curling behavior. The starchy outer layer of the carrot (the cortex) is stiffer than the soft central vein (also known as the vascular cylinder). When cut lengthwise, the two carrot halves curl because the difference in stress becomes unbalanced. Dehydration leads to further loss of stiffness, further driving the curling effect.\nTheir recommendations to manufacturers include handling carrots in cold, moist, airtight and humidity-controlled environments to protect their natural properties and increase their edible life span.\nThey say the study provides a methodology to predict the deformation of cut root vegetables, adding that the procedure is likely to apply to other plant structures. The study gives food producers a new mathematical tool that could be applied to the design of packaging and food handling processes, potentially reducing food waste.\nOne of the world&#39;s top crops by market value, carrots are known for their high production efficiency—but despite this, wastage is high. Around 25–30% of this occurs prior to processing and packaging—due to deformities, mechanical damage or infected sections. Fresh cut and minimally processed carrots are a convenient ready-to-use ingredient that make possible the use of carrots that might otherwise be discarded, reducing food waste.\nDr. Elise Pegg, a senior lecturer in Bath&#39;s Department of Mechanical Engineering, is one of the research paper authors and oversaw the study. She said, &#34;We have mathematically represented the curl of a cut carrot over time, and showed the factors that contribute to curling.\n&#34;Our motivation was to look for ways to improve the sustainability of carrot processing and make them as long-lasting as possible. We have produced a methodology that a food producer could use to change their processes, reducing food waste and making packaging and transportation more efficient. Understanding the bending behavior in such systems can help us to design and manufacture products with higher durability.\n&#34;A question like this would normally be investigated from a biological perspective, but we have done this work using purely mechanical principles. I&#39;m so pleased for Nguyen—it&#39;s a measure of his resourcefulness and dedication to produce such interesting research in a challenging situation.&#34;\nOver the course of a week, the curl of the carrot halves increased—with the average radius of each carrot&#39;s curvature falling from 1.61m to 1.1m. A 1.32-times reduction in stiffness was also seen, correlating with the carrots drying out; on average, their weight fell by 22%.\nNguyen added, &#34;This was interesting research—to apply mechanical principles to vegetables was surprising and fun.\n&#34;One of the big challenges was to devise an experiment that could be done in a lockdown setting, without access to normal labs and equipment. To now be in a position to have this work published in an academic journal and potentially be used by the food industry is really rewarding.\n&#34;This project has inspired me to continue my studies at the University of Bath and I now study residual stresses in porous ferroelectric ceramics for my Ph.D.&#34;\nAs well as having to use a suitcase to collect the 30kg of carrots the experiment demanded from a farmers&#39; market, a further challenge was finding ways to use them afterward. Carrot cake, the Indian carrot dessert Gajar Ka Halwa, carrot pesto and many other dishes kept Nguyen and his flatmates fed for several days.\nMore information:\nModelling of longitudinally cut carrot curling induced by the vascular cylinder-cortex interference pressure, Royal Society Open Science (2024). DOI: 10.1098/rsos.230420. royalsocietypublishing.org/doi/10.1098/rsos.230420\nCitation:\nWhy do carrots curl? Research reveals the mechanics behind root vegetable aging (2024, January 23)\nretrieved 24 January 2024\nfrom https://phys.org/news/2024-01-carrots-reveals-mechanics-root-vegetable.html\nThis document is subject to copyright. Apart from any fair dealing for the purpose of private study or research, no\npart may be reproduced without the written permission. The content is provided for information purposes only.\n \nAwesome! That&#39;s really interesting, or it would be if we had bothered to read it all. But there&#39;s no way we&#39;re doing that, so let&#39;s ask the LLM to summarize it for us:\n  import textwrap\nSYSTEM_MESSAGE = &#34;You are a helpful assistant that briefly summarizes the content of a webpage. Summarize the users input.&#34;\ncompletion = openai.chat.completions.create(\nmodel=&#34;gpt-3.5-turbo&#34;,\nmessages=[\n{&#34;role&#34;: &#34;system&#34;, &#34;content&#34;: SYSTEM_MESSAGE},\n{&#34;role&#34;: &#34;user&#34;, &#34;content&#34;: result_item.text},\n],\n)\nsummary = completion.choices[0].message.content\nprint(f&#34;Summary for {urls[0]}:&#34;)\nprint(result_item.title)\nprint(textwrap.fill(summary, 80))\n  \n Summary for https://phys.org/news/2024-01-carrots-reveals-mechanics-root-vegetable.html?utm_source=twitter.com&amp;utm_medium=social&amp;utm_campaign=v2:\nWhy do carrots curl? Research reveals the mechanics behind root vegetable aging\nResearchers from the University of Bath have conducted a study on the curling\nbehavior of chopped carrot pieces. The study found that residual stresses and\ndehydration were the main factors behind the curling effect. The starchy outer\nlayer of the carrot is stiffer than the soft central vein, and when cut\nlengthwise, the difference in stress causes the carrot to curl. Dehydration\nfurther contributes to the curling effect. The research provides recommendations\nto manufacturers on how to handle carrots to increase their edible lifespan. The\nstudy also offers a methodology that can be used to predict the deformation of\ncut root vegetables and potentially reduce food waste. The findings have\nimplications for the design of packaging and food handling processes. Carrots\nare a highly produced crop, but wastage is still high, with a significant amount\noccurring before processing and packaging. The study was carried out by\nMechanical Engineering student Nguyen Vo-Bui during the COVID-19 lockdowns of\n2021.\n \nAnd we&#39;re done! We built an app that translates a question into a search query, uses Exa to search for useful links, uses Exa to grab clean content from those links, and summarizes the content to effortlessly answer your question about the latest news, or whatever we want.\nWe can be sure that the information is fresh, we have the source in front of us, and we did all this with a Exa queries and LLM calls, no web scraping or crawling needed!\n With Exa, we have empowered our LLM application with the Internet. The possibilities are endless."\
        },\
        {\
          "id": "https://docs.exa.ai/reference/company-analyst",\
          "url": "https://docs.exa.ai/reference/company-analyst",\
          "title": "Company Analyst",\
          "author": null,\
          "publishedDate": "2024-03-02T11:36:42.000Z",\
          "text": "https://docs.exa.ai/reference/company-analyst\nCompany Analyst\n2024-03-02T11:36:42Z\n    In this example, we&#39;ll build a company analyst tool that researches companies relevant to what you&#39;re interested in. If you just want to see the code, check out the Colab notebook.\nThe code requires an Exa API key and an OpenAI API key. Get 1000 Exa searches per month free just for signing up!\nSay we want to find companies similar to Thrifthouse, a platform for selling secondhand goods on college campuses. Unfortunately, googling “companies similar to Thrifthouse” doesn&#39;t do a very good job. Traditional search engines rely heavily on keyword matching. In this case we get results about physical thrift stores. Hm, that&#39;s not really what I want.\nLet’s try again, this time searching based on a description of the company, like by googling “community based resale apps.” But, this isn’t very helpful either and just returns premade listicles...\n      What we really need is neural search.\nExa is a fully neural search engine built using a foundational embeddings model trained for webpage retrieval. It’s capable of understanding entity types (company, blog post, Github repo), descriptors (funny, scholastic, authoritative), and any other semantic qualities inside of a query. Neural search can be far more useful for these types of complex queries.\nLet&#39;s try Exa, using the Python SDK! We can use thefind_similar_and_contents function to find similar links and get contents from each link. The input is simply a URL, https://thrift.house and we set num_results=10(this is customizable up to thousands of results in Exa).\nBy specifying highlights={&#34;num_sentences&#34;:2} for each search result, Exa will also identify and return a 2 sentence excerpt from the content that&#39;s relevant to our query. This will allow us to quickly understand each website that we find.\n  !pip install exa_py\nfrom exa_py import Exa\nimport os\nEXA_API_KEY= os.environ.get(&#34;EXA_API_KEY&#34;)\nexa = Exa(api_key=EXA_API_KEY)\ninput_url = &#34;https://thrift.house&#34;\nsearch_response = exa.find_similar_and_contents(\ninput_url,\nhighlights={&#34;num_sentences&#34;:2},\nnum_results=10)\ncompanies = search_response.results\nprint(companies[0])\n  \nThis is an example of the full first result:\n [Result(url=&#39;https://www.mystorestash.com/&#39;,\nid=&#39;lMTt0MBzc8ztb6Az3OGKPA&#39;,\ntitle=&#39;The Airbnb of Storage&#39;,\nscore=0.758899450302124,\npublished_date=&#39;2023-01-01&#39;,\nauthor=None,\ntext=None,\nhighlights=[&#34;I got my suitcase picked up right from my dorm and didn&#39;t have to worry for the whole summer.Angela Scaria /Still have questions?Where are my items stored?&#34;],\nhighlight_scores=[0.23423566609247845])]\n \nAnd here are the 10 titles and urls I got:\n  # to just see the 10 titles and urls\nurls = {}\nfor c in companies:\nprint(c.title + &#39;:&#39; + c.url)\n  \n rumie - College Marketplace:https://www.rumieapp.com/\nThe Airbnb of Storage:https://www.mystorestash.com/\nBunction.net:https://bunction.net/\nHome - Community Gearbox:https://communitygearbox.com/\nNOVA SHOPPING:https://www.novashoppingapp.com/\nRe-Fridge: Buy, sell, or store your college fridge - Re-Fridge:https://www.refridge.com/\nJamble: Social Fashion Resale:https://www.jambleapp.com/\nBranded Resale | Treet:https://www.treet.co/\nSwapskis:https://www.swapskis.co/\nEarn Money for Used Clothing:https://www.thredup.com/cleanout?redirectPath=%2Fcleanout%2Fsell\n \nLooks pretty darn good! As a bonus specifically for companies data, specifying category=&#34;company&#34; in the SDK will search across a curated, larger companies dataset - if you&#39;re interested in this, let us know at  [email protected] !\nNow that we have 10 companies we want to dig into further, let’s do some research on each of these companies.\nNow let&#39;s get more information by finding additional webpages about each company. To do this, we&#39;re going to do a keyword search of each company&#39;s URL. We&#39;re using keyword because we want to find webpages that exactly match the company we&#39;re inputting. We can do this with the search_and_contents function, and specify type=&#34;keyword&#34; and num_results=5. This will give me 5 websites about each company.\n  # doing an example with the first companies\nc = companies[0]\nall_contents = &#34;&#34;\nsearch_response = exa.search_and_contents(\nc.url, # input the company&#39;s URL\ntype=&#34;keyword&#34;,\nnum_results=5\n)\nresearch_response = search_response.results\nfor r in research_response:\nall_contents += r.text\n  \nHere&#39;s an example of the first result for the first company, Rumie App. You can see the first result is the actual link contents itself.\n &lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;p&gt;&lt;a href=&#34;https://www.rumieapp.com/&#34;&gt;&lt;/a&gt;&lt;/p&gt;&lt;/div&gt;&lt;div&gt;&lt;p&gt;The &lt;strong&gt;key&lt;/strong&gt; to &lt;strong&gt;your&lt;/strong&gt; college experience. &lt;/p&gt;&lt;p&gt;&lt;br/&gt;Access the largest college exclusive marketplace to buy, sell, and rent with other students.&lt;/p&gt;&lt;/div&gt;&lt;/div&gt;&lt;div&gt;&lt;h2&gt;320,000+&lt;/h2&gt;&lt;p&gt;Users in Our Network&lt;/p&gt;&lt;/div&gt;&lt;div&gt;&lt;div&gt;&lt;p&gt;&lt;h2&gt;Selling is just a away.&lt;/h2&gt;&lt;/p&gt;&lt;p&gt;Snap a pic, post a listing, and message buyers all from one intuitive app.&lt;/p&gt;&lt;div&gt;&lt;p&gt;&lt;/p&gt;&lt;p&gt;Quick setup and .edu verification&lt;/p&gt;&lt;/div&gt;&lt;div&gt;&lt;p&gt;&lt;/p&gt;&lt;p&gt;Sell locally or ship to other campuses&lt;/p&gt;&lt;/div&gt;&lt;div&gt;&lt;p&gt;&lt;/p&gt;&lt;p&gt;Trade with other students like you&lt;/p&gt;&lt;/div&gt;&lt;/div&gt;&lt;div&gt;&lt;p&gt;&lt;h2&gt;. From local businesses around your campus&lt;/h2&gt;&lt;/p&gt;&lt;h4&gt;Get access to student exclusive discounts&lt;/h4&gt;&lt;p&gt;rumie students get access to student exclusive discounts from local and national businesses around their campus.&lt;/p&gt;&lt;/div&gt;&lt;/div&gt;&lt;div&gt;&lt;p&gt;&lt;h2&gt;Rent dresses from &lt;/h2&gt;&lt;/p&gt;&lt;p&gt;Wear a new dress every weekend! Just rent it directly from a student on your campus.&lt;/p&gt;&lt;div&gt;&lt;p&gt;&lt;/p&gt;&lt;p&gt;Make money off of the dresses you&#39;ve already worn&lt;/p&gt;&lt;/div&gt;&lt;div&gt;&lt;p&gt;&lt;/p&gt;&lt;p&gt;rumie rental guarantee ensures your dress won&#39;t be damaged&lt;/p&gt;&lt;/div&gt;&lt;div&gt;&lt;p&gt;&lt;/p&gt;&lt;p&gt;Find a new dress every weekend and save money&lt;/p&gt;&lt;/div&gt;&lt;/div&gt;&lt;div&gt;&lt;p&gt;&lt;h2&gt;. The only place to buy student tickets at student prices&lt;/h2&gt;&lt;/p&gt;&lt;h4&gt;Buy or Sell students Football and Basketball tickets with your campus&lt;/h4&gt;&lt;p&gt;rumie students get access to the first-ever student ticket marketplace. No more getting scammed trying to buy tickets from strangers on the internet.&lt;/p&gt;&lt;/div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;p&gt;&lt;/p&gt;&lt;h4&gt;Secure&lt;/h4&gt;&lt;p&gt;.edu authentication and buyer protection on purchases.&lt;/p&gt;&lt;/div&gt;&lt;div&gt;&lt;p&gt;&lt;/p&gt;&lt;h4&gt;Lightning-fast&lt;/h4&gt;&lt;p&gt;Post your first listing in under a minute.&lt;/p&gt;&lt;/div&gt;&lt;div&gt;&lt;p&gt;&lt;/p&gt;&lt;h4&gt;Verified Students&lt;/h4&gt;&lt;p&gt;Trade with other students, not strangers.&lt;/p&gt;&lt;/div&gt;&lt;div&gt;&lt;p&gt;&lt;/p&gt;&lt;h4&gt;Intuitive&lt;/h4&gt;&lt;p&gt;List an item in a few simple steps. Message sellers with ease.&lt;/p&gt;&lt;/div&gt;&lt;/div&gt;&lt;p&gt;&lt;a href=&#34;https://apps.apple.com/us/app/rumie-college-marketplace/id1602465206&#34;&gt;Download the app now&lt;/a&gt;&lt;/p&gt;&lt;/div&gt;&lt;div&gt;&lt;p&gt;&lt;h2&gt;Trusted by students.&lt;/h2&gt;&lt;/p&gt;&lt;div&gt;&lt;div&gt;&lt;p&gt;&lt;/p&gt;&lt;p&gt;Saves me money&lt;/p&gt;&lt;p&gt;Facebook Marketplace and Amazon are great but often times you have to drive a long way to meet up or pay for shipping. rumie let’s me know what is available at my school… literally at walking distance. &lt;/p&gt;&lt;/div&gt;&lt;div&gt;&lt;p&gt;&lt;/p&gt;&lt;p&gt;5 stars!&lt;/p&gt;&lt;p&gt;Having this app as a freshman is great! It makes buying and selling things so safe and easy! Much more efficient than other buy/sell platforms!&lt;/p&gt;&lt;/div&gt;&lt;div&gt;&lt;p&gt;&lt;/p&gt;&lt;p&gt;Amazing!&lt;/p&gt;&lt;p&gt;5 stars for being simple, organized, safe, and a great way to buy and sell in your college community.. much more effective than posting on Facebook or Instagram!&lt;/p&gt;&lt;/div&gt;&lt;div&gt;&lt;p&gt;&lt;/p&gt;&lt;p&gt;The BEST marketplace for college students!!!&lt;/p&gt;&lt;p&gt;Once rumie got to my campus, I was excited to see what is has to offer! Not only is it safe for students like me, but the app just has a great feel and is really easy to use. The ONLY place I’ll be buying and selling while I’m a student.&lt;/p&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div&gt;&lt;p&gt;&lt;h2&gt;Easier to than GroupMe or Instagram.&lt;/h2&gt;&lt;/p&gt;&lt;p&gt;Forget clothing instas, selling groupme&#39;s, and stress when buying and selling. Do it all from the rumie app.&lt;/p&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;\n \nFinally, let&#39;s create a summarized report that lists our 10 companies and gives us an easily digestible summary of each company. We can input all of this web content into an LLM and have it generate a nice report!\n  import textwrap\nimport openai\nimport os\nSYSTEM_MESSAGE = &#34;You are a helpful assistant writing a research report about a company. Summarize the users input into multiple paragraphs. Be extremely concise, professional, and factual as possible. The first paragraph should be an introduction and summary of the company. The second paragraph should include pros and cons of the company. Things like what are they doing well, things they are doing poorly or struggling with. And ideally, suggestions to make the company better.&#34;\nopenai.api_key = os.environ.get(&#34;OPENAI_API_KEY&#34;)\ncompletion = openai.chat.completions.create(\nmodel=&#34;gpt-4&#34;,\nmessages=[\n{&#34;role&#34;: &#34;system&#34;, &#34;content&#34;: SYSTEM_MESSAGE},\n{&#34;role&#34;: &#34;user&#34;, &#34;content&#34;: all_contents},\n],\n)\nsummary = completion.choices[0].message.content\nprint(f&#34;Summary for {c.url}:&#34;)\nprint(textwrap.fill(summary, 80))\n  \n Summary for https://www.rumieapp.com/:\nRumie is a college-exclusive marketplace app that allows students to buy, sell,\nand rent items with other students. It has over 320,000 users in its network and\noffers features such as quick setup, .edu verification, local and campus-wide\nselling options, and exclusive discounts from local businesses. Students can\nalso rent dresses from other students, buy or sell student tickets at student\nprices, and enjoy secure and intuitive transactions. The app has received\npositive feedback from users for its convenience, safety, and effectiveness in\nbuying and selling within the college community.\nPros of Rumie include its focus on college students&#39; needs, such as providing a\nsafe platform and exclusive deals for students. The app offers an intuitive and\nfast setup process, making it easy for students to start buying and selling.\nThe option to trade with other students is also appreciated. Users find it convenient\nthat they can sell locally or ship items to other campuses. The app&#39;s rental\nguarantee for dresses provides assurance to users that their dresses won&#39;t be\ndamaged. Overall, Rumie is highly regarded as a simple, organized, and safe\nplatform for college students to buy and sell within their community.\nSuggestions to improve Rumie include expanding its reach to more colleges and\nuniversities across the nation and eventually internationally. Enhancing\nmarketing efforts and fundraising can aid in raising awareness among college\nstudents. Additionally, incorporating features such as improved search filters\nand a rating/review system for buyers and sellers could enhance the user\nexperience. Continual updates and improvements to the app&#39;s interface and\nfunctionality can also ensure that it remains user-friendly and efficient.\n \nAnd we’re done! We’ve built an app that takes in a company webpage and uses Exa to \nDiscover similar startups\nFind information about each of those startups\nGather useful content and summarize it with OpenAI\nHopefully you found this tutorial helpful and are ready to start building your very own company analyst! Whether you want to generate sales leads or research competitors to your own company, Exa&#39;s got you covered."\
        },\
        {\
          "id": "https://docs.exa.ai/reference/exa-researcher",\
          "url": "https://docs.exa.ai/reference/exa-researcher",\
          "title": "Exa Researcher",\
          "author": null,\
          "publishedDate": "2024-03-02T11:36:30.000Z",\
          "text": "https://docs.exa.ai/reference/exa-researcher\nExa Researcher\n2024-03-02T11:36:30Z\n    In this example, we will build Exa Researcher, a Javascript app that given a research topic, automatically searches for different sources about the topic with Exa and synthesizes the searched contents into a research report.\nThis interactive notebook was made with the Deno Javascript kernel for Jupyter. Check out the plain JS version if you prefer a regular Javascript file you can run with NodeJS, or want to skip to the final result. If you&#39;d like to run this notebook locally, Installing Deno and connecting Deno to Jupyter is fast and easy.\nTo play with this code, first we need a Exa API key and an OpenAI API key. Get 1000 Exa searches per month free just for signing up! \nLet&#39;s import the Exa and OpenAI SDKs and put in our API keys to create a client object for each.\nMake sure to pick the right imports for your runtime and paste or load your API keys.\n  // Deno imports\nimport Exa from &#39;npm:exa-js&#39;;\nimport OpenAI from &#39;npm:openai&#39;;\n// NodeJS imports\n//import Exa from &#39;exa-js&#39;;\n//import OpenAI from &#39;openai&#39;;\nconst EXA_API_KEY = &#34;&#34; // insert or load your API key here\nconst OPENAI_API_KEY = &#34;&#34;// insert or load your API key here\nconst exa = new Exa(EXA_API_KEY);\nconst openai = new OpenAI({ apiKey: OPENAI_API_KEY });\n  \nSince we&#39;ll be making several calls to the OpenAI API to get a completion from GPT 3.5-turbo, let&#39;s make a simple utility wrapper function so we can pass in the system and user messages directly, and get the LLM&#39;s response back as a string.\n  async function getLLMResponse({system = &#39;You are a helpful assistant.&#39;, user = &#39;&#39;, temperature = 1, model = &#39;gpt-3.5-turbo&#39;}){\nconst completion = await openai.chat.completions.create({\nmodel,\ntemperature,\nmessages: [\n{&#39;role&#39;: &#39;system&#39;, &#39;content&#39;: system},\n{&#39;role&#39;: &#39;user&#39;, &#39;content&#39;: user},\n]\n});\nreturn completion.choices[0].message.content;\n}\n  \nOkay, great! Now let&#39;s starting building Exa Researcher. The app should be able to automatically generate research reports for all kinds of different topics. Here&#39;s two to start:\n  const SAMA_TOPIC = &#39;Sam Altman&#39;;\nconst ART_TOPIC = &#39;renaissance art&#39;;\n  \nThe first thing our app has to do is decide what kind of search to do for the given topic. \nExa offers two kinds of search: neural and keyword search. Here&#39;s how we decide:\nNeural search is preferred when the query is broad and complex because it lets us retrieve high quality, semantically relevant data. Neural search is especially suitable when a topic is well-known and popularly discussed on the Internet, allowing the machine learning model to retrieve contents which are more likely recommended by real humans. \nKeyword search is useful when the topic is specific, local or obscure. If the query is a specific person&#39;s name, and identifier, or acronym, such that relevant results will contain the query itself, keyword search may do well. And if the machine learning model doesn&#39;t know about the topic, but relevant documents can be found by directly matching the search query, keyword search may be necessary.\nSo, Exa Researcher is going to get a query, and it needs to automatically decide whether to use keyword or neural search to research the query based on the criteria. Sounds like a job for the LLM! But we need to write a prompt that tells it about the difference between keyword and neural search-- oh wait, we have a perfectly good explanation right there.\n  // Let&#39;s generalize the prompt and call the search types (1) and (2) in case the LLM is sensitive to the names. We can replace them with different names programmatically to see what works best.\nconst SEARCH_TYPE_EXPLANATION = `- (1) search is usually preferred when the query is a broad topic or semantically complex because it lets us retrieve high quality, semantically relevant data. (1) search is especially suitable when a topic is well-known and popularly discussed on the Internet, allowing the machine learning model to retrieve contents which are more likely recommended by real humans.\n- (2) search is useful when the topic is specific, local or obscure. If the query is a specific person&#39;s name, and identifier, or acronym, such that relevant results will contain the query itself, (2) search may do well. And if the machine learning model doesn&#39;t know about the topic, but relevant documents can be found by directly matching the search query, (2) search may be necessary.\n`;\n  \nHere&#39;s a function that instructs the LLM to choose between the search types and give its answer in a single word. Based on its choice, we return keyword or neural.\n  async function decideSearchType(topic, choiceNames = [&#39;neural&#39;, &#39;keyword&#39;]){\nlet userMessage = &#39;Decide whether to use (1) or (2) search for the provided research topic. Output your choice in a single word: either &#34;(1)&#34; or &#34;(2)&#34;. Here is a guide that will help you choose:\\n&#39;;\nuserMessage += SEARCH_TYPE_EXPLANATION;\nuserMessage += `Topic: ${topic}\\n`;\nuserMessage += `Search type: `;\nuserMessage = userMessage.replaceAll(&#39;(1)&#39;, choiceNames[0]).replaceAll(&#39;(2)&#39;, choiceNames[1]);\nconst response = await getLLMResponse({\nsystem: &#39;You will be asked to make a choice between two options. Answer with your choice in a single word.&#39;,\nuser: userMessage,\ntemperature: 0\n});\nconst useKeyword = response.trim().toLowerCase().startsWith(choiceNames[1].toLowerCase());\nreturn useKeyword ? &#39;keyword&#39; : &#39;neural&#39;;\n}\n  \nLet&#39;s test it out:\n  console.log(SAMA_TOPIC, &#39;expected: keyword, got:&#39;, await decideSearchType(SAMA_TOPIC));\nconsole.log(ART_TOPIC, &#39;expected: neural, got:&#39;, await decideSearchType(ART_TOPIC));\n  \n Sam Altman expected: keyword, got: keyword\nrenaissance art expected: neural, got: neural\n \nGreat! Now we have to craft some search queries for the topic and the search type. There are two cases here: keyword search and neural search. Let&#39;s do the easy one first. LLMs already know what Google-like keyword searches look like. So let&#39;s just ask the LLM for what we want:\n  function createKeywordQueryGenerationPrompt(topic, n){\nreturn `I&#39;m writing a research report on ${topic} and need help coming up with Google keyword search queries.\nGoogle keyword searches should just be a few words long. It should not be a complete sentence.\nPlease generate a diverse list of ${n} Google keyword search queries that would be useful for writing a research report on ${topic}. Do not add any formatting or numbering to the queries.`\n}\nconsole.log(await getLLMResponse({\nsystem: &#39;The user will ask you to help generate some search queries. Respond with only the suggested queries in plain text with no extra formatting, each on it\\&#39;s own line.&#39;,\nuser: createKeywordQueryGenerationPrompt(SAMA_TOPIC, 3),\n}));\n  \n Sam Altman biography\nY Combinator founder\nInvestments made by Sam Altman\n \nThose are some good ideas!\nNow we have to handle the neural Exa search. This is tougher: you can read all about crafting good Exa searches here. But this is actually a really good thing: making the perfect Exa search is hard because Exa is so powerful! Exa allows us to express so much more nuance in our searches and gives us unparalleled ability to steer our search queries towards our real objective.\nWe need to our app to understand our goal, what Exa is, and how to use it to achieve the goal. So let&#39;s just tell the LLM everything it needs to know.\n  function createNeuralQueryGenerationPrompt(topic, n){\nreturn `I&#39;m writing a research report on ${topic} and need help coming up with Exa keyword search queries.\nExa is a fully neural search engine that uses an embeddings based approach to search. Exa was trained on how people refer to content on the internet. The model is trained given the description to predict the link. For example, if someone tweets &#34;This is an amazing, scientific article about Roman architecture: &lt;link&gt;&#34;, then our model is trained given the description to predict the link, and it is able to beautifully and super strongly learn associations between descriptions and the nature of the content (style, tone, entity type, etc) after being trained on many many examples. Because Exa was trained on examples of how people talk about links on the Internet, the actual Exa queries must actually be formed as if they are content recommendations that someone would make on the Internet where a highly relevant link would naturally follow the recommendation, such as the example shown above.\nExa neural search queries should be phrased like a person on the Internet indicating a webpage to a friend by describing its contents. It should end in a colon :.\nPlease generate a diverse list of ${n} Exa neural search queries for informative and trustworthy sources useful for writing a research report on ${topic}. Do not add any quotations or numbering to the queries.`\n}\nconsole.log(await getLLMResponse({\nsystem: &#39;The user will ask you to help generate some search queries. Respond with only the suggested queries in plain text with no extra formatting, each on it\\&#39;s own line.&#39;,\nuser: createNeuralQueryGenerationPrompt(ART_TOPIC, 3),\n//model: &#39;gpt-4&#39;\n}));\n  \n Hey, check out this comprehensive guide to Renaissance art:\nCan you recommend any scholarly articles on Renaissance art?\nI found an excellent website that explores the influence of religion on Renaissance art:\n \nNow let&#39;s put them together into a function that generates queries for the right search mode.\n  async function generateSearchQueries(topic, n, searchType){\nif(searchType !== &#39;keyword&#39; &amp;&amp; searchType !== &#39;neural&#39;){\nthrow &#39;invalid searchType&#39;;\n}\nconst userPrompt = searchType === &#39;neural&#39; ? createNeuralQueryGenerationPrompt(topic, n) : createKeywordQueryGenerationPrompt(topic, n);\nconst completion = await getLLMResponse({\nsystem: &#39;The user will ask you to help generate some search queries. Respond with only the suggested queries in plain text with no extra formatting, each on it\\&#39;s own line.&#39;,\nuser: userPrompt,\ntemperature: 1\n});\nconst queries = completion.split(&#39;\\n&#39;).filter(s =&gt; s.trim().length &gt; 0).slice(0, n);\nreturn queries;\n}\n  \nLet&#39;s make sure it works, and check out some more queries:\n  const samaQueries = await generateSearchQueries(SAMA_TOPIC, 3, &#39;keyword&#39;);\nconst artQueries = await generateSearchQueries(ART_TOPIC, 3, &#39;neural&#39;);\n  \n  console.log(samaQueries);\nconsole.log(artQueries);\n  \n [\n&#34;Sam Altman biography&#34;,\n&#34;Y Combinator founder&#34;,\n&#34;Sam Altman startup advice&#34;\n]\n[\n&#34;Check out this comprehensive guide to Renaissance art:&#34;,\n&#34;Discover the key characteristics of Renaissance art and its influential artists.&#34;,\n&#34;Explore the development of perspective and human anatomy in Renaissance paintings.&#34;\n]\n \nNow it&#39;s time to use Exa to do the search, either neural or keyword. Using searchAndContents, we can get clean text contents bundled with each link.\n  async function getSearchResults(queries, type, linksPerQuery=2){\nlet results = [];\nfor (const query of queries){\nconst searchResponse = await exa.searchAndContents(query, { type, numResults: linksPerQuery, useAutoprompt: false });\nresults.push(...searchResponse.results);\n}\nreturn results;\n}\n  \n  const artLinks = await getSearchResults(artQueries, &#39;neural&#39;);\nconsole.log(artLinks[0]); // first result of six\n  \n {\ntitle: &#34;How to Look at and Understand Great Art&#34;,\nurl: &#34;https://www.wondrium.com/how-to-look-at-and-understand-great-art?lec=29%3Futm_source%3DSocialMedia&amp;p&#34;... 5 more characters,\npublishedDate: &#34;2013-11-19&#34;,\nauthor: &#34;Doc&#34;,\nid: &#34;dq0L1GOKroUBuryT3ypSsQ&#34;,\ntext: &#34;\\n&#34; +\n&#34; \\n&#34; +\n&#34; \\n&#34; +\n&#34; \\n&#34; +\n&#34; \\n&#34; +\n&#34; \\n&#34; +\n&#34; \\n&#34; +\n&#34; Trailer\\n&#34; +\n&#34; \\n&#34; +\n&#34; \\n&#34; +\n&#34;\\n&#34; +\n&#34; \\n&#34; +\n&#34; \\n&#34; +\n&#34; \\n&#34; +\n&#34; \\n&#34; +\n&#34; \\n&#34; +\n&#34; \\n&#34; +\n&#34; 01: The Importance of First Impressions\\n&#34; +\n&#34; \\n&#34; +\n&#34; Examine the conte&#34;... 14543 more characters,\nscore: 0.1785949170589447\n}\n \nIn just a couple lines of code, we&#39;ve used Exa to go from some search queries to useful Internet content.\nThe final step is to instruct the LLM to synthesize the content into a research report, including citations of the original links. We can do that by pairing the content and the urls and writing them into the prompt.\n  async function synthesizeReport(topic, searchContents, contentSlice = 750){\nconst inputData = searchContents.map(item =&gt; `--START ITEM--\\nURL: ${item.url}\\nCONTENT: ${item.text.slice(0, contentSlice)}\\n--END ITEM--\\n`).join(&#39;&#39;);\nreturn await getLLMResponse({\nsystem: &#39;You are a helpful research assistant. Write a report according to the user\\&#39;s instructions.&#39;,\nuser: &#39;Input Data:\\n&#39; + inputData + `Write a two paragraph research report about ${topic} based on the provided information. Include as many sources as possible. Provide citations in the text using footnote notation ([#]). First provide the report, followed by a single &#34;References&#34; section that lists all the URLs used, in the format [#] &lt;url&gt;.`,\n//model: &#39;gpt-4&#39; //want a better report? use gpt-4\n});\n}\n  \n  const artReport = await synthesizeReport(ART_TOPIC, artLinks);\n  \n Research Report: Renaissance Art\nRenaissance art is a significant period in the history of art characterized by technical innovation and a richly symbolic visual language. It is known for combining the advancements in technique with the exploration of deeper layers of meaning in artworks. In Renaissance paintings, the identification of the patron or donor often provides insights into the intended message of the artwork. For example, a painting discussed in an article from the Royal Academy[^1] was commissioned by Jacopo Pesaro, the Bishop of Paphos on the island of Cyprus, and was likely painted by Titian during his early twenties. Analyzing the patronage and symbolism in Renaissance paintings allows for a better understanding of the multifaceted meanings conveyed by the artists.\nAnother key aspect of studying Renaissance art is understanding the contexts and environments in which art is encountered and viewed. The influence of the viewer&#39;s point of view and focal point plays a critical role in shaping the experience of art. Lectures provided by Wondrium[^3] discuss the importance of first impressions and explore how the artist positions the viewer with respect to the image. Additionally, the genres of Western art and the artist&#39;s media, tools, and techniques are explored in these lectures, providing a comprehensive understanding of the various elements that contribute to the creation and perception of Renaissance art.\nOverall, studying Renaissance art encompasses an exploration of not only the technical skills and innovations of the artists but also the cultural and historical contexts in which the artworks were created. By analyzing the patronage, symbolism, and viewing experience, researchers gain a deeper appreciation and interpretation of this significant period in the history of art.\nReferences:\n[1] How to Read a Renaissance Painting. (2016, April 1). Royal Academy. Retrieved from https://www.royalacademy.org.uk/article/how-to-read-a-renaissance-painting\n[3] How to Look at and Understand Great Art (#29). Wondrium. Retrieved from https://www.wondrium.com/how-to-look-at-and-understand-great-art?lec=29\n \nLet&#39;s wrap up by putting it all together into one researcher() function that starts from a topic and returns us the finished report. We can also let Exa Researcher generate us a report about our keyword search topic as well.\n  async function researcher(topic){\nconst searchType = await decideSearchType(topic);\nconst searchQueries = await generateSearchQueries(topic, 3, searchType);\nconsole.log(searchQueries);\nconst searchResults = await getSearchResults(searchQueries, searchType);\nconsole.log(searchResults[0]);\nconst report = await synthesizeReport(topic, searchResults);\nreturn report;\n}\n  \n  console.log(await researcher(SAMA_TOPIC));\n  \n [\n&#34;Sam Altman biography&#34;,\n&#34;Y Combinator founder&#34;,\n&#34;Sam Altman startup advice&#34;\n]\n{\ntitle: &#34;Sam Altman - Wikipedia&#34;,\nurl: &#34;https://en.wikipedia.org/wiki/Sam_Altman&#34;,\nauthor: null,\nid: &#34;8942e4e1-a37d-42fd-bec1-cf1715ef8d35&#34;,\ntext: &#34;\\n&#34; +\n&#34;From Wikipedia, the free encyclopedia\\n&#34; +\n&#34;\\n&#34; +\n&#34;Sam AltmanAltman in 2019BornSamuel Harris AltmanApril 22, 19&#34;... 7424 more characters\n}\nResearch Report: Sam Altman\nSam Altman is an American entrepreneur, investor, and former CEO of OpenAI[^1^]. He is widely known for his significant contributions as the president of Y Combinator from 2014 to 2019[^1^]. Altman was born on April 22, 1985, in Chicago, Illinois[^2^]. He grew up in St. Louis, Missouri, where he attended John Burroughs School[^3^]. Altman&#39;s interest in computers began at a young age, and he received his first computer, an Apple Macintosh, at the age of eight[^3^]. His childhood idol was Steve Jobs[^4^]. Sam Altman dropped out of Stanford University after one year to pursue his entrepreneurial endeavors[^1^].\nAltman&#39;s career has been marked by his involvement in various tech ventures. He notably served as the CEO of OpenAI from 2019 to 2023[^1^]. Additionally, Altman played a pivotal role as the president of Y Combinator, a startup accelerator[^1^]. His influence in the tech industry has drawn comparisons to renowned figures like Steve Jobs and Bill Gates[^2^]. Altman firmly believes in the potential of artificial general intelligence (AGI) and its ability to accomplish tasks comparable to those performed by humans[^2^].\nReferences:\n[^1^] Wikipedia. (n.d.). Sam Altman. Retrieved from https://en.wikipedia.org/wiki/Sam_Altman\n[^2^] Britannica. (n.d.). Sam Altman. Retrieved from https://www.britannica.com/biography/Sam-Altman\n \nFor a link to a complete, cleaned up version of this project that you can execute in your NodeJS environment, check out the alternative JS-only version."\
        },\
        {\
          "id": "https://docs.exa.ai/reference/exa-rag",\
          "url": "https://docs.exa.ai/reference/exa-rag",\
          "title": "Exa RAG",\
          "author": null,\
          "publishedDate": "2024-03-02T11:36:43.000Z",\
          "text": "https://docs.exa.ai/reference/exa-rag\nExa RAG\n2024-03-02T11:36:43Z\n   \nLLMs are powerful because they compress large amounts of data and patterns into a format that allows convenient access, but this compressions isn&#39;t lossless. Exa can bring the most relevant data into context. This lets us to combine the compressed data of the LLM with a select quantity of uncompressed data for the problem at hand for the best generations possible.\nExa&#39;s SDKs make incorporating quality data into your LLM pipelines quick and painless. Install the SDK by running this command in your terminal:\n pip install exa-py \n  # Now, import the Exa class and pass your API key to it.\nfrom exa_py import Exa\nmy_exa_api_key = &#34;YOUR_API_KEY_HERE&#34;\nexa = Exa(my_exa_api_key)\n  \nFor our first example, we&#39;ll set up Exa to answer questions with OpenAI&#39;s popular GPT 3.5 model. (You can use GPT 4 or another model if you prefer!) We&#39;ll use Exa&#39;s highlight feature, which directly returns relevant text of customizable length for a query. You&#39;ll need to run pip install openai to get access to OpenAI&#39;s SDK if you haven&#39;t used it before. More information about the OpenAI Python SDK can be found here.\n  # Set up OpenAI&#39; SDK\nfrom openai import OpenAI\nopenai_api_key = &#34;YOUR_API_KEY_HERE&#34;\nopenai_client = OpenAI(api_key=openai_api_key)\n  \nNow, we just need some questions to answer!\n  questions = [\n&#34;How did bats evolve their wings?&#34;,\n&#34;How did Rome defend Italy from Hannibal?&#34;,\n]\n  \nWhile LLMs can answer some questions on their own, they have limitations:\nLLMs don&#39;t have knowledge past when their training was stopped, so they can&#39;t know about recent events\nIf an LLM doesn&#39;t know the answer, it will often &#39;hallucinate&#39; a correct-sounding response, and it can be difficult and inconvenient to distinguish these from correct answers\nBecause of the opaque manner of generation and the problems mentioned above, it is difficult to trust an LLM&#39;s responses when accuracy is important \nRobust retrieval helps solve all of these issues by providing quality sources of ground truth for the LLM (and their human users) to leverage. Let&#39;s use Exa to get some information about our questions:\n  # Parameters for our Highlights search\nhighlights_options = {\n&#34;num_sentences&#34;: 7, # how long our highlights should be\n&#34;highlights_per_url&#34;: 1, # just get the best highlight for each URL\n}\n# Let the magic happen!\ninfo_for_llm = []\nfor question in questions:\nsearch_response = exa.search_and_contents(question, highlights=highlights_options, num_results=3, use_autoprompt=True)\ninfo = [sr.highlights[0] for sr in search_response.results]\ninfo_for_llm.append(info)\n  \n [[&#39;As the only mammals with powered flight, the evolutionary\\xa0history of their wings has been poorly understood. However, research published Monday in Nature and PLoS Genetics has provided the first comprehensive look at the genetic origins of their incredible wings.But to appreciate the genetics of their wing development, it’s important to know how crazy a bat in flight truly\\xa0looks.Try a little experiment: Stick your arms out to the side, palms facing forward, thumbs pointing up toward the ceiling. Now imagine that your fingers are\\xa0long, arching down toward the floor like impossibly unkempt fingernails — but still made of bone, sturdy and spread apart. Picture the sides of your body connecting to your hands, a rubbery membrane attaching your leg and torso to those long fingers, binding you with strong, stretchy skin. Then, finally, imagine using your muscles to flap those enormous hands.Bats, man.As marvelous as bat flight is to behold, the genetic origins of their storied wings has remained murky. However, new findings from an international team of researchers led by Nadav Ahituv, PhD, of the University of California at San Francisco, Nicola Illing, PhD, of the University of Cape Town\\xa0in\\xa0South Africa\\xa0and Katie Pollard, PhD of the UCSF-affiliated Gladstone Institutes has shed new light on how, 50 million years ago, bats took a tetrapod blueprint for arms and legs and went up into the sky.Using a sophisticated set of genetic tools, researchers approached the question of how bats evolved flight by looking not only at which genes were used in the embryonic development of wings, but at what point during development the genes were turned on and off, and — critically — what elements in the genome were regulating the expression of these genes. Genes do not just turn themselves on without input; genetic switches, called enhancers, act to regulate the timing and levels of gene expression in the body.&#39;,\n&#34;Since flight evolved millions of years ago in all of the groups that are capable of flight today, we can&#39;t observe the changes in behavior and much of the morphology that the evolution of flight involves. We do have the fossil record, though, and it is fairly good for the three main groups that evolved true flight. We&#39;ll spare you an in-depth description of how each group evolved flight for now; see the later exhibits for a description of each group and how they developed flight.&#34;,\n&#34;It&#39;s easy to forget that one in five species of mammal on this planet have wings capable of delivering spectacularly acrobatic flying abilities. Equally incredibly, two-thirds of these 1,200 species of flying mammal can fly in the dark, using exquisite echolocation to avoid obstacles and snatch airborne prey with stunning deftness. These amazing feats have helped make bats the focus not only of folkloric fascination, but also of biological enquiry and mimicry by human engineers from Leonardo da Vinci onwards. Recent research in PLOS journals continues to add surprising new findings to what we know about bats, and how they might inspire us to engineer manmade machines such as drones to emulate their skills. Bats, unlike most birds and flying insects, have relatively heavy wings – something that might appear disadvantageous. But a recent study in PLOS Biology by Kenny Breuer and colleagues shows that bats can exploit the inertia of the wings to make sharp turns that would be near-impossible using aerodynamic forces alone. The authors combined high-speed film of real bats landing upside-down on ceiling roosts with computational modelling to tease apart aerodynamic and inertial effects.&#34;],\n[&#34;things, gold and silver, could buy a victory. And this Other Italian cities, inspired by Rome&#39;s example, overpowered occupying troops, shut their gates again and invited a second siege. Hannibal could not punish them without dividing his he had no competent leadership to do so, what with one member of&#34;,\n&#39;A group of Celts known as the Senone was led through Italy by their commander, Brennus. The Senone Gauls were threatening the nearby town of Clusium, when Roman Ambassadors from the Fabii family were sent to negotiate peace for Clusium. The Romans were notoriously aggressive, and so it is only a little surprising that when a scuffle broke out between the Gauls and Clusians, the Fabii joined in and actually killed a Senone chieftain. The Roman people voted to decide the fate of those who broke the sacred conduct of ambassadors, but the Fabii were so popular that they were instead voted to some of the highest positions in Rome. This absolutely infuriated Brennus and his people and they abandoned everything and headed straight for Rome. Rome was woefully unprepared for this sudden attack. The Gauls had marched with purpose, declaring to all the towns they passed that they would not harm them, they were heading straight for Rome.&#39;,\n&#34;Hannibal had no intention to sit and recieve the romans in spain.Hannibal clearly considered the nature of roman power-and came to the conclusion that Rome could only be defeated in Italy.The cornerstone of Rome&#39;s power was a strategic manpower base that in theory could produce 7,00,000 infantry and 70,000 cavalry.More than half of this manpower base (4,00,000) was provided by rome&#39;s Italian allies,who paid no taxes but had to render military service to rome&#39;s armies.Not all were content.Carthage on the other hand rarely used its own citizens for war,bulk of its army being mercenaries.In any case its manpower could never even come close to Rome,the fact that had aided roman victory in the 1st Punic war.Hannibal thus understood that Rome could afford to raise and send army after army to spain and take losses. Meanwhile any carthiginian losses in spain would encourage the recently conquered iberian tribes to defect. The only way to defeat Rome,was to fight in italy itself.By winning battle after battle on italian soil and demonstrating to the italian allies rome&#39;s inability to protect them and weakness,he could encourage them to break free of Rome eroding Rome&#39;s manpower to sizeable proportions. But there was one problem,his fleet was tiny and Rome ruled the seas.By land,the coastal route would be blocked by Roman forces and her ally-the great walled city of massalia.Hannibal thus resolved to think and do the impossible - move thousands of miles by land through the pyranees mountains,uncharted territory inhabited by the fierce gauls ,then through the Alps mountains and invade italy. Even before the siege of Saguntum had concluded,Hannibal had set things in motion.Having sent a number of embassies to the Gallic tribes in the Po valley with the mission of establishing a safe place for Hannibal to debouch from the Alps into the Po valley. He did not desire to cross this rugged mountain chain and to descend into the Po valley with exhausted troops only to have to fight a battle.Additionally the fierce gauls would provide a source of manpower for Hannibal&#39;s army.The romans had recently conquered much territory from the gauls in this area,brutally subjagating them ,seizing their land and redistributing it to roman colonists.Thus securing an alliance proved to be easy. After the sack of Saguntum he dismissed his troops to their own localities.&#34;]]\n \nNow, let&#39;s give the context we got to our LLM so it can answer our questions with solid sources backing them up!\n  responses = []\nfor question, info in zip(questions, info_for_llm):\nsystem_prompt = &#34;You are RAG researcher. Read the provided contexts and, if relevant, use them to answer the user&#39;s question.&#34;\nuser_prompt = f&#34;&#34;&#34;Sources: {info}\nQuestion: {question}&#34;&#34;&#34;\ncompletion = openai_client.chat.completions.create(\nmodel=&#34;gpt-3.5-turbo&#34;,\nmessages=[\n{&#34;role&#34;: &#34;system&#34;, &#34;content&#34;: system_prompt},\n{&#34;role&#34;: &#34;user&#34;, &#34;content&#34;: user_prompt},\n]\n)\nresponse = f&#34;&#34;&#34;\nQuestion: {question}\nAnswer: {completion.choices[0].message.content}\n&#34;&#34;&#34;\nresponses.append(response)\n  \n  from pprint import pprint # pretty print\npprint(responses)\n  \n [&#39;\\n&#39;\n&#39; Question: How did bats evolve their wings?\\n&#39;\n&#39; Answer: Recent research has shed new light on how bats evolved their &#39;\n&#39;wings. An international team of researchers used genetic tools to study the &#39;\n&#39;embryonic development of bat wings and the genes involved in their &#39;\n&#39;formation. They also investigated the regulatory elements in the genome that &#39;\n&#39;control the expression of these genes. By analyzing these factors, the &#39;\n&#39;researchers discovered that bats took a tetrapod blueprint for arms and legs &#39;\n&#39;and adapted it to develop wings, allowing them to fly. This research &#39;\n&#39;provides a comprehensive understanding of the genetic origins of bat wings &#39;\n&#39;and how they evolved over 50 million years ago.\\n&#39;\n&#39; &#39;,\n&#39;\\n&#39;\n&#39; Question: How did Rome defend Italy from Hannibal?\\n&#39;\n&#39; Answer: Rome defended Italy from Hannibal by using various strategies. One &#39;\n&#39;of the main defenses relied on the Roman manpower base, which consisted of a &#39;\n&#39;large army made up of Roman citizens and Italian allies who were obligated &#39;\n&#34;to render military service. Rome&#39;s strategic manpower base was a cornerstone &#34;\n&#39;of their power, as it could produce a significant number of infantry and &#39;\n&#39;cavalry. This posed a challenge for Hannibal, as Carthage relied heavily on &#39;\n&#34;mercenaries and could not match Rome&#39;s manpower.\\n&#34;\n&#39;\\n&#39;\n&#39;Hannibal realized that in order to defeat Rome, he needed to fight them in &#39;\n&#39;Italy itself. His plan was to win battles on Italian soil and demonstrate &#39;\n&#34;Rome&#39;s inability to protect their Italian allies, with the intention of &#34;\n&#34;encouraging them to break free from Rome. This would erode Rome&#39;s manpower &#34;\n&#39;base to a sizeable proportion. However, Hannibal faced several obstacles. &#39;\n&#39;Rome ruled the seas, making it difficult for him to transport troops and &#39;\n&#39;supplies by sea. Additionally, the coastal route to Italy would be blocked &#39;\n&#39;by Roman forces and their ally, the walled city of Massalia.\\n&#39;\n&#39;\\n&#39;\n&#39;To overcome these challenges, Hannibal devised a daring plan. He decided to &#39;\n&#39;lead his troops on a treacherous journey through the Pyrenees mountains, &#39;\n&#39;inhabited by fierce Gauls, and then through the Alps mountains to invade &#39;\n&#39;Italy. He sent embassies to Gallic tribes in the Po valley, securing &#39;\n&#39;alliances and establishing a safe place for his army to enter the Po valley &#39;\n&#39;from the Alps.\\n&#39;\n&#39;\\n&#39;\n&#39;Overall, Rome defended Italy from Hannibal by leveraging their manpower &#39;\n&#39;base, their control of the seas, and their strategic alliances with Italian &#39;\n&#39;allies. They also had the advantage of better infrastructure and control &#39;\n&#39;over resources within Italy itself. These factors ultimately played a &#39;\n&#34;significant role in Rome&#39;s defense against Hannibal&#39;s invasion.\\n&#34;\n&#39; &#39;]\n \nExa can be used for more than simple question answering. One superpower of embeddings-based search is that we can search for the meaning of sentences or even paragraphs:\n  paragraph = &#34;&#34;&#34;\nGeorgism, also known as Geoism, is an economic philosophy and ideology named after the American\npolitical economist Henry George (1839–1897).This doctrine advocates for the societal collective,\nrather than individual property owners, to capture the economic value derived from land and other\nural resources. To this end, Georgism proposes a single tax on the unimproved value of land, known\nas a &#34;land value tax,&#34; asserting that this would deter speculative land holding and promote efficient\nuse of valuable resources. Adherents argue that because the supply of land is fundamentally inelastic,\ntaxing it will not deter its availability or use, unlike other forms of taxation. Georgism differs\nfrom Marxism and capitalism, underscoring the distinction between common and private property while\nlargely contending that individuals should own the fruits of their labor.&#34;&#34;&#34;\nquery = f&#34;The best academic source about {paragraph} is (paper: &#34;\ngeorgism_search_response = exa.search_and_contents(paragraph, highlights=highlights_options, num_results=5, use_autoprompt=False)\n  \n  for result in georgism_search_response.results:\nprint(result.title)\nprint(result.url)\npprint(result.highlights)\n  \n Henry George\nhttps://www.newworldencyclopedia.org/entry/Henry_George\n[&#34;George&#39;s theory of interest is nowadays dismissed even by some otherwise &#34;\n&#39;Georgist authors, who see it as mistaken and irrelevant to his ideas about &#39;\n&#39;land and free trade. The separation of the value of land into improved and &#39;\n&#34;unimproved is problematic in George&#39;s theory. Once construction has taken &#34;\n&#39;place, not only the land on which such improvements were made is affected, &#39;\n&#39;the value of neighboring, as yet unimproved, land is impacted. Thus, while &#39;\n&#39;the construction of a major attraction nearby may increase the value of &#39;\n&#39;land, the construction of factories or nuclear power plants decreases its &#39;\n&#39;value. Indeed, location is the single most important asset in real estate. &#39;\n&#39;George intended to propose a tax that would have the least negative impact &#39;\n&#39;on productive activity. However, even unimproved land turns out to be &#39;\n&#39;affected in value by productive activity in the neighborhood.&#39;]\nWikiwand\nhttps://www.wikiwand.com/en/Georgism\n[&#39;Georgism is concerned with the distribution of economic rent caused by land &#39;\n&#39;ownership, natural monopolies, pollution rights, and control of the commons, &#39;\n&#39;including title of ownership for natural resources and other contrived &#39;\n&#39;privileges (e.g. intellectual property). Any natural resource which is &#39;\n&#39;inherently limited in supply can generate economic rent, but the classical &#39;\n&#39;and most significant example of land monopoly involves the extraction of &#39;\n&#39;common ground rent from valuable urban locations. Georgists argue that &#39;\n&#39;taxing economic rent is efficient, fair and equitable. The main Georgist &#39;\n&#39;policy recommendation is a tax assessed on land value, arguing that revenues &#39;\n&#39;from a land value tax (LVT) can be used to reduce or eliminate existing &#39;\n&#39;taxes (such as on income, trade, or purchases) that are unfair and &#39;\n&#39;inefficient. Some Georgists also advocate for the return of surplus public &#39;\n&#34;revenue to the people by means of a basic income or citizen&#39;s dividend. The &#34;\n&#39;concept of gaining public revenues mainly from land and natural resource &#39;\n&#39;privileges was widely popularized by Henry George through his first book, &#39;\n&#39;Progress and Poverty (1879).&#39;]\nHenry George\nhttps://www.conservapedia.com/Henry_George\n[&#39;He argued that land, unlike other factors of production, is supplied by &#39;\n&#39;nature and that rent is unearned surplus. The landless deserve their share &#39;\n&#39;of this surplus as a birthright, according to George. Henry George was born &#39;\n&#39;in Philadelphia, Pennsylvania, on the 2nd of September 1839. He settled in &#39;\n&#39;California in 1858; then later removed to New York in 1880; was first a &#39;\n&#39;printer, then an editor, but finally devoted all his life to economic and &#39;\n&#39;social questions. In 1860, George met Annie Corsina Fox. Her family was very &#39;\n&#39;opposed to the relationship, and in 1861 they eloped. In 1871 he published &#39;\n&#39;Our Land Policy, which, as further developed in 1879 under the title of &#39;\n&#39;Progress and Poverty, speedily attracted the widest attention both in &#39;\n&#39;America and in Europe.&#39;]\nGeorgism - Wikipedia\nhttps://en.wikipedia.org/wiki/Georgism\n[&#39;A key issue to the popular adoption of Georgism is that homes are illiquid &#39;\n&#39;yet governments need cash every year. Some economists have proposed other &#39;\n&#39;ways of extracting value from land such as building government housing and &#39;\n&#39;selling homes to new buyers in areas of fast-rising land value. The &#39;\n&#39;government would theoretically collect revenue from home sales without much &#39;\n&#39;cost to current homeowners while slowing down land value appreciation in &#39;\n&#39;high-demand areas. Henry George, whose writings and advocacy form the basis &#39;\n&#39;for Georgism Georgist ideas heavily influenced the politics of the early &#39;\n&#39;20th century. Political parties that were formed based on Georgist ideas &#39;\n&#39;include the Commonwealth Land Party in the United States, the Henry George &#39;\n&#39;Justice Party in Victoria, the Single Tax League in South Australia, and the &#39;\n&#34;Justice Party in Denmark. In the United Kingdom, George&#39;s writings were &#34;\n&#39;praised by emerging socialist groups in 1890s such as the Independent Labour &#39;\n&#39;Party and the Fabian Society, which would each go on to help form the &#39;\n&#39;modern-day Labour Party.&#39;]\nGeorgism\nhttps://rationalwiki.org/wiki/Georgism\n[&#39;Even with mostly primitive methods, land values are already assessed around &#39;\n&#39;the world wherever property/council taxes exist, and some municipalities &#39;\n&#39;even collect all their revenue from land values. Though these are &#39;\n&#39;market-based measures, they can still prove difficult and require upfront &#39;\n&#39;investment. Georgists believe that the potential value of land is greater &#39;\n&#39;than the current sum of government spending, since the abolition of taxes on &#39;\n&#39;labor and investment would further increase the value of land. Conversely, &#39;\n&#39;the libertarian strain in Georgism is evident in the notion that their land &#39;\n&#39;tax utopia also entails reducing or eliminating the need for many of the &#39;\n&#39;things governments currently supply, such as welfare, infrastructure to &#39;\n&#39;support urban sprawl, and military &amp; foreign aid spending to secure &#39;\n&#34;resources abroad. Therefore, many Georgists propose a citizen&#39;s dividend. &#34;\n&#39;This is a similar concept to basic income but its proponents project its &#39;\n&#39;potential to be much larger due to supposedly huge takings from the land &#39;\n&#39;tax, combined with lowered government spending. It has been recognized since &#39;\n&#39;Adam Smith and David Ricardo that a tax on land value itself cannot be &#39;\n&#39;passed on to tenants, but instead would be paid for by the owners of the &#39;\n&#39;land:&#39;]\n \nUsing Exa, we can easily find related papers, either for further research or to provide a source for our claims. This is just a brief intro into what Exa can do. For a look at how you can leverage getting full contents, check out this article."\
        },\
        {\
          "id": "https://docs.exa.ai/",\
          "url": "https://docs.exa.ai/",\
          "title": "Introduction",\
          "author": "",\
          "publishedDate": "2023-03-03T23:47:48.000Z",\
          "text": "Exa is a search engine made for AIs.  \n Exa has three core functionalities. \n Search Find webpages using Exa's embeddings-based or Google-style keyword search.\n Get contents Obtain clean, up-to-date, parsed HTML from Exa search results. Supports full text, LLM summaries, and highlights (snippets of relevant text).\n Find similar pages Based on a link, find and return pages that are similar in meaning\nLearn how to do an Exa search in your project\nPython Quickstart\nJavaScript Quickstart\ncURL Quickstart\nLearn how to do Exa-powered RAG\nGetting Started with RAG in Python\nGetting Started with RAG in TypeScript\nGetting Started with LangChain\nGetting Started with OpenAI\nGetting Started with CrewAI\nGetting Started with LlamaIndex\n              Table of Contents   \n Exa finds the exact content you're looking for on the web."\
        },\
        {\
          "id": "https://exa.ai/blog/announcing-exa",\
          "url": "https://exa.ai/blog/announcing-exa",\
          "title": "Exa API",\
          "author": "exa",\
          "text": "Steps toward the mission Today, we're excited to announce that we're renaming Metaphor to \"Exa” to better reflect our\nmission. We're also launching a new type of search experience – highlights. With highlights, you can instantly extract any webpage content from each search result using a\ncustomizable embedding model. All together, we’re taking big steps toward our core mission – organize the world’s knowledge.  Why Exa? The internet contains the collective knowledge output of mankind – all the great works of art\nand literature, millions of essays, hundreds of millions of research papers, billions of\nimages and videos, trillions of ideas sprinkled across tweets, forums, and memes. Searching the internet should feel like navigating a grand library of knowledge, where you\ncould weave insights across cultures, industries, and millenia. Of course it doesn’t feel that way. Today, searching the internet feels more like navigating a\nlandfill.  Many. have. debated. what's. wrong. with. search.  But the core problem is actually simple – knowledge on the internet is buried under an\noverwhelming amount of information. The core solution is also simple – we need a better search algorithm to filter all that\ninformation and organize the knowledge buried inside. Exa is going to organize the world’s knowledge.  To illustrate the problem, try googling \"startups working on climate change\".     You get 43,800,000 results. That’s a lot of information! But how much actual knowledge? I see\nmany listicle results, but no actual startups working on climate change. That's because Google still uses a keyword based algorithm. Keywords as a filtering\nmechanism may have worked in 1998, but they don't work for an internet with a thousand times more\ncontent and an SEO industry devoted to hacking keywords. Exa, in contrast, is the first web-scale neural search engine. Our algorithm uses\ntransformers end-to-end, the same technology that built ChatGPT. This enables us to filter the\ninternet by meaning, not by keyword. Here's the same search on Exa:  startups working on climate change   Rewind Climate Change https://www.rewind.earth/ Stored on the bottom of the sea, the carbon will be sequestered for thousands of years.     Holocene — Harnessing organic chemistry to remove CO2 https://www.theholocene.co/  Harnessing organic chemistry to remove CO 2 from the atmosphere, forever.     A NOVEL PHOTOCHEMICAL PROCESS TO CAPTURE CARBON DIOXIDE https://www.banyucarbon.com/ Combined they have &gt;130 peer-reviewed publications, have managed research projects worth millions of dollars, and have both presented before the National Academies of Science.     Living Carbon https://www.livingcarbon.com/  Restoring ecosystems from the ground up More biomass and faster growth means more carbon capture Our trees accumulate up to 53% more biomass than control seedlings We incorporated a photosynthesis enhancement trait to help trees grow faster Weâve developed a metal accumulation trait so trees can absorb more metals in their roots and stem These metals naturally slow wood decay, creating durable wood products and retaining carbon in wood for a longer period of time Our trees are unique in their ability to grow on degraded land with high concentrations of heavy metals As our trees grow, they can clean soil made toxic by industrial activity, store more carbon, and create investment opportunities on otherwise abandoned land      Phykos, PBC https://www.phykos.co/ We've built houses and farms and families, and we've travelled widely to see firsthand just how precious this world is.     Eion Carbon | Carbon removal that checks all the right boxes https://eioncarbon.com/ For every 10,000 tons of carbon removal, we create about five local jobs.     Climate Robotics https://www.climaterobotics.com/ In order to save ourselves from catastrophic climate change, we must automate sequestering carbon as well.     Carbon Dioxide Removal | Carba https://www.carba.com/ When biomass biodegrades, up to half of the carbon can be converted into methane, which carries 28 times the greenhouse warming potential.     Unemit https://unemit.com/ We firmly believe humanity can and will reach net zero greenhouse gas emissions, and ours will be a significant contribution to stopping and then reversing climate change by driving permanent Carbon Dioxide Removal (CDR) of more than 10% of historical emissions by the end of the century.\t     Twelve | The Carbon Transformation Company https://www.twelve.co/ To get there, we are working with brands and industrial partners to implement our technology at scale and eliminate emissions from global manufacturing supply chains.     Note that these results don't necessarily mention the words \"climate change\" or \"startup\". Exa\nfiltered out all the noisy webpages – the listicles talking about startups – and returned the\nactual knowledge – the startups themselves. Exa's goal is to understand any query – no matter how complex – and filter the internet to\nexactly the knowledge required for that query. This is the solution to the problem of overwhelming information. Instead of 40 million\nnoisy/redundant links, we’ll filter down to exactly the pieces of knowledge needed. In doing\nso, we’ll convert an internet landfill into a library of knowledge with each and every search. That's why we chose the name Exa. Exa means 10^18th power. Google means 10^100th power. While\nGoogle aims to surface all information, Exa aims to filter all information into organized\nknowledge. And when it comes to organized knowledge, 10^18 is greater than 10^100. Why .ai? It just so happens that a creature recently emerged on this planet with a particularly strong\nneed for organized, high quality knowledge. AIs, powered by LLMs like ChatGPT, are overhauling the way we do knowledge work. But to\nperform knowledge work optimally, AIs must incorporate the internet’s knowledge. That means\nthey need to be paired with a web retrieval system, like Exa. The quality of web retrieval particularly matters for LLMs. If retrieval returns junk\ninformation, the LLM will output junk content. If the retrieval is powerful enough to filter\nthe internet to the right knowledge, the LLM will output the highest quality content possible. Most of our customers have tried search APIs like Bing and Google SERP. They come to us\nbecause those APIs just don’t work for their use cases. Those APIs work for humans, but not\nfor LLMs, which have quite different needs. We’ve been on the frontlines witnessing this transformation of knowledge work and of\nretrieval. We believe AI applications will soon search the internet more than humans. That’s why Exa wasn’t just built with AI, it was also built for AI. Building with the Exa API Exa was designed with all the features necessary for AI applications:  Filter out noisy SEO results to only the type of content the AI requests Handle long queries – a sentence, a paragraph, or even a whole webpage can be a query Retrieve the page content of any url for downstream processing  Today we're adding highlights. Highlights means Exa can instantly extract any\npiece of content from any result's webpage. Behind the scenes, we’re chunking and embedding\nfull webpages with a paragraph prediction model. Because this happens live, you can customize\nhighlights length, # per page, and specify a secondary query specific to what content you want\nto find. Customers using highlights have seen significant increases in user conversion compared to Bing\nand other search providers. It's exciting to see customers using Exa for so many applications that just weren't possible a\nyear ago, from research paper writing assistants, to lead generation research bots, to\nlearning tools for students. A mission we take seriously As builders at the doorway to the world’s knowledge, we recognize the power we wield. The\nknowledge people consume underlies nearly everything, from our politics to our scientific\nprogress to our daily perceptions of the world. We believe that organizing the world's knowledge, and thereby giving users immense power to\nfilter the internet, is critical societal infrastructure that does not currently exist. Luckily, our incentives are aligned with our values. We have no ad-based need to monetize\nattention. Our API customers want the highest quality search possible. So do we. When the\ninternet feels like a library of all knowledge, we'll know we succeeded. If you want to help us build some of the coolest technology – designing internet-scale web\ncrawling infrastructure, training foundation models for search on our own GPU cluster, serving\ncustom vector databases at scale – you can check out our roles here. And if you're ready to build with the Exa API, you can sign up here. Thanks for reading and we'll keep writing more posts soon so you can join us on the ride!  See more",\
          "image": "https://exa.imgix.net/og-image.png"\
        },\
        {\
          "id": "https://dashboard.exa.ai/",\
          "url": "https://dashboard.exa.ai/",\
          "title": "Exa API Dashboard",\
          "author": "Exa",\
          "publishedDate": "2012-01-06T00:00:00.000Z",\
          "text": "Get started with Exa No credit card required   If you are supposed to join a team, please contact your team's administrator for an invite link."\
        }\
      ]\
    }\
  ]
}

```

2. **News Archives**: Crawl through a company’s news section:

Python

Copy

```python
result = exa.get_contents(
  ["https://www.apple.com/"],
  livecrawl="always",
  subpage_target=["news", "product"],
  subpages=10
)

```

Output:

Shell

Copy

```Shell
{
  "results": [\
    {\
      "id": "https://www.apple.com/",\
      "url": "https://www.apple.com/",\
      "title": "Apple",\
      "author": "",\
      "publishedDate": "2024-10-30T16:54:13.000Z",\
      "text": "Apple Intelligence is here.\nExperience it now on the latest iPhone, iPad, and Mac models with a free software update.1 \nMacBook Pro\nA work of smart.\nAvailable starting 11.8\n Hello, Apple Intelligence. \nApple Intelligence is here.\nExperience it now on the latest iPhone, iPad, and Mac models with a free software update.1 \nMac mini\nSize down. Power up.\nAvailable starting 11.8\n Hello, Apple Intelligence. \nApple Intelligence is here.\nExperience it now on the latest iPhone, iPad, and Mac models with a free software update.1 \niMac\nBril l l l l liant.\nAvailable starting 11.8\n Hello, Apple Intelligence. \niPhone 16 Pro\nHello, Apple Intelligence.\niPhone 16\nHello, Apple Intelligence.\nAirPods Pro 2\nHearing Test, Hearing Aid, and Hearing Protection features in a free software update.2\n Apple Intelligence \nAI for the rest of us.\n Apple Trade In \nGet $180-$650 in credit when you trade in iPhone 12 or higher.3 \n Apple Card \nGet up to 3% Daily Cash back with every purchase.\nApple TV+\nFAM Gallery",\
      "image": "https://www.apple.com/ac/structured-data/images/open_graph_logo.png?202110180743",\
      "subpages": [\
        {\
          "id": "https://www.apple.com/apple-news/",\
          "url": "https://www.apple.com/apple-news/",\
          "title": "Apple News+",\
          "author": "",\
          "publishedDate": "2024-05-07T20:24:00.000Z",\
          "text": "Get 3 months of Apple News+ free with a new iPhone, iPad, or Mac. 1  Learn more\nA world of journalism. One trusted subscription.\n Access top stories from over 400 leading publications.\n Get the latest news from local, national, and international titles.\n Solve daily puzzles created exclusively for Apple News+.\n Listen to the week’s best articles with Apple News+ audio stories.\nBuy an Apple device\n3 months free\nGet 3 months of Apple News+ free with the purchase of an eligible device. 1  \n  Check eligibility \n \nFree 1-month trial\nApple News+\nNew subscribers get 1 month of Apple News+ free, then pay\n$12.99 per month. \nFree 1-month trial\nApple One\nBundle Apple News+ with five other great services for one low monthly price.  Learn more    \nRewriting the reading experience.\nExplore an incredibly diverse and wide range of global publications in just one app. Expert editors surface the most compelling, must-read articles in Top Stories, Spotlight, and other collections. Vivid photography and animation, rich videos, and immersive layouts bring each story to life in striking detail. And you can even download issues to read offline.\nSolve puzzles \n \nApple News+ includes original mini and full-size crossword puzzles, ranging in difficulty from easy to challenging. New crosswords are available daily, and you can take on past games from the archive.\n The stories you need to hear. Everywhere you want to listen.\n \nSubscribers to Apple News+ can hear professionally narrated articles in the iPhone app or on the Apple News+ Narrated podcast. And everyone can listen weekday mornings as our host, Shumita Basu, talks you through the day’s headlines on Apple News Today — and catch weekly interviews with top journalists on In Conversation.\nA global news source.Personalized for you.\nStay close to what’s happening close to home.\nGet all the latest news from local publications in a growing number of cities — with coverage on politics, sports, dining, culture, and more.\nThe hard-hitting, fast-breaking sports news you need.\nGet highlights, scores, and schedules for professional and college teams and leagues. Apple News+ unlocks access to The Athletic, Sports Illustrated, local newspapers, and more.\nThe feed that feeds your interests.\nAs you read, Apple News gets a better understanding of your interests and suggests relevant stories that you can easily find throughout the app.\nOnly you see what you read.\nApple News only uses on-device intelligence to recommend stories and doesn’t access your information without your permission. We never share it with others or allow advertisers to track you.\n Read, listen, and play Apple News on your favorite devices.\n \niPhone\nMac\niPad\nCarPlay\nHomePod\nApple Watch\nExtra. Extra.Apple News+ delivers more.\n $12.99/mo. after free trial *  \nHundreds of magazines and leading newspapers\nincluded\n not included\n Apple News+ audio stories \nincluded\n not included\nLocal news from top regional sources\nincluded\n not included\nSports coverage from local and premium publications\nincluded\n not included\nExclusive daily puzzles\nincluded\n not included\nReading online and off across devices\nincluded\n not included\nCover-to-cover magazines\nincluded\n not included\nFamily Sharing for up to six\nincluded\n not included\nTop stories chosen by editors, personalized for you\nincluded\nincluded\nMy Sports with scores, standings, and highlights\nincluded\nincluded\n Apple News Today and In Conversation \nincluded\nincluded\nLocal news\nincluded\nincluded\nPrivate and secure reading\nincluded\nincluded\nCarPlay\nincluded\nincluded\nApple News+\nGet 3 months of Apple News+ free with a new iPhone, iPad, or Mac. 1  \n \nApple One\nBundle Apple News+ with 5 other great services. And enjoy more for less.\n \n Questions? Answers.\n \nApple News is the easiest way to stay up to date with the news and information that matter most, with a seamless reading experience across all your devices. Experienced Apple News editors curate the day’s top stories from trusted sources, and advanced algorithms help you discover stories you’ll find interesting. Our editors create an audio briefing called Apple News Today, covering the biggest stories each weekday morning. You can also subscribe to a daily email newsletter from the Apple News editors highlighting the news you need to know to start your day.\nApple News and Apple News+ both feature the world’s best journalism from trusted sources, curated by human editors and personalized to your interests. With Apple News+ you unlock access to premium content from hundreds of magazines and leading local, national, and international newspapers, cover-to-cover magazine issues you can read online or off, and audio stories — professionally narrated versions of some of the best stories available in Apple News+.\nApple News+ costs just\n$12.99 per month after a free trial. Apple News+ is also included in the Apple One Premier plan, which bundles five other Apple services into a single monthly subscription for\n$37.95 per month.\nWith an Apple News+ subscription, you get access to more than 400 of the world’s best magazines, newspapers, and digital publishers. The magazines cover a wide range of interests, from food to fashion to politics and much more. Newspapers include leading titles such as The Wall Street Journal, Los Angeles Times, Houston Chronicle, and San Francisco Chronicle. Subscribers also receive access to audio stories — professionally narrated versions of some of the best articles available in Apple News+ — and exclusive puzzles updated daily.\nYou can download full issues of your favorite magazines to your Apple devices and access them anywhere, anytime, without an internet connection. You can also listen to Apple News+ audio stories, Apple News Today, and In Conversation offline.\n \nUpdate to the latest version of iOS or macOS to start your Apple News+ free trial.",\
          "image": "https://www.apple.com/v/apple-news/l/images/shared/apple-news__6xg2yiktruqy_og.png?202401091100"\
        },\
        {\
          "id": "https://www.apple.com/us/shop/goto/store",\
          "url": "https://www.apple.com/us/shop/goto/store",\
          "title": "Apple Store Online",\
          "author": "",\
          "publishedDate": "2024-06-18T09:56:09.000Z",\
          "text": "∆ Apple Intelligence is available in beta on all iPhone 16 models, iPhone 15 Pro, and iPhone 15 Pro Max, with Siri and device language set to U.S. English, as an iOS 18 update. English (Australia, Canada, New Zealand, South Africa, UK) language support available this December. Some features and support for additional languages, like Chinese, English (India, Singapore), French, German, Italian, Japanese, Korean, Portuguese, Spanish, Vietnamese, and others, will be coming over the course of the next year. \n^ Apple Intelligence is available in beta on all Mac models with M1 and later, with Siri and device language set to U.S. English, as a macOS Sequoia update. English (Australia, Canada, New Zealand, South Africa, UK) language support available this December. Some features and support for additional languages, like Chinese, English (India, Singapore), French, German, Italian, Japanese, Korean, Portuguese, Spanish, Vietnamese, and others, will be coming over the course of the next year. \n± Apple Intelligence is available in beta on iPad mini (A17 Pro) and iPad models with M1 and later, with Siri and device language set to U.S. English, as an iPadOS 18 update. English (Australia, Canada, New Zealand, South Africa, UK) language support available this December. Some features and support for additional languages, like Chinese, English (India, Singapore), French, German, Italian, Japanese, Korean, Portuguese, Spanish, Vietnamese, and others, will be coming over the course of the next year.\n∆∆ Apple Intelligence is available in beta on all iPhone 16 models, iPhone 15 Pro, iPhone 15 Pro Max, iPad mini (A17 Pro), and iPad and Mac models with M1 and later, with Siri and device language set to U.S. English, as part of an iOS 18, iPadOS 18, and macOS Sequoia update. English (Australia, Canada, New Zealand, South Africa, UK) language support available this December. Some features and support for additional languages, like Chinese, English (India, Singapore), French, German, Italian, Japanese, Korean, Portuguese, Spanish, Vietnamese, and others, will be coming over the course of the next year.\n* Pricing for iPhone 16 and iPhone 16 Plus includes a $30 connectivity discount that requires activation with AT&amp;T, Boost Mobile, T-Mobile, or Verizon. Available to qualified customers and requires 24-month installment loan when you select Citizens One or Apple Card Monthly Installments (ACMI) as payment type at checkout at Apple. You’ll need to select AT&amp;T, Boost Mobile, T-Mobile, or Verizon as your carrier when you check out. An iPhone purchased with ACMI is always unlocked, so you can switch carriers at any time. Subject to credit approval and credit limit. Taxes and shipping are not included in ACMI and are subject to your card’s variable APR. Additional Apple Card Monthly Installments terms are in the Apple Card Customer Agreement (Opens in a new window) . Additional iPhone Payments terms are here (Opens in a new window) . ACMI is not available for purchases made online at special storefronts. The last month’s payment for each product will be the product's purchase price, less all other payments at the monthly payment amount. ACMI financing is subject to change at any time for any reason, including but not limited to, installment term lengths and eligible products. See https://support.apple.com/kb/HT211204 (Opens in a new window)  for information about upcoming changes to ACMI financing.\n◊ Apple Card Monthly Installments (ACMI) is a 0% APR payment option that is only available if you select it at checkout in the U.S. for eligible products purchased at Apple Store locations, apple.com (Opens in a new window) , the Apple Store app, or by calling 1-800-MY-APPLE, and is subject to credit approval and credit limit. See support.apple.com/kb/HT211204 (Opens in a new window)  for more information about eligible products. APR ranges may vary based on when you accepted an Apple Card. Cardholders who accept an Apple Card on and/or after August 1, 2024: Variable APRs for Apple Card, other than ACMI, range from 19.24% to 29.49% based on creditworthiness. Rates as of August 1, 2024. Existing cardholders: See your Customer Agreement for applicable rates and fee. If you buy an ACMI-eligible product by choosing to pay in full with Apple Card (instead of using ACMI), that purchase is subject to the Apple Card variable APR, not 0% APR. Taxes and shipping on ACMI purchases are subject to the variable APR, not 0% APR. When you buy an iPhone with ACMI, you’ll need to select AT&amp;T, Boost Mobile, T-Mobile, or Verizon as your carrier when you check out. An iPhone purchased with ACMI is always unlocked, so you can switch carriers at any time. ACMI is not available for purchases made online at the following special stores: Apple Employee Purchase Plan; participating corporate Employee Purchase Programs; Apple at Work for small businesses; Government and Veterans and Military Purchase Programs; or on refurbished devices. The last month’s payment for each product will be the product’s purchase price, less all other payments at the monthly payment amount. ACMI financing is subject to change at any time for any reason, including but not limited to installment term lengths and eligible products. See support.apple.com/kb/HT211204 (Opens in a new window)  for information about upcoming changes to ACMI financing. See the Apple Card Customer Agreement (Opens in a new window)  for more information about ACMI financing.\nTo access and use all Apple Card features and products available only to Apple Card users, you must add Apple Card to Wallet on an iPhone or iPad that supports and has the latest version of iOS or iPadOS. Apple Card is subject to credit approval, available only for qualifying applicants in the United States, and issued by Goldman Sachs Bank USA, Salt Lake City Branch.\nIf you reside in the U.S. territories, please call Goldman Sachs at 877-255-5923 with questions about Apple Card.\n † Monthly pricing is available when you select Apple Card Monthly Installments (ACMI) as payment type at checkout at Apple, and is subject to credit approval and credit limit. Financing terms vary by product. Taxes and shipping are not included in ACMI and are subject to your card’s variable APR. See the Apple Card Customer Agreement (Opens in a new window)  for more information. ACMI is not available for purchases made online at special storefronts. The last month’s payment for each product will be the product’s purchase price, less all other payments at the monthly payment amount. ACMI financing is subject to change at any time for any reason, including but not limited to, installment term lengths and eligible products. See support.apple.com/kb/HT211204 (Opens in a new window)  for information about upcoming changes to ACMI financing.\n1. Special pricing available to qualified customers. To learn more about how to start qualifying toward special pricing, talk to an Apple Specialist in a store or give us a call at 1‑800‑MY‑APPLE.\n2. $9 two-hour delivery on eligible Apple products in most metros. Offer is not available on customized Mac, engraved products, and for certain order types including orders paid for with financing or by bank transfer. Delivery times vary according to your selected delivery address, availability of your items, and the time of day you place your order. Find a store to view local store hours or see checkout for estimated delivery. A signature is required for delivery. Drivers may ask for verbal confirmation of receipt from a safe distance to satisfy the signature requirement. See  https://www.apple.com/shop/shipping-pickup/ for more information.\n3. Trade-in values will vary based on the condition, year, and configuration of your eligible trade-in device. Not all devices are eligible for credit. You must be at least the age of majority to be eligible to trade in for credit or for an Apple Gift Card. Trade-in value may be applied toward qualifying new device purchase, or added to an Apple Gift Card. Actual value awarded is based on receipt of a qualifying device matching the description provided when estimate was made. Sales tax may be assessed on full value of a new device purchase. In-store trade-in requires presentation of a valid photo ID (local law may require saving this information). Offer may not be available in all stores, and may vary between in-store and online trade-in. Some stores may have additional requirements. Apple or its trade-in partners reserve the right to refuse, cancel, or limit quantity of any trade-in transaction for any reason. More details are available from Apple’s trade-in partner for trade-in and recycling of eligible devices. Restrictions and limitations may apply.\n4. AT&amp;T iPhone 16 Special Deal: Monthly price (if shown) reflects net monthly payment, after application of AT&amp;T trade-in credit applied over 36 months with purchase of an iPhone 16 Pro, iPhone 16 Pro Max, iPhone 16, or iPhone 16 Plus and trade-in of eligible smartphone. Receive credit with purchase of an iPhone 16 Pro or iPhone 16 Pro Max of either $1000, $700, or $350 (based upon the model and condition of your trade-in smartphone). Receive credit with purchase of an iPhone 16 or iPhone 16 Plus of either $700 or $350 (based upon the model and condition of your trade-in smartphone). Max bill credits will not exceed the cost of the device. Requires upgrade of an existing line or activation of a new line and purchase of a new iPhone 16 Pro, iPhone 16 Pro Max, iPhone 16, or iPhone 16 Plus on qualifying 36 month 0% APR installment plan, subject to carrier credit qualification. Customers purchasing this offer through Apple cannot add the Next Up Anytime option. $0 down for well qualified customers only, or down payment may be required and depends on a variety of factors. Tax on full retail price due at sale. Requires activation on eligible AT&amp;T unlimited plan. AT&amp;T may temporarily slow data speeds if the network is busy. If you cancel eligible wireless service, credits will stop and you will owe the remaining device balance. Activation/Upgrade Fee: $35. Trade in device may not be on existing installment plan. Bill credits are applied as a monthly credit over the 36 month installment plan. Credits start within 3 bills. Will receive catchup credits once credits start. Wireless line must be on an installment agreement, active, and in good standing for 30 days to qualify. Installment agreement starts when device is shipped. To get all credits, device must remain on agreement for entire term and you must keep eligible service on device for entire installment term. Limited time offer; subject to change. Limits: one trade-in per qualifying purchase and one credit per line. May not be combinable with other offers, discounts, or credits. Purchase, financing, other limits, and restrictions apply. Price for iPhone 16 and iPhone 16 Plus includes $30 AT&amp;T connectivity discount. Activation required.\n  AT&amp;T iPhone 15 Special Deal: Buy an iPhone 15 128 GB and get $334.36 in bill credits applied over 36 months. Buy an iPhone 15 256 GB and get $254.36 in bill credits applied over 36 months. Buy an iPhone 15 512 GB and get $274.36 in bill credits applied over 36 months. Requires upgrade of an existing line (or activation of a new line) and purchase on qualifying 36-month 0% APR installment plan, subject to carrier credit qualification. $0 down for well-qualified customers only, or down payment may be required and depends on a variety of factors. Tax on full retail price due at sale. Requires activation on eligible AT&amp;T unlimited plan. AT&amp;T may temporarily slow data speeds if the network is busy. If you cancel eligible wireless service, credits will stop and you will owe the remaining device balance. Activation/Upgrade Fee: $35. Bill credits are applied as a monthly credit over the 36-month installment plan. Credits start within 3 bills. Will receive catch-up credits once credits start. Wireless line must be on an installment agreement, active, and in good standing for 30 days to qualify. Installment agreement starts when device is shipped. To get all credits, device must remain on agreement for entire term and you must keep eligible service on device for entire installment term. Limited-time offer; subject to change. Limits: one credit per line. May not be combinable with other offers, discounts, or credits. Purchase, financing, other limits, and restrictions apply. Activation required.\n AT&amp;T iPhone SE Special Deal: Buy an iPhone SE 64 GB and get $214.36 in bill credits applied over 36 months. Buy an iPhone SE 128 GB and get $84.36 in bill credits applied over 36 months. Buy an iPhone SE 256 GB and get $4.36 in bill credits applied over 36 months. Requires upgrade of an existing line (or activation of a new line) and purchase on qualifying 36-month 0% APR installment plan, subject to carrier credit qualification. $0 down for well-qualified customers only, or down payment may be required and depends on a variety of factors. Tax on full retail price due at sale. Requires activation on eligible AT&amp;T unlimited plan. AT&amp;T may temporarily slow data speeds if the network is busy. If you cancel eligible wireless service, credits will stop and you will owe the remaining device balance. Activation/Upgrade Fee: $35. Bill credits are applied as a monthly credit over the 36-month installment plan. Credits start within 3 bills. Will receive catch-up credits once credits start. Wireless line must be on an installment agreement, active, and in good standing for 30 days to qualify. Installment agreement starts when device is shipped. To get all credits, device must remain on agreement for entire term and you must keep eligible service on device for entire installment term. Limited-time offer; subject to change. Limits: one credit per line. May not be combinable with other offers, discounts, or credits. Purchase, financing, other limits, and restrictions apply. Activation required.\n Boost Mobile iPhone 16 Special Deal: Buy an iPhone 16 Pro, iPhone 16 Pro Max, iPhone 16, or iPhone 16 Plus and get $1000 in bill credits (not to exceed the cost of the iPhone) applied over 36 months. No trade-in required. If you are trading in a device with this deal, trade-in value will be applied as additional bill credits over 36 months. Monthly price (if shown) reflects net monthly payment, after application of $1000 in bill credit (not to exceed the cost of the iPhone purchased) and trade-in credit (if applicable) applied over 36 months respectively. Requires activation of a new line, Boost Mobile Infinite Access plan and purchase on qualifying 36-month 0% APR installment plan, subject to carrier credit qualification. After making 12 installment payments, you may upgrade to a new iPhone and get up to $1000 in bill credits (not to exceed the cost of the iPhone) applied over 36 months for the new iPhone on the Infinite Access plan and purchase on new qualifying 36-month 0% APR installment plan, subject to carrier credit qualification. Tax on full retail price due at sale. If you cancel eligible wireless service, credits will stop and you will owe the remaining device balance. Bill credits are applied as a monthly credit over the 36-month installment plan. Trade-in credits start within 3 bills. Installment agreement starts when device is shipped. To get all credits, device must remain on agreement for entire term and you must keep eligible service on device for entire installment term. Limited-time offer; subject to change. Limits: one credit per line. May not be combined with other offers, discounts, or credits. Purchase, financing, other limits, and restrictions apply. Price for iPhone 16 and iPhone 16 Plus includes $30 Boost Mobile connectivity discount. Activation required.\n T-Mobile iPhone 16 Special Deal: Monthly price (if shown) reflects net monthly payment, after application of T-Mobile trade-in credit applied over 24 months with purchase of an iPhone 16 Pro, iPhone 16 Pro Max, iPhone 16, or iPhone 16 Plus and trade-in of eligible smartphone. Receive credit with purchase of an iPhone 16 Pro, iPhone 16 Pro Max, iPhone 16, or iPhone 16 Plus of $1000 or $500 for customers on a Go5G Next plan (based upon the model and condition of your trade-in smartphone); or $800 or $400 for customers on a Go5G Plus plan (based upon the model and condition of your trade-in smartphone). Offer excludes customers on Go5G Next First Responder, Go5G Plus First Responder, Go5G Next Military, Go5G Plus Military, Go5G Next 55, and Go5G Plus 55 plans. Max bill credits will not exceed the cost of the device. Credit comprised of (i) Apple instant trade-in credit at checkout and (ii) T-Mobile monthly bill credits applied over 24 months. Allow 2 bill cycles from valid submission and validation of trade-in. Tax on pre-credit price due at sale. Limited-time offer; subject to change. Qualifying credit, data plan, and trade-in in good condition required. Max 4 promotional offers on any iPhone per account. May not be combinable with some offers or discounts. Price for iPhone 16 and iPhone 16 Plus includes $30 T-Mobile connectivity discount. Activation required. Contact T-Mobile before cancelling service to continue remaining bill credits on current device, or credits stop &amp; balance on required finance agreement is due. \n T-Mobile iPhone 15 Special Deal: Monthly price (if shown) reflects net monthly payment, after application of T-Mobile trade-in credit applied over 24 months with purchase of an iPhone 15 or iPhone 15 Plus and trade-in of eligible smartphone. Receive credit with purchase of an iPhone 15 or 15 Plus of $1000 or $500 for customers on a Go5G Next plan (based upon the model and condition of your trade-in smartphone); or $800 or $400 for customers on a Go5G Plus plan (based upon the model and condition of your trade-in smartphone). Offer excludes customers on Go5G Next First Responder, Go5G Plus First Responder, Go5G Next Military, Go5G Plus Military, Go5G Next 55, and Go5G Plus 55 plans. Max bill credits will not exceed the cost of the device. Credit comprised of (i) Apple instant trade-in credit at checkout and (ii) T-Mobile monthly bill credits applied over 24 months. Allow 2 bill cycles from valid submission and validation of trade-in. Tax on pre-credit price due at sale. Limited-time offer; subject to change. Qualifying credit, data plan, and trade-in in good condition required. Max 4 promotional offers on any iPhone per account. May not be combinable with some offers or discounts. Price for iPhone 15 and iPhone 15 Plus includes $30 T-Mobile connectivity discount. Activation required. Contact T-Mobile before cancelling service to continue remaining bill credits on current device, or credits stop &amp; balance on required finance agreement is due. \n T-Mobile iPhone 14 Special Deal: Monthly price (if shown) reflects net monthly payment, after application of T-Mobile trade-in credit applied over 24 months with purchase of an iPhone 14 or iPhone 14 Plus and trade-in of eligible smartphone. Receive credit with purchase of an iPhone 14 or 14 Plus of $999 or $500 for customers on a Go5G Next plan (based upon the model and condition of your trade-in smartphone); or $800 or $400 for customers on a Go5G Plus plan (based upon the model and condition of your trade-in smartphone). Offer excludes customers on Go5G Next First Responder, Go5G Plus First Responder, Go5G Next Military, Go5G Plus Military, Go5G Next 55, and Go5G Plus 55 plans. Max bill credits will not exceed the cost of the device. Credit comprised of (i) Apple instant trade-in credit at checkout and (ii) T-Mobile monthly bill credits applied over 24 months. Allow 2 bill cycles from valid submission and validation of trade-in. Tax on pre-credit price due at sale. Limited-time offer; subject to change. Qualifying credit, data plan, and trade-in in good condition required. Max 4 promotional offers on any iPhone per account. May not be combinable with some offers or discounts. Price for iPhone 14 and iPhone 14 Plus includes $30 T-Mobile connectivity discount. Activation required. Contact T-Mobile before cancelling service to continue remaining bill credits on current device, or credits stop &amp; balance on required finance agreement is due. \n T-Mobile iPhone SE 3 Special Deal: Monthly price (if shown) reflects net monthly payment, after application of T-Mobile trade-in credit applied over 24 months with purchase of an iPhone SE 3 and trade-in of eligible smartphone. Receive credit with purchase of an iPhone SE 3 of $579 or $500 for customers on a Go5G Next plan (based upon the model and condition of your trade-in smartphone); or $579 or $400 for customers on a Go5G Plus plan (based upon the model and condition of your trade-in smartphone). Offer excludes customers on Go5G Next First Responder, Go5G Plus First Responder, Go5G Next Military, Go5G Plus Military, Go5G Next 55, and Go5G Plus 55 plans. Max bill credits will not exceed the cost of the device. Credit comprised of (i) Apple instant trade-in credit at checkout and (ii) T-Mobile monthly bill credits applied over 24 months. Allow 2 bill cycles from valid submission and validation of trade-in. Tax on pre-credit price due at sale. Limited-time offer; subject to change. Qualifying credit, data plan, and trade-in in good condition required. Max 4 promotional offers on any iPhone per account. May not be combinable with some offers or discounts. Activation required. Contact T-Mobile before cancelling service to continue remaining bill credits on current device, or credits stop &amp; balance on required finance agreement is due. \n Verizon iPhone 16 Special Deal: Monthly price (if shown) reflects net monthly payment, after application of Verizon trade-in credit applied over 36 months with purchase of an iPhone 16 Pro, iPhone 16 Pro Max, iPhone 16, or iPhone 16 Plus. Customers on an Unlimited Ultimate plan receive: $1000 credit (based upon the model and condition of your trade-in smartphone) with purchase of an iPhone 16 Pro or iPhone 16 Pro Max; $930 credit (based upon the model and condition of your trade-in smartphone) with purchase of an iPhone 16 Plus; or $830 credit (based upon the model and condition of your trade-in smartphone) with purchase of an iPhone 16. Customers on an Unlimited Plus plan receive $730 credit (based upon the model and condition of your trade-in smartphone) with purchase of an iPhone 16 Pro, iPhone 16 Pro Max, iPhone 16, or iPhone 16 Plus. Credit comprised of (i) Apple instant trade-in credit at checkout and (ii) Verizon monthly bill credits applied over 36 months. Customer must remain in the Verizon Device Payment Program for 36 months to receive the full benefit of the Verizon bill credits. Bill credits may take 1-2 bill cycles to appear. If it takes two cycles for bill credits to appear, you'll see the credit for the first cycle on your second bill in addition to that month's credit. Requires purchase and activation of a new iPhone 16 Pro, iPhone 16 Pro Max, iPhone 16, or iPhone 16 Plus with the Verizon Device Payment Program at 0% APR for 36 months, subject to carrier credit qualification, and iPhone availability and limits. Taxes and shipping not included in monthly price. Sales tax may be assessed on full value of new iPhone. Requires eligible unlimited service plan. Requires trade-in of eligible device in eligible condition. Must be at least 18 to trade-in. Apple or its trade-in partners reserve the right to refuse or limit any trade-in transaction for any reason. In-store trade-in requires presentation of a valid, government-issued photo ID (local law may require saving this information). In-store promotion availability subject to local law; speak to a Specialist to learn more. Limited-time offer; subject to change. Additional terms from Apple, Verizon, and Apple's trade-in partners may apply. Price for iPhone 16 and iPhone 16 Plus includes $30 Verizon connectivity discount. Activation required.\n⁺ New subscribers only. $10.99/month after trial. Offer is available for new Apple Music subscribers with a new eligible device for a limited time only. Offer redemption for eligible audio devices requires connecting or pairing to an Apple device running the latest iOS or iPadOS. Offer redemption for Apple Watch requires connecting or pairing to an iPhone running the latest iOS. Offer good for three months after eligible device activation. Only one offer per Apple ID, regardless of the number of eligible devices you purchase. Plan automatically renews until cancelled. Restrictions and other terms (Opens in a new window)  apply.\nApple Pay is a service provided by Apple Payments Services LLC, a subsidiary of Apple Inc. Neither Apple Inc. nor Apple Payments Services LLC is a bank. Any card used in Apple Pay is offered by the card issuer.\n We approximate your location from your internet IP address by matching it to a geographic region or from the location entered during your previous visit to Apple.",\
          "image": "https://as-images.apple.com/is/og-default?wid=1200&hei=630&fmt=jpeg&qlt=95&.v=1525370171638"\
        },\
        {\
          "id": "https://www.apple.com/mac/",\
          "url": "https://www.apple.com/mac/",\
          "title": "Mac",\
          "author": "",\
          "publishedDate": "2024-05-07T20:24:00.000Z",\
          "text": "Answer calls or messages from your iPhone directly on your Mac. See and control what’s on your iPhone from your Mac with iPhone Mirroring. Use Universal Clipboard to copy images, video, or text from your iPhone, then paste into another app on your nearby Mac. And thanks to iCloud, you can access your files from either your iPhone or your Mac. And so much more.\nSketch on your iPad and have it appear instantly on your Mac. Or use your iPad as a second display, so you can work on one screen while you reference the other. You can even start a Final Cut Pro project on your iPad and continue it on your Mac.\nAutomatically log in to your Mac when you’re wearing your Apple Watch with Auto Unlock. No password typing required.",\
          "image": "https://www.apple.com/v/mac/home/cb/images/meta/mac__c3zv0c86zu0y_og.png?202410291046"\
        },\
        {\
          "id": "https://www.apple.com/ipad/",\
          "url": "https://www.apple.com/ipad/",\
          "title": "iPad",\
          "author": "",\
          "publishedDate": "2024-05-07T20:24:00.000Z",\
          "text": "Get 3% Daily Cash back with Apple Card. And pay for your new iPad over 12 months, interest‑free when you choose to check out with Apple Card Monthly Installments. ◊  Learn more \niPad is perfect for taking the content you capture on iPhone and bringing it to life on an immersive canvas. You can shoot videos and photos on your iPhone and use the large display of your iPad to edit, add animations, and more. You can also pick up wherever you left off with Handoff.\niPad and Mac are designed to work together to form the ultimate creative setup. Sketch on your iPad and have it appear instantly on your Mac with Sidecar. Then use your iPad for drawing or editing with Apple Pencil or as a second display. Extend your workflow to new places, and when you return to your desk, Universal Control allows you to use one mouse or trackpad seamlessly across both devices.\niPad is a great way to optimize your workouts while tracking your progress on Apple Watch. See personal metrics from Apple Watch integrated on the screen of your iPad in real time. The sensors in Apple Watch combine with advanced algorithms to provide data that keeps you motivated. And see it all come together on your Health app on iPad.",\
          "image": "https://www.apple.com/v/ipad/home/cm/images/meta/ipad__f350v51yy3am_og.png?202410241440"\
        },\
        {\
          "id": "https://www.apple.com/iphone/",\
          "url": "https://www.apple.com/iphone/",\
          "title": "iPhone",\
          "author": "",\
          "publishedDate": "2024-05-07T20:24:00.000Z",\
          "text": "Get credit toward iPhone 16 or iPhone 16 Pro when you trade in an eligible smartphone.    Get credit toward iPhone 16 or iPhone 16 Pro when you trade in an eligible smartphone.  *  Shop iPhone \nWith iPhone Mirroring, you can view your iPhone screen on your Mac and control it without picking up your phone. Continuity features also let you answer calls or messages right from your Mac. You can even copy images, video, or text from your iPhone and paste it all into a different app on your Mac. And with iCloud, you can access your files from either device.\nMisplaced your iPhone? The latest Apple Watch models can show you its approximate distance and direction. 14  To set up a group photo on your iPhone, join the group and use Apple Watch as a viewfinder to snap the shot. And when you take a call on your Apple Watch, just tap your iPhone to continue the conversation there.\nSet up AirPods on iPhone with just a tap. You’ll love Adaptive Audio, which automatically tailors the noise control for you to provide the best listening experience across different environments and interactions throughout the day.",\
          "image": "https://www.apple.com/v/iphone/home/bx/images/meta/iphone__kqge21l9n26q_og.png?202410241440"\
        },\
        {\
          "id": "https://www.apple.com/watch/",\
          "url": "https://www.apple.com/watch/",\
          "title": "Apple Watch",\
          "author": "",\
          "publishedDate": "2024-05-07T20:24:00.000Z",\
          "text": "Combining Apple Watch and iPhone opens up a world of features that make each device better. You can do things like create a custom route with Maps on your iPhone, then download it to your watch to use any time. Or start a cycling workout on your watch and see your metrics automatically appear as a Live Activity on your iPhone.\nApple Watch supercharges your Fitness+ experience with real‑time, personalized metrics onscreen, like your heart rate, calories burned, and Activity rings. 26  And you get the freedom of audio‑guided walks, runs, and meditations with just your watch and AirPods.\nYou can do so much with just Apple Watch and AirPods — all without your iPhone. Take calls, stream music and podcasts, hear incoming notifications. Even respond to messages with Siri.",\
          "image": "https://www.apple.com/v/watch/bo/images/meta/apple-watch__f6h72tjlgx26_og.png?202410031527"\
        },\
        {\
          "id": "https://www.apple.com/apple-vision-pro/",\
          "url": "https://www.apple.com/apple-vision-pro/",\
          "title": "Apple Vision Pro",\
          "author": "",\
          "publishedDate": "2024-05-07T20:24:00.000Z",\
          "text": "Apple Vision Pro seamlessly blends digital content with your physical space.\nSo you can work, watch, relive memories, and connect in ways never before possible.\nThe era of spatial computing is here.\n    Watch the film   \n \nExplore Apple Vision Pro\n \n \nFront\nCameras and sensors\nAudio Straps\nHead bands\nDisplays\nLight Seal\nDigital Crown\nTop button\nPower\nA singular piece of three-dimensionally formed laminated glass flows into an aluminum alloy frame that gently curves to wrap around your face.\nAn array of advanced cameras and sensors work together to let you see the world clearly, understand your environment, and detect hand input.\nSpeakers are positioned close to your ears, delivering rich Spatial Audio that seamlessly blends with real-world sounds.\nTwo head bands are included. The Solo Knit Band provides cushioning, breathability, and stretch, and a Fit Dial lets you adjust Apple Vision Pro to your head. The Dual Loop Band features a pair of adjustable upper and lower straps for a precise fit.\nA pair of custom micro‑OLED displays deliver more pixels than a 4K TV to each eye — for stunning clarity.\nThe Light Seal gently conforms to your face, delivering a precise fit while blocking out stray light.\nPress the Digital Crown to bring up the Home View, and turn it to control your level of immersion while using Environments.\nPress the top button to take spatial videos and spatial photos in the moment.\nThe external battery supports up to 2 hours of general use and up to 2.5 hours of video playback. 1  \nClick or tap each tab to explore Apple Vision Pro.\nEntertainment\nThe ultimate theater.Wherever you are.\nA new dimension for entertainment.\nApple Vision Pro can transform any room into your own personal theater. Expand your movies, shows, and games to your perfect size and experience them in Spatial Audio. Apple Immersive Video puts you in the center of the action with mind‑blowing immersion. And with more pixels than a 4K TV for each eye, you can enjoy stunning content wherever you are — on a long flight or the couch at home.\nProductivity\nA workspace with infinite space.\nDiscover new ways to work.\nApple Vision Pro gives you limitless space to get things done. Organize everything you need anywhere around you, in any way you like. Seamlessly bring in your Mac workflows using Mac Virtual Display. Connect a Magic Keyboard, a Magic Trackpad, and other Bluetooth accessories to expand how you navigate. And with SharePlay in FaceTime, you can collaborate with colleagues using apps together in real time.\nPhotos and Videos\nBe in the moment.All over again.\nYour memories come alive.\nApple Vision Pro is Apple’s first 3D camera. You can capture magical spatial photos and spatial videos in 3D, then relive those cherished moments like never before with immersive Spatial Audio. Your existing library of photos and videos looks incredible at remarkable scale — and now you can transform your 2D photos into spatial photos with just a tap. Even panoramas wrap around you — making you feel like you’re standing right where you took them. You can also take spatial videos with iPhone 16 Pro, iPhone 16, or iPhone 15 Pro, as well as spatial photos with iPhone 16 Pro or iPhone 16, then view them on Apple Vision Pro.\nConnection\nShare quality time.And space.\nA more engaging way to get together.\nApple Vision Pro makes it easy to collaborate and connect wherever you are. You can see FaceTime participants in life-size video tiles, or you can choose to use your spatial Persona and feel like you are sharing the same space with others. And use SharePlay to watch, listen, and play together with your favorite people.\nApps\nDo what you love. Reimagine how you do it.\nA world of apps. A world of discovery.\nApple Vision Pro expands the experience of your go‑to apps and opens up new possibilities in entertainment, productivity, gaming, and more. Browse the web in Safari, create a to‑do list in Notes, chat in Messages, and seamlessly move between them with a glance. And explore the App Store to discover an ever-expanding collection of awe-inspiring spatial apps designed for Apple Vision Pro.\n Visit the App Store    \nvisionOS\nAn operating system designed for spatial.\nNavigate spatial experiences. Naturally.\nBuilt on the foundation of macOS, iOS, and iPadOS, visionOS enables powerful spatial experiences. Control Apple Vision Pro with your eyes, hands, and voice — interactions feel intuitive and magical. Simply look at an element, tap your fingers together to select, and use the virtual keyboard or dictation to type. And visionOS 2 delivers even more ways to enhance work, entertainment, and connecting with friends and family using Apple Vision Pro.\n Learn more about visionOS 2    \nDesign\nDesigned by Apple.\nApple Vision Pro is the result of decades of experience designing high‑performance, mobile, and wearable devices — culminating in the most ambitious product Apple has ever created. Apple Vision Pro integrates incredibly advanced technology into an elegant, compact form, resulting in an amazing experience every time you put it on.\nTechnology\nInnovation you can see, hear, and feel.\nPushing boundaries from the inside out.  Spatial experiences on Apple Vision Pro are only possible through groundbreaking Apple technology. Displays the size of a postage stamp that deliver more pixels than a 4K TV to each eye. Incredible advances in Spatial Audio. A revolutionary dual‑chip design featuring custom Apple silicon. A sophisticated array of cameras and sensors. All the elements work together to create an unprecedented experience you have to see to believe.  \nMore pixels than a 4K TV. For each eye.\nThe custom micro‑OLED display system features 23 million pixels, delivering stunning resolution and colors. And a specially designed three‑element lens creates the feeling of a display that’s everywhere you look.\nOur most advanced Spatial Audio system ever.\nDual-driver audio pods positioned next to each ear deliver personalized sound while letting you hear what’s around you. Spatial Audio makes sounds feel like they’re coming from your surroundings. Audio ray tracing analyzes your room’s acoustic properties to adapt and match sound to your space. And if you want to use headphones with Apple Vision Pro, AirPods Pro 2 with USB‑C and AirPods 4 offer the perfect experience — featuring Lossless Audio with ultra-low latency, supported by the H2‑to‑H2 connection across devices.\nResponsive, precision eye tracking.\nA high‑performance eye‑tracking system of LEDs and infrared cameras projects invisible light patterns onto each eye. This advanced system provides ultraprecise input without your needing to hold any controllers, so you can accurately select elements just by looking at them.\nA sophisticated sensor array.\nA pair of high-resolution cameras transmit over one billion pixels per second to the displays so you can see the world around you clearly. The system also helps deliver precise head and hand tracking and real‑time 3D mapping, all while understanding your hand gestures from a wide range of positions.\nRevolutionary dual‑chip performance.\nA unique dual‑chip design enables the spatial experiences on Apple Vision Pro. The powerful M2 chip simultaneously runs visionOS, executes advanced computer vision algorithms, and delivers stunning graphics, all with incredible efficiency. And the brand-new R1 chip is specifically dedicated to process input from the cameras, sensors, and microphones, streaming images to the displays within 12 milliseconds — for a virtually lag-free, real-time view of the world.\nValues\nDesigned to make a difference.\nOur values lead the way.  Apple Vision Pro was designed to help protect your privacy and keep you in control of your data. Its built‑in accessibility features are designed to work the way you do.  \nUse AR to view Apple Vision Pro.\nOpen this page using Safari on your iPhone or iPad.\nExplore Apple Vision Pro accessories.\n  Shop    \nAn all‑new platform.An all‑new world for developers.\nThe possibilities for what developers can dream up and build for Apple Vision Pro are endless. And with familiar tools and frameworks like Xcode, SwiftUI, RealityKit, and ARKit, as well as support for Unity and the 3D-content preparation app Reality Composer Pro, developers have everything they need to create amazing spatial experiences.\n  Learn more about developing for visionOS",\
          "image": "https://www.apple.com/v/apple-vision-pro/e/images/meta/apple-vision-pro-us__f28gp8ey4vam_og.png?202409261242"\
        },\
        {\
          "id": "https://www.apple.com/airpods/",\
          "url": "https://www.apple.com/airpods/",\
          "title": "AirPods",\
          "author": "",\
          "publishedDate": "2024-09-27T17:22:17.000Z",\
          "text": "AirPods Pro 2 now feature a scientifically validated Hearing Test and clinical‑grade Hearing Aid capability. 1  Learn more \nAirPods 4\nThe next evolution of sound and comfort.\nAirPods Pro 2\nThe world’s first all-in-one hearing health experience.\nFeatures available with a free software update.\nAirPods Max\nFive fresh colors. Bold sound.\nWhich AirPods areright for you?\n    Active Noise Cancellation, Adaptive Audio, and Transparency mode unavailable\n \n \n    Personalized Spatial Audio with dynamic head tracking  ◊◊◊   \n  \n    Hearing Test, Hearing Aid feature, and Hearing Protection unavailable\n \n \n     Voice Isolation,  ΔΔΔ   Hey Siri,and Siri Interactions  ΔΔΔ   \n  \n \n     Charging Case (USB‑C)  ΔΔΔΔ   \n  \n New  AirPods 4\nActive Noise Cancellation\nThe next evolution of sound, comfort, and noise control.\nBuy\n Learn more    \nView in AR\n \n    Active Noise Cancellation, Adaptive Audio, and Transparency mode  ◊   \n  \n \n    Personalized Spatial Audio with dynamic head tracking  ◊◊◊   \n  \n    Hearing Test, Hearing Aid feature, and Hearing Protection unavailable\n \n \n     Voice Isolation,  ΔΔΔ   Hey Siri,and Siri Interactions  ΔΔΔ   \n  \n \n    Wireless Charging Case (USB‑C)  ΔΔΔΔ   with speaker for Find My\n  \n \n    Up to 2x more Active Noise Cancellation,  ◊◊   with Adaptive Audio and Transparency mode  ◊   \n  \n \n    Personalized Spatial Audio with dynamic head tracking  ◊◊◊   \n  \n \n     Hearing Test,  Δ   Hearing Aid,  Δ   and Hearing Protection  ΔΔ   features\n  \n \n     Voice Isolation,  ΔΔΔ   Hey Siri,and Siri Interactions  ΔΔΔ   \n  \n \n    Wireless Charging Case (USB‑C) with MagSafe,  ΔΔΔΔ   speaker for Find My with Precision Finding,  ΔΔΔΔΔ   and lanyard loop\n  \n \n    Up to 2x more Active Noise Cancellation,  ◊◊   with Transparency mode\n  \n \n    Personalized Spatial Audio with dynamic head tracking  ◊◊◊   \n  \n    Hearing Test, Hearing Aid feature, and Hearing Protection unavailable\n \n Compare all AirPods models    \n Get to know AirPods.\n \nApple Music\nGet 3 months of Apple Music free with your AirPods. * \n  Learn more",\
          "image": "https://www.apple.com/v/airpods/x/images/meta/airpods__dh7xkbort402_og.png?202410241631"\
        },\
        {\
          "id": "https://www.apple.com/tv-home/",\
          "url": "https://www.apple.com/tv-home/",\
          "title": "TV & Home",\
          "author": "",\
          "publishedDate": "2024-05-07T20:24:00.000Z",\
          "text": "The future hits home.\nSimply connect your favorite devices and transform your house into a remarkably smart, convenient, and entertaining home. Elevate movie night with theater-like picture and sound. Play any song, in any room, from anywhere. And control lights, locks, and thermostats using Siri. All with the security and privacy of Apple.\nHomePod mini\nSurprising sound for its size.\nThe Apple experience.Cinematic in every sense.\nHome app\nThe foundation for a smarter home.\n Every reason to turn your house into a smart home.\n \nHey Siri, set my bedtime scene\nHey Siri, make it warmer\nHey Siri, turn off the lights downstairs\nNanoleaf A19 Bulb\nLogitech Circle View Wired Doorbell\nComfort\nTurn up the heat or keep your cool with temperature controls and fans.\n  Shop Thermostats     \necobee Smart Thermostat Premium with Siri and Built‑In Air Quality Monitor\nLevel Lock+ with Home Key Support\n Watch, sing, play, and work out. On the big screen.",\
          "image": "https://www.apple.com/v/tv-home/n/images/meta/tv-home__fedwm0ly3mqi_og.png?202409151638"\
        }\
      ]\
    }\
  ],
  "requestId": "17e8a79ff11bcb73115ef3efcb8e0457"
}

```

3. **Blog Content**: Gather recent blog posts:

Python

Copy

```Python
results = exa.get_contents(["https://medium.com"], subpages=5, subpage_target=["blog", "articles"], livecrawl='always')

```

## [](\#best-practices)  Best Practices

1. **Limit Depth**: Start with a smaller `subpages` value (5-10) and increase if needed
2. **Consider Caching**: Use `livecrawl='always'` only when you need the most recent content
3. **Target Specific Sections**: Use `subpage_target` to focus on relevant sections rather than crawling the entire site

## [](\#combining-with-livecrawl)  Combining with LiveCrawl

For the most up-to-date and comprehensive results, combine subpage crawling with livecrawl:

Python

Copy

```Python
result = exa.get_contents(
  ["https://www.apple.com/"],
  livecrawl="always",
  subpage_target=["news", "product"],
  subpages=10
)

```

This ensures you get fresh content from all discovered subpages.

Note that regarding usage, additional subpages count as an additional piece of content retrieval for each type you specify.

[FAQs](/reference/faqs) [Exa LiveCrawl](/reference/should-we-use-livecrawl)

On this page

- [Using Subpage Crawling](#using-subpage-crawling)
- [Parameters:](#parameters)
- [Common Use Cases](#common-use-cases)
- [Best Practices](#best-practices)
- [Combining with LiveCrawl](#combining-with-livecrawl)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

![](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/images/be0cab3-blue-wanderer.png)[Exa home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Search...

Navigation

Getting Started

Welcome to Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

Exa finds the exact content you’re looking for on the web, with three core functionalities:

[**/SEARCH ->**](search)

Find webpages using Exa’s embeddings-based or Google-style keyword search.

[**/CONTENTS ->**](get-contents)

Obtain clean, up-to-date, parsed HTML from Exa search results.

[**/FINDSIMILAR ->**](find-similar-links)

Based on a link, find and return pages that are similar in meaning.

## [](\#get-started)  Get Started

[**QuickStart** \\
\\
Use our SDKs to do your first Exa search.](quickstart) [**RAG with Exa** \\
\\
Use our integrations to peform RAG with Exa.](rag-quickstart) [**Examples** \\
\\
Learn from our pre-built tutorials and live demos.](../examples) [**API Reference** \\
\\
Explore the API endpoints and parameters.](../api-reference)

[Quickstart with SDKs](/reference/quickstart)

On this page

- [Get Started](#get-started)

````