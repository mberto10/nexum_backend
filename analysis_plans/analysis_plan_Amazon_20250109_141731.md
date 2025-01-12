# Analysis Plan for Amazon

## Query
Analyze Amazons executive compensation structure.

## Analysis Type
Executive Compensation Analysis

## Information Needs

### 1. Amazon's executive compensation details
- **Description**: Detailed breakdown of compensation for key executives, including base salary, bonuses, stock awards, options, and other benefits.  Data should include historical trends and comparisons across executives.
- **Type**: factual
- **Data Source**: 10k
- **Storage ID**: `amazon_exec_comp_data`

### 2. Amazon's executive compensation philosophy and rationale
- **Description**: Description of Amazon's approach to executive compensation, including the rationale behind the structure and any relevant governance policies.
- **Type**: broad
- **Data Source**: 10k
- **Storage ID**: `amazon_comp_philosophy`

### 3. Industry benchmarks for executive compensation
- **Description**: Compensation data for comparable executives in similar companies within the technology and e-commerce sectors.  This will allow for a comparative analysis of Amazon's compensation structure.
- **Type**: broad
- **Data Source**: web
- **Storage ID**: `industry_comp_benchmarks`

## Execution Plan

### Step 1: Compensation Structure Breakdown
#### Action 1
- **Type**: FinancialCalculation
- **Task**: Calculate the total compensation for each executive over the past three years, separating base salary, bonuses, stock awards, and other benefits.
- **Required Information**:
  - `amazon_exec_comp_data`

### Step 2: Compensation Trend Analysis
#### Action 1
- **Type**: FinancialCalculation
- **Task**: Calculate year-over-year growth rates for each compensation component for each executive.
- **Required Information**:
  - `amazon_exec_comp_data`

### Step 3: Comparative Analysis
#### Action 1
- **Type**: ComparisonAnalysis
- **Task**: Compare Amazon's executive compensation to industry benchmarks, considering company size, performance, and sector.
- **Required Information**:
  - `amazon_exec_comp_data`
  - `industry_comp_benchmarks`

### Step 4: Alignment with Company Performance
#### Action 1
- **Type**: ComparisonAnalysis
- **Task**: Analyze the correlation between executive compensation and Amazon's financial performance (revenue, profit, stock price) over the past three years.
- **Required Information**:
  - `amazon_exec_comp_data`

### Step 5: Qualitative Assessment
#### Action 1
- **Type**: TextAnalysis
- **Task**: Analyze Amazon's stated compensation philosophy and rationale in relation to the observed compensation structure and industry benchmarks.
- **Required Information**:
  - `amazon_comp_philosophy`

### Step 6: Result Formatting
#### Action 1
- **Type**: ResultFormatting
- **Task**: Summarize the findings, including key metrics, comparisons, and qualitative assessments. Present the results in a clear and concise manner, potentially including tables and charts.
- **Required Information**:
  - `amazon_exec_comp_data`
  - `industry_comp_benchmarks`
  - `amazon_comp_philosophy`
