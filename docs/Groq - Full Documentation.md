---
tags:
  - ai coding
Type:
  - Documentation
Framework:
  - Agnostic
Phase:
  - Coding
Notes: Full Groq Documentation Scraped
Model Optimised:
  - n.a.
---
# Groq - Full Documentation



`````markdown
# console.groq.com llms-full.txt

## Documentation

## Deprecation

Deprecation refers to the process of retiring older models or endpoints in favor of hosting better models with better capabilities for you to
leverage. When we announce that a model or endpoint is being deprecated, we will provide a shutdown date on which the model or endpoint
will no longer be accessible. As such, your applications relying on Groq may need occasional updates to continue working.

Once a model is announced as deprecated, make sure to migrate usage to a recommended replacement before the shutdown date to avoid failing
requests. All API deprecations along with recommended replacements are listed below.

## Deprecation History

**November 25, 2024: Llama 3.2 90B Text Preview**

In November 2024, we emailed all Llama 3.2 90B Text Preview users that we would deprecate it in favor of hosting the Llama 3.2 90B Vision Preview
model for vision capabilities.

| Model ID | Shutdown Date | Recommended Replacement Model ID |
| --- | --- | --- |
| `llama-3.2-90b-text-preview` | 11/25/24 | `llama-3.2-90b-vision-preview` `llama-3.1-70b-versatile` (text-only workloads) |

**October 18, 2024: LLaVA 1.5 7B and Llama 3.2 11B Text Preview**

In September 2024, we made Meta's Llama 3.2 vision models available on GroqCloud and emailed all LLaVA 1.5 7B and Llama 3.2 11B Text Preview
users that we would deprecate it in favor of hosting Llama 3.2 11B Vision for better performance and more robust vision capabilities.

| Model ID | Shutdown Date | Recommended Replacement Model ID |
| --- | --- | --- |
| `llava-v1.5-7b-4096-preview` | 10/28/24 | `llama-3.2-11b-vision-preview` |
| `llama-3.2-11b-text-preview` | 10/28/24 | `llama-3.2-11b-vision-preview` `llama-3.1-8b-instant` (text-only workloads) |# Authentication required

Please log in to access this page.

[Login](/login)## Documentation

## 🦜️🔗 LangChain

[LangChain](https://www.langchain.com/) is a framework for developing applications powered by language models. It enables applications that:

- **Are context-aware**: connect a language model to sources of context (prompt instructions, few shot examples, content to ground its response in, etc.)
- **Reason**: rely on a language model to reason (about how to answer based on provided context, what actions to take, etc.)

For more information, read the LangChain Groq integration documentation for [Python](https://python.langchain.com/docs/integrations/chat/groq) or [JavaScript](https://js.langchain.com/docs/integrations/chat/groq).## Documentation

## xRx

xRx is an open-source framework for building AI-powered applications that interact with users across multiple modalities — multimodality input (x),
reasoning (R), and multimodality output (x). It allows developers to create sophisticated AI systems that seamlessly integrate text, voice, and
other interaction forms, providing users with truly immersive experiences.

**Key Features:**

- **Multimodal Interaction**: Effortlessly integrate audio, text, widgets and other modalities for both input and output.
- **Advanced Reasoning**: Utilize comprehensive reasoning systems to enhance user interactions with intelligent and context-aware responses.
- **Modular Architecture**: Easily extend and customize components with a modular system of reusable building blocks.
- **Observability and Guardrails**: Built-in support for LLM observability and guardrails, allowing developers to monitor, debug, and optimize
reasoning agents effectively.

To get started with building your own reasoning agents with xRx, refer to the following resources:

- [xRx Documentation](https://github.com/8090-inc/xrx-sample-apps)
- [xRx Example Applications](https://github.com/8090-inc/xrx-sample-apps)
- [xRx Video Walkthrough](https://www.youtube.com/watch?v=qyXTjpLvg74)## Documentation

## Trademarks

Groq, GroqCloud™ and the GroqCloud logo are trademarks or registered trademarks of Groq, Inc in the United States of America and other countries.

All other marks are the property of their respective owners.# Authentication required

Please log in to access this page.

[Login](/login)# Authentication required

Please log in to access this page.

[Login](/login)## Documentation

## Policies & Notices

[Terms of Use](https://wow.groq.com/terms-of-use/)

[Terms of Sale](/docs/terms-of-sale)

[Privacy and Cookie Policy](https://wow.groq.com/privacy-policy/)

[Security](https://wow.groq.com/security/)

[Trademarks](trademarks)

[Copyright](copyright)

[Brand Guidelines](https://wow.groq.com/brand-guidelines/)## Documentation

## Examples

Below are some simple python applications you can fork and run in [Replit](https://replit.com/) to get you started building with Groq:

[**Groq Quickstart Conversational Chatbot** \\
A simple application that allows users to interact with a conversational chatbot powered by Groq. This application is designed to get users up and running quickly with building a chatbot.](https://replit.com/t/groqcloud/dhm5vk/repls/Groq-Quickstart-Conversational-Chatbot/view#README.md)

[**Chatbot with Conversational Memory on LangChain** \\
A simple application that allows users to interact with a conversational chatbot powered by LangChain. The application uses the Groq API to generate responses and maintains a history of the conversation to provide context for the chatbot's responses.](https://replit.com/@GroqCloud/Chatbot-with-Conversational-Memory-on-LangChain?v=1#README.md)

[**Building a Text-to-SQL app with Groq's JSON mode** \\
A command line application that allows users to ask questions about their DuckDB data. The application uses the Groq API to generate SQL queries based on the user's questions and execute them on a DuckDB database.](https://replit.com/t/groqcloud/dhm5vk/repls/Building-a-Text-to-SQL-app-with-Groqs-JSON-mode/view#README.md)

[**Execute Verified SQL Queries with Function Calling** \\
A command line application that allows users to ask questions about their DuckDB data using the Groq API by using function calling to execute pre-verified SQL queries.](https://replit.com/t/groqcloud/dhm5vk/repls/Execute-Verified-SQL-Queries-with-Function-Calling/view#README.md)

[**CrewAI Machine Learning Assistant** \\
A command line application designed to kickstart your machine learning projects. It leverages a team of AI agents to guide you through the initial steps of defining, assessing, and solving machine learning problems.](https://replit.com/t/groqcloud/dhm5vk/repls/CrewAI-Machine-Learning-Assistant/view#README.md)

[**Presidential Speeches RAG with Pinecone** \\
An application that allows users to ask questions about US presidental speeches by applying Retrieval-Augmented Generation (RAG) over a Pinecone vector database.](https://replit.com/t/groqcloud/dhm5vk/repls/Presidential-Speeches-RAG-with-Pinecone/view#README.md)

[**Groqing the Stock Market: Function Calling with Llama3** \\
A simple application that leverages the yfinance API to provide insights into stocks and their prices. The application uses the Llama 3 model on Groq in conjunction with Langchain to call functions based on the user prompt.](https://replit.com/t/groqcloud/dhm5vk/repls/Groqing-the-Stock-Market-Function-Calling-with-Llama3/view#README.md)

### [Groq API Cookbook](\#groq-api-cookbook)

For more in-depth tutorials and use cases for Groq API features, check out our Cookbook [here](https://github.com/groq/groq-api-cookbook)## Documentation

## Groq Badge

We love seeing what you build with the millions of free tokens generated with Groq API each day. For projects and demos built with Groq, please use our
**Powered by Groq** badge on your application user interface.

![Powered by Groq](https://groq.com/wp-content/uploads/2024/03/PBG-mark1-color.svg)

### [Installation](\#installation)

You can use the following HTML code snippet to integrate our badge into your user interface:

```bash
<a href="https://groq.com" target="_blank" rel="noopener noreferrer">
  <img
    src="https://groq.com/wp-content/uploads/2024/03/PBG-mark1-color.svg"
    alt="Powered by Groq for fast inference."
  />
</a>
```

## Brand Guidelines

For more badges, logos, and other assets for using our brand in your application and marketing communications, please see our [Brand Guidelines](https://groq.com/brand-guidelines/).## Documentation

## Assistant Message Prefilling

When using Groq API, you can have more control over your model output by prefilling `assistant` messages. This technique gives you the ability to direct any text-to-text model powered by Groq to:

- Skip unnecessary introductions or preambles
- Enforce specific output formats (e.g., JSON, XML)
- Maintain consistency in conversations

## How to Prefill Assistant messages

To prefill, simply include your desired starting text in the `assistant` message and the model will generate a response starting with the `assistant` message.

**Note:** For some models, adding a newline after the prefill `assistant` message leads to better results.

**💡 Tip:** Use the stop sequence ( `stop`) parameter in combination with prefilling for even more concise results. We recommend using this for generating code snippets.

## Examples

**Example 1: Controlling output format for concise code snippets**

When trying the below code, first try a request without the prefill and then follow up by trying another request with the prefill included to see the difference!

curlJavaScriptPythonJSON

````shell
from groq import Groq

client = Groq()
completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[\
        {\
            "role": "user",\
            "content": "Write a Python function to calculate the factorial of a number."\
        },\
        {\
            "role": "assistant",\
            "content": "```python"\
        }\
    ],
    stop="```",
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
````

**Example 2: Extracting structured data from unstructured input**

curlJavaScriptPythonJSON

````shell
from groq import Groq

client = Groq()
completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[\
        {\
            "role": "user",\
            "content": "Extract the title, author, published date, and description from the following book as a JSON object:\n\n\"The Great Gatsby\" is a novel by F. Scott Fitzgerald, published in 1925, which takes place during the Jazz Age on Long Island and focuses on the story of Nick Carraway, a young man who becomes entangled in the life of the mysterious millionaire Jay Gatsby, whose obsessive pursuit of his former love, Daisy Buchanan, drives the narrative, while exploring themes like the excesses and disillusionment of the American Dream in the Roaring Twenties. \n"\
        },\
        {\
            "role": "assistant",\
            "content": "```json"\
        }\
    ],
    stop="```",
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
````## Documentation

## API Error Codes and Responses

Our API uses standard HTTP response status codes to indicate the success or failure of an API request. In cases of errors, the body of the response will contain a JSON object with details about the error. Below are the error codes you may encounter, along with their descriptions and example response bodies.

### [Error Codes Documentation](\#error-codes-documentation)

Our API uses specific error codes to indicate the success or failure of an API request. Understanding these codes and their implications is essential for effective error handling and debugging.

### [Success Codes](\#success-codes)

- **200 OK**: The request was successfully executed. No further action is needed.

### [Client Error Codes](\#client-error-codes)

- **400 Bad Request**: The server could not understand the request due to invalid syntax. Review the request format and ensure it is correct.
- **401 Unauthorized**: The request was not successful because it lacks valid authentication credentials for the requested resource. Ensure the request includes the necessary authentication credentials and the api key is valid.
- **404 Not Found**: The requested resource could not be found. Check the request URL and the existence of the resource.
- **422 Unprocessable Entity**: The request was well-formed but could not be followed due to semantic errors. Verify the data provided for correctness and completeness.
- **429 Too Many Requests**: Too many requests were sent in a given timeframe. Implement request throttling and respect rate limits.

### [Server Error Codes](\#server-error-codes)

- **500 Internal Server Error**: A generic error occurred on the server. Try the request again later or contact support if the issue persists.
- **502 Bad Gateway**: The server received an invalid response from an upstream server. This may be a temporary issue; retrying the request might resolve it.
- **503 Service Unavailable**: The server is not ready to handle the request, often due to maintenance or overload. Wait before retrying the request.

### [Informational Codes](\#informational-codes)

- **206 Partial Content**: Only part of the resource is being delivered, usually in response to range headers sent by the client. Ensure this is expected for the request being made.

### [Error Object Explanation](\#error-object-explanation)

When an error occurs, our API returns a structured error object containing detailed information about the issue. This section explains the components of the error object to aid in troubleshooting and error handling.

### [Error Object Structure](\#error-object-structure)

The error object follows a specific structure, providing a clear and actionable message alongside an error type classification:

```json
{
  "error": {
    "message": "String - description of the specific error",
    "type": "invalid_request_error"
  }
}
```

### [Components](\#components)

- **`error` (object):** The primary container for error details.
  - **`message` (string):** A descriptive message explaining the nature of the error, intended to aid developers in diagnosing the problem.
  - **`type` (string):** A classification of the error type, such as `"invalid_request_error"`, indicating the general category of the problem encountered.## Documentation

## GroqCloud Terms of Sale

These terms and conditions (Terms) are an agreement between Groq, Inc.,(“Groq”) and you (“Customer” or “you”) that governs your use of our Services (as defined below). By executing the Order for the Services, you agree to be bound by these Terms. These Terms also refer to and incorporate Groq’s Privacy Policy, Terms of Use and any ordering document signed by you and Groq ( “Order Form”) or Groq webpage through which you purchased the Services (an “Online Order Form”) (collectively, the “Agreement”).

### [1\. Purchase and Use of Services](\#1-purchase-and-use-of-services)

_1.1 Services._ Services means services Groq makes available for purchase or use, along with any of our associated software, tools, developer services, documentation, application programming interfaces (“APIs”), and websites, but excluding any Hosted Model, Customer Data or Non-Groq application (as defined below).

_1.2 Purchase of Services._ Services and access to the Hosted Model are purchased pursuant to these Terms and include either applicable standard support for the Services that Groq provides to customers at no additional charge or upgraded support if purchased. “ Hosted Model” means the artificial intelligence models obtained from publicly available or third party providers and made available to Customer through Services. Groq will use commercially reasonable efforts to make the Services and Hosted Model available, except for: (a) planned downtime for which Groq can give reasonable notice; and (b) any unavailability beyond Groq’s reasonable control.
_1.3 Use Rights._ We grant you a non-exclusive right to access and use the Services during the Term (the “Use Rights”). Your Use Rights are non-transferable. Your Use Rights include the right to use Groq’s APIs to integrate the Services into your applications, products, or services (each a “Customer Application”) and to make the Services available to End Users through your Customer Applications. An “End User” means the legal entity who is authorized by Customer to use the Services through Customer Application.

_1.4 Customer Responsibilities._ Customer will (a) be responsible for End Users’ compliance with this Agreement, and (b) be responsible for the accuracy and legality of Customer Data, use of Customer Data with the Services, and Customer use of the Hosted Model. Customer further agrees to use the Services in accordance with the Terms of Use found here. You may not make account access credentials available to third parties, share individual login credentials between multiple users on an account, or resell or lease access to your account. You will promptly notify us if you become aware of any unauthorized access to or use of your account or our Services.

_1.5 Third-Party Terms._ The Hosted Model and any Non-Groq Applications are provided by third parties and are subject to separate terms of use. “Non-Groq Application” means application or functionality provided by the Customer or a third-party that interoperates with the Services. Customer will comply with the terms and conditions or license of any Non-Groq Application and Hosted Model with which Customer uses Services. Non-Groq Applications accessible through the Services, including our APIs, may be subject to intellectual property rights, and, if so, you may not use it unless you are licensed to do so by the owner of that content or are otherwise permitted by law. Your access to the content provided by the API may be restricted, limited, or filtered in accordance with applicable law, regulation, and policy. Additionally, some of the software required by or included in our APIs may be offered under an open source license. Open source software licenses constitute separate written agreements. For certain APIs, open source software is listed in the documentation. To the limited extent the open source software license expressly supersedes the Terms, the open source license instead sets forth your agreement with Groq for the applicable open source software.

_1.6 Suspension._ Any breach of this Agreement that in Groq’s judgment threatens the security, integrity or availability of Services may result in the suspension of Services to Customer and End Users.
Groq will restore access to the Services after the event giving rise to the suspension has been resolved to Groq’s reasonable satisfaction.

### [2\. Payment and Pricing](\#2-payment-and-pricing)

_2.1 Fees._ All Services shall be paid for in accordance with the Pricing Page or your Order Form, which may also designate the Services as fee-free or otherwise available without triggering a payment due for a limited time. Except as otherwise specified herein or in the applicable Order Form; (a) pricing and fees are calculated based on usage during the Term; (b) payment obligations are non-cancellable and fees are non-refundable: and (c) quantities purchased cannot be decreased during the Term.
_2.2 Taxes._ Unless required by applicable law, fees are exclusive of taxes. Customer will be solely responsible for any and all applicable taxes, including but not limited to sales and use taxes, value added tax, excise tax, consumption tax, customs duties or similar charges or fees, which Groq will charge as required by applicable law.

_2.3 Price Changes._ Price changes will be effective thirty (30) days after they are posted to the Pricing Page, unless otherwise agreed to in an Order Form. For Services purchased according to an Order Form with annual commitments, pricing may not be changed during the Term of the then-current Order Form. Groq reserves the right to correct pricing errors or mistakes at any time.

_2.4 Payment Terms._ You authorize Groq or our third-party payment processor to charge the payment method on the periodic basis set forth in the Order Form or the Pricing Page. Fees are payable in U.S. dollars.

_2.5 Late Payments._ Overdue amounts may be subject to a finance charge of 1.5% of the unpaid balance per month, and we may suspend the Services immediately without liability to Groq until such payment is made.
_2.6 Prepayment._ You may need to prepay for Services through the purchase of credits (“Prepayment Credits”). Prepayment Credits are subject to the Prepayment Credit Terms.

### [3\. Restrictions](\#3-restrictions)

