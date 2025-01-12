# Analysis Plan for Amazon

## Query
Analyze Amazons executive compensation structure.

## Analysis Type
Executive Compensation Analysis

## Information Needs

### 1. Amazon's executive compensation details
- **Description**: Detailed breakdown of compensation for key executives, including base salary, bonuses, stock awards, options, other compensation, and total compensation for each executive.  Data should include historical trends where available.
- **Type**: factual
- **Data Source**: 10k
- **Storage ID**: `amazon_executive_compensation_data`

### 2. Amazon's executive compensation philosophy and structure
- **Description**: Description of Amazon's approach to executive compensation, including the rationale behind the structure, performance metrics used, and any relevant governance policies.
- **Type**: broad
- **Data Source**: 10k
- **Storage ID**: `amazon_compensation_philosophy`

### 3. Industry benchmarks for executive compensation
- **Description**: Average compensation data for executives in similar roles within comparable companies in the technology sector.  This will provide context for evaluating Amazon's compensation levels.
- **Type**: broad
- **Data Source**: web
- **Storage ID**: `industry_compensation_benchmarks`

## Execution Plan

### Step 1: Compensation Structure Decomposition
#### Action 1
- **Type**: TextAnalysis
- **Task**: Analyze the textual description of Amazon's executive compensation philosophy to understand the key drivers and rationale behind the structure.
- **Required Information**:
  - `amazon_compensation_philosophy`

### Step 2: Compensation Data Analysis
#### Action 1
- **Type**: FinancialCalculation
- **Task**: Calculate the average annual percentage change in total compensation for each executive over the available historical period.
- **Required Information**:
  - `amazon_executive_compensation_data`

#### Action 2
- **Type**: FinancialCalculation
- **Task**: Calculate the ratio of each component of compensation (salary, bonus, stock awards, etc.) to total compensation for each executive, to understand the relative importance of each component.
- **Required Information**:
  - `amazon_executive_compensation_data`

### Step 3: Benchmarking Analysis
#### Action 1
- **Type**: ComparisonAnalysis
- **Task**: Compare Amazon's executive compensation levels (total compensation, salary, bonus, stock awards) to the industry benchmarks, identifying any significant differences or outliers.
- **Required Information**:
  - `amazon_executive_compensation_data`
  - `industry_compensation_benchmarks`

### Step 4: Result Formatting
#### Action 1
- **Type**: ResultFormatting
- **Task**: Summarize the findings, including a description of Amazon's executive compensation structure, an analysis of compensation trends, a comparison to industry benchmarks, and key conclusions regarding the effectiveness and competitiveness of Amazon's executive compensation program.
- **Required Information**:
  - `amazon_executive_compensation_data`
  - `amazon_compensation_philosophy`
  - `industry_compensation_benchmarks`
