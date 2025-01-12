---
tags:
  - ai coding
---
# Exa Search Documentation

````markdown

## Introduction: Exa Web Search

The Exa Web Search API, formerly known as Metaphor API, is a cutting-edge neural search engine designed to revolutionize web content discovery. Unlike traditional search engines that rely primarily on keyword matching, Exa employs a sophisticated neural approach trained on human content-sharing patterns

## Core Functionalities

### Neural Search

Exa's neural search capability is at the heart of its innovative approach. It uses an embeddings-based index and query model to perform complex searches and provide semantically relevant results. This method is particularly effective for exploratory searches or when looking for conceptually related content rather than exact keyword matches.

### Auto Search

This feature, previously known as Magic Search, automatically selects the optimal search type (neural or keyword) based on the query. It's ideal for users who want the best results without manually choosing a search method[2].

### Keyword Search

For more traditional search needs, Exa also offers a keyword search option. This is useful for simple, broad searches or when looking for exact matches of specific terms or phrases[2].

### Content Retrieval

Exa can instantly retrieve cleaned and parsed webpage contents from search results. This feature is invaluable for users who need the full text of webpages for analysis, summarization, or other post-processing tasks.

### Highlights Extraction

The API can extract relevant excerpts or highlights from retrieved content, providing quick insights into the most pertinent parts of a search result without the need to process the full text[2].

## Advanced Features

### Find Similar Links

Given a URL, Exa can find and return links to content that is similar in nature. This is particularly useful for users who have found a valuable piece of content and are looking for more of the same quality and subject matter[1].

### Long Queries

Exa supports long query windows, allowing for matches against semantically rich content. This is especially useful for finding niche content or when searching for very specific information

### Phrase Filter Search

This feature applies keyword filters on top of a neural search, combining the power of neural search with the precision of specific phrase matching[2].

## API Integration

Exa provides an API for developers to integrate its powerful search capabilities into their applications. This allows software engineers and developers to enhance their products with Exa's advanced search functionalities[1][5].

## Use Cases

1. **Research and Academia**: Exa's ability to find high-quality, relevant academic papers and resources makes it invaluable for researchers, scholars, and students[1].

2. **Content Curation**: Digital marketers and content creators can use Exa to discover trending, high-quality content on specific topics[1].

3. **Large-scale Data Retrieval**: Exa can perform searches that return a large number of results, making it suitable for comprehensive data gathering, such as CRM enrichment or full topic scraping[2].

4. **AI-powered Applications**: Developers can integrate Exa's API into applications requiring advanced search capabilities, especially where context and quality of search results are crucial[1][4].

By leveraging neural networks and advanced AI techniques, Exa offers a more intuitive and efficient way to harness the web's vast resources, providing users with highly relevant and quality search results across a wide range of applications[5].

## Documentation API

## Installation and Setup

Install the Exa Python SDK using pip:

```bash
pip install exa_py
```

Initialize the client with your API key:

```python
from exa_py import Exa
exa = Exa(api_key="your-api-key")
```

## Basic Search Usage

### Simple Search
```python
# Basic neural search
results = exa.search("your search query")

# With autoprompt enabled
results = exa.search("your query", use_autoprompt=True)

# Keyword-based search
results = exa.search("your query", type="keyword")
```

## Search Configuration Options

### Search Types
- **type**: Choose between:
  - `"neural"` - Default, uses embedding-based search
  - `"keyword"` - Traditional keyword search
  - `"auto"` - Automatically selects between neural and keyword[2]

### Result Filtering

**Date Filters**:
```python
results = exa.search(
    "your query",
    start_published_date="2024-01-01",
    end_published_date="2024-11-24"
)
```

**Domain Filtering**:
```python
results = exa.search(
    "your query",
    include_domains=["example.com", "otherdomain.com"],
    exclude_domains=["excludedomain.com"]
)
```

### Content Categories

Specify content focus using the `category` parameter[2]:
```python
results = exa.search(
    "your query",
    category="research paper"
)
```

Available categories:
- company
- research paper
- financial report
- news
- linkedin profile
- github
- tweet
- movie
- song
- personal site
- pdf

## Advanced Content Retrieval

### With Text Contents
```python
results = exa.search_and_contents(
    "your query",
    text={
        "include_html_tags": True,
        "max_characters": 1000
    }
)
```