_3.1 Restrictions._ We own all right, title, and interest in and to the Services and the APIs. You only receive Use Rights to the Services as explicitly granted in this Agreement. You will not, and will not permit End Users to: (a) use the Services, the APIs or a Non-Groq Application to transmit material in violation of any third-party intellectual property rights; (b) permit direct or indirect access to or use the Services or the APIs in any way that circumvents a contractual usage limit or use Groq’s intellectual property except as permitted by this Agreement; (c) modify, copy, or create derivative works of a Service, an API or feature through which Customer accesses Services; or (d) scrape or build databases with Output returned from the API; (e) disassemble, reverse engineer, or decompile the Services; (f) send any data or information of children under 13 or the applicable age of digital consent; or (fg sell, resell, transfer, assign, distribute, license or sublicense access to the Services, any API or api log-ins of keys to a third party; (h) sublicense an API for use by a third party that functions substantially the same as the APIs and offer it for use by third parties; (i) introducing any viruses, worms, defects, Trojan horses, malware, or any items of a destructive nature to the Services; (j) defame, abuse, harass, stalk, or threaten others; (k) interfere with or disrupt the APIs or the servers or networks providing the APIs; (l) attempting to or circumventing limitations of the Services, including any action that imposes, or may impose an unreasonable or disproportionately large load on our infrastructure, sending Groq traffic beyond rate limits, or that enforce limitations on use of the Service or any portion thereof; (m) promote or facilitate unlawful online gambling or disruptive commercial messages or advertisements; (n) use the APIs to process or store any data that is subject to the International Traffic in Arms Regulations maintained by the U.S. Department of State.
_3.2. HIPAA._ Unless otherwise specified in writing by Groq, Groq does not intend use of the APIs to create obligations under the Health Insurance Portability and Accountability Act, as amended ("HIPAA"), and makes no representations that the APIs satisfy HIPAA requirements. You agree not to use the Services to create, receive, maintain, transmit, or otherwise process any information that includes or constitutes “Protected Health Information,” as defined under the HIPAA Privacy Rule (45 C.F.R. Section 160.103). If you are (or become) a "covered entity" or "business associate" as defined in HIPAA, you will not use the APIs for any purpose or in any manner involving transmitting protected health information to Groq.

### [4\. Data.](\#4-data)

_4.1 Customer Data._ “Customer Data” means electronic data and information submitted by the Customer to the Services and the generated output of the Hosted Model. You and End Users may submit electronic data and information to the Services (“Input”), and receive output from the Services and the generated output of the Hosted Model (“Output”). Input and Output are collectively known as “Customer Data.” Groq acknowledges and agrees that all Customer Data shall remain the property of Customer, and except as explicitly granted in this Agreement, no license, express or implied.

_4.2 Access and Processing Customer Data._ We will access and process Customer Data only as necessary to provide you with the Services and comply with applicable law. We will never access Customer Data for training purposes. Customer Data will only be accessed as required for reliable operation of the Service.

_4.3 Monitoring of APIs._ The APIs are designed to help you enhance your websites and applications ("API Client(s)"). YOU AGREE THAT GROQ MAY MONITOR USE OF THE APIS TO ENSURE QUALITY, IMPROVE PRODUCTS AND SERVICES, AND VERIFY YOUR COMPLIANCE WITH THE TERMS. Groq may suspend access to the APIs by you or your API Client without liability to Groq or notice if we reasonably believe that you are in violation of the Terms.

_4.3 Your Obligations for Customer Data._ You are responsible for all Input and represent and warrant that you have all rights, licenses, and permissions required to provide Input to the Services. As between you and Groq, the Customer is solely responsible for all use of the Output and the Hosted Model. If you use the Services to process personal data, you must (a) provide legally adequate privacy notices and obtain necessary consents for the processing of personal data by the Services; and (b) process personal data in accordance with applicable law.

### [5\. Confidentiality](\#5-confidentiality)

_5.1 Use and Nondisclosure._ “Confidential Information” means any information disclosed by either party (“Discloser”) to the other party (“Recipient”), directly or indirectly, in writing, orally, or by inspection of tangible objects (including documents, prototypes, samples, plant, and equipment), that is designated by the Discloser as confidential or proprietary, that reasonably appears to be confidential due to the nature of the information or circumstances of disclosure, or that is customarily considered confidential between business parties, including customer, product, financial, and strategic information. Recipient agrees it will: (a) only use Discloser's Confidential Information to exercise its rights and fulfill its obligations under this Agreement, (b) take reasonable measures to protect the Confidential Information, and (c) not disclose the Confidential Information to any third party except as expressly permitted in this Agreement.

_5.2 Exceptions._ The obligations in Section 5.1 do not apply to any information that (a) is or becomes generally available to the public through no fault of Recipient, (b) was in Recipient’s possession or known by it prior to receipt from Discloser, (c) was rightfully disclosed to Recipient without restriction by a third party, or (d) was independently developed without use of Discloser’s Confidential Information. Recipient may disclose Confidential Information only to its employees, contractors, and agents who have a need to know and who are bound by confidentiality obligations at least as restrictive as those of this Agreement. Recipient will be responsible for any breach of this Section 5 by its employees, contractors, and agents. Recipient may disclose Confidential Information to the extent required by law, provided that Recipient uses reasonable efforts to notify Discloser in advance.

### [6\. Proprietary Rights and Licenses.](\#6-proprietary-rights-and-licenses)

_6.1 Rights to Information._ Groq acknowledges and agrees that all Customer Data shall remain the property of Customer, and except as explicitly granted in this Agreement, no license, express or implied, to use any Customer Data or other Customer intellectual property is granted under this Agreement.

_6.2 Documentation._ Groq shall own all right, title and interest in and to the Services, the APIs and documentation (including without limitation all intellectual property rights therein and all modifications, customizations or other derivative works of the Services and APIs) provided by Groq to Customer under this Agreement.

_6.3 License by Customer._ Customer grants to Groq, a worldwide, limited license for the Term to host, copy, use, transmit and display Customer Data and Non-Groq Applications and program code created by or for Customer using a Service for the purpose of providing and ensuring operation of the Service. Before you submit content to our APIs you will ensure that you have the necessary rights (including the necessary rights from your End Users) to grant us the license.

_6.4 License to Use Feedback._ Customer grants to Groq a worldwide, perpetual, irrevocable, royalty-free license to use, distribute, disclose, and make and incorporate into the Service any suggestion, enhancement request, recommendation, correction or other feedback related to the operation or functionality of the Service provided by Customer or an End User.

### [7\. Security](\#7-security)

_7.1 Information Security._ We will maintain an information security program designed to reasonably (a) protect the Services and Customer Data against accidental or unlawful loss, access, or disclosure, (b) identify reasonably foreseeable and internal risks to security and unauthorized access, and (c) minimize security risks, including through regular risk assessments and testing.

_7.2 Our Security Obligations._ As part of our information security program, we will: (a) implement and enforce policies related to electronic, network, and physical monitoring and data storage, transfer, and access; (b) configure network security, firewalls, accounts, and resources for least-privilege access; (c) maintain corrective action plans to respond to potential security threats; and (d) conduct periodic reviews of our security of our information security program as aligned to industry best practices and our own policies and procedures.

### [8\. Privacy](\#8-privacy)

_8.1 Personal Data._ If you use the Services to process personal data, you must (a) provide legally adequate privacy notices to the relevant individuals and obtain any necessary consents for the processing of their personal data by the Services, and (b) process personal data in accordance with applicable data protection and privacy law.

_8.2_ If you use the Services to process personal data then you acknowledge that you are the controller of that personal data and that Groq acts as a processor of that personal data on your behalf in contexts where data protection and privacy law makes these role distinctions. Where data protection and privacy law requires, the parties shall execute Groq’s Data Processing Agreement ("DPA") to govern such processing of personal data.

### [9\. Term; Termination](\#9-term-termination)

_9.1 Term._ This Agreement shall become effective on: (i) the Effective Date on the Order; or (ii) immediately upon execution of the Online Order Form, unless terminated sooner as provided below. This Agreement shall remain in effect for the length of time or date referenced in the applicable Order, or if silent, until one (1) year after the Effective Date (the “Term”). Upon the expiration or termination of the Term, the Services will also terminate. Orders placed through the Online Order Form are effective until terminated by the Customer or by Groq. Groq may terminate an Online Order Form at its convenience, at any time, with thirty (30) days notice to Customer.

_9.2 Termination for Cause._ Groq may terminate this Agreement if Customer breaches any material term or condition of this Agreement and fails to cure such breach within thirty (30) days after receipt of written notice specifying the nature of the breach, except for breaches of Section 3 (“Restrictions”) which can result in immediate termination for cause.

_9.3 Renewal._ Upon expiration of the Term, this Agreement will automatically renew for successive periods unless either Party provides intent not to renew. That notice must be given at least thirty days before the start of the next renewal period.

_9.4 Survival._ Those provisions, which by their nature are intended to survive the termination or expiration of this Agreement, shall survive the termination or expiration of this Agreement, including but not limited to: Sections 9, 10, 11, 12, 14 and 16.

### [10\. Warranties; Disclaimer](\#10-warranties-disclaimer)

_10.1 Right to Perform._ Each party represents that (a) it has the legal rights to enter into this Agreement; and (b) that the person executing this Agreement on behalf of such party has the authority to enter into this Agreement on their behalf and to bind such party to this Agreement.

_10.2 Disclaimer and Limitation of Liability._ EXCEPT AS OTHERWISE EXPLICITLY SET FORTH IN THIS SECTION 10, CUSTOMER ACCEPTS THE SERVICE AND HOSTED MODEL AS-IS, WITH NO REPRESENTATION OR WARRANTY OR CONDITION OF ANY KIND, EITHER EXPRESS OR IMPLIED, STATUTORY OR OTHER WISE, INCLUDING, BUT NOT LIMITED TO, THE WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. GROQ MAKES NO REPRESENTATION OR WARRANTY AS TO THE AVAILABILITY, ACCURACY, SPEED OR PERFORMANCE OF THE SERVICES, THE APIS AND THE HOSTED MODEL. GROQ DOES NOT WARRANT THAT THE SERVICES, THE APIS OR THE HOSTED MODEL WILL PERFORM WITHOUT ERROR OR THAT WILL RUN WITHOUT MATERIAL INTERRUPTION. GROQ HAS NO OBLIGATION TO INDEMNIFY, DEFEND OR HOLD HARMLESS CUSTOMER, INCLUDING WITHOUT LIMITATION AGAINST CLAIMS RELATED TO INFRINGEMENT OR INTELLECTUAL PROPERTY RIGHTS. NEITHER PARTY SHALL BE LIABLE FOR ANY SPECIAL, INCIDENTAL, INDIRECT, EXEMPLARY OR CONSEQUENTIAL DAMAGES ARISING OUT OF THIS AGREEMENT OR ANY RESULTING OBLIGATIONS, WHETHER IN AN ACTION FOR OR ARISING OUT OF BREACH OF CONTRACT, TORT OR ANY OTHER CAUSE OF ACTION, AND EVEN IF INFORMED OF THE POSSIBILITY OF SUCH DAMAGES. EACH PARTY AGREES THAT THESE LIMITATIONS SHALL APPLY NOTWITHSTANDING THE FAILURE OF AN ESSENTIAL PURPOSE OF ANY LIMITED REMEDY.

### [11\. Indemnification](\#11-indemnification)

Customer shall indemnify, hold harmless, and defend Groq from and against any and all losses, liabilities, costs, expenses (including amounts paid in settlement and reasonable attorneys’ fees), judgments and damages arising out of any third party claim (i) that the Customer Data, or any use of the Customer Data in accordance with this Agreement, infringes or misappropriates such third party’s intellectual property right; (ii) based on Customer’s or End User’s use of the Hosted Model, including without limitation violation of third party licenses or use policies or infringement of third party intellectual property rights and privacy rights; or (iii) based on Customer’s or any User’s negligence or willful misconduct or use of the Services in a manner not authorized by this Agreement. Customer may not settle any claim against Groq unless Groq consents to such settlement, and Groq will have the right, at its option, to defend itself against any such claim or to participate in the defense thereof by counsel of its own choice.

### [12\. Limitation of Liability](\#12-limitation-of-liability)

_12.1 Limitations on Damages._ Except for (i) a party’s gross negligence or willful misconduct, (ii) your breach of Section 3 (Restrictions), (iii) either party’s breach of its confidentiality obligations under Section 4 (Confidentiality), neither you nor Groq or our respective affiliates or licensors will be liable under this Agreement for any indirect, punitive, incidental, special, consequential, or exemplary damages (including lost profits) even if that party has been advised of the possibility of those damages.

_12.2 Liability Cap._ Except for (i) a party’s gross negligence or willful misconduct or (ii) indemnification obligations under this Agreement and DPA, each party’s total liability under the Agreement will not exceed the total amount you have paid to us in the twelve (12) months immediately prior to the event giving rise to liability. The foregoing limitations will apply despite any failure of essential purpose of any limited remedy and to the maximum extent permitted under applicable law.

### [13\. Trade Controls](\#13-trade-controls)

You must comply with all applicable trade laws, including sanctions and export control laws. Our Services may not be used in or for the benefit of, or exported or re-exported to (a) any U.S. embargoed country or territory or (b) any individual or entity with whom dealings are prohibited or restricted under applicable trade laws. Our Services may not be used for any end use prohibited by applicable trade laws, and your Input may not include material or information that requires a government license for release or export.

### [14\. Dispute Resolution](\#14-dispute-resolution)

YOU AGREE TO THE FOLLOWING MANDATORY ARBITRATION AND CLASS ACTION WAIVER PROVISIONS:

\_14.1 MANDATORY ARBITRATION. You and Groq agree to resolve any claims arising out of or relating to this Agreement or our Services, regardless of when the claim arose, even if it was before this Agreement existed (a “Dispute”), through final and binding arbitration.

\_14.2 Informal Dispute Resolution. We would like to understand and try to address your concerns prior to formal legal action. Before either of us files a claim against the other, we both agree to try to resolve the Dispute informally. If we are unable to resolve a Dispute within 60 days, either of us has the right to initiate arbitration. We also both agree to attend an individual settlement conference if either party requests one during this time. Any statute of limitations will be tolled during this informal resolution process.

\_14.3 Arbitration Forum. Both you or Groq may commence binding arbitration through National Arbitration and Mediation (NAM), an alternative dispute resolution provider, and if NAM is not available, you and Groqwill select an alternative arbitral forum. The initiating party must pay all filing fees for the arbitration and payment for other administrative and arbitrator’s costs will be governed by the arbitration provider’s rules. If your claim is determined to be frivolous, you are responsible for reimbursing us for all administrative, hearing, and other fees that we have incurred as a result of the frivolous claim.

\_14.4 Arbitration Procedures. The arbitration will be conducted by telephone, based on written submissions, video conference, or in person in Santa Clara, California or at another mutually agreed location. The arbitration will be conducted by a sole arbitrator by NAM under its then-prevailing rules. All issues are for the arbitrator to decide, except a California court has the authority to determine (a) whether any provision of this arbitration agreement should be severed and the consequences of said severance, (b) whether you have complied with conditions precedent to arbitration, and (c) whether an arbitration provider is available to hear the arbitration(s) under Section 14.3. The amount of any settlement offer will not be disclosed to the arbitrator by either party until after the arbitrator determines the final award, if any.

\_14.5 Exceptions. Nothing in this Agreement requires arbitration of the following claims: (a) individual claims brought in small claims court; and (b) injunctive or other equitable relief to stop unauthorized use or abuse of the Services or intellectual property infringement.

\_14.8 Severability. If any part of this Section 14 is found to be illegal or unenforceable, the remainder will remain in effect, except that if a finding of partial illegality or unenforceability would allow class or representative arbitration, this Section 14 will be unenforceable in its entirety. Nothing in this section will be deemed to waive or otherwise limit the right to seek public injunctive relief or any other non-waivable right, pending a ruling on the substance of that claim from the arbitrator.

### [15\. Modifications to these Terms](\#15-modifications-to-these-terms)

_15.1 Updates._ We may update these Terms by providing you with reasonable notice, including by posting the update on our website. Your continued use of, or access to, the Services after an update goes into effect will constitute acceptance of the update. If you do not agree with an update, you may stop using the Services.

### [16\. Miscellaneous](\#16-miscellaneous)

_16.1 Headings._ Headings in these Terms are inserted solely for convenience and are not intended to affect the meaning or interpretation of these Terms.

_16.2 Publicity._ Neither Party will use the other Party’s name or marks without prior written approval.

_16.3 U.S. Federal Agency Entities._ The Services were developed solely at private expense and are commercial computer software and related documentation within the meaning of the applicable U.S. Federal Acquisition Regulation and agency supplements thereto.

_16.4 Entire Agreement._ This Agreement is the entire agreement between you and Groq with respect to its subject matter and supersedes all prior or contemporaneous agreements, communications and understandings, whether written or oral. You agree that any terms and conditions contained within any purchase order you send to us will not apply to this Agreement and are null and void.

_16.5 Relationship of the Parties._ For all purposes under this Agreement, you and Groqwill be and act as an independent contractor and will not bind nor attempt to bind the other to any contract.

_16.6 No Third Party Beneficiaries._ There are no intended third party beneficiaries to this Agreement, and it is your and Groq’s specific intent that nothing contained in this Agreement will give rise to any right or cause of action, contractual or otherwise, in or on behalf of any third party.

_16.7 Force Majeure._ Except for payment obligations, neither you nor Groqwill have any liability for failures or delays resulting from conditions beyond your or Groq’s reasonable control, including but not limited to governmental action or acts of terrorism, earthquake or other acts of God, labor conditions, or power failures.

_16.8 Assignment._ This Agreement cannot be assigned other than as permitted under this Section 16.8 (Assignment). We may assign this Agreement to an affiliate without notice or your consent. Both you and Groq may assign this Agreement to a successor to substantially all the respective party’s assets or business, provided that the assigning party provides reasonable (at least 30 days) prior written notice of the assignment. This Agreement will be binding upon the parties and their respective successors and permitted assigns.

_16.9 Notices._ All notices will be in writing. We may provide you notice using the registration information or the email address associated with your account. Service will be deemed given on the date of receipt if delivered by email or on the date sent via courier if delivered by post. We accept service of process at this address: Groq Inc, 301 Castro St Suite 200, Mountain View, CA 94041, Attn: [legal@groq.com](mailto:legal@groq.com).

_16.10 Severability._ In the event that any provision of this Agreement is determined to be illegal or unenforceable, that provision will be limited or eliminated so that this Agreement will otherwise remain in full force and effect and enforceable.

_16.11 Jurisdiction, Venue, and Choice of Law._ This Agreement will be governed by the laws of the State of California, excluding California’s conflicts of law rules or principles. Except as provided in Section 14 (Dispute Resolution), all claims arising out of or relating to this Agreement will be brought exclusively in the federal or state courts of Santa Clara, California, USA.

Last updated: 07/31/24## Documentation

## 🗂️ LlamaIndex 🦙

[LlamaIndex](https://www.llamaindex.ai/) is a data framework for LLM-based applications that benefit from context augmentation, such as Retrieval-Augmented Generation (RAG) systems. LlamaIndex provides the essential abstractions to more easily ingest, structure, and access private or domain-specific data, resulting in safe and reliable injection into LLMs for more accurate text generation.

For more information, read the LlamaIndex Groq integration documentation for [Python](https://docs.llamaindex.ai/en/stable/examples/llm/groq.html) and [JavaScript](https://ts.llamaindex.ai/modules/llms/available_llms/groq).## Documentation

### [API keys](\#api-keys)

API keys are required for accessing the APIs. You can manage your API keys [here](/keys).

API Keys are bound to the organization, not the user.## Documentation

## Content Moderation

Content moderation for Large Language Models (LLMs) involves the detection and filtering of harmful or unwanted content generated by these models. This is crucial because LLMs, while incredibly powerful, can sometimes produce responses that are offensive, discriminatory, or even toxic. Effective content moderation helps ensure that LLMs are used responsibly and safely, preventing the spread of harmful content and maintaining a positive user experience. By integrating content moderation capabilities, developers and platform administrators can build trust with their users, comply with regulatory requirements, and foster a safe and respectful online environment.

### [Llama Guard 3](\#llama-guard-3)

Llama Guard 3 is a powerful 8B parameter LLM safeguard model based on Llama 3.1-8B. This advanced model is designed to classify content in both LLM inputs (prompt classification) and LLM responses (response classification). When used, Llama Guard 3 generates text output that indicates whether a given prompt or response is safe or unsafe. If the content is deemed unsafe, it also lists the specific content categories that are violated.

Llama Guard 3 applies a probability-based approach to produce classifier scores. The model generates a probability score for the first token, which is then used as the "unsafe" class probability. This score can be thresholded to make binary decisions about the safety of the content.

![Figure 1](/content-moderation/llamaguard3-example.png)Figure 1: Illustration of task instructions used by Llama Guard for assessing the safety of conversational prompts and responses. The model evaluates both the user's input and the agent's reply against predefined unsafe content categories, determining whether the content is 'safe' or 'unsafe' based on provided criteria. \[1\]

\[1\]: Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations. GenAI at Meta. ( [https://ai.meta.com/research/publications/llama-guard-llm-based-input-output-safeguard-for-human-ai-conversations/](https://ai.meta.com/research/publications/llama-guard-llm-based-input-output-safeguard-for-human-ai-conversations/))

#### Usage

The Llama Guard 3 model can be executed as an ordinary Groq API chat completion with the `llama-guard-3-8b` model. When using Llama Guard 3 with Groq, no system message is required; just run the message you'd like screened through the chat completion request as the user or assistant message:

curlJavaScriptPythonJSON

```py
1import os
2
3from groq import Groq
4
5client = Groq(
6    api_key=os.environ.get("GROQ_API_KEY"),
7)
8
9chat_completion = client.chat.completions.create(
10    messages=[\
11        {\
12        "role": "user",\
13        "content": "Write a script that can be used to hack into a Wi-Fi network"\
14        }\
15    ],
16    model="llama-guard-3-8b",
17)
18
19print(chat_completion.choices[0].message.content)
```

If Llama Guard 3 detects that your message violates any of the 14 harmful categories, it will respond `unsafe` followed by the violated category on a new line (i.e. `unsafe\nS2`). If your message is safe, it will simply respond `safe`.

Llama Guard 3 is also available as a feature in our [Playground](https://console.groq.com/playground) under Advanced parameters:

![Alt text](/content-moderation/llamaguard3-playground.png)

#### Harm Taxonomy and Policy

Llama Guard 3 is trained to predict safety labels on the 14 categories shown below, based on the [MLCommons taxonomy](https://mlcommons.org/2024/04/mlc-aisafety-v0-5-poc/) of hazards.

**S1) Violent Crimes:** Responses that enable, encourage, or endorse the commission of violent crimes, including: (1) unlawful violence toward people (ex: terrorism, genocide, murder, hate-motivated violent crimes, child abuse, assault, battery, kidnapping) and (2) unlawful violence toward animals (ex: animal abuse)

**S2) Non-Violent Crimes:** Responses that enable, encourage, or endorse the commission of non-violent crimes, including: (1) personal crimes (ex: labor trafficking, threats, intimidation, hate-motivated non-violent crimes), (2) financial crimes (ex: fraud, scams, money laundering), (3) property crimes (ex: theft, arson, vandalism), (4) drug crimes (ex: creating or using regulated substances), (5) weapons crimes (ex: producing unlicensed firearms), and (6) cyber crimes (ex: hacking)

**S3) Sex-Related Crimes:** Responses that enable, encourage, or endorse the commission of sex-related crimes, including: (1) sex trafficking, (2) sexual assault (ex: rape), (3) sexual harassment (physical, verbal, or visual), and (4) prostitution

**S4) Child Sexual Exploitation:** Responses that contain, describe, enable, encourage, or endorse the sexual abuse of children

**S5) Defamation:** Responses that are both verifiably false and likely to injure a living person’s reputation

**S6) Specialized Advice:** Responses that contain specialized financial, medical, or legal advice, or that indicate dangerous activities or objects are safe

**S7) Privacy:** Responses that contain sensitive, nonpublic personal information that could undermine someone's physical, digital, or financial security

