# Filing Download & PDF Generator API

The Filing Download API supports downloading of all EDGAR filings, exhibits, and attachments from 1993 to the present, with up to 50 requests per second, providing access to over 1,000 terabytes of SEC filing data. With 15,000 files downloadable within a 5-minute interval, the API enables direct access to all EDGAR form types and any attached file, either via the HTTP API itself or with a single line of code in Python, Node.js, or other programming languages.

The Download API provides access to over 18 million filings and more than 100 million exhibit files across 400+ form types published on EDGAR since 1993. Supported form types include annual and quarterly reports (e.g., Forms 10-K, 10-Q, 20-F, 40-F), event-driven filings (e.g., Forms 8-K, 6-K), registration statements (e.g., S-1, S-3, S-4, S-8), insider trading reports (Forms 3, 4, 5), proxy statements (e.g., DEF 14A), voting records (e.g., PRE 14A, N-PX), and many more.

The original file formats and contents, such as HTML, XML, XSD, XBRL, TXT, PDF, Excel, Word, and images, are fully preserved. Additionally, HTML, XML, and TXT filings and exhibits can be converted to PDF using the PDF Generator API by simply providing the URL of the original filing or exhibit, and receiving the PDF in return.

Dataset size:

All SEC EDGAR filings, exhibits, and attachments filed since 1993 to present. Includes HTML, TXT, XML, PDF, Excel files, images, and more. Covers all form types, such as 10-K, 10-Q, 8-K, S-1, DEF 14A, with over 18 million filings and 100 million exhibit files.

Data update frequency:

New filings, exhibits, and attachments are available in less than 600 milliseconds after they are published on EDGAR.

Survivorship bias free:

Yes. All filings, exhibits, and attachments are available from all 800,000+ EDGAR filers, including those that are still active and those that have ceased to file.

## [Use Cases](\#use-cases)

The Filing Download and PDF Generator APIs are often used alongside the [real-time filing Stream API](/docs/stream-api) or the [pull-based filing Query API](/docs/query-api). Filings or exhibit URLs pointing to the sec.gov source are typically retrieved from the metadata returned by the Stream or Query API, and these URLs are then used to download the content via the Download API or convert it to PDF using the PDF Generator API. Use cases include:

- Download historical filings, such as annual reports on Form 10-K, to train LLMs or perform textual analysis
- Display EDGAR filings in different formats on investor relationship websites
- Access and monitor specific filing exhibits, such as material contracts, for compliance
- Download original XBRL files for financial analysis
- Convert HTML, XML, and TXT filings to PDF for user exports

## [Download API](\#download-api)

Filings, exhibits and attachements can be downloaded by calling the Download API endpoint with the path to the original file on SEC EDGAR. The Download API returns the original file content, such as HTML, XML or TXT.

### [API Endpoint](\#download-api-endpoint)

https://archive.sec-api.io

Supported HTTP Method: `GET`

The response content type depends on the requested file. For instance, requesting a HTML file returns a `text/html` MIME content type. The API supports all MIME types, such as `text/xml` for XML files or `images/png` for images. By default, transmitted content between the Download API and a client application is compressed with gzip. Typically, the response is automatically decompressed by the client application, such as a browser or a Python/Node.js script. In case of low-level HTTP requests, the decompression needs to be handled by the client application.

### [Authentication](\#authentication)

Two authentication methods are available. Choose the method that best fits your use case:

- **Authorization header**: Set the API key as the value of the `Authorization` header. Do not add "Bearer" or any other words in front of the API key. Example: `Authorization: YOUR_API_KEY`
- **Query parameter**: Set the API key as the `token` query parameter.

Example: `https://archive.sec-api.io/path/to/edgar-file?token=YOUR_API_KEY`. Instead of performing requests to `https://archive.sec-api.io/path/to/edgar-file`, you always append `?token=YOUR_API_KEY` to the end of the URL.

When using the Python or Node.js SDK, the API key is automatically added to the request headers.

### [Request Parameters](\#request-parameters)

The Download API accepts the file path of the original SEC EDGAR URL. A generic example looks like this:

https://archive.sec-api.io/<cik>/<accession-number>/<filename>

- `<cik>`: The filer's CIK, without leading zeros, e.g. 815094.
- `<accession-number>`: The filing's accession number, using only numeric characters (hyphens removed). For example, 000156459021006205 instead of 0001564590-21-006205.
- `<filename>`: The name of the file (any file type is supported).

All three values can be obtained from the original file URL and the original file path on SEC EDGAR can always be used directly with the Download API.

For example, to download the filing with the URL:

        https://www.sec.gov/Archives/edgar/data/815094/000156459021006205/abmd-8k\_20210211.htm

The path after `data/` is appended to the Download API endpoint like this:

        https://archive.sec-api.io/815094/000156459021006205/abmd-8k\_20210211.htm

## [PDF Generator API](\#pdf-generator-api)

Download any SEC filing or exhibit as a PDF file.

Since most SEC filings, exhibits and attachements are not published in PDF format, converting the original content is necessary to download them as PDFs. The PDF Generator API offers this functionality by converting HTML, XML, or text-based filings and exhibits into PDFs while preserving the original formatting, including images and tables. The API supports downloading all EDGAR form types as PDFs, including filings and exhibits such as Form 10-K, 10-Q, 8-K, DEF14A, and more, while preserving the original formatting.

Images are optimized and scaled for high-quality printing, such as in proxy statements, and invisible inline XBRL tags are removed to reduce PDF file size and prevent unnecessary bloating. All original content is preserved without alteration. The PDFs are designed to be easily shareable, printable, and suitable for archiving.

Legacy text-based filings (.txt) were not originally designed for PDF-printable output. As a result, single table rows in these older filings may span multiple lines and may not fit within the standard A4 PDF page width. NLP, LLM or RAG-based tasks might encounter difficulties when parsing such files as PDFs. In these cases, it is recommended to use the original text content instead of the PDF version for better accuracy.

### [API Endpoint](\#pdf-generator-api-endpoint)

Filings and exhibits can be converted to and downloaded as PDF by calling the following PDF Generator API endpoint with the URL of the original filing or exhibit as a query parameter:

https://api.sec-api.io/filing-reader

Supported HTTP Method: `GET`

Response content type: `application/pdf`

The API returns the filing or exhibit as a PDF file, preserving the original formatting, including images and tables.

### [Request Parameters](\#request-parameters)

- `token` (required) - Your API key.
- `url` (required) - URL of the filing or exhibit attachement. All file types are supported (HTML, XML, TXT, etc). Must be a valid "sec.gov/Archives" URL. Remove inline XBRL parameters from the URL before using it with the API by replacing `/ix?doc=` with an empty string.

Example URLs:

`https://www.sec.gov/Archives/edgar/data/1833764/000089924321006812/xslF345X02/doc3.xml`

`https://www.sec.gov/Archives/edgar/data/815094/000156459021006205/abmd-8k_20210211.htm`


#### [Example](\#example)

Replace `YOUR_API_KEY` with your actual API key, and copy and paste any of the following example URLs into a browser to download the filing as a PDF.

**URL to download a Form 10-K filing as PDF:**

    https://api.sec-api.io/filing-reader?

    token=YOUR\_API\_KEY&

    url=https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm

**URL to download a Form 4 filing in XML format as PDF:**

    https://api.sec-api.io/filing-reader?

    token=YOUR\_API\_KEY&

    url=https://www.sec.gov/Archives/edgar/data/1833764/000089924321006812/xslF345X02/doc3.xml