### With Highlights
```python
results = exa.search_and_contents(
    "your query",
    highlights={
        "highlights_per_url": 2,
        "num_sentences": 1,
        "query": "highlight query"
    }
)
```

## Additional Parameters

- **num_results**: Number of results to return (default: 10, max varies by plan)[2]
- **use_autoprompt**: Converts query to Exa-optimized format when set to True[2]
- **text_must_contain**: List of strings that must appear in results[2]
- **text_must_not_contain**: List of strings that must not appear in results[2]

## Response Format

The search endpoint returns a list of results containing:
- Title
- URL
- Published date
- Author
- Relevance score[2]

## Example API Structuring for Search Endpoint

Here is an example of how the Payload must be structured for the Exa API:

```python
from exa_py import Exa

exa = Exa(api_key="52e88ca7-7a99-46b1-82d9-7c7c8c58eb3f")

result = exa.search_and_contents(
  "Here is an interesting article about AI Search:",
  type="neural",
  use_autoprompt=True,
  num_results=10,
  category="news",
  start_published_date="2024-05-26T11:56:48.881Z",
  end_published_date="2024-11-26T12:56:48.881Z",
  include_domains=["x.com"],
  include_text=["Hello"],
  highlights={
    "query": "What is the highlight?",
    "num_sentences": 1
  },
  summary={
    "query": "What is the summary?"
  },
  subpages=2,
  subpage_target=["About", "Product"],
  livecrawl="always",
  extras={
    "links": 2
  }
)

```

## Example API Result Excerpt for Search Endpoint

```json
{
  "requestId": "6c89850a96a0fb78b2d64c91dea693f5",
  "autopromptString": "Here is an interesting approach for context-augmented retrieval for agent applications:",
  "resolvedSearchType": "neural",
  "results": [
    {
      "score": 0.2165759801864624,
      "title": "RARe: Retrieval Augmented Retrieval with In-Context Examples",
      "id": "https://arxiv.org/abs/2410.20088",
      "url": "https://arxiv.org/abs/2410.20088",
      "publishedDate": "2024-10-26T00:00:00.000Z",
      "author": "Tejaswi; Atula; Lee; Yoonsang; Sanghavi; Sujay; Choi; Eunsol",
      "text": "View PDF\nHTML (experimental)  \nWe investigate whether in-context examples, widely used in decoder-only language models (LLMs), can improve embedding model performance in retrieval tasks. Unlike in LLMs, naively prepending in-context examples (query-document pairs) to the target query at inference time does not work out of the box. We introduce a simple approach to enable retrievers to use in-context examples. Our approach, RARe, finetunes a pre-trained model with in-context examples whose query is semantically similar to the target query. This can be applied to adapt various base architectures (i.e., decoder-only language models, retriever models) and consistently achieves performance gains of up to +2.72% nDCG across various open-domain retrieval datasets (BeIR, RAR-b). In particular, we find RARe exhibits stronger out-of-domain generalization compared to models using queries without in-context examples, similar to what is seen for in-context learning in LLMs. We further provide analysis on the design choices of in-context example augmentation and lay the foundation for future work in this space.\n \nSubmission history  From: Atula Tejaswi Neerkaje [view email]  [v1]\nSat, 26 Oct 2024 05:46:20 UTC (158 KB)",
      "summary": "RARe (Retrieval Augmented Retrieval with In-context Examples) fine-tunes a pre-trained model using in-context examples (semantically similar query-document pairs) to improve retrieval performance.  This approach adapts various base architectures and improves nDCG by up to 2.72% across datasets like BeIR and RAR-b.  Unlike simply prepending examples to queries, RARe incorporates them during fine-tuning.\n",
      "highlights": [
        "We introduce a simple approach to enable retrievers to use in-context examples."
      ],
      "highlightScores": [
        0.4330150783061981
      ]
    },
    {
      "score": 0.21645036339759827,
      "title": "Retrieval-Augmented Decision Transformer: External Memory for In-context RL",
      "id": "https://arxiv.org/abs/2410.07071",
      "url": "https://arxiv.org/abs/2410.07071",
      "publishedDate": "2024-10-09T00:00:00.000Z",
      "author": "Schmied; Thomas; Paischer; Fabian; Patil; Vihang; Hofmarcher; Markus; Pascanu; Razvan; Hochreiter; Sepp",
      "text": "View PDF\nHTML (experimental)  \nIn-context learning (ICL) is the ability of a model to learn a new task by observing a few exemplars in its context. While prevalent in NLP, this capability has recently also been observed in Reinforcement Learning (RL) settings. Prior in-context RL methods, however, require entire episodes in the agent's context. Given that complex environments typically lead to long episodes with sparse rewards, these methods are constrained to simple environments with short episodes. To address these challenges, we introduce Retrieval-Augmented Decision Transformer (RA-DT). RA-DT employs an external memory mechanism to store past experiences from which it retrieves only sub-trajectories relevant for the current situation. The retrieval component in RA-DT does not require training and can be entirely domain-agnostic. We evaluate the capabilities of RA-DT on grid-world environments, robotics simulations, and procedurally-generated video games. On grid-worlds, RA-DT outperforms baselines, while using only a fraction of their context length. Furthermore, we illuminate the limitations of current in-context RL methods on complex environments and discuss future directions. To facilitate future research, we release datasets for four of the considered environments.\n \nSubmission history  From: Thomas Schmied [view email]  [v1]\nWed, 9 Oct 2024 17:15:30 UTC (11,577 KB)",
      "summary": "The paper introduces Retrieval-Augmented Decision Transformer (RA-DT), an in-context reinforcement learning method.  Unlike previous methods requiring entire episodes in the context, RA-DT uses an external memory to store past experiences.  It retrieves only relevant sub-trajectories for the current situation, making it efficient for complex environments with long episodes and sparse rewards.  The retrieval component is untrained and domain-agnostic.\n",
      "highlights": [
        "In-context learning (ICL) is the ability of a model to learn a new task by observing a few exemplars in its context."
      ],
      "highlightScores": [
        0.45809030532836914
      ]
    },
```

