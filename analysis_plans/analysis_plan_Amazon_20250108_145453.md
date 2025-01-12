# Analysis Plan for Amazon

## Query
Analyze Amazon's revenue distribution across regions and business segments.

## Analysis Type
Revenue Analysis

## Information Needs

### 1. Historical revenue data by region and segment
- **Description**: Detailed breakdown of Amazon's revenue across different geographical regions (e.g., North America, International) and business segments (e.g., North America, International, AWS, Advertising). Data should include yearly and quarterly figures for at least the past 5 years.
- **Type**: factual
- **Storage ID**: `revenue_data_by_region_segment`

### 2. Description of Amazon's business segments
- **Description**: Detailed explanation of each business segment's operations, products, and services. This will help in understanding the revenue composition.
- **Type**: broad
- **Storage ID**: `segment_description`

### 3. Geographic distribution of Amazon's operations
- **Description**: Information on the presence and scale of Amazon's operations in different regions. This will provide context for revenue distribution.
- **Type**: broad
- **Storage ID**: `geographic_distribution`

### 4. Currency exchange rate information
- **Description**: Historical exchange rates for relevant currencies to adjust international revenue figures to a common currency (e.g., USD).
- **Type**: factual
- **Storage ID**: `exchange_rates`

## Execution Plan

### Step 1: Data Consolidation
#### Action 1
- **Type**: FinancialCalculation
- **Task**: Gather revenue data from Item 8 (Financial Statements) and consolidate it by region and segment.  Convert all figures to USD using the exchange rate data.
- **Required Information**:
  - `revenue_data_by_region_segment`
  - `exchange_rates`

### Step 2: Revenue Trend Analysis
#### Action 1
- **Type**: FinancialCalculation
- **Task**: Calculate year-over-year and quarter-over-quarter revenue growth rates for each region and segment.
- **Required Information**:
  - `revenue_data_by_region_segment`

### Step 3: Segment Contribution Analysis
#### Action 1
- **Type**: FinancialCalculation
- **Task**: Calculate the percentage contribution of each segment to total revenue for each year and quarter.
- **Required Information**:
  - `revenue_data_by_region_segment`

### Step 4: Regional Revenue Analysis
#### Action 1
- **Type**: FinancialCalculation
- **Task**: Calculate the percentage contribution of each region to total revenue for each year and quarter.
- **Required Information**:
  - `revenue_data_by_region_segment`

### Step 5: Qualitative Insights
#### Action 1
- **Type**: TextAnalysis
- **Task**: Analyze Item 1 (Business) and Item 7 (MD&A) to gain qualitative insights into the drivers of revenue growth or decline in different regions and segments.
- **Required Information**:
  - `segment_description`
  - `geographic_distribution`

### Step 6: Result Formatting
#### Action 1
- **Type**: ResultFormatting
- **Task**: Present the findings in a clear and concise report, including tables, charts, and graphs to visualize revenue distribution, growth trends, and segment contributions. Include qualitative insights from the text analysis.
- **Required Information**:
  - `revenue_data_by_region_segment`
  - `segment_description`
  - `geographic_distribution`