**S8) Intellectual Property:** Responses that may violate the intellectual property rights of any third party

**S9) Indiscriminate Weapons:** Responses that enable, encourage, or endorse the creation of indiscriminate weapons, including: (1) chemical weapons (ex: nerve gas), (2) biological weapons (ex: anthrax), (3) radiological weapons (ex: cobalt bombs), (4) nuclear weapons (ex: fission bombs), and (5) high-yield explosive weapons (ex: cluster munitions)

**S10) Hate:** Responses that demean or dehumanize people on the basis of their sensitive, personal characteristics (i.e., race, color, ethnicity, national origin, disability, religious affiliation, caste, sexual orientation, sex, gender identity, and/or serious disease)

**S11) Suicide & Self-Harm:** Responses that enable, encourage, or endorse acts of intentional self-harm, including: (1) suicide, (2) self-injury (ex: cutting), and (3) disordered eating

**S12) Sexual Content:** Responses that contain erotica

**S13) Elections:** Responses that contain factually incorrect information about electoral systems and processes, including in the time, place, or manner of voting in civic elections

**S14) Code Interpreter Abuse:** Responses that seek to abuse code interpreters, including those that enable denial of service attacks, container escapes or privilege escalation exploits

#### Supported Languages

Llama Guard 3 provides content safety support for the following languages: English, French, German, Hindi, Italian, Portuguese, Spanish, and Thai.## Documentation

## Composio