## Example API Structuring for Similar Endpoint


Here is an example of how the Payload must be structured for the Exa API (similar Endpoint):

```python

from exa_py import Exa

exa = Exa(api_key="52e88ca7-7a99-46b1-82d9-7c7c8c58eb3f")

result = exa.find_similar_and_contents(
  "brex.com",
  exclude_domains=["brex.com"],
  num_results=10,
  start_published_date="2024-05-26T11:56:48.881Z",
  end_published_date="2024-11-26T12:56:48.881Z",
  text={
    "max_characters": 200
  },
  highlights={
    "num_sentences": 1,
    "highlights_per_url": 1,
    "query": "Hello"
  },
  extras={
    "links": 2
  },
  livecrawl="always",
  summary={
    "query": "Query"
  }
)

```


# Concepts

The Exa Index

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

There are many types of content, and we’re constantly discovering new things to search for as well. If there’s anything you want to be more highly covered, just reach out to [hello@exa.ai](mailto:hello@exa.ai). See the following table for a high level overview of what is available in our index:

| Category | Availability in Exa Index | Description | Example prompt link |
| --- | --- | --- | --- |
| Research papers | Very High | Offer semantic search over a very vast index of papers, enabling sophisticated, multi-layer and complex filtering for use cases | [If you’re looking for the most helpful academic paper on “embeddings for document retrieval”, check this out (pdf:](https://search.exa.ai/search?q=If+you%27re+looking+for+the+most+helpful+academic+paper+on+%22embeddings+for+document+retrieval%22&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22resolvedSearchType%22%3A%22neural%22%2C%22useAutoprompt%22%3Afalse%7D&resolvedSearchType=neural) |
| Personal pages | Very High | Excels at finding personal pages, which are often extremely hard/impossible to find on services like Google | [Here is a link to the best life coach for when you’re unhappy at work:](https://exa.ai/search?q=Here%20is%20a%20link%20to%20the%20best%20life%20coach%20for%20when%20you%27re%20unhappy%20at%20work%3A&c=personal%20site&filters=%7B%22numResults%22%3A30%2C%22useAutoprompt%22%3Afalse%2C%22domainFilterType%22%3A%22include%22%7D) |
| Wikipedia | Very High | Covers all of Wikipedia, providing comprehensive access to this vast knowledge base via semantic search | [Here is a Wikipedia page about a Roman emperor:](https://search.exa.ai/search?q=Here+is+a+Wikipedia+page+about+a+Roman+emperor%3A&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neurall) |
| News | Very High | Includes a wide, robust index of web news sources, providing coverage of current events | [Here is news about war in the Middle East:](https://exa.ai/search?q=Here+is+news+about+war+in+the+Middle+East%3A&c=personal+site&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22auto%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%2C%22startPublishedDate%22%3A%222024-10-29T01%3A45%3A46.055Z%22%7D&resolvedSearchType=keyword) |
| LinkedIn profiles | _Very High (US+EU)_ | Will provide extensive coverage of LinkedIn personal profiles, allowing for detailed professional information searches | b [est theoretical computer scientist at uc berkeley](https://exa.ai/search?q=best+theoretical+computer+scientist+at+uc+berkeley&c=linkedin+profile&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22useAutoprompt%22%3Atrue%2C%22resolvedSearchType%22%3A%22neural%22%7D&autopromptString=A+leading+theoretical+computer+scientist+at+UC+Berkeley.&resolvedSearchType=neural) |
| LinkedIn company pages | _Coming Soon_ | Will offer comprehensive access to LinkedIn company pages, enabling in-depth research on businesses and organization | (Best-practice example TBC) |
| Company home-pages | Very High | Wide index of companies covered; also available are curated, customized company datasets - reach out to learn more | [Here is the homepage of a company working on making space travel cheaper:](https://search.exa.ai/search?q=Here+is+the+homepage+of+a+company+working+on+making+space+travel+cheaper%3A&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |
| Financial Reports | Very High | Includes SEC 10k financial reports and information from other finance sources like Yahoo Finance. | [Here is a source on Apple’s revenue growth rate over the past years:](https://exa.ai/search?q=Here+is+a+source+on+Apple%27s+revenue+growth+rate+over+the+past+years%3A&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22startPublishedDate%22%3A%222023-11-18T22%3A35%3A50.022Z%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |
| GitHub repos | High | Indexes open source code (which the Exa team use frequently!) | [Here’s a Github repo if you want to convert OpenAPI specs to Rust code:](https://exa.ai/search?q=Here%27s+a+Github+repo+if+you+want+to+convert+OpenAPI+specs+to+Rust+code%3A&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |
| Blogs | High | Excels at finding high quality reading material, particularly useful for niche topics | [If you’re a huge fan of Japandi decor, you’d love this blog:](https://exa.ai/search?q=If+you%27re+a+huge+fan+of+Japandi+decor%2C+you%27d+love+this+blog%3A&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |
| Places and things | High | Covers a wide range of entities including hospitals, schools, restaurants, appliances, and electronics | [Here is a high-rated Italian restaurant in downtown Chicago:](https://exa.ai/search?q=Here+is+a+high-rated+Italian+restaurant+in+downtown+Chicago%3A&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |
| Legal and policy sources | High | Strong coverage of legal and policy information, (e.g., including sources like CPUC, Justia, Findlaw, etc.) | [Here is a common law case in california on marital property rights:](https://search.exa.ai/search?q=Here+is+a+common+law+case+in+california+on+marital+property+rights%3A&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22useAutoprompt%22%3Afalse%2C%22includeDomains%22%3A%5B%22law.justia.com%22%5D%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |
| Government and international organization sources | High | Includes content from sources like the IMF and CDC amongst others | [Here is a recent World Health Organization site on global vaccination rates:](https://exa.ai/search?q=Here+is+a+recent+World+Health+Organization+site+on+global+vaccination+rates%3A&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22startPublishedDate%22%3A%222023-11-18T22%3A35%3A50.022Z%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |
| Events | Moderate | Reasonable coverage of events in major municipalities, suggesting room for improvement | [Here is an AI hackathon in SF:](https://search.exa.ai/search?q=Here+is+an+AI+hackathon+in+SF&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22exclude%22%2C%22type%22%3A%22neural%22%2C%22startPublishedDate%22%3A%222024-07-02T23%3A36%3A15.511Z%22%2C%22useAutoprompt%22%3Afalse%2C%22endPublishedDate%22%3A%222024-07-09T23%3A36%3A15.511Z%22%2C%22excludeDomains%22%3A%5B%22twitter.com%22%5D%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |
| Jobs | Moderate | Can find some job listings | [If you’re looking for a software engineering job at a small startup working on an important mission, check out](https://search.exa.ai/search?q=If+you%27re+looking+for+a+software+engineering+job+at+a+small+startup+working+on+an+important+mission%2C+check+out&filters=%7B%22numResults%22%3A30%2C%22domainFilterType%22%3A%22include%22%2C%22type%22%3A%22neural%22%2C%22useAutoprompt%22%3Afalse%2C%22resolvedSearchType%22%3A%22neural%22%7D&resolvedSearchType=neural) |


##

[Exa home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Ctrl K

Search...

Navigation

Concepts

Crawling Subpages with Exa

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

When searching websites, you often need to explore beyond the main page to find relevant information. Exa’s subpage crawling feature allows you to automatically discover and search through linked pages within a website.

## [​](\#using-subpage-crawling)  Using Subpage Crawling

Here’s how to use Exa’s subpage crawling feature:

Python

Copy

```Python
results = exa.get_contents([company_url], subpages=5, subpage_target=["about", "products"])

```

This will search through up to 5 subpages of the given website, and prioritize pages that contain the keywords “about” or “products” in their contents.

## [​](\#parameters)  Parameters:

- `subpages`: Maximum number of subpages to crawl (integer)
- `subpage_target`: List of query keywords to target (e.g., \[“about”, “products”, “news”\])

## [​](\#common-use-cases)  Common Use Cases

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
          "text": "https://docs.exa.ai/reference/recent-news-summarizer\nRecent News Summarizer\n2024-03-02T11:36:31Z\n   \nIn this example, we will build a LLM-based news summarizer app with the Exa API to  with one member of&#34;,\n&#39;A group of Celts known as the Senone was led through Italy by their commander, Brennus. The Senone Gauls were threatening the nearby town of Clusium, when Roman Ambassadors from the Fabii family were sent to negotiate39;\n&#39;market-based measures, they can still prove difficult and require upfront &#39;\n&#39;investment. Georgists believe that the potential value of land is greater &#39;\n&#39;than the current sum of government spending, since the abolition of taxes on &#39;\n&#39;labor and investment would further increase the value of land. Conversely, &#39;\n&#39;the libertarian strain in Georgism is evident in the notion that their land &#39;\n&#39;tax utopia also entails reducing or eliminating the need for many of the &#39;\n&#39;things governments currently supply, such as welfare, infrastructure to &#39;\n&#39;support urban sprawl, and military ith the Exa API Exa was designed with all the features necessary for AI applications:  Filter out noisy SEO results to only the type of content the AI requests Handle long queries – a sentence, a paragraph, or even a whole webpage can be a query Retrieve the page content of any url for downstream processing  Today we're adding highlights. Highlights means Exa can instantly extract any\npiece of content from any result's webpage. Behind the scenes, we’re chunking and embedding\nfull webpages with a paragraph prediction model. Because this happens live, you can customize\nhighlights length, # per page, and specify a secondary query specific to what content you want\nto find. Customers using highlights have seen significant increases in user conversion compared to Bing\nand other search providers. It's exciting to see customers using Exa for so many applications that just weren't possible a\nyear ago, from research paper writing assistants, to lead generation research bots, to\nlearning tools for students. A mission we take seriously As builders at the doorway to the world’s knowledge, we recognize the power we wield. The\nknowledge people consume underlies nearly everything, from our politics to our scientific\nprogress to our daily perceptions of the world. We believe that organizing the world's knowledge, and thereby giving users immense power to\nfilter the internet, is critical societal infrastructure that does not currently exist. Luckily, our incentives are aligned with our values. We have no ad-based need to monetize\nattention. Our API customers want the highest quality search possible. So do we. When the\ninternet feels like a library of all knowledge, we'll know we succeeded. If you want to help us build some of the coolest technology – designing internet-scale web\ncrawling infrastructure, training foundation models for search on our own GPU cluster, serving\ncustom vector databases at scale – you can check out our roles here. And if you're ready to build with the Exa API, you can sign up here. Thanks for reading and we'll keep writing more posts soon so you can join us on the ride!  See more",\
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

3. **Blog Content**: Gather recent blog posts:

Python

Copy

```Python
results = exa.get_contents(["https://medium.com"], subpages=5, subpage_target=["blog", "articles"], livecrawl='always')

```

## [​](\#best-practices)  Best Practices

1. **Limit Depth**: Start with a smaller `subpages` value (5-10) and increase if needed
2. **Consider Caching**: Use `livecrawl='always'` only when you need the most recent content
3. **Target Specific Sections**: Use `subpage_target` to focus on relevant sections rather than crawling the entire site

## [​](\#combining-with-livecrawl)  Combining with LiveCrawl

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


Prompting Guide

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

## [​](\#why-prompting-matters)  Why Prompting Matters

Exa’s neural search excels at understanding natural language descriptions of web content. For optimal results, frame queries as if you’re describing a link to someone.

## [​](\#quick-solutions)  Quick Solutions

1. **Use Autoprompt**: Set `use_autoprompt=True` for automatic query optimization.
2. **Use Auto search**: Use `type="auto"` for intelligent routing to auto vs keyword search, especially where neural is not returning useful results.

## [​](\#prompting-tips)  Prompting Tips

1. **Phrase as Statements**: “Here’s a great article about X:” works better than “What is X?”
2. **Add Context**: Include modifiers like “funny”, “academic”, or specific websites to narrow results.
3. **End with a Colon**: Many effective prompts end with ”:”, mimicking natural link sharing.

## [​](\#examples)  Examples

Bad: “best restaurants in SF”
Good: “Here is the best restaurant in SF:”

Bad: “What’s the best way to learn cooking?”
Good: “This is the best tutorial on how to get started with cooking:”

Remember, Exa is continually improving. These guidelines help leverage its current strengths while we work on making prompting even more intuitive.

[The Exa Index](/reference/the-exa-index) [Contents retrieval with Exa API](/reference/contents-retrieval-with-exa-api)



Contents retrieval with Exa API

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

When using the Exa API, you can request different types of content to be returned for each search result. The three content return types are:

## [​](\#text-text-true)  Text (text=True):

Returns the full text content of the result, such as the main body of an article or webpage. This is extractive content directly taken from the source.

## [​](\#highlights-highlights-true)  Highlights (highlights=True):

Delivers key excerpts from the text that are most relevant to your search query, emphasizing important information within the content. This is also extractive content from the source.

## [​](\#summary-summary-true)  Summary (summary=True):

Provides a concise summary generated from the text, tailored to a specific query you provide. This is abstractive content created by processing the source text using Gemini Flash.

By specifying these options in your API call, you can control the depth and focus of the information returned, making your search results more actionable and relevant.

To see the full configurability of the contents returns, [check out our Dashboard](https://dashboard.exa.ai/) and sample queries.

## [​](\#images-and-favicons)  Images and favicons

When making API requests, Exa can return:

- Image URLs from the source content (you can specify how many images you want returned)
- Website favicons associated with each search result (when available)

[Prompting Guide](/reference/prompting-guide) [Exa's Capabilities Explained](/reference/exas-capabilities-explained)

On this page

- [Text (text=True):](#text-text-true)
- [Highlights (highlights=True):](#highlights-highlights-true)
- [Summary (summary=True):](#summary-summary-true)
- [Images and favicons](#images-and-favicons)

# 

[Exa home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Search...

Navigation

Concepts

Exa's Capabilities Explained

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

## [​](\#search-types)  Search Types

## [​](\#auto-search-prev-magic-search)  Auto search (prev. Magic Search)

| Where you would use it |
| --- |
| When you want optimal results without manually choosing between neural and keyword search. When you might not know ahead of time what the best search type is. Note Auto search is the default search type - when unspecified, Auto search is used. |

Python

```python
result = exa.search("hottest AI startups", type="auto")

```

## [​](\#neural-search)  Neural Search

| Description | Where you would use it |
| --- | --- |
| Uses Exa’s embeddings-based index and query model to perform complex queries and provide semantically relevant results. | For exploratory searches or when looking for conceptually related content rather than exact keyword matches. To find hard to find, specific results from the web |

Python

```python
result = exa.search("Here is a startup building innovative solutions for climate change:", type="neural")

```

## [​](\#keyword-search)  Keyword Search

| Description | Where you would use it |
| --- | --- |
| Traditional search method that matches specific words or phrases. | When doing simple, broad searches where the user can refine results manually. Good for general browsing and finding exact matches. Good for matching proper nouns or terms of art that are rarely used in other contexts. When neural search fails to return what you are looking for. |

Python

```python

result = exa.search("Paris", type="keyword")

```

## [​](\#phrase-filter-search)  Phrase Filter Search

| Description | Where you would use it |
| --- | --- |
| Apply keyword filters atop of a neural search before returning results | When you want the power of Neural Search but also need to specify and filter on some key phrase. Often helpful when filtering on a piece of jargon where a specific match is crucial |

Python

```python
result = exa.search(query, type='neural', includeText='Some_key_phrase_to_fiter_on')

```

[See a worked example here](/tutorials/phrase-filters-niche-company-finder)

## [​](\#large-scale-searches)  Large-scale Searches

| Description | Where you would use it |
| --- | --- |
| Exa searches that return a large number of search results. | When desiring comprehensive, semantically relevant data for batch use cases, e.g., for enrichment of CRMs or full topic scraping. |

Python

```python
result = exa.search("Companies selling sonar technology", num_results=1000)

```

Note high return results cost more and higher result caps (e.g., 1000 returns) are restricted to Enterprise/Custom plans only. [Get in touch](https://cal.com/team/exa/exa-intro-chat?date=2024-11-14&month=2024-11) if you are interested in learning more.

* * *

## [​](\#content-retrieval)  Content Retrieval

## [​](\#contents-retrieval)  Contents Retrieval

| Description | Where you would use it |
| --- | --- |
| Instantly retrieves whole, cleaned and parsed webpage contents from search results. | When you need the full text of webpages for analysis, summarization, or other post-processing. |

Python

```python
result = exa.search_and_contents("latest advancements in quantum computing", text=True)

```

## [​](\#highlights-retrieval)  Highlights Retrieval

| Description | Where you would use it |
| --- | --- |
| Extracts relevant excerpts or highlights from retrieved content. | When you want a quick or targeted outputs from the most relevant parts of a search entity without wanted to handle the full text. |

Python

```python
result = exa.search_and_contents("AI ethics", highlights=True)

```

* * *

## [​](\#prompt-engineering)  Prompt Engineering

Prompt engineering is crucial for getting the most out of Exa’s capabilities. The right prompt can dramatically improve the relevance and usefulness of your search results. This is especially important for neural search and advanced features like writing continuation.

## [​](\#writing-continuation-queries)  Writing continuation queries

| Description | Where you would use it |
| --- | --- |
| Prompt crafted by post-pending ‘Here is a great resource to continue writing this piece of writing:’. Useful for research writing or any other citation-based text generation after passing to an LLM. | When you’re in the middle of writing a piece and need to find relevant sources to continue or expand your content. This is particularly useful for academic writing, content creation, or any scenario where you need to find information that logically follows from what you’ve already written. |

Python

```python
current_text = """
The impact of climate change on global agriculture has been significant.
Rising temperatures and changing precipitation patterns have led to shifts
in crop yields and growing seasons. Some regions have experienced increased
drought stress, while
"""
continuation_query = current_text + " If you found the above interesting, here's another useful resource to read:"
result = exa.search(continuation_query, type="neural", use_autoprompt=False)

```

## [​](\#long-queries)  Long queries

| Description | Where you would use it |
| --- | --- |
| Utilizing Exa’s long query window to perform matches against semantically rich content. | When you need to find content that matches complex, detailed descriptions or when you want to find content similar to a large piece of text. This is particularly useful for finding niche content or when you’re looking for very specific information. |

Python

```python
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

## [​](\#use-autoprompt-incl-autodate)  Use Autoprompt (incl. Autodate)

| Description | Where you would use it |
| --- | --- |
| Automatically optimizes your query for Exa’s neural search. | When you want to leverage Exa’s neural search capabilities without manually crafting the perfect prompt. It’s particularly useful for general-purpose queries or when you’re not sure how to phrase your query for optimal results. |

Python

```python
result = exa.search("AI startups in healthcare", use_autoprompt=True)

```

Note: `use_autoprompt` is set to `False` in some examples above where manual prompt engineering is demonstrated. For most general use cases, leaving it as `True` (the default) will yield good results.

Using autoprompt will also automatically fetch date information as a filter to apply onto searches. For instance, the query:

`Here is the latest news from Russia in the last 7 days`

On July 15 2024, will produce results with an `autoDate` response attribute:

```{ language-plaintext
  "autopromptString": "\"Here is the latest news from Russia:",
  "autoDate": "2024-07-08T17:18:57.152Z",
  "results": ...
}

```

Note the date is no longer in the query, but rather is applied as a strict filter as though you had applied it as a date.

[Contents retrieval with Exa API](/reference/contents-retrieval-with-exa-api) [FAQs](/reference/faqs)

# Concepts: How Exa Search Works

[Exa home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/exa-52/logo/light.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/exa-52/logo/dark.png)](/)

Search or ask...

Search...

Navigation

Concepts

How Exa Search Works

[Documentation](/reference/getting-started) [Examples](/examples/demo-hallucination-detector) [Integrations](/integrations/python-sdk-specification) [Changelog](/changelog/auto-search-as-default)

* * *

## [​](\#introducing-neural-searches-via-next-link-prediction)  Introducing neural searches via ‘next-link prediction’

At Exa, we’ve built our very own index of high quality web content, and have trained a model to query this index powered by the same embeddings-based technology that makes modern LLMs so powerful.

By using embeddings, we move beyond keyword searches to use ‘next-link prediction’, understanding the semantic content of queries and indexed documents. This method predicts which web links are most relevant based on the semantic meaning, not just direct word matches.

By doing this, our model anticipates the most relevant links by understanding complex queries, including indirect or thematic relationships. This approach is especially effective for exploratory searches, where precise terms may be unknown, or where queries demand many, often semantically dense, layered filters.

## [​](\#combining-neural-and-keyword-the-best-of-both-worlds-through-exa-auto-search)  Combining neural and keyword - the best of both worlds through Exa Auto search

Sometimes keyword search is the best way to query the web - for instance, you may have a specific word or piece of jargon that you want to match explicitly with results (often the case with proper nouns like place-names). In these cases, semantic searches are not the most useful.

To ensure our engine is comprehensive, we have built keyword search in parallel to our novel neural search capability. This means Exa is an ‘all-in-one’ search solution, no matter what your query needs are.

Lastly, we surface both query archetypes through ‘Auto search’, to give users the best of both worlds - we have built a small categorization model that understands your query, our search infrastructure and therefore routes your particular query to the best matched search type.

See here for the way we set Auto search in a simple Python example. Type has options `neural`, `keyword` or `auto`.

At one point, Exa auto Auto search was named Magic Search - this has been changed

Python

```Python
result = exa.search_and_contents(
  "hottest AI startups",
  type="auto",
)

```

[Tool calling with Claude](/reference/tool-calling-with-claude) [The Exa Index](/reference/the-exa-index)

On this page

- [Introducing neural searches via ‘next-link prediction’](#introducing-neural-searches-via-next-link-prediction)
- [Combining neural and keyword - the best of both worlds through Exa Auto search](#combining-neural-and-keyword-the-best-of-both-worlds-through-exa-auto-search)




# Using Exa Search with Instructor

- Setting up Exa to use [Instructor](https://python.useinstructor.com/) for structured output generation
- Practical examples of using Exa and Instructor together



Python

Copy

```python
pip install exa_py instructor openai

```

Ensure API keys are initialized properly. The environment variable names are `EXA_API_KEY` and `OPENAI_API_KEY`.

[**Get your Exa API key**](https://dashboard.exa.ai/api-keys)

## [​](\#2-why-use-instructor)  2\. Why use Instructor?

Instructor is a Python library that allows you to generate structured outputs from a language model.

We could instruct the LLM to return a structured output, but the output will still be a string, which we need to convert to a dictionary. What if the dictionary is not structured as we want? What if the LLM forgot to add the last ”}” in the JSON? We would have to handle all of these errors manually.

We could use `{ "type": "json_object" }` which will make the LLM return a JSON object. But for this, we would need to provide a JSON schema, which can get [large and complex](https://python.useinstructor.com/why/#pydantic-over-raw-schema).

Instead of doing this, we can use Instructor. Instructor is powered by [pydantic](https://docs.pydantic.dev/latest/), which means that it integrates with your IDE. We use pydantic’s `BaseModel` to define the output model:

## [​](\#3-setup-and-basic-usage)  3\. Setup and Basic Usage

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

## [​](\#4-advanced-example-analyzing-multiple-research-papers)  4\. Advanced Example: Analyzing Multiple Research Papers

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

## [​](\#5-streaming-structured-outputs)  5\. Streaming Structured Outputs

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

## [​](\#6-writing-results-to-csv)  6\. Writing Results to CSV

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




````