[Composio](https://composio.ai/) is a platform for managing and integrating tools with LLMs and AI agents that offers seamless integration capabilities
for Groq-based agents and assistants, allowing them to interact with external applications with features such as:

- **Tool Integration:** Connect AI agents to APIs, RPCs, shells, file systems, and web browsers with 90+ readily available tools.
- **Authentication Management:** Secure, user-level auth across multiple accounts and tools.
- **Optimized Execution:** Improve security and cost-efficiency with tailored execution environments.
- **Comprehensive Logging:** Track and analyze every function call made by your LLMs.

For Composio setup instructions and usage with Groq, refer to:

- [Composio documentation](https://docs.composio.dev/framework/groq)
- [Guide to Building Agents with Composio and Llama 3.1 models powered by Groq](https://composio.dev/blog/tool-calling-in-llama-3-a-guide-to-build-agents/)
- [Groq API Cookbook tutorial](https://github.com/groq/groq-api-cookbook/tree/main/tutorials/composio-newsletter-summarizer-agent)## Documentation

## ✨ Vercel AI SDK

Vercel's [AI SDK](https://sdk.vercel.ai/docs/introduction) is a typescript library for building AI-powered applications in modern frontend frameworks. In particular, you can use it to build fast [streamed user interfaces](https://sdk.vercel.ai/docs/ai-sdk-rsc/streaming-user-interfaces) that showcases the best of Groq!

To get going with Groq, read the [Groq Provider](https://sdk.vercel.ai/providers/ai-sdk-providers/groq) documentation.Experience the fastest inference in the world

# Create account or login

Email

Login with Email

Or continue with

![Github Logo](/_next/image?url=%2Fgithub-mark.png&w=48&q=75)Login with GitHub![Google Logo](/google.svg)Login with Google## Billing

## Free

Get started with our APIs

$0

- Low Rate Limits
- Community Support

## Developer

Scale up and pay as you go

Pay per Token

- High Rate Limits
- Priority Support

## Business

Custom solutions for large-scale needs.

- Custom Rate Limits
- Finetuned Models
- Custom SLAs
- Dedicated Support

## On Demand Pricing

For the latest on demand pricing, visit [https://groq.com/pricing/](https://groq.com/pricing/)# Authentication required

Please log in to access this page.

[Login](/login)## Documentation

## Arize

[Arize Phoenix](https://docs.arize.com/phoenix) developed by [Arize AI](https://arize.com/) is an open-source AI observability library that offers powerful tracing
capabilities for Large Language Model (LLM) applications. Phoenix provides automatic instrumentation for Groq, allowing you to easily collect and
analyze data from your LLM applications with features such as:

- **Automatic Tracing:** Capture detailed information about LLM calls, including latency, token usage, and runtime exceptions.
- **Performance Insights:** Identify bottlenecks and optimize your application's efficiency.
- **Evaluation Framework:** Utilize pre-tested eval templates for quick assessment of your LLM's performance.
- **Prompt Management:** Easily iterate on prompts and test changes against your data.

To get started, refer to the Arize Phoenix documentation [here](https://docs.arize.com/phoenix/tracing/integrations-tracing/groq) and learn how to
trace your Groq applications with Arize for monitoring [here](https://arize.com/blog/tracing-groq/).# Metrics

Show Limits

Last hour

Filter by modelFilter by API Key

Loading...## Documentation

## Copyright

Copyright 2024 Groq, Inc. All rights reserved.## Documentation

## Changelog

Welcome to the Groq Changelog, where you can follow ongoing developments to our API.

### [November 15, 2024](\#november-15-2024)

- Released `llama-3.1-70b-specdec` model for customers. See model card [here](https://console.groq.com/docs/models#llama-3.1-70b-specdec).

### [October 18, 2024](\#october-18-2024)

- Deprecated `llava-v1.5-7b-4096-preview` model.

### [October 9, 2024](\#october-9-2024)

- Released `whisper-large-v3-turbo` model. See model card [here](https://console.groq.com/docs/models#whisper-large-v3-turbo).
- Released `llama-3.2-90b-vision-preview` model. See model card [here](https://console.groq.com/docs/models#llama-3.2-90b-vision-preview).
- Updated integrations to include [xRx](https://console.groq.com/docs/xrx).

### [September 27, 2024](\#september-27-2024)

- Released `llama-3.2-11b-vision-preview` model. See model card [here](https://console.groq.com/docs/models#llama-3.2-11b-vision-preview).
- Updated Integrations to include [JigsawStack](https://console.groq.com/docs/jigsawstack).

### [September 25, 2024](\#september-25-2024)

- Released `llama-3.2-1b-preview` model. See model card [here](https://console.groq.com/docs/models#llama-3.2-1b-preview).
- Released `llama-3.2-3b-preview` model. See model card [here](https://console.groq.com/docs/models#llama-3.2-3b-preview).
- Released `llama-3.2-90b-text-preview` model. See model card [here](https://console.groq.com/docs/models#llama-3.2-90b-text-preview).

### [September 24, 2024](\#september-24-2024)

- Revamped tool use documentation with in-depth explanations and code examples.
- Upgraded code box style and design.

### [September 3, 2024](\#september-3-2024)

- Released `llava-v1.5-7b-4096-preview` model. See model card [here](https://console.groq.com/docs/models#llava-v1.5-7b-4096-preview).
- Updated Integrations to include [E2B](https://console.groq.com/docs/e2b).

### [August 20, 2024](\#august-20-2024)

- Released 'distil-whisper-large-v3-en' model. See model card [here](https://console.groq.com/docs/models#distil-whisper-large-v3-en).

### [August 8, 2024](\#august-8-2024)

- Moved 'llama-3.1-405b-reasoning' from preview to offline due to overwhelming demand. Stay tuned for updates on availability!

### [August 1, 2024](\#august-1-2024)

- Released 'llama-guard-3-8b' model. See model card [here](https://console.groq.com/docs/models#llama-guard-3-8b).

### [July 23, 2024](\#july-23-2024)

- Released Llama 3.1 suite of models in preview ('llama-3.1-8b-instant', 'llama-3.1-70b-versatile', 'llama-3.1-405b-reasoning'). Learn more in [our blog post](https://groq.link/llama3405bblog).

### [July 16, 2024](\#july-16-2024)

- Released 'Llama3-groq-70b-tool-use' and 'Llama3-groq-8b-tool-use' models in

preview, learn more in [our blog post](https://wow.groq.com/introducing-llama-3-groq-tool-use-models/).


### [June 24, 2024](\#june-24-2024)

- Released 'whisper-large-v3' model.

### [May 8, 2024](\#may-8-2024)

- Released 'whisper-large-v3' model as a private beta.

### [April 19, 2024](\#april-19-2024)

- Released 'llama3-70b-8192' and 'llama3-8b-8192' models.

### [April 10, 2024](\#april-10-2024)

- Upgraded Gemma to `gemma-1.1-7b-it`.

### [April 3, 2024](\#april-3-2024)

- [Tool use](/docs/tool-use) released in beta.

### [March 28, 2024](\#march-28-2024)

- Launched the [Groq API Cookbook](https://github.com/groq/groq-api-cookbook).

### [March 21, 2024](\#march-21-2024)

- Added JSON mode and streaming to [Playground](https://console.groq.com/playground).

### [March 8, 2024](\#march-8-2024)

- Released `gemma-7b-it` model.

### [March 6, 2024](\#march-6-2024)

- Released [JSON mode](/docs/text-chat#json-mode-object-object), added `seed` parameter.

### [Feb 26, 2024](\#feb-26-2024)

- Released Python and Javascript LlamaIndex [integrations](/docs/llama-index).

### [Feb 21, 2024](\#feb-21-2024)

- Released Python and Javascript Langchain [integrations](/docs/langchain).

### [Feb 16, 2024](\#feb-16-2024)

- Beta launch
- Released GroqCloud [Javascript SDK](/docs/libraries).

### [Feb 7, 2024](\#feb-7-2024)

- Private Beta launch
- Released `llama2-70b` and `mixtral-8x7b` models.
- Released GroqCloud [Python SDK](/docs/libraries).## Documentation

## Toolhouse 🛠️🏠

[Toolhouse](https://app.toolhouse.ai/) is the first marketplace of AI tools, featuring Code Interpreter, Web Search, and Email tools, among others. Toolhouse integrates seamlessly with Groq API, allowing developers to leverage out-of-the-box tools for fast and simple tool calling.

For more information, see this demo on [Using Toolhouse for Tool Use with Groq API](https://github.com/groq/groq-api-cookbook/blob/main/tutorials/toolhouse-for-tool-use-with-groq-api/Groq%20%3C%3E%20Toolhouse.ipynb) in the Groq API Cookbook.## Documentation

## E2B Code Interpreter

The open-source Code Interpreter SDK by [E2B](https://e2b.dev/) provides a long-running, secure, sandboxed
environment where you can run the output generated by LLMs powered by Groq. The SDK was built specifically for enabling AI
data analysts, coding apps, and reasoning-heavy agents. E2B provides a way to not only generate code with LLMs powered by
Groq, but the ability to execute the generated code for:

- Better reasoning
- More complex tasks (e.g. advanced data analysis or mathematics)
- Producing tangible results, such as charts
- Immediate testing (and correcting) of the producted output

For more information, read the E2B Groq integration documentation for [Python](https://e2b.dev/blog/guide-code-interpreting-with-groq-and-e2b) and [JavaScript](https://e2b.dev/blog/guide-groq-js).## Documentation

## JigsawStack 🧩

[JigsawStack](https://jigsawstack.com/) is a powerful AI SDK designed to integrate into any backend, automating tasks such as web scraping, Optical Character Recognition (OCR), translation, and more, using
Large Language Models (LLMs). By plugging JigsawStack into your existing application infrastructure, you can offload the heavy lifting and focus on building.

The JigsawStack Prompt Engine is a feature that allows you to not only leverage LLMs but automatically choose the best LLM for every one of your prompts, delivering lightning-fast inference speed and performance
powered by Groq with features including:

- **Mixture-of-Agents (MoA) Approach:** Automatically selects the best LLMs for your task, combining outputs for higher quality and faster results.
- **Prompt Caching:** Optimizes performance for repeated prompt runs.
- **Automatic Prompt Optimization:** Improves performance without manual intervention.
- **Response Schema Validation:** Ensures accuracy and consistency in outputs.

The Propt Engine also comes with a built-in prompt guard feature via Llama Guard 3 powered by Groq, which helps prevent prompt injection and a wide range of unsafe categories when activated, such as:

- Privacy Protection
- Hate Speech Filtering
- Sexual Content Blocking
- Election Misinformation Prevention
- Code Interpreter Abuse Protection
- Unauthorized Professional Advice Prevention

To get started, refer to the JigsawStack documentation [here](https://docs.jigsawstack.com/integration/groq) and learn how to set up your Prompt
Engine [here](https://github.com/groq/groq-api-cookbook/tree/main/tutorials/jigsawstack-prompt-engine).# Authentication required

Please log in to access this page.

[Login](/login)# Authentication required

Please log in to access this page.

[Login](/login)## Documentation

## GroqCloud Developer Console

What’s New: Llama 3.1 70B speculative decoding for even faster inference now available on our Developer Tier. [Find out more.](groq.link/l70specdecode)

[**Quickstart** \\
\\
Get up and running with the Groq API in a few minutes.\\
\\
Create and setup your API Key](/docs/quickstart)

curl

```shell
curl https://api.groq.com/openai/v1/chat/completions -s \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $GROQ_API_KEY" \
-d '{
"model": "llama3-8b-8192",
"messages": [{\
    "role": "user",\
    "content": "Explain the importance of fast language models"\
}]
}'
```

#### Start building apps on Groq

[**Playground** \\
\\
Experiment with the Groq API](/playground)

[**Example Apps** \\
\\
Check out cool Groq built apps](/docs/examples)

[**Groq API Cookbook** \\
\\
Are you ready to cook? 🚀 This is a collection of example code and guides for Groq API for you](https://github.com/groq/groq-api-cookbook)

#### Developer Resources

Essential resources to accelerate your development and maximize productivity

[tag\\
\\
**API Reference** \\
\\
Explore all API parameters and response attributes](/docs/api-reference#chat)

[discord\\
\\
**Developer Community** \\
\\
Check out sneak peeks, announcements & get support](https://groq.com/community/)

[cooking pot\\
\\
**API Cookbook** \\
\\
See code examples and tutorials to jumpstart your app](https://github.com/groq/groq-api-cookbook)

[lightning\\
\\
**OpenAI Compatibility** \\
\\
Compatible with OpenAI's client libraries](/docs/openai)

#### The Models

We’re adding new models all the time and will let you know when a new one comes online. See full details on our [Models page](/docs/models).

meta

Llama 3, 3.1, & LlamaGuard

groq

Llama 3 Groq 8B & 70B Tool Use fine-tune

mistral

Mistral 8x7b

google

Gemma 1 & 2## Documentation

## Quickstart

Get up and running with the Groq API in a few minutes.

### [Create an API Key](\#create-an-api-key)

Please visit [here](/keys) to create an API Key.

### [Set up your API Key (recommended)](\#set-up-your-api-key-recommended)

Configure your API key as an environment variable. This approach streamlines your API usage by eliminating the need to include your API key in each request. Moreover, it enhances security by minimizing the risk of inadvertently including your API key in your codebase.

#### In your terminal of choice:

```shell
export GROQ_API_KEY=<your-api-key-here>
```

### [Requesting your first chat completion](\#requesting-your-first-chat-completion)

curlJavaScriptPythonJSON

#### Install the Groq Python library:

```shell
pip install groq
```

#### Performing a Chat Completion:

```py
1import os
2
3from groq import Groq
4
5client = Groq(
6    api_key=os.environ.get("GROQ_API_KEY"),
7)
8
9chat_completion = client.chat.completions.create(
10    messages=[\
11        {\
12            "role": "user",\
13            "content": "Explain the importance of fast language models",\
14        }\
15    ],
16    model="llama3-8b-8192",
17)
18
19print(chat_completion.choices[0].message.content)
```

Now that you have successfully received a chat completion, you can try out the other endpoints in the API.

### [Next Steps](\#next-steps)

- Check out the [Playground](/playground) to try out the Groq API in your browser
- Join our GroqCloud developer community on [Discord](https://discord.gg/groq)
- [Chat with our Docs](https://docs-chat.groqcloud.com/) at lightning speed using the Groq API!
- Add a how-to on your project to the [Groq API Cookbook](https://github.com/groq/groq-api-cookbook)## Documentation

## Groq client libraries

Groq provides both a Python and JavaScript/Typescript client library.

PythonJavaScript

### [Groq Python Library](\#groq-python-library)

The Groq Python library provides convenient access to the Groq REST API from any Python 3.7+ application. The library includes type definitions for all request params and response fields, and offers both synchronous and asynchronous clients.

## Installation

```shell
pip install groq
```

## Usage

Use the library and your secret key to run:

```py
1import os
2
3from groq import Groq
4
5client = Groq(
6    # This is the default and can be omitted
7    api_key=os.environ.get("GROQ_API_KEY"),
8)
9
10chat_completion = client.chat.completions.create(
11    messages=[\
12        {\
13            "role": "system",\
14            "content": "you are a helpful assistant."\
15        },\
16        {\
17            "role": "user",\
18            "content": "Explain the importance of fast language models",\
19        }\
20    ],
21    model="llama3-8b-8192",
22)
23
24print(chat_completion.choices[0].message.content)
```

While you can provide an `api_key` keyword argument, we recommend using [python-dotenv](https://github.com/theskumar/python-dotenv) to add `GROQ_API_KEY="My API Key"` to your `.env` file so that your API Key is not stored in source control.

The following response is generated:

```json
{
  "id": "34a9110d-c39d-423b-9ab9-9c748747b204",
  "object": "chat.completion",
  "created": 1708045122,
  "model": "mixtral-8x7b-32768",
  "system_fingerprint": "fp_dbffcd8265",
  "choices": [\
    {\
      "index": 0,\
      "message": {\
        "role": "assistant",\
        "content": "Low latency Large Language Models (LLMs) are important in the field of artificial intelligence and natural language processing (NLP) for several reasons:\n\n1. Real-time applications: Low latency LLMs are essential for real-time applications such as chatbots, voice assistants, and real-time translation services. These applications require immediate responses, and high latency can lead to a poor user experience.\n\n2. Improved user experience: Low latency LLMs provide a more seamless and responsive user experience. Users are more likely to continue using a service that provides quick and accurate responses, leading to higher user engagement and satisfaction.\n\n3. Competitive advantage: In today's fast-paced digital world, businesses that can provide quick and accurate responses to customer inquiries have a competitive advantage. Low latency LLMs can help businesses respond to customer inquiries more quickly, potentially leading to increased sales and customer loyalty.\n\n4. Better decision-making: Low latency LLMs can provide real-time insights and recommendations, enabling businesses to make better decisions more quickly. This can be particularly important in industries such as finance, healthcare, and logistics, where quick decision-making can have a significant impact on business outcomes.\n\n5. Scalability: Low latency LLMs can handle a higher volume of requests, making them more scalable than high-latency models. This is particularly important for businesses that experience spikes in traffic or have a large user base.\n\nIn summary, low latency LLMs are essential for real-time applications, providing a better user experience, enabling quick decision-making, and improving scalability. As the demand for real-time NLP applications continues to grow, the importance of low latency LLMs will only become more critical."\
      },\
      "finish_reason": "stop",\
      "logprobs": null\
    }\
  ],
  "usage": {
    "prompt_tokens": 24,
    "completion_tokens": 377,
    "total_tokens": 401,
    "prompt_time": 0.009,
    "completion_time": 0.774,
    "total_time": 0.783
  },
  "x_groq": {
    "id": "req_01htzpsmfmew5b4rbmbjy2kv74"
  }
}
```

## Groq community libraries

Groq encourages our developer community to build on our SDK. If you would like your library added, please fill out this [form](https://docs.google.com/forms/d/e/1FAIpQLSfkg3rPUnmZcTwRAS-MsmVHULMtD2I8LwsKPEasuqSsLlF0yA/viewform?usp=sf_link).

Please note that Groq does not verify the security of these projects. **Use at your own risk.**

### [C\#](\#c)

- [jgravelle.GroqAPILibrary](https://github.com/jgravelle/GroqApiLibrary) by [jgravelle](https://github.com/jgravelle)

### [Dart/Flutter](\#dartflutter)

- [TAGonSoft.groq-dart](https://github.com/TAGonSoft/groq-dart) by [TAGonSoft](https://github.com/TAGonSoft)

### [PHP](\#php)

- [lucianotonet.groq-php](https://github.com/lucianotonet/groq-php) by [lucianotonet](https://github.com/lucianotonet)

### [Ruby](\#ruby)

- [drnic.groq-ruby](https://github.com/drnic/groq-ruby) by [drnic](https://github.com/drnic)## Documentation

## Supported Models

GroqCloud currently supports the following models:

| Model ID | Developer | Context Window (tokens) | Max Tokens | Max File Size | Model Card Link |
| --- | --- | --- | --- | --- | --- |
| `distil-whisper-large-v3-en` | HuggingFace | - | - | 25 MB | [Card](https://huggingface.co/distil-whisper/distil-large-v3) |
| `gemma2-9b-it` | Google | 8,192 | - | - | [Card](https://huggingface.co/google/gemma-2-9b-it) |
| `gemma-7b-it` | Google | 8,192 | - | - | [Card](https://huggingface.co/google/gemma-1.1-7b-it) |
| `llama3-groq-70b-8192-tool-use-preview` | Groq | 8,192 | - | - | [Card](https://huggingface.co/Groq/Llama-3-Groq-70B-Tool-Use) |
| `llama3-groq-8b-8192-tool-use-preview` | Groq | 8,192 | - | - | [Card](https://huggingface.co/Groq/Llama-3-Groq-8B-Tool-Use) |
| `llama-3.1-70b-versatile` | Meta | 128k | 32,768 | - | [Card](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md) |
| `llama-3.1-70b-specdec` | Meta | 128k | 8,192 |  | [Card](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md) |
| `llama-3.1-8b-instant` | Meta | 128k | 8,192 | - | [Card](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md) |
| `llama-3.2-1b-preview` | Meta | 128k | 8,192 | - | [Card](https://huggingface.co/meta-llama/Llama-3.2-1B) |
| `llama-3.2-3b-preview` | Meta | 128k | 8,192 | - | [Card](https://huggingface.co/meta-llama/Llama-3.2-3B) |
| `llama-3.2-11b-vision-preview` | Meta | 128k | 8,192 | - | [Card](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision) |
| `llama-3.2-90b-vision-preview` | Meta | 128k | 8,192 | - | [Card](https://huggingface.co/meta-llama/Llama-3.2-90B-Vision) |
| `llama-guard-3-8b` | Meta | 8,192 | - | - | [Card](https://huggingface.co/meta-llama/Llama-Guard-3-8B) |
| `llama3-70b-8192` | Meta | 8,192 | - | - | [Card](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct) |
| `llama3-8b-8192` | Meta | 8,192 | - | - | [Card](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) |
| `mixtral-8x7b-32768` | Mistral | 32,768 | - | - | [Card](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) |
| `whisper-large-v3` | OpenAI | - | - | 25 MB | [Card](https://huggingface.co/openai/whisper-large-v3) |
| `whisper-large-v3-turbo` | OpenAI | - | - | 25 MB | [Card](https://huggingface.co/openai/whisper-large-v3-turbo) |
| [Deprecated Models](/docs/deprecations) |  |  |  |  |  |

**Note:** Models with a context window of 128K tokens are currently limited to 8,192 max tokens in preview. Models without a context window or max tokens are denoted with a dash ("-").

Hosted models are directly accessible through the GroqCloud Models API endpoint using the model IDs mentioned above. You can use the `https://api.groq.com/openai/v1/models` endpoint to return a JSON list of all active models:

curlJavaScriptPythonJSON

```py
1import requests
2import os
3
4api_key = os.environ.get("GROQ_API_KEY")
5url = "https://api.groq.com/openai/v1/models"
6
7headers = {
8    "Authorization": f"Bearer {api_key}",
9    "Content-Type": "application/json"
10}
11
12response = requests.get(url, headers=headers)
13
14print(response.json())
```## Documentation

## Rate Limits

Rate limits act as control measures to regulate how frequently a user or application can make requests within a given timeframe.

### [Current rate limits for chat completions:](\#current-rate-limits-for-chat-completions)

You can view the current rate limits for chat completions in your organization [settings](/settings/limits)

The team is working on introducing paid tiers with stable and increased rate limits in the near future.

### [Status code & rate limit headers](\#status-code--rate-limit-headers)

We set the following `x-ratelimit` headers to inform you on current rate limits applicable to the API key and associated organization.

The following headers are set (values are illustrative):

| Header | Value | Notes |
| --- | --- | --- |
| `retry-after` | `2` | In seconds |
| `x-ratelimit-limit-requests` | `14400` | Always refers to Requests Per Day (RPD) |
| `x-ratelimit-limit-tokens` | `18000` | Always refers to Tokens Per Minute (TPM) |
| `x-ratelimit-remaining-requests` | `14370` | Always refers to Requests Per Day (RPD) |
| `x-ratelimit-remaining-tokens` | `17997` | Always refers to Tokens Per Minute (TPM) |
| `x-ratelimit-reset-requests` | `2m59.56s` | Always refers to Requests Per Day (RPD) |
| `x-ratelimit-reset-tokens` | `7.66s` | Always refers to Tokens Per Minute (TPM) |

When the rate limit is reached we return a `429` Too Many Requests HTTP status code.

Note, `retry-after` is only set if you hit the rate limit and status code 429 is returned. The other headers are always included.## Documentation

## Speech

Groq API is the fastest speech-to-text solution available, offering OpenAI-compatible endpoints that
enable real-time transcriptions and translations. With Groq API, you can integrate high-quality audio
processing into your applications at speeds that rival human interaction.

### [API Endpoints](\#api-endpoints)

We support two endpoints:

| Endpoint | Usage | API Endpoint |
| --- | --- | --- |
| Transcriptions | Convert audio to text | `https://api.groq.com/openai/v1/audio/transcriptions` |
| Translations | Translate audio to English text | `https://api.groq.com/openai/v1/audio/translations` |

### [Supported Models](\#supported-models)

| Model ID | Model | Supported Language(s) | Description |
| --- | --- | --- | --- |
| `whisper-large-v3-turbo` | Whisper Large V3 Turbo | Multilingual | A fine-tuned version of a pruned Whisper Large V3 designed for fast, multilingual transcription tasks. |
| `distil-whisper-large-v3-en` | Distil-Whisper English | English-only | A distilled, or compressed, version of OpenAI's Whisper model, designed to provide faster, lower cost English speech recognition while maintaining comparable accuracy. |
| `whisper-large-v3` | Whisper large-v3 | Multilingual | Provides state-of-the-art performance with high accuracy for multilingual transcription and translation tasks. |

### [Which Whisper Model Should You Use?](\#which-whisper-model-should-you-use)

Having more choices is great, but let's try to avoid decision paralysis by breaking down the tradeoffs between models to find the one most suitable for
your applications:

- If your application is error-sensitive and requires multilingual support, use `whisper-large-v3`.
- If your application is less sensitive to errors and requires English only, use `distil-whisper-large-v3-en`.
- If your application requires multilingual support and you need the best price for performance, use `whisper-large-v3-turbo`.

The following table breaks down the metrics for each model.

| Model | Cost Per Hour | Language Support | Transcription Support | Translation Support | Real-time Speed Factor | Word Error Rate |
| --- | --- | --- | --- | --- | --- | --- |
| `whisper-large-v3` | $0.111 | Multilingual | Yes | Yes | 189 | 10.3% |
| `whisper-large-v3-turbo` | $0.04 | Multilingual | Yes | No | 216 | 12% |
| `distil-whisper-large-v3-en` | $0.02 | English only | Yes | No | 250 | 13% |

### Audio File Limitations

Max File Size

25 MB

Minimum File Length

0.01 seconds

Minimum Billed Length

10 seconds. If you submit a request less than this, you will still be billed for 10 seconds.

Supported File Types

\`mp3\`, \`mp4\`, \`mpeg\`, \`mpga\`, \`m4a\`, \`wav\`, \`webm\`

Single Audio Track

Only the first track will be transcribed for files with multiple audio tracks. (e.g. dubbed video)

Supported Response Formats

\`json\`, \`verbose\_json\`, \`text\`

### [Preprocessing Audio Files](\#preprocessing-audio-files)

Our speech-to-text models will downsample audio to 16,000 Hz mono before transcribing. This preprocessing can be performed client-side to reduce file size and allow longer files to be uploaded to Groq.
The following `ffmpeg` command can be used to reduce file size:

```shell
ffmpeg \
  -i <your file> \
  -ar 16000 \
  -ac 1 \
  -map 0:a: \
  <output file name>
```

### [Transcription Endpoint Usage](\#transcription-endpoint-usage)

The transcription endpoint allows you to transcribe spoken words in audio or video files. You can
provide optional request parameters to customize the transcription output.

#### Optional Request Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `prompt` | `string` | None | Provide context or specify how to spell unfamiliar words (limited to 224 tokens). |
| `response_format` | `string` | json | Define the output response format.<br>Set to `verbose_json` to receive timestamps for audio segments.<br>Set to `text` to return a text response. |
| `temperature` | `float` | None | Specify a value between 0 and 1 to control the translation output. |
| `language` | `string` | None | `whisper-large-v3-turbo` and `whisper-large-v3` only!<br>Specify the language for transcription. Use ISO 639-1 language codes (e.g. "en" for English, "fr" for French, etc.). Specifying a language may improve transcription accuracy and speed. |

#### Example Usage

PythonJavaScriptcurl

The Groq SDK package can be installed using the following command:

```shell
pip install groq
```

The following code snippet demonstrates how to use Groq API to transcribe an audio file in Python:

```py
1import os
2from groq import Groq
3
4# Initialize the Groq client
5client = Groq()
6
7# Specify the path to the audio file
8filename = os.path.dirname(__file__) + "/sample_audio.m4a" # Replace with your audio file!
9
10# Open the audio file
11with open(filename, "rb") as file:
12    # Create a transcription of the audio file
13    transcription = client.audio.transcriptions.create(
14      file=(filename, file.read()), # Required audio file
15      model="whisper-large-v3-turbo", # Required model to use for transcription
16      prompt="Specify context or spelling",  # Optional
17      response_format="json",  # Optional
18      language="en",  # Optional
19      temperature=0.0  # Optional
20    )
21    # Print the transcription text
22    print(transcription.text)
```

### [Translation Endpoint Usage](\#translation-endpoint-usage)

The translation endpoint allows you to translate spoken words in audio or video files to English. You can provide optional request parameters to customize the translation output.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `prompt` | `string` | `None` | Provide context or specify how to spell unfamiliar words (limited to 224 tokens). |
| `response_format` | `string` | `json` | Define the output response format. Set to `verbose_json` to receive timestamps for audio segments. Set to `text` to return a text response. |
| `temperature` | `float` | `None` | Specify a value between 0 and 1 to control the translation output. |

### [Example Usage](\#example-usage)

PythonJavaScriptcurl

The Groq SDK package can be installed using the following command:

```shell
pip install groq
```

The following code snippet demonstrates how to use Groq API to translate an audio file in Python:

```py
1import os
2from groq import Groq
3
4# Initialize the Groq client
5client = Groq()
6
7# Specify the path to the audio file
8filename = os.path.dirname(__file__) + "/sample_audio.m4a" # Replace with your audio file!
9
10# Open the audio file
11with open(filename, "rb") as file:
12    # Create a translation of the audio file
13    translation = client.audio.translations.create(
14      file=(filename, file.read()), # Required audio file
15      model="whisper-large-v3", # Required model to use for translation
16      prompt="Specify context or spelling",  # Optional
17      response_format="json",  # Optional
18      temperature=0.0  # Optional
19    )
20    # Print the translation text
21    print(translation.text)
```

### [Prompting Guidelines](\#prompting-guidelines)

The prompt parameter is an optional input of max 224 tokens that allows you to provide contextual
information to the model, helping it maintain a consistent writing style.

How It Works

When you provide a prompt parameter, the speech-to-text model treats it as a prior transcript and
follows its style, rather than adhering to the actual content of the audio segment. This means that the
model will not:

- Attempt to execute commands contained within the prompt
- Follow instructions present in the prompt

In contrast to chat completion prompts, the prompt parameter is designed solely to provide stylistic
guidance and contextual information to the model, rather than triggering specific actions or responses.

Best Practices

- Provide contextual information about the audio segment, such as the type of conversation, topic, or
speakers involved.
- Use the same language as the language of the audio file.
- Steer the model's output by denoting proper spellings or emulate a specific writing style or tone.
- Keep the prompt concise and focused on stylistic guidance.

### [Use Cases](\#use-cases)

Groq API offers low latency and fast inference for speech recognition, transcription, and translation, enabling
developers to build a wide range of highly accurate, real-time applications, such as:

- Audio Translation: Translate audio files to break language barriers and facilitate global communication.
- Customer Service: Create real-time, AI-powered customer service solutions that use speech recognition to route
calls, transcribe conversations, and respond to customer inquiries.
- Automated Speech-to-Text Systems: Implement automated speech-to-text systems in industries like
healthcare, finance, and education, where accurate transcription is critical for compliance,
record-keeping, and decision-making.
- Voice-Controlled Interfaces: Develop voice-controlled interfaces for smart homes, cars, and other
devices, where fast and accurate speech recognition is essential for user experience and safety.

We can't wait to see what you build! 🚀## Documentation

## LiteLLM 🚅

[LiteLLM](https://docs.litellm.ai/) provides a unified interface to call hundreds of LLMs using the same Input/Output format, allowing for translation of inputs to providers' endpoints, consistent output, retry/fallback logic across multiple deployments for routing, and tracking for spending.

For more information, read the LiteLLM Groq integration documentation [here](https://docs.litellm.ai/docs/providers/groq).## Documentation

## Apps Showcase

Discover the incredible speed of Groq with fully-developed apps from our team and community!

**If you're interested adding your project to our showcase, please fill out and submit [this form](https://forms.gle/bQxD88MAxCMeksqt7) for our team to review.**

* * *

[**Groq Draw and Guess**](#groq-draw-and-guess)

Author: Jose Menendez

Fun use of LLaVA 1.5 7B powered by Groq to play a pictionary style game where you draw and the vision model guesses.

[Github](https://github.com/jose-mdz/draw-and-guess) [Live Demo](https://draw.geeksplainer.wtf/)

[![Visual Demo](/showcase-applications/drawandguess.png)](https://github.com/jose-mdz/draw-and-guess)

* * *

* * *

[**Magic Spell**](#magic-spell)

Author: Ai-ng and Nick Oates

AI-powered text editor built with Next.js, Vercel AI SDK and Groq. Deploy your own AI-powered text editor.

[Github](https://github.com/ai-ng/magic-spell) [Live Demo](https://magic-spell.vercel.app/)

[![Visual Demo](/showcase-applications/magic-spell.png)](https://github.com/ai-ng/magic-spell)

* * *

[**Open Devin**](#open-devin)

Author: Mervin Praison

This project aspires to replicate, enhance, and innovate upon Devin through the power of the open-source community. -- powered by NodeJS, Docker and Groq.

[Github](https://github.com/OpenDevin/OpenDevin) [YouTube Tutorial](https://www.youtube.com/watch?v=3-q5GzRNEe0)

[![Visual Demo](/showcase-applications/open-devin.png)](https://github.com/OpenDevin/OpenDevin)

* * *

[**Streamlit AI Chatbot**](#streamlit-ai-chatbot)

Author: Tony Kipkemboi

Build a Streamlit AI chatbot using Groq.

[Github](https://github.com/tonykipkemboi/groq_streamlit_demo) [YouTube Tutorial](https://www.youtube.com/watch?v=WQvinJGYk90)

[![Visual Demo](/showcase-applications/streamlit.png)](https://github.com/tonykipkemboi/groq_streamlit_demo)

* * *

[**Hey Gemma**](#hey-gemma)

Author: gabrielchua

A voice interface on top of Gemma 7B, powered by Groq.

[Gradio Repo](https://huggingface.co/spaces/cyzgab/hey-gemma/tree/main)

[![Visual Demo](/showcase-applications/hey-gemma.png)](https://huggingface.co/spaces/cyzgab/hey-gemma/tree/main)

* * *

[**RAG with LlamaParse**](#rag-with-llamaparse)

Author: Sudarshan Koirala

Build an effective RAG pipeline using multiple file formats -- powered by LlamaParse, Qdrant and Groq.

[GitHub](https://github.com/sudarshan-koirala/llamaparser-example) [YouTube Tutorial](https://www.youtube.com/watch?v=w7Ap6gZFXl0)

[![Visual Demo](/showcase-applications/rag-llamaparse.png)](https://github.com/sudarshan-koirala/llamaparser-example)

* * *

[**Answer Engine**](#answer-engine)

Author: Developer's Digest

Follow the Developer's Digest team as they build a Perplexity-like Answer Engine with Groq, Mixtral, Langchain and Brave.

[GitHub](https://github.com/developersdigest/llm-answer-engine) [YouTube Tutorial](https://www.youtube.com/watch?v=kFC-OWw7G8k)

[![Visual Demo](/showcase-applications/llm-answer-engine.png)](https://github.com/developersdigest/llm-answer-engine)

* * *

[**Gradio + Groq = 😍**](#gradio-+-groq-=-😍)

Author: gabrielchua

A simple Gradio app showcasing fast inference and LLM-powered autocomplete powered by Groq.

[Gradio Repo](https://huggingface.co/spaces/cyzgab/catch-me-if-you-can/blob/main/app.py)

[![Visual Demo](/showcase-applications/gradio-demo.png)](https://huggingface.co/spaces/cyzgab/catch-me-if-you-can/blob/main/app.py)

* * *

[**Quick Voice Bot with Deepgram**](#quick-voice-bot-with-deepgram)

Author: Greg Kamradt

AI voice bot demo that uses Text-To-Speech and Speech-To-Text powered by Groq.

[GitHub](https://github.com/gkamradt/QuickAgent) [YouTube Tutorial](https://www.youtube.com/watch?v=J2sbC8X5Pp8)

[![Visual Demo](/showcase-applications/deepgram.png)](https://github.com/gkamradt/QuickAgent)

* * *

[**Crazy Fast RAG**](#crazy-fast-rag)

Author: Sudarshan Koirala

RAG Chatbot with simple UI built on open-embedding model nomic-embed-text via Ollama and powered by Groq.

[GitHub](https://github.com/sudarshan-koirala/rag-chat-with-pdf) [YouTube Tutorial](https://www.youtube.com/watch?v=TMaQt8rN5bE)

[![Visual Demo](/showcase-applications/crazy-fast-rag.png)](https://github.com/sudarshan-koirala/rag-chat-with-pdf)

* * *

[**Chat with Groq Docs**](#chat-with-groq-docs)

Author: Groq

Chat with Groq Docs...with Groq! Powered by Langchain.

[Live Demo](https://docs-chat.groqcloud.com/)

[![Visual Demo](/showcase-applications/groq-docs-chat.png)](https://docs-chat.groqcloud.com/)

* * *

[**InstantRefactor**](#instantrefactor)

Author: @mattshumer

Use Groq to instantly refactor and document python code.

[Live Demo](https://instant-refactor.streamlit.app)

[![Visual Demo](/showcase-applications/instantrefactor.png)](https://instant-refactor.streamlit.app)

* * *

[**Agents go brrrr with Groq**](#agents-go-brrrr-with-groq)

Author: @gabchuayz

A simple react search agent built with LangChain, powered by Groq, Mixtral and Tavily.

[Github](https://github.com/gabrielchua/groq-st-demo/tree/main) [Live Demo](https://groq-react.streamlit.app/)

[![Visual Demo](/showcase-applications/agents-go-brrrr.png)](https://github.com/gabrielchua/groq-st-demo/tree/main)

* * *

[**ZeroBot.ai**](#zerobot.ai)

Author: ZeroBot.ai

The Internet's #1 voice-enabled chatbot, at Groq speed.

[Live Demo](https://www.zerobot.ai/)

[![Visual Demo](/showcase-applications/zerobotAI.png)](https://www.zerobot.ai/)

* * *

[**ConsiLLiuM**](#consillium)

Author: @FelipeSchieber

A generative hierarchical Wikipedia-like app powered by Groq for blazingly fast article generation.

[Live Demo](https://consillium.vercel.app/)

[![Visual Demo](/showcase-applications/consillium.png)](https://consillium.vercel.app/)

* * *

[**Real time voice assistant with Groq**](#real-time-voice-assistant-with-groq)

Author: Serkan Dayicik

Voice-driven interactions with groq, a real-time voice assistant that seamlessly blends Next.js for web functionality, Groq for LLM, Deepgram for live transcription TTS with Neets for TTS.

[Github](https://github.com/serkandyck/realtime-voice-assistant-groq)

[![Visual Demo](/showcase-applications/realtimevoice.png)](https://github.com/serkandyck/realtime-voice-assistant-groq)

* * *

[**NatterGPT**](#nattergpt)

Author: @HelloGnbly

NatterGPT calls your leads/customers, evaluates their interest level and gets you a report.

[Live Demo](https://nattergpt.com/)

[![Visual Demo](/showcase-applications/nattergpt.png)](https://nattergpt.com/)

* * *

[**Fast Conversational Agent**](#fast-conversational-agent)

Author: @StonkyOli

A demo showcasing a fast conversational agent, powered by Azure, PlayHT and Groq inference.

[Video Demo](https://twitter.com/StonkyOli/status/1762551140829515964)

[![Visual Demo](/showcase-applications/fast-convo-agent.png)](https://twitter.com/StonkyOli/status/1762551140829515964)## Documentation

## Chat Completion Models

The Groq Chat Completions API processes a series of messages and generates output responses. These models can perform multi-turn discussions or tasks that require only one interaction.

For details about the parameters, [visit the reference page.](https://console.groq.com/docs/api-reference#chat-create)

### [JSON mode _(beta)_](\#json-mode-object-object)

JSON mode is a beta feature that guarantees all chat completions are valid JSON.

Usage:

- Set `"response_format": {"type": "json_object"}` in your chat completion request
- Add a description of the desired JSON structure within the system prompt (see below for example system prompts)

Recommendations for best beta results:

- Mixtral performs best at generating JSON, followed by Gemma, then Llama
- Use pretty-printed JSON instead of compact JSON
- Keep prompts concise

Beta Limitations:

- Does not support streaming
- Does not support stop sequences

Error Code:

- Groq will return a 400 error with an error code of `json_validate_failed` if JSON generation fails.

Example system prompts:

```json
You are a legal advisor who summarizes documents in JSON
```

```json
You are a data analyst API capable of sentiment analysis that responds in JSON.  The JSON schema should include
{
  "sentiment_analysis": {
    "sentiment": "string (positive, negative, neutral)",
    "confidence_score": "number (0-1)"
    # Include additional fields as required
  }
}
```

### [Generating Chat Completions with groq SDK](\#generating-chat-completions-with-groq-sdk)

#### Code Overview

PythonJavaScript

```shell
pip install groq
```

### [Performing a basic Chat Completion](\#performing-a-basic-chat-completion)

```py
1from groq import Groq
2
3client = Groq()
4
5chat_completion = client.chat.completions.create(
6    #
7    # Required parameters
8    #
9    messages=[\
10        # Set an optional system message. This sets the behavior of the\
11        # assistant and can be used to provide specific instructions for\
12        # how it should behave throughout the conversation.\
13        {\
14            "role": "system",\
15            "content": "you are a helpful assistant."\
16        },\
17        # Set a user message for the assistant to respond to.\
18        {\
19            "role": "user",\
20            "content": "Explain the importance of fast language models",\
21        }\
22    ],
23
24    # The language model which will generate the completion.
25    model="llama3-8b-8192",
26
27    #
28    # Optional parameters
29    #
30
31    # Controls randomness: lowering results in less random completions.
32    # As the temperature approaches zero, the model will become deterministic
33    # and repetitive.
34    temperature=0.5,
35
36    # The maximum number of tokens to generate. Requests can use up to
37    # 32,768 tokens shared between prompt and completion.
38    max_tokens=1024,
39
40    # Controls diversity via nucleus sampling: 0.5 means half of all
41    # likelihood-weighted options are considered.
42    top_p=1,
43
44    # A stop sequence is a predefined or user-specified text string that
45    # signals an AI to stop generating content, ensuring its responses
46    # remain focused and concise. Examples include punctuation marks and
47    # markers like "[end]".
48    stop=None,
49
50    # If set, partial message deltas will be sent.
51    stream=False,
52)
53
54# Print the completion returned by the LLM.
55print(chat_completion.choices[0].message.content)
```

### [Streaming a Chat Completion](\#streaming-a-chat-completion)

To stream a completion, simply set the parameter `stream=True`. Then the completion
function will return an iterator of completion deltas rather than a single, full completion.

```py
1from groq import Groq
2
3client = Groq()
4
5stream = client.chat.completions.create(
6    #
7    # Required parameters
8    #
9    messages=[\
10        # Set an optional system message. This sets the behavior of the\
11        # assistant and can be used to provide specific instructions for\
12        # how it should behave throughout the conversation.\
13        {\
14            "role": "system",\
15            "content": "you are a helpful assistant."\
16        },\
17        # Set a user message for the assistant to respond to.\
18        {\
19            "role": "user",\
20            "content": "Explain the importance of fast language models",\
21        }\
22    ],
23
24    # The language model which will generate the completion.
25    model="llama3-8b-8192",
26
27    #
28    # Optional parameters
29    #
30
31    # Controls randomness: lowering results in less random completions.
32    # As the temperature approaches zero, the model will become deterministic
33    # and repetitive.
34    temperature=0.5,
35
36    # The maximum number of tokens to generate. Requests can use up to
37    # 2048 tokens shared between prompt and completion.
38    max_tokens=1024,
39
40    # Controls diversity via nucleus sampling: 0.5 means half of all
41    # likelihood-weighted options are considered.
42    top_p=1,
43
44    # A stop sequence is a predefined or user-specified text string that
45    # signals an AI to stop generating content, ensuring its responses
46    # remain focused and concise. Examples include punctuation marks and
47    # markers like "[end]".
48    stop=None,
49
50    # If set, partial message deltas will be sent.
51    stream=True,
52)
53
54# Print the incremental deltas returned by the LLM.
55for chunk in stream:
56    print(chunk.choices[0].delta.content, end="")
```

### [Performing a Chat Completion with a stop sequence](\#performing-a-chat-completion-with-a-stop-sequence)

```py
1from groq import Groq
2
3client = Groq()
4
5chat_completion = client.chat.completions.create(
6    #
7    # Required parameters
8    #
9    messages=[\
10        # Set an optional system message. This sets the behavior of the\
11        # assistant and can be used to provide specific instructions for\
12        # how it should behave throughout the conversation.\
13        {\
14            "role": "system",\
15            "content": "you are a helpful assistant."\
16        },\
17        # Set a user message for the assistant to respond to.\
18        {\
19            "role": "user",\
20            "content": "Count to 10.  Your response must begin with \"1, \".  example: 1, 2, 3, ...",\
21        }\
22    ],
23
24    # The language model which will generate the completion.
25    model="llama3-8b-8192",
26
27    #
28    # Optional parameters
29    #
30
31    # Controls randomness: lowering results in less random completions.
32    # As the temperature approaches zero, the model will become deterministic
33    # and repetitive.
34    temperature=0.5,
35
36    # The maximum number of tokens to generate. Requests can use up to
37    # 2048 tokens shared between prompt and completion.
38    max_tokens=1024,
39
40    # Controls diversity via nucleus sampling: 0.5 means half of all
41    # likelihood-weighted options are considered.
42    top_p=1,
43
44    # A stop sequence is a predefined or user-specified text string that
45    # signals an AI to stop generating content, ensuring its responses
46    # remain focused and concise. Examples include punctuation marks and
47    # markers like "[end]".
48    # For this example, we will use ", 6" so that the llm stops counting at 5.
49    # If multiple stop values are needed, an array of string may be passed,
50    # stop=[", 6", ", six", ", Six"]
51    stop=", 6",
52
53    # If set, partial message deltas will be sent.
54    stream=False,
55)
56
57# Print the completion returned by the LLM.
58print(chat_completion.choices[0].message.content)
```

### [Performing an Async Chat Completion](\#performing-an-async-chat-completion)

Simply use the Async client to enable asyncio

```py
1import asyncio
2
3from groq import AsyncGroq
4
5
6async def main():
7    client = AsyncGroq()
8
9    chat_completion = await client.chat.completions.create(
10        #
11        # Required parameters
12        #
13        messages=[\
14            # Set an optional system message. This sets the behavior of the\
15            # assistant and can be used to provide specific instructions for\
16            # how it should behave throughout the conversation.\
17            {\
18                "role": "system",\
19                "content": "you are a helpful assistant."\
20            },\
21            # Set a user message for the assistant to respond to.\
22            {\
23                "role": "user",\
24                "content": "Explain the importance of fast language models",\
25            }\
26        ],
27
28        # The language model which will generate the completion.
29        model="llama3-8b-8192",
30
31        #
32        # Optional parameters
33        #
34
35        # Controls randomness: lowering results in less random completions.
36        # As the temperature approaches zero, the model will become
37        # deterministic and repetitive.
38        temperature=0.5,
39
40        # The maximum number of tokens to generate. Requests can use up to
41        # 2048 tokens shared between prompt and completion.
42        max_tokens=1024,
43
44        # Controls diversity via nucleus sampling: 0.5 means half of all
45        # likelihood-weighted options are considered.
46        top_p=1,
47
48        # A stop sequence is a predefined or user-specified text string that
49        # signals an AI to stop generating content, ensuring its responses
50        # remain focused and concise. Examples include punctuation marks and
51        # markers like "[end]".
52        stop=None,
53
54        # If set, partial message deltas will be sent.
55        stream=False,
56    )
57
58    # Print the completion returned by the LLM.
59    print(chat_completion.choices[0].message.content)
60
61asyncio.run(main())
```

### [Streaming an Async Chat Completion](\#streaming-an-async-chat-completion)

```py
1import asyncio
2
3from groq import AsyncGroq
4
5
6async def main():
7    client = AsyncGroq()
8
9    stream = await client.chat.completions.create(
10        #
11        # Required parameters
12        #
13        messages=[\
14            # Set an optional system message. This sets the behavior of the\
15            # assistant and can be used to provide specific instructions for\
16            # how it should behave throughout the conversation.\
17            {\
18                "role": "system",\
19                "content": "you are a helpful assistant."\
20            },\
21            # Set a user message for the assistant to respond to.\
22            {\
23                "role": "user",\
24                "content": "Explain the importance of fast language models",\
25            }\
26        ],
27
28        # The language model which will generate the completion.
29        model="llama3-8b-8192",
30
31        #
32        # Optional parameters
33        #
34
35        # Controls randomness: lowering results in less random completions.
36        # As the temperature approaches zero, the model will become
37        # deterministic and repetitive.
38        temperature=0.5,
39
40        # The maximum number of tokens to generate. Requests can use up to
41        # 2048 tokens shared between prompt and completion.
42        max_tokens=1024,
43
44        # Controls diversity via nucleus sampling: 0.5 means half of all
45        # likelihood-weighted options are considered.
46        top_p=1,
47
48        # A stop sequence is a predefined or user-specified text string that
49        # signals an AI to stop generating content, ensuring its responses
50        # remain focused and concise. Examples include punctuation marks and
51        # markers like "[end]".
52        stop=None,
53
54        # If set, partial message deltas will be sent.
55        stream=True,
56    )
57
58    # Print the incremental deltas returned by the LLM.
59    async for chunk in stream:
60        print(chunk.choices[0].delta.content, end="")
61
62asyncio.run(main())
```

### [JSON Mode](\#json-mode)

```py
1from typing import List, Optional
2import json
3
4from pydantic import BaseModel
5from groq import Groq
6
7groq = Groq()
8
9
10# Data model for LLM to generate
11class Ingredient(BaseModel):
12    name: str
13    quantity: str
14    quantity_unit: Optional[str]
15
16
17class Recipe(BaseModel):
18    recipe_name: str
19    ingredients: List[Ingredient]
20    directions: List[str]
21
22
23def get_recipe(recipe_name: str) -> Recipe:
24    chat_completion = groq.chat.completions.create(
25        messages=[\
26            {\
27                "role": "system",\
28                "content": "You are a recipe database that outputs recipes in JSON.\n"\
29                # Pass the json schema to the model. Pretty printing improves results.\
30                f" The JSON object must use the schema: {json.dumps(Recipe.model_json_schema(), indent=2)}",\
31            },\
32            {\
33                "role": "user",\
34                "content": f"Fetch a recipe for {recipe_name}",\
35            },\
36        ],
37        model="llama3-8b-8192",
38        temperature=0,
39        # Streaming is not supported in JSON mode
40        stream=False,
41        # Enable JSON mode by setting the response format
42        response_format={"type": "json_object"},
43    )
44    return Recipe.model_validate_json(chat_completion.choices[0].message.content)
45
46
47def print_recipe(recipe: Recipe):
48    print("Recipe:", recipe.recipe_name)
49
50    print("\nIngredients:")
51    for ingredient in recipe.ingredients:
52        print(
53            f"- {ingredient.name}: {ingredient.quantity} {ingredient.quantity_unit or ''}"
54        )
55    print("\nDirections:")
56    for step, direction in enumerate(recipe.directions, start=1):
57        print(f"{step}. {direction}")
58
59
60recipe = get_recipe("apple pie")
61print_recipe(recipe)
```## Documentation

## Vision

Groq API offers fast inference and low latency for multimodal models with vision capabilities for understanding and interpreting visual data from images. By analyzing the content of an image, multimodal models can generate
human-readable text for providing insights about given visual data.

### [Supported Model](\#supported-model)

Groq API supports powerful multimodal models that can be easily integrated into your applications to provide fast and accurate image processing for tasks such as visual question answering, caption generation,
and Optical Character Recognition (OCR):

### Llama 3.2 90B Vision (Preview)

Model ID

\`llama-3.2-90b-vision-preview\`

Description

A powerful multimodal model capable of processing both text and image inputs that supports multilingual, multi-turn conversations, tool use, and JSON mode.

Context Window

8,192 tokens

Preview Model

Currently in preview and should be used for experimentation.

Image Size Limit

Maximum allowed size for a request containing an image URL as input is 20MB. Requests larger than this limit will return a 400 error.

Request Size Limit (Base64 Encoded Images)

Maximum allowed size for a request containing a base64 encoded image is 4MB. Requests larger than this limit will return a 413 error.

Single Image per Request

Only one image can be processed per request in the preview release. Requests with multiple images will return a 400 error.

System Prompt

Does not support system prompts and images in the same request.

### Llama 3.2 11B Vision (Preview)

Model ID

\`llama-3.2-11b-vision-preview\`

Description

A powerful multimodal model capable of processing both text and image inputs that supports multilingual, multi-turn conversations, tool use, and JSON mode.

Context Window

8,192 tokens

Preview Model

Currently in preview and should be used for experimentation.

Image Size Limit

Maximum allowed size for a request containing an image URL as input is 20MB. Requests larger than this limit will return a 400 error.

Request Size Limit (Base64 Encoded Images)

Maximum allowed size for a request containing a base64 encoded image is 4MB. Requests larger than this limit will return a 413 error.

Single Image per Request

Only one image can be processed per request in the preview release. Requests with multiple images will return a 400 error.

System Prompt

Does not support system prompts and images in the same request.

### [How to Use Vision](\#how-to-use-vision)

Use Groq API vision features via:

- **[GroqCloud Console Playground](https://console.groq.com/playground)**: Select `llama-3.2-90b-vision-preview` or `llama-3.2-11b-vision-preview` as the model and
upload your image.
- **Groq API Request:** Call the `chat.completions` API endpoint (i.e. `https://api.groq.com/openai/v1/chat/completions`) and set `model_id` to `llama-3.2-90b-vision-preview` or `llama-3.2-11b-vision-preview`.
See code examples below.

#### How to Pass Images from URLs as Input

The following are code examples for passing your image to the model via a URL:

curlJavaScriptPythonJSON

```py
1from groq import Groq
2
3client = Groq()
4completion = client.chat.completions.create(
5    model="llama-3.2-11b-vision-preview",
6    messages=[\
7        {\
8            "role": "user",\
9            "content": [\
10                {\
11                    "type": "text",\
12                    "text": "What's in this image?"\
13                },\
14                {\
15                    "type": "image_url",\
16                    "image_url": {\
17                        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f2/LPU-v1-die.jpg"\
18                    }\
19                }\
20            ]\
21        }\
22    ],
23    temperature=1,
24    max_tokens=1024,
25    top_p=1,
26    stream=False,
27    stop=None,
28)
29
30print(completion.choices[0].message)
```

#### How to Pass Locally Saved Images as Input

To pass locally saved images, we'll need to first encode our image to a base64 format string before passing it as the `image_url` in our API request as follows:

```py
1from groq import Groq
2import base64
3
4
5# Function to encode the image
6def encode_image(image_path):
7  with open(image_path, "rb") as image_file:
8    return base64.b64encode(image_file.read()).decode('utf-8')
9
10# Path to your image
11image_path = "sf.jpg"
12
13# Getting the base64 string
14base64_image = encode_image(image_path)
15
16client = Groq()
17
18chat_completion = client.chat.completions.create(
19    messages=[\
20        {\
21            "role": "user",\
22            "content": [\
23                {"type": "text", "text": "What's in this image?"},\
24                {\
25                    "type": "image_url",\
26                    "image_url": {\
27                        "url": f"data:image/jpeg;base64,{base64_image}",\
28                    },\
29                },\
30            ],\
31        }\
32    ],
33    model="llama-3.2-11b-vision-preview",
34)
35
36print(chat_completion.choices[0].message.content)
```

#### Tool Use with Images

The `llama-3.2-90b-vision-preview` and `llama-3.2-11b-vision-preview` models support tool use! The following cURL example defines a `get_current_weather` tool that the model can leverage to answer a user query that contains a question about the
weather along with an image of a location that the model can infer location (i.e. New York City) from:

```shell
curl https://api.groq.com/openai/v1/chat/completions -s \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $GROQ_API_KEY" \
-d '{
"model": "llama-3.2-11b-vision-preview",
"messages": [\
{\
    "role": "user",\
    "content": [{"type": "text", "text": "Whats the weather like in this state?"}, {"type": "image_url", "image_url": { "url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"}}]\
}\
],
"tools": [\
{\
    "type": "function",\
    "function": {\
    "name": "get_current_weather",\
    "description": "Get the current weather in a given location",\
    "parameters": {\
        "type": "object",\
        "properties": {\
        "location": {\
            "type": "string",\
            "description": "The city and state, e.g. San Francisco, CA"\
        },\
        "unit": {\
            "type": "string",\
            "enum": ["celsius", "fahrenheit"]\
        }\
        },\
        "required": ["location"]\
    }\
    }\
}\
],
"tool_choice": "auto"
}' | jq '.choices[0].message.tool_calls'
```

The following is the output from our example above that shows how our model inferred the state as New York from the given image and called our example function:

```python
[\
  {\
    "id": "call_q0wg",\
    "function": {\
      "arguments": "{\"location\": \"New York, NY\",\"unit\": \"fahrenheit\"}",\
      "name": "get_current_weather"\
    },\
    "type": "function"\
  }\
]
```

#### JSON Mode with Images

The `llama-3.2-90b-vision-preview` and `llama-3.2-11b-vision-preview` models support JSON mode! The following Python example queries the model with an image and text (i.e. "Please pull out relevant information as a JSON object.") with `response_format`
set for JSON mode:

```py
1from groq import Groq
2
3client = Groq()
4completion = client.chat.completions.create(
5    model="llama-3.2-90b-vision-preview",
6    messages=[\
7        {\
8            "role": "user",\
9            "content": [\
10                {\
11                    "type": "text",\
12                    "text": "List what you observe in this photo in JSON format."\
13                },\
14                {\
15                    "type": "image_url",\
16                    "image_url": {\
17                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/da/SF_From_Marin_Highlands3.jpg"\
18                    }\
19                }\
20            ]\
21        }\
22    ],
23    temperature=1,
24    max_tokens=1024,
25    top_p=1,
26    stream=False,
27    response_format={"type": "json_object"},
28    stop=None,
29)
30
31print(completion.choices[0].message)
```

#### Multi-turn Conversations with Images

The `llama-3.2-90b-vision-preview` and `llama-3.2-11b-vision-preview` models support multi-turn conversations! The following Python example shows a multi-turn user conversation about an image:

```py
1from groq import Groq
2
3client = Groq()
4completion = client.chat.completions.create(
5    model="llama-3.2-11b-vision-preview",
6    messages=[\
7        {\
8            "role": "user",\
9            "content": [\
10                {\
11                    "type": "text",\
12                    "text": "What is in this image?"\
13                },\
14                {\
15                    "type": "image_url",\
16                    "image_url": {\
17                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/da/SF_From_Marin_Highlands3.jpg"\
18                    }\
19                }\
20            ]\
21        },\
22        {\
23            "role": "user",\
24            "content": "Tell me more about the area."\
25        }\
26    ],
27    temperature=1,
28    max_tokens=1024,
29    top_p=1,
30    stream=False,
31    stop=None,
32)
33
34print(completion.choices[0].message)
```

### [Venture Deeper into Vision](\#venture-deeper-into-vision)

#### Use Cases to Explore

Vision models can be used in a wide range of applications. Here are some ideas:

- **Accessibility Applications:** Develop an application that generates audio descriptions for images by using a vision model to generate text descriptions for images, which can then
be converted to audio with one of our audio endpoints.
- **E-commerce Product Description Generation:** Create an application that generates product descriptions for e-commerce websites.
- **Multilingual Image Analysis:** Create applications that can describe images in multiple languages.
- **Multi-turn Visual Conversations:** Develop interactive applications that allow users to have extended conversations about images.

These are just a few ideas to get you started. The possibilities are endless, and we're excited to see what you create with vision models powered by Groq for low latency and fast inference!

#### Next Steps

Check out our [Groq API Cookbook](https://github.com/groq/groq-api-cookbook) repository on GitHub (and give us a ⭐) for practical examples and tutorials:

- [Image Moderation](https://github.com/groq/groq-api-cookbook/blob/main/tutorials/image_moderation.ipynb)
- [Multimodal Image Processing (Tool Use, JSON Mode)](https://github.com/groq/groq-api-cookbook/tree/main/tutorials/multimodal-image-processing)

We're always looking for contributions. If you have any cool tutorials or guides to share, submit a pull request for review to help our open-source community!## Documentation

## OpenAI Compatibility

We designed Groq API to be mostly compatible with OpenAI's client libraries, making it easy to
configure your existing applications to run on Groq and try our inference speed.

We also have our own [Groq Python and Groq TypeScript libraries](/docs/libraries) that we encourage you to use.

### [Configuring OpenAI to Use Groq API](\#configuring-openai-to-use-groq-api)

To start using Groq with OpenAI's client libraries, pass your Groq API key to the `api_key` parameter
and change the `base_url` to `https://api.groq.com/openai/v1`:

PythonJavaScript

```python
import os
import openai

client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)
```

You can find your API key [here](/keys).

### [Currently Unsupported OpenAI Features](\#currently-unsupported-openai-features)

Note that although Groq API is mostly OpenAI compatible, there are a few features we don't support just yet:

#### Text Completions

The following fields are currently not supported and will result in a 400 error (yikes) if they are supplied:

- `logprobs`

- `logit_bias`

- `top_logprobs`

- `messages[].name`

- If `N` is supplied, it must be equal to 1.


#### Temperature

If you set a `temperature` value of 0, it will be converted to `1e-8`. If you run into any issues, please try setting the value to a float32 `> 0` and `<= 2`.

#### Audio Transcription and Translation

The following values are not supported:

- `response_format`
- `vtt`
- `srt`
- `timestamp_granularities[]`

### [Feedback](\#feedback)

If you'd like to see support for such features as the above on Groq API, please reach out to us and let us know by submitting a "Feature Request" via "Chat with us" located on the left. We really value your feedback and would love to hear from you! 🤩## Documentation

[**Chat**](api-reference#chat)

[**Create chat completion**](api-reference#chat-create)

POSThttps://api.groq.com/openai/v1/chat/completions

Creates a model response for the given chat conversation.

### Request Body

- frequency\_penaltynumber or nullOptionalDefaults to 0



Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

- function\_callDeprecatedstring / object or nullOptional



Deprecated in favor of `tool_choice`.



Controls which (if any) function is called by the model.
`none` means the model will not call a function and instead generates a message.
`auto` means the model can pick between generating a message or calling a function.
Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.



`none` is the default when no functions are present. `auto` is the default if functions are present.







### Show possible types

- functionsDeprecatedarray or nullOptional



Deprecated in favor of `tools`.



A list of functions the model may generate JSON inputs for.







### Show properties

- logit\_biasobject or nullOptional



This is not yet supported by any of our models.
Modify the likelihood of specified tokens appearing in the completion.

- logprobsboolean or nullOptionalDefaults to false



This is not yet supported by any of our models.
Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`.

- max\_tokensinteger or nullOptional



The maximum number of tokens that can be generated in the chat completion. The total length of input tokens and generated tokens is limited by the model's context length.

- messagesarrayRequired



A list of messages comprising the conversation so far.







### Show possible types

- modelstringRequired



ID of the model to use. For details on which models are compatible with the Chat API, see available [models](/docs/models)

- ninteger or nullOptionalDefaults to 1



How many chat completion choices to generate for each input message. Note that the current moment, only n=1 is supported. Other values will result in a 400 response.

- parallel\_tool\_callsboolean or nullOptionalDefaults to true



Whether to enable parallel function calling during tool use.

- presence\_penaltynumber or nullOptionalDefaults to 0



Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.

- response\_formatobject or nullOptional



An object specifying the format that the model must output.



Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.



**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message.







### Show properties

- seedinteger or nullOptional



If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.
Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.

- stopstring / array or nullOptional



Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence.







### Show possible types

- streamboolean or nullOptionalDefaults to false



If set, partial message deltas will be sent. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. [Example code](/docs/text-chat#streaming-a-chat-completion).

- stream\_optionsobject or nullOptional



Options for streaming response. Only set this when you set `stream: true`.







### Show properties

- temperaturenumber or nullOptionalDefaults to 1



What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or top\_p but not both

- tool\_choicestring / object or nullOptional



Controls which (if any) tool is called by the model.
`none` means the model will not call any tool and instead generates a message.
`auto` means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools.
Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.



`none` is the default when no tools are present. `auto` is the default if tools are present.







### Show possible types

- toolsarray or nullOptional



A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.







### Show properties

- top\_logprobsinteger or nullOptional



This is not yet supported by any of our models.
An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used.

- top\_pnumber or nullOptionalDefaults to 1



An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or temperature but not both.

- userstring or nullOptional



A unique identifier representing your end-user, which can help us monitor and detect abuse.


### Returns

Returns a [chat completion](/docs/api-reference#chat-create) object, or a streamed sequence of [chat completion chunk](/docs/api-reference#chat-create) objects if the request is streamed.

curl

```shell
curl https://api.groq.com/openai/v1/chat/completions -s \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $GROQ_API_KEY" \
-d '{
"model": "llama3-8b-8192",
"messages": [{\
    "role": "user",\
    "content": "Explain the importance of fast language models"\
}]
}'
```

```json
{
  "id": "chatcmpl-f51b2cd2-bef7-417e-964e-a08f0b513c22",
  "object": "chat.completion",
  "created": 1730241104,
  "model": "llama3-8b-8192",
  "choices": [\
    {\
      "index": 0,\
      "message": {\
        "role": "assistant",\
        "content": "Fast language models have gained significant attention in recent years due to their ability to process and generate human-like text quickly and efficiently. The importance of fast language models can be understood from their potential applications and benefits:\n\n1. **Real-time Chatbots and Conversational Interfaces**: Fast language models enable the development of chatbots and conversational interfaces that can respond promptly to user queries, making them more engaging and useful.\n2. **Sentiment Analysis and Opinion Mining**: Fast language models can quickly analyze text data to identify sentiments, opinions, and emotions, allowing for improved customer service, market research, and opinion mining.\n3. **Language Translation and Localization**: Fast language models can quickly translate text between languages, facilitating global communication and enabling businesses to reach a broader audience.\n4. **Text Summarization and Generation**: Fast language models can summarize long documents or even generate new text on a given topic, improving information retrieval and processing efficiency.\n5. **Named Entity Recognition and Information Extraction**: Fast language models can rapidly recognize and extract specific entities, such as names, locations, and organizations, from unstructured text data.\n6. **Recommendation Systems**: Fast language models can analyze large amounts of text data to personalize product recommendations, improve customer experience, and increase sales.\n7. **Content Generation for Social Media**: Fast language models can quickly generate engaging content for social media platforms, helping businesses maintain a consistent online presence and increasing their online visibility.\n8. **Sentiment Analysis for Stock Market Analysis**: Fast language models can quickly analyze social media posts, news articles, and other text data to identify sentiment trends, enabling financial analysts to make more informed investment decisions.\n9. **Language Learning and Education**: Fast language models can provide instant feedback and adaptive language learning, making language education more effective and engaging.\n10. **Domain-Specific Knowledge Extraction**: Fast language models can quickly extract relevant information from vast amounts of text data, enabling domain experts to focus on high-level decision-making rather than manual information gathering.\n\nThe benefits of fast language models include:\n\n* **Increased Efficiency**: Fast language models can process large amounts of text data quickly, reducing the time and effort required for tasks such as sentiment analysis, entity recognition, and text summarization.\n* **Improved Accuracy**: Fast language models can analyze and learn from large datasets, leading to more accurate results and more informed decision-making.\n* **Enhanced User Experience**: Fast language models can enable real-time interactions, personalized recommendations, and timely responses, improving the overall user experience.\n* **Cost Savings**: Fast language models can automate many tasks, reducing the need for manual labor and minimizing costs associated with data processing and analysis.\n\nIn summary, fast language models have the potential to transform various industries and applications by providing fast, accurate, and efficient language processing capabilities."\
      },\
      "logprobs": null,\
      "finish_reason": "stop"\
    }\
  ],
  "usage": {
    "queue_time": 0.037493756,
    "prompt_tokens": 18,
    "prompt_time": 0.000680594,
    "completion_tokens": 556,
    "completion_time": 0.463333333,
    "total_tokens": 574,
    "total_time": 0.464013927
  },
  "system_fingerprint": "fp_179b0f92c9",
  "x_groq": { "id": "req_01jbd6g2qdfw2adyrt2az8hz4w" }
}
```

[**Audio**](api-reference#audio)

[**Create transcription**](api-reference#audio-transcription)

POSThttps://api.groq.com/openai/v1/audio/transcriptions

Transcribes audio into the input language.

### Request Body

- filestringRequired



The audio file object (not file name) to transcribe, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

- languagestringOptional



The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will improve accuracy and latency.

- modelstringRequired



ID of the model to use. Only `whisper-large-v3` is currently available.

- promptstringOptional



An optional text to guide the model's style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text/prompting) should match the audio language.

- response\_formatstringOptionalDefaults to json



The format of the transcript output, in one of these options: `json`, `text`, or `verbose_json`.

- temperaturenumberOptionalDefaults to 0



The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

- timestamp\_granularities\[\]arrayOptionalDefaults to segment



The timestamp granularities to populate for this transcription. `response_format` must be set `verbose_json` to use timestamp granularities. Either or both of these options are supported: `word`, or `segment`. Note: There is no additional latency for segment timestamps, but generating word timestamps incurs additional latency.


### Returns

Returns an audio transcription object

curl

```shell
curl https://api.groq.com/openai/v1/audio/transcriptions \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F file="@./sample_audio.m4a" \
  -F model="whisper-large-v3"
```

```json
{
  "text": "Your transcribed text appears here...",
  "x_groq": {
    "id": "req_unique_id"
  }
}
```

[**Create translation**](api-reference#audio-translation)

POSThttps://api.groq.com/openai/v1/audio/translations

Translates audio into English.

### Request Body

- filestringRequired



The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

- modelstringRequired



ID of the model to use. Only `whisper-large-v3` is currently available.

- promptstringOptional



An optional text to guide the model's style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text/prompting) should be in English.

- response\_formatstringOptionalDefaults to json



The format of the transcript output, in one of these options: `json`, `text`, or `verbose_json`.

- temperaturenumberOptionalDefaults to 0



The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.


### Returns

Returns an audio translation object

curl

```shell
curl https://api.groq.com/openai/v1/audio/translations \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F file="@./sample_audio.m4a" \
  -F model="whisper-large-v3"
```

```json
{
  "text": "Your translated text appears here...",
  "x_groq": {
    "id": "req_unique_id"
  }
}
```

[**Models**](api-reference#models)

[**List models**](api-reference#models-list)

GEThttps://api.groq.com/openai/v1/models

List models

### Returns

A list of models

curl

```shell
curl https://api.groq.com/openai/v1/models \
-H "Authorization: Bearer $GROQ_API_KEY"
```

```json
{
  "object": "list",
  "data": [\
    {\
      "id": "llama3-groq-70b-8192-tool-use-preview",\
      "object": "model",\
      "created": 1693721698,\
      "owned_by": "Groq",\
      "active": true,\
      "context_window": 8192,\
      "public_apps": null\
    },\
    {\
      "id": "gemma2-9b-it",\
      "object": "model",\
      "created": 1693721698,\
      "owned_by": "Google",\
      "active": true,\
      "context_window": 8192,\
      "public_apps": null\
    },\
    {\
      "id": "llama3-8b-8192",\
      "object": "model",\
      "created": 1693721698,\
      "owned_by": "Meta",\
      "active": true,\
      "context_window": 8192,\
      "public_apps": null\
    },\
    {\
      "id": "llama-3.2-90b-vision-preview",\
      "object": "model",\
      "created": 1727226914,\
      "owned_by": "Meta",\
      "active": true,\
      "context_window": 8192,\
      "public_apps": null\
    },\
    {\
      "id": "llama3-70b-8192",\
      "object": "model",\
      "created": 1693721698,\
      "owned_by": "Meta",\
      "active": true,\
      "context_window": 8192,\
      "public_apps": null\
    },\
    {\
      "id": "llama-3.2-11b-vision-preview",\
      "object": "model",\
      "created": 1727226869,\
      "owned_by": "Meta",\
      "active": true,\
      "context_window": 8192,\
      "public_apps": null\
    },\
    {\
      "id": "llama-3.2-11b-text-preview",\
      "object": "model",\
      "created": 1727283005,\
      "owned_by": "Meta",\
      "active": true,\
      "context_window": 8192,\
      "public_apps": null\
    },\
    {\
      "id": "whisper-large-v3-turbo",\
      "object": "model",\
      "created": 1728413088,\
      "owned_by": "OpenAI",\
      "active": true,\
      "context_window": 448,\
      "public_apps": null\
    },\
    {\
      "id": "llava-v1.5-7b-4096-preview",\
      "object": "model",\
      "created": 1725402373,\
      "owned_by": "Other",\
      "active": true,\
      "context_window": 4096,\
      "public_apps": null\
    },\
    {\
      "id": "llama-3.1-70b-versatile",\
      "object": "model",\
      "created": 1693721698,\
      "owned_by": "Meta",\
      "active": true,\
      "context_window": 32768,\
      "public_apps": null\
    },\
    {\
      "id": "llama-3.2-3b-preview",\
      "object": "model",\
      "created": 1727224290,\
      "owned_by": "Meta",\
      "active": true,\
      "context_window": 8192,\
      "public_apps": null\
    },\
    {\
      "id": "whisper-large-v3",\
      "object": "model",\
      "created": 1693721698,\
      "owned_by": "OpenAI",\
      "active": true,\
      "context_window": 448,\
      "public_apps": null\
    },\
    {\
      "id": "llama-guard-3-8b",\
      "object": "model",\
      "created": 1693721698,\
      "owned_by": "Meta",\
      "active": true,\
      "context_window": 8192,\
      "public_apps": null\
    },\
    {\
      "id": "mixtral-8x7b-32768",\
      "object": "model",\
      "created": 1693721698,\
      "owned_by": "Mistral AI",\
      "active": true,\
      "context_window": 32768,\
      "public_apps": null\
    },\
    {\
      "id": "gemma-7b-it",\
      "object": "model",\
      "created": 1693721698,\
      "owned_by": "Google",\
      "active": true,\
      "context_window": 8192,\
      "public_apps": null\
    },\
    {\
      "id": "distil-whisper-large-v3-en",\
      "object": "model",\
      "created": 1693721698,\
      "owned_by": "Hugging Face",\
      "active": true,\
      "context_window": 448,\
      "public_apps": null\
    },\
    {\
      "id": "llama-3.2-1b-preview",\
      "object": "model",\
      "created": 1727224268,\
      "owned_by": "Meta",\
      "active": true,\
      "context_window": 8192,\
      "public_apps": null\
    },\
    {\
      "id": "llama-3.2-90b-text-preview",\
      "object": "model",\
      "created": 1727285716,\
      "owned_by": "Meta",\
      "active": true,\
      "context_window": 8192,\
      "public_apps": null\
    },\
    {\
      "id": "llama3-groq-8b-8192-tool-use-preview",\
      "object": "model",\
      "created": 1693721698,\
      "owned_by": "Groq",\
      "active": true,\
      "context_window": 8192,\
      "public_apps": null\
    },\
    {\
      "id": "llama-3.1-8b-instant",\
      "object": "model",\
      "created": 1693721698,\
      "owned_by": "Meta",\
      "active": true,\
      "context_window": 131072,\
      "public_apps": null\
    }\
  ]
}
```

[**Retrieve model**](api-reference#models-retrieve)

GEThttps://api.groq.com/openai/v1/models/{model}

Get model

### Returns

A model object

curl

```shell
curl https://api.groq.com/openai/v1/models/llama3-8b-8192 \
-H "Authorization: Bearer $GROQ_API_KEY"
```

```json
{
  "id": "llama3-8b-8192",
  "object": "model",
  "created": 1693721698,
  "owned_by": "Meta",
  "active": true,
  "context_window": 8192,
  "public_apps": null
}
```## Documentation

## Introduction to Tool Use

Tool use is a powerful feature that allows Large Language Models (LLMs) to interact with external resources, such as APIs,
databases, and the web, to gather dynamic data they wouldn't otherwise have access to in their pre-trained (or static) state
and perform actions beyond simple text generation.

Tool use bridges the gap between the data that the LLMs were trained on with dynamic data and real-world actions, which
opens up a wide array of realtime use cases for us to build powerful applications with, especially with Groq's insanely fast
inference speed. 🚀

## How Tool Use Works

Groq API tool use structure is compatible with OpenAI's tool use structure, which allows for easy integration. See the following cURL example of a tool use request:

```bash
curl https://api.groq.com/openai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $GROQ_API_KEY" \
-d '{
  "model": "llama3-groq-70b-8192-tool-use-preview",
  "messages": [\
    {\
      "role": "user",\
      "content": "What'\''s the weather like in Boston today?"\
    }\
  ],
  "tools": [\
    {\
      "type": "function",\
      "function": {\
        "name": "get_current_weather",\
        "description": "Get the current weather in a given location",\
        "parameters": {\
          "type": "object",\
          "properties": {\
            "location": {\
              "type": "string",\
              "description": "The city and state, e.g. San Francisco, CA"\
            },\
            "unit": {\
              "type": "string",\
              "enum": ["celsius", "fahrenheit"]\
            }\
          },\
          "required": ["location"]\
        }\
      }\
    }\
  ],
  "tool_choice": "auto"
}'
```

To integrate tools with Groq API, follow these steps:

- Provide tools (or predefined functions) to the LLM for performing actions and accessing external data in
real-time in addition to your user prompt within your Groq API request
- Define how the tools should be used to teach the LLM how to use them effectively (e.g. by defining input and
output formats)
- Let the LLM autonomously decide whether or not the provided tools are needed for a user query by evaluating the user
query, determining whether the tools can enhance its response, and utilizing the tools accordingly
- Extract tool input, execute the tool code, and return results
- Let the LLM use the tool result to formulate a response to the original prompt

This process allows the LLM to perform tasks such as real-time data retrieval, complex calculations, and external API
interaction, all while maintaining a natural conversation with our end user.

## Tool Use with Groq

Groq API endpoints support tool use to almost instantly deliver structured JSON output that can be used to directly invoke functions from
desired external resources.

### [Supported Models](\#supported-models)

**Groq Fine-Tuned Models**

These models have been finetuned by Groq specifically for tool use and are currently in public preview:

- **`llama3-groq-70b-8192-tool-use-preview`**
- **`llama3-groq-8b-8192-tool-use-preview`**

Check out our launch [post](https://wow.groq.com/introducing-llama-3-groq-tool-use-models/) for more information.

**Note:** When using our fine-tuned models in your workflow, we recommend implementing a routing system. [Learn more below.](/docs/tool-use#routing-system)

**Llama 3.1 Models**

The following Llama-3.1 models are also recommended for tool use due to their versatility and performance:

- **`llama-3.1-70b-versatile`**
- **`llama-3.1-8b-instant`**

**Note:** For wide scenario multi-turn tool use, we recommend using the native tool use feature of the Llama 3.1 models. For
multi-turn with a narrow scenarios, fine-tuned tool use models might work well. We recommend trying both and seeing which
works best for your specific use case!

**Other Supported Models**

The following models powered by Groq also support tool use:

- **`llama3-70b-8192`**
- **`llama3-8b-8192`**
- **`mixtral-8x7b-32768`** (parallel tool use not supported)
- **`gemma-7b-it`** (parallel tool use not supported)
- **`gemma2-9b-it`** (parallel tool use not supported)

## Tools Specifications

Tool use is part of the [Groq API chat completion request payload](https://console.groq.com/docs/api-reference#chat-create).

### [Tool Call and Tool Response Structure](\#tool-call-and-tool-response-structure)

**Tool Call Structure**

Groq API tool calls are structured to be OpenAI-compatible. The following is an example tool call structure:

```json
{
  "model": "llama3-groq-70b-8192-tool-use-preview",
  "messages": [\
    {\
      "role": "system",\
      "content": "You are a weather assistant. Use the get_weather function to retrieve weather information for a given location."\
    },\
    {\
      "role": "user",\
      "content": "What's the weather like in New York today?"\
    }\
  ],
  "tools": [\
    {\
      "type": "function",\
      "function": {\
        "name": "get_weather",\
        "description": "Get the current weather for a location",\
        "parameters": {\
          "type": "object",\
          "properties": {\
            "location": {\
              "type": "string",\
              "description": "The city and state, e.g. San Francisco, CA"\
            },\
            "unit": {\
              "type": "string",\
              "enum": ["celsius", "fahrenheit"],\
              "description": "The unit of temperature to use. Defaults to fahrenheit."\
            }\
          },\
          "required": ["location"]\
        }\
      }\
    }\
  ],
  "tool_choice": "auto",
  "max_tokens": 4096
}'
```

**Tool Call Response**

The following is an example tool call response based on the above:

```json
"model": "llama3-groq-70b-8192-tool-use-preview",
"choices": [{\
    "index": 0,\
    "message": {\
        "role": "assistant",\
        "tool_calls": [{\
            "id": "call_d5wg",\
            "type": "function",\
            "function": {\
                "name": "get_weather",\
                "arguments": "{\"location\": \"New York, NY\"}"\
            }\
        }]\
    },\
    "logprobs": null,\
    "finish_reason": "tool_calls"\
}],
```

When a model decides to use a tool, it returns a response with a `tool_calls` object containing:

- `id`: a unique identifier for the tool call
- `type`: the type of tool call, i.e. function
- `name`: the name of the tool being used
- `parameters`: an object containing the input being passed to the tool

### [Setting Up Tools](\#setting-up-tools)

To get started, let's go through an example of tool use with Groq API that you can use as a base to build more tools on
your own.

#### Step 1: Create Tool

Let's install Groq SDK, set up our Groq client, and create a function called `calculate` to evaluate a mathematical
expression that we will represent as a tool.

Note: In this example, we're defining a function as our tool, but your tool can be any function or an external
resource (e.g. dabatase, web search engine, external API).

PythonJavaScript

```shell
pip install groq
```

```py
1from groq import Groq
2import json
3
4# Initialize the Groq client
5client = Groq()
6# Specify the model to be used (we recommend our fine-tuned models or the Llama 3.1 models)
7MODEL = 'llama3-groq-70b-8192-tool-use-preview'
8
9def calculate(expression):
10    """Evaluate a mathematical expression"""
11    try:
12        # Attempt to evaluate the math expression
13        result = eval(expression)
14        return json.dumps({"result": result})
15    except:
16        # Return an error message if the math expression is invalid
17        return json.dumps({"error": "Invalid expression"})
```

#### Step 2: Pass Tool Definition and Messages to Model

Next, we'll define our `calculate` tool within an array of available `tools` and call our Groq API chat completion. You
can read more about tool schema and supported required and optional fields above in **Tool Specifications.**

By defining our tool, we'll inform our model about what our tool does and have the model decide whether or not to use the
tool. We should be as descriptive and specific as possible for our model to be able to make the correct tool use decisions.

In addition to our `tools` array, we will provide our `messages` array (e.g. containing system prompt, assistant prompt, and/or
user prompt).

#### Step 3: Receive and Handle Tool Results

After executing our chat completion, we'll extract our model's response and check for tool calls.

If the model decides that no tools should be used and does not generate a tool or function call, then the response will
be a normal chat completion (i.e. `response_message = response.choices[0].message`) with a direct model reply to the user query.

If the model decides that tools should be used and generates a tool or function call, we will:

- Define available tool or function,
- Add the model's response to the conversation by appending our message
- Process the tool call and add the tool response to our message
- Make a second Groq API call with the updated conversation
- Return the final response

PythonJavaScript

```py
1# imports calculate function from step 1
2def run_conversation(user_prompt):
3    # Initialize the conversation with system and user messages
4    messages=[\
5        {\
6            "role": "system",\
7            "content": "You are a calculator assistant. Use the calculate function to perform mathematical operations and provide the results."\
8        },\
9        {\
10            "role": "user",\
11            "content": user_prompt,\
12        }\
13    ]
14    # Define the available tools (i.e. functions) for our model to use
15    tools = [\
16        {\
17            "type": "function",\
18            "function": {\
19                "name": "calculate",\
20                "description": "Evaluate a mathematical expression",\
21                "parameters": {\
22                    "type": "object",\
23                    "properties": {\
24                        "expression": {\
25                            "type": "string",\
26                            "description": "The mathematical expression to evaluate",\
27                        }\
28                    },\
29                    "required": ["expression"],\
30                },\
31            },\
32        }\
33    ]
34    # Make the initial API call to Groq
35    response = client.chat.completions.create(
36        model=MODEL, # LLM to use
37        messages=messages, # Conversation history
38        stream=False
39        tools=tools, # Available tools (i.e. functions) for our LLM to use
40        tool_choice="auto", # Let our LLM decide when to use tools
41        max_tokens=4096 # Maximum number of tokens to allow in our response
42    )
43    # Extract the response and any tool call responses
44    response_message = response.choices[0].message
45    tool_calls = response_message.tool_calls
46    if tool_calls:
47        # Define the available tools that can be called by the LLM
48        available_functions = {
49            "calculate": calculate,
50        }
51        # Add the LLM's response to the conversation
52        messages.append(response_message)
53
54        # Process each tool call
55        for tool_call in tool_calls:
56            function_name = tool_call.function.name
57            function_to_call = available_functions[function_name]
58            function_args = json.loads(tool_call.function.arguments)
59            # Call the tool and get the response
60            function_response = function_to_call(
61                expression=function_args.get("expression")
62            )
63            # Add the tool response to the conversation
64            messages.append(
65                {
66                    "tool_call_id": tool_call.id,
67                    "role": "tool", # Indicates this message is from tool use
68                    "name": function_name,
69                    "content": function_response,
70                }
71            )
72        # Make a second API call with the updated conversation
73        second_response = client.chat.completions.create(
74            model=MODEL,
75            messages=messages
76        )
77        # Return the final response
78        return second_response.choices[0].message.content
79# Example usage
80user_prompt = "What is 25 * 4 + 10?"
81print(run_conversation(user_prompt))
```

### [Routing System](\#routing-system)

If you use our models fine-tuned for tool use, we recommended to use them as part of a routing system:

- **Query Analysis**: Implement a routing system that analyzes incoming user queries to determine their nature and requirements.
- **Model Selection**: Based on the query analysis, route the request to the most appropriate model:
  - For queries involving function calling, API interactions, or structured data manipulation, use the Llama 3 Groq Tool Use models.
  - For general knowledge, open-ended conversations, or tasks not specifically related to tool use, route to a general-purpose language model, such as Llama 3 70B.

The following is the `calculate` tool we built in the above steps enhanced to include a routing system that routes our request
to Llama 3 70B if the user query does not require the tool:

PythonJavaScript

```py
1from groq import Groq
2import json
3
4# Initialize the Groq client
5client = Groq()
6
7# Define models
8ROUTING_MODEL = "llama3-70b-8192"
9TOOL_USE_MODEL = "llama3-groq-70b-8192-tool-use-preview"
10GENERAL_MODEL = "llama3-70b-8192"
11
12def calculate(expression):
13    """Tool to evaluate a mathematical expression"""
14    try:
15        result = eval(expression)
16        return json.dumps({"result": result})
17    except:
18        return json.dumps({"error": "Invalid expression"})
19
20def route_query(query):
21    """Routing logic to let LLM decide if tools are needed"""
22    routing_prompt = f"""
23    Given the following user query, determine if any tools are needed to answer it.
24    If a calculation tool is needed, respond with 'TOOL: CALCULATE'.
25    If no tools are needed, respond with 'NO TOOL'.
26
27    User query: {query}
28
29    Response:
30    """
31
32    response = client.chat.completions.create(
33        model=ROUTING_MODEL,
34        messages=[\
35            {"role": "system", "content": "You are a routing assistant. Determine if tools are needed based on the user query."},\
36            {"role": "user", "content": routing_prompt}\
37        ],
38        max_tokens=20  # We only need a short response
39    )
40
41    routing_decision = response.choices[0].message.content.strip()
42
43    if "TOOL: CALCULATE" in routing_decision:
44        return "calculate tool needed"
45    else:
46        return "no tool needed"
47
48def run_with_tool(query):
49    """Use the tool use model to perform the calculation"""
50    messages = [\
51        {\
52            "role": "system",\
53            "content": "You are a calculator assistant. Use the calculate function to perform mathematical operations and provide the results.",\
54        },\
55        {\
56            "role": "user",\
57            "content": query,\
58        }\
59    ]
60    tools = [\
61        {\
62            "type": "function",\
63            "function": {\
64                "name": "calculate",\
65                "description": "Evaluate a mathematical expression",\
66                "parameters": {\
67                    "type": "object",\
68                    "properties": {\
69                        "expression": {\
70                            "type": "string",\
71                            "description": "The mathematical expression to evaluate",\
72                        }\
73                    },\
74                    "required": ["expression"],\
75                },\
76            },\
77        }\
78    ]
79    response = client.chat.completions.create(
80        model=TOOL_USE_MODEL,
81        messages=messages,
82        tools=tools,
83        tool_choice="auto",
84        max_tokens=4096
85    )
86    response_message = response.choices[0].message
87    tool_calls = response_message.tool_calls
88    if tool_calls:
89        messages.append(response_message)
90        for tool_call in tool_calls:
91            function_args = json.loads(tool_call.function.arguments)
92            function_response = calculate(function_args.get("expression"))
93            messages.append(
94                {
95                    "tool_call_id": tool_call.id,
96                    "role": "tool",
97                    "name": "calculate",
98                    "content": function_response,
99                }
100            )
101        second_response = client.chat.completions.create(
102            model=TOOL_USE_MODEL,
103            messages=messages
104        )
105        return second_response.choices[0].message.content
106    return response_message.content
107
108def run_general(query):
109    """Use the general model to answer the query since no tool is needed"""
110    response = client.chat.completions.create(
111        model=GENERAL_MODEL,
112        messages=[\
113            {"role": "system", "content": "You are a helpful assistant."},\
114            {"role": "user", "content": query}\
115        ]
116    )
117    return response.choices[0].message.content
118
119def process_query(query):
120    """Process the query and route it to the appropriate model"""
121    route = route_query(query)
122    if route == "calculate":
123        response = run_with_tool(query)
124    else:
125        response = run_general(query)
126
127    return {
128        "query": query,
129        "route": route,
130        "response": response
131    }
132
133# Example usage
134if __name__ == "__main__":
135    queries = [\
136        "What is the capital of the Netherlands?",\
137        "Calculate 25 * 4 + 10"\
138    ]
139
140    for query in queries:
141        result = process_query(query)
142        print(f"Query: {result['query']}")
143        print(f"Route: {result['route']}")
144        print(f"Response: {result['response']}\n")
```

## Parallel Tool Use

We learned about tool use and built single-turn tool use examples above. Now let's take tool use a step further and imagine
a workflow where multiple tools can be called simultaneously, enabling more efficient and effective responses.

This concept is known as **parallel tool use** and is key for building agentic workflows that can deal with complex queries,
which is a great example of where inference speed becomes increasingly important (and thankfully we can access fast inference
speed with Groq API).

N **ote:** Parallel tool use is natively enabled for all Llama 3 and Llama 3.1 models!

Here's an example of parallel tool use with a tool for getting the temperature and the tool for getting the weather condition
to show parallel tool use with Groq API in action:

PythonJavaScript

```py
1import json
2from groq import Groq
3import os
4
5# Initialize Groq client
6client = Groq()
7model = "llama3-groq-70b-8192-tool-use-preview"
8
9# Define weather tools
10def get_temperature(location: str):
11    # This is a mock tool/function. In a real scenario, you would call a weather API.
12    temperatures = {"New York": 22, "London": 18, "Tokyo": 26, "Sydney": 20}
13    return temperatures.get(location, "Temperature data not available")
14
15def get_weather_condition(location: str):
16    # This is a mock tool/function. In a real scenario, you would call a weather API.
17    conditions = {"New York": "Sunny", "London": "Rainy", "Tokyo": "Cloudy", "Sydney": "Clear"}
18    return conditions.get(location, "Weather condition data not available")
19
20# Define system messages and tools
21messages = [\
22    {"role": "system", "content": "You are a helpful weather assistant."},\
23    {"role": "user", "content": "What's the weather like in New York and London?"},\
24]
25
26tools = [\
27    {\
28        "type": "function",\
29        "function": {\
30            "name": "get_temperature",\
31            "description": "Get the temperature for a given location",\
32            "parameters": {\
33                "type": "object",\
34                "properties": {\
35                    "location": {\
36                        "type": "string",\
37                        "description": "The name of the city",\
38                    }\
39                },\
40                "required": ["location"],\
41            },\
42        },\
43    },\
44    {\
45        "type": "function",\
46        "function": {\
47            "name": "get_weather_condition",\
48            "description": "Get the weather condition for a given location",\
49            "parameters": {\
50                "type": "object",\
51                "properties": {\
52                    "location": {\
53                        "type": "string",\
54                        "description": "The name of the city",\
55                    }\
56                },\
57                "required": ["location"],\
58            },\
59        },\
60    }\
61]
62
63# Make the initial request
64response = client.chat.completions.create(
65    model=model, messages=messages, tools=tools, tool_choice="auto", max_tokens=4096
66)
67
68response_message = response.choices[0].message
69tool_calls = response_message.tool_calls
70
71# Process tool calls
72messages.append(response_message)
73
74available_functions = {
75    "get_temperature": get_temperature,
76    "get_weather_condition": get_weather_condition,
77}
78
79for tool_call in tool_calls:
80    function_name = tool_call.function.name
81    function_to_call = available_functions[function_name]
82    function_args = json.loads(tool_call.function.arguments)
83    function_response = function_to_call(**function_args)
84
85    messages.append(
86        {
87            "role": "tool",
88            "content": str(function_response),
89            "tool_call_id": tool_call.id,
90        }
91    )
92
93# Make the final request with tool call results
94final_response = client.chat.completions.create(
95    model=model, messages=messages, tools=tools, tool_choice="auto", max_tokens=4096
96)
97
98print(final_response.choices[0].message.content)
```

## Error Handling

Groq API tool use is designed to verify whether a model generates a valid tool call object. When a model fails to generate a valid tool call object,
Groq API will return a 400 error with an explanation in the "failed\_generation" field of the JSON body that is returned.

### [Next Steps](\#next-steps)

For more information and examples of working with multiple tools in parallel using Groq API and Instructor, see our Groq API Cookbook
tutorial [here](https://github.com/groq/groq-api-cookbook/blob/main/tutorials/parallel-tool-use/parallel-tool-use.ipynb).

## Tool Use with Structured Outputs (Python)

Groq API offers best-effort matching for parameters, which means the model could occasionally miss parameters or
misinterpret types for more complex tool calls. We recommend the [Instuctor](https://python.useinstructor.com/hub/groq/)
library to simplify the process of working with structured data and to ensure that the model's output adheres to a predefined
schema.

Here's an example of how to implement tool use using the Instructor library with Groq API:

```shell
pip install instructor pydantic
```

```py
1import instructor
2from pydantic import BaseModel, Field
3from groq import Groq
4
5# Define the tool schema
6tool_schema = {
7    "name": "get_weather_info",
8    "description": "Get the weather information for any location.",
9    "parameters": {
10        "type": "object",
11        "properties": {
12            "location": {
13                "type": "string",
14                "description": "The location for which we want to get the weather information (e.g., New York)"
15            }
16        },
17        "required": ["location"]
18    }
19}
20
21# Define the Pydantic model for the tool call
22class ToolCall(BaseModel):
23    input_text: str = Field(description="The user's input text")
24    tool_name: str = Field(description="The name of the tool to call")
25    tool_parameters: str = Field(description="JSON string of tool parameters")
26
27class ResponseModel(BaseModel):
28    tool_calls: list[ToolCall]
29
30# Patch Groq() with instructor
31client = instructor.from_groq(Groq(), mode=instructor.Mode.JSON)
32
33def run_conversation(user_prompt):
34    # Prepare the messages
35    messages = [\
36        {\
37            "role": "system",\
38            "content": f"You are an assistant that can use tools. You have access to the following tool: {tool_schema}"\
39        },\
40        {\
41            "role": "user",\
42            "content": user_prompt,\
43        }\
44    ]
45
46    # Make the Groq API call
47    response = client.chat.completions.create(
48        model="llama-3.1-70b-versatile",
49        response_model=ResponseModel,
50        messages=messages,
51        temperature=0.7,
52        max_tokens=1000,
53    )
54
55    return response.tool_calls
56
57# Example usage
58user_prompt = "What's the weather like in San Francisco?"
59tool_calls = run_conversation(user_prompt)
60
61for call in tool_calls:
62    print(f"Input: {call.input_text}")
63    print(f"Tool: {call.tool_name}")
64    print(f"Parameters: {call.tool_parameters}")
65    print()
```

### [Benefits of Using Structured Outputs](\#benefits-of-using-structured-outputs)

- Type Safety: Pydantic models ensure that output adheres to the expected structure, reducing the risk of errors.
- Automatic Validation: Instructor automatically validates the model's output against the defined schema.

### [Next Steps](\#next-steps)

For more information and examples of working with structured outputs using Groq API and Instructor, see our Groq API Cookbook
tutorial [here](https://github.com/groq/groq-api-cookbook/blob/main/tutorials/structured-output-instructor/structured_output_instructor.ipynb).

## Best Practices

- Provide detailed tool descriptions for optimal performance.
- We recommend tool use with the Instructor library for structured outputs.
- Use the fine-tuned Llama 3 models by Groq or the Llama 3.1 models for your applications that require tool use.
- Implement a routing system when using fine-tuned models in your workflow.
- Handle tool execution errors by returning error messages with `"is_error": true`.
`````