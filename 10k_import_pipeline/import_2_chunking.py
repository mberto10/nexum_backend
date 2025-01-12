import re
import json
from typing import List, Dict, Optional, Tuple, Any
from datetime import datetime
import os

# If we want to limit chunk size (approximate character-based threshold)
DEFAULT_MAX_CHUNK_SIZE = 300

# Regex pattern for matching Table of Contents heading (case insensitive)
RE_TABLE_OF_CONTENTS = re.compile(r"(?:TABLE\s+OF\s+CONTENTS|INDEX)", re.IGNORECASE)

# Regex for identifying lines that might be markdown headings: #, ##, ###, ...
RE_SUBHEADING = re.compile(r"^#+\s+(.*)$")

# Regex for identifying part headers (PART I, PART II, etc.)
RE_PART_HEADER = re.compile(r"^(?:#\s*)?PART\s+[IVX]+", re.IGNORECASE)

# Regex pattern for top-level Item headings: e.g. "Item 1.", "Item 1A."
RE_ITEM_HEADING = re.compile(r"(?i)^(?:#\s*)?(?:Item\s*(\d+[A-Za-z]?)\.?)\s*(.*)$")

# Standard 10-K Item headings
STANDARD_10K_HEADINGS = [
    "Item 1. Business",
    "Item 1A. Risk Factors",
    "Item 1B. Unresolved Staff Comments",
    "Item 1C. Cybersecurity",
    "Item 2. Properties",
    "Item 3. Legal Proceedings",
    "Item 4. Mine Safety Disclosures",
    "Item 5. Market for Registrant's Common Equity, Related Stockholder Matters and Issuer Purchases of Equity Securities",
    "Item 6. [Reserved]",
    "Item 7. Management's Discussion and Analysis of Financial Condition and Results of Operations",
    "Item 7A. Quantitative and Qualitative Disclosures About Market Risk",
    "Item 8. Financial Statements and Supplementary Data",
    "Item 9. Changes in and Disagreements with Accountants on Accounting and Financial Disclosure",
    "Item 9A. Controls and Procedures",
    "Item 9B. Other Information",
    "Item 9C. Disclosure Regarding Foreign Jurisdictions that Prevent Inspections",
    "Item 10. Directors, Executive Officers and Corporate Governance",
    "Item 11. Executive Compensation",
    "Item 12. Security Ownership of Certain Beneficial Owners and Management and Related Stockholder Matters",
    "Item 13. Certain Relationships and Related Transactions, and Director Independence",
    "Item 14. Principal Accountant Fees and Services",
    "Item 15. Exhibits, Financial Statement Schedules",
    "Item 16. Form 10-K Summary"
]

# Regex pattern to detect tables. We try to capture blocks of lines starting with "|"
RE_TABLE_LINE = re.compile(r"^\|.*\|$")

def extract_document_metadata(text: str) -> Dict[str, str]:
    """
    Extract some metadata from the document header.
    We'll guess the company_name from a line starting with '#' that is not Firecrawl or Analysis, etc.
    We'll also check for a "Document Type:" line if present.
    """
    lines = text.split("\n")
    metadata = {
        "company_name": "Unknown",
        "document_type": "Unknown"
    }
    for i, line in enumerate(lines[:40]):
        tline = line.strip()
        if tline.startswith("# ") and "Firecrawl" not in tline and "Analysis" not in tline:
            # For now, take the first occurrence as the Company Name.
            metadata["company_name"] = tline.replace("#", "").strip()
        elif "Document Type:" in tline:
            # e.g. "Document Type: Form 10-K annual report"
            doc_type_part = tline.split("Document Type:", 1)[1].strip()
            metadata["document_type"] = doc_type_part
    return metadata

def is_likely_toc_entry(line: str) -> bool:
    """
    Check if a line looks like a TOC entry (item heading followed by a page number).
    """
    line = line.strip()
    # Check if line ends with a number after some whitespace
    if re.search(r'\s+\d+$', line):
        # Check if it starts with an item heading
        item_info = detect_item_heading(line)
        if item_info and item_info['full_heading'] in STANDARD_10K_HEADINGS:
            return True
    return False

def find_start_of_content(text: str) -> int:
    """
    Find where the actual content starts by:
    1. Looking for dense standard item headings (indicating TOC)
    2. Finding either Item 1. Business or Forward-Looking Statements
    Returns the index where content should start.
    """
    lines = text.split('\n')
    
    # Find first non-XBRL line
    start_idx = 0
    for i, line in enumerate(lines):
        line = line.strip()
        if line == "---":
            start_idx = i + 1
            break
        if not line or "http://" in line or "Member" in line:
            continue
        start_idx = i
        break
    
    # Look for dense item headings in the first portion (indicating TOC)
    item_heading_positions = []
    for i in range(start_idx, min(start_idx + 200, len(lines))):
        line = lines[i].strip()
        item_info = detect_item_heading(line)
        if item_info and item_info['full_heading'] in STANDARD_10K_HEADINGS:
            item_heading_positions.append(i)
            # If we find at least 5 item headings within 50 lines, it's likely the TOC
            if len(item_heading_positions) >= 5 and item_heading_positions[-1] - item_heading_positions[0] <= 50:
                # Found TOC, now look for start of content
                for j in range(i + 1, len(lines)):
                    line = lines[j].strip()
                    # Check for Forward-Looking Statements
                    if line.lower() == "# forward-looking statements":
                        return j
                    # Check for real Item 1. Business (not just TOC entry)
                    item_info = detect_item_heading(line)
                    if (item_info and 
                        item_info['full_heading'] == "Item 1. Business" and 
                        len(line.split()) > 3):  # More than just "Item 1. Business"
                        return j
    
    # If we didn't find TOC or content start, return original start
    return start_idx

def normalize_text(text: str) -> str:
    """
    Normalize text by:
    1. Converting to lowercase
    2. Replacing various apostrophe types with a standard one
    3. Removing extra whitespace
    """
    text = text.lower()
    # Replace various apostrophe types with a standard one
    text = re.sub(r"['`'']", "'", text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def detect_item_heading(line: str) -> Optional[Dict[str, str]]:
    """
    If line matches 'Item X. [title]', parse it out.
    Returns dictionary with item_number, item_title, full_heading if matched.
    More flexible with formatting but still reliable.
    """
    # Remove any markdown heading prefix for matching
    clean_line = re.sub(r'^#+\s*', '', line.strip())
    
    # Basic pattern to match "Item X." at start (case insensitive)
    m = re.match(r'(?i)item\s+(\d+[A-Za-z]?)\.?\s*(.*)', clean_line)
    if not m:
        return None

    # group(1) is the item number, group(2) is the item title
    item_number = m.group(1).upper().strip()
    item_title = m.group(2).strip()
    
    # Find matching standard heading by normalizing both strings
    normalized_title = normalize_text(item_title)
    
    # First try exact match with standard headings
    standard_heading = None
    for heading in STANDARD_10K_HEADINGS:
        if f"Item {item_number}." in heading:
            standard_heading = heading
            break
    
    if standard_heading:
        # Use the standard heading's title
        item_title = standard_heading.split(".", 1)[1].strip()
    else:
        # If no exact match but we have a valid item number, use the standard heading
        for heading in STANDARD_10K_HEADINGS:
            if f"Item {item_number}." in heading:
                item_title = heading.split(".", 1)[1].strip()
                break
    
    full_heading = f"Item {item_number}. {item_title}".strip()
    
    # Additional validation: if this is meant to be a standard item heading
    # but doesn't match our standard list exactly, it might be a false positive
    if item_number.isdigit() or (len(item_number) > 1 and item_number[:-1].isdigit()):
        if not any(h.startswith(f"Item {item_number}.") for h in STANDARD_10K_HEADINGS):
            return None
    
    return {
        "item_number": item_number,
        "item_title": item_title,
        "full_heading": full_heading
    }

def detect_subheading(line: str) -> Optional[str]:
    """
    If line matches a sub-heading in markdown (#, ##, etc.), return the text.
    Otherwise return None.
    We'll exclude lines that are empty or should be ignored based on our ignore rules.
    """
    m = RE_SUBHEADING.match(line)
    if not m:
        return None
    heading_text = m.group(1).strip()
    
    # First check if this is a standard item heading or financial statement
    item_info = detect_item_heading(heading_text)
    if item_info:
        if item_info['item_number'] == "8":
            # For financial statements, use the heading text as the subheading
            return heading_text
        elif item_info['full_heading'] in STANDARD_10K_HEADINGS:
            return None  # Never treat standard item headings as subheadings
        
    # Special handling for financial statement sections
    financial_statement_patterns = [
        r'(?i)consolidated\s+statements?\s+of\s+(?:income|operations|comprehensive\s+income|financial\s+position|cash\s+flows|shareholders\'\s+equity)',
        r'(?i)consolidated\s+balance\s+sheets?',
        r'(?i)report\s+of\s+independent\s+registered\s+public\s+accounting\s+firm',
        r'(?i)notes\s+to\s+(?:the\s+)?consolidated\s+financial\s+statements',
        r'(?i)opinions\s+on\s+the\s+financial\s+statements',
        r'(?i)basis\s+for\s+opinions',
        r'(?i)critical\s+audit\s+matters'
    ]
    
    # Check if this is a financial statement heading
    for pattern in financial_statement_patterns:
        if re.search(pattern, heading_text, re.IGNORECASE):
            return heading_text
            
    # Use our comprehensive ignore rules
    if should_ignore_heading(heading_text):
        return None
        
    return heading_text

def is_table_line(line: str) -> bool:
    """
    Check if the line is a typical table format line:
    starts with '|' and ends with '|', or at least has '|---|'.
    We'll rely on the simpler pattern RE_TABLE_LINE here.
    """
    return bool(RE_TABLE_LINE.match(line.strip()))

def finalize_chunk_text_and_determine_type(text_lines: List[str]) -> Tuple[str, str]:
    """
    Given the chunk text lines, decide if it's 'table', 'text', or 'mix'.
    Return (joined_text, chunk_type).
    If all lines are table lines, type=table.
    If all lines are non-table lines, type=text.
    Else mix.
    """
    # Filter out empty lines for table detection logic
    non_empty = [ln for ln in text_lines if ln.strip()]
    if not non_empty:
        # it's basically empty, we'll treat it as text
        return ("\n".join(text_lines).strip(), "text")

    has_table = False
    has_text = False
    for ln in non_empty:
        if is_table_line(ln):
            has_table = True
        else:
            has_text = True
        if has_table and has_text:
            return ("\n".join(text_lines).strip(), "mix")
    # if we get here, it's all text or all table
    if has_table and not has_text:
        return ("\n".join(text_lines).strip(), "table")
    return ("\n".join(text_lines).strip(), "text")

def detect_standard_item_heading(line: str) -> Optional[str]:
    """
    Detect if a line is a standard 10-K Item heading.
    Returns the standardized heading if found, None otherwise.
    """
    print(f"Checking line: {repr(line)}")  # Debug
    
    # Only match lines that start with exactly "# Item "
    if not line.startswith("# Item "):
        print("  Not starting with '# Item '")  # Debug
        return None
        
    # Remove the "# " prefix
    line = line[2:].strip()
    print(f"  After prefix removal: {repr(line)}")  # Debug
    
    # Check if this exact heading is in our standard list
    if line in STANDARD_10K_HEADINGS:
        print(f"  Found match: {line}")  # Debug
        return line
            
    print("  No match in standard headings")  # Debug
    return None

def chunkify_by_items(text: str, toc_item_headings: List[str] = None) -> List[Dict[str, str]]:
    """
    Split text into chunks based on Item headings.
    Each chunk should start with a standard 10-K Item heading.
    """
    chunks = []
    lines = text.split("\n")
    current_chunk_lines = []
    current_item_heading = None
    found_forward_looking = False
    in_toc = True  # Start assuming we're in TOC
    
    # Initialize with first TOC item if available
    first_toc_item = toc_item_headings[0] if toc_item_headings and len(toc_item_headings) > 0 else None
    
    for i, line in enumerate(lines):
        line_strip = line.strip()
        
        # Check for Forward-Looking Statements
        if line_strip.lower() == "# forward-looking statements":
            found_forward_looking = True
            # Save any previous content as TOC if we're still in TOC mode
            if in_toc and current_chunk_lines:
                chunks.append({
                    "heading": "Table of Contents",
                    "text": "\n".join(current_chunk_lines).strip()
                })
                current_chunk_lines = []
                in_toc = False
            current_item_heading = "Item 1. Business"
            current_chunk_lines.append(line)
            continue
        
        # Check if this is a new Item heading
        item_heading_info = detect_item_heading(line_strip)
        
        if item_heading_info and item_heading_info['full_heading'] in STANDARD_10K_HEADINGS:
            # If this is a real item heading (not just TOC entry)
            if len(line_strip.split()) > 3 and not is_likely_toc_entry(line_strip):
                # If we're still in TOC mode, save TOC first
                if in_toc and current_chunk_lines:
                    chunks.append({
                        "heading": "Table of Contents",
                        "text": "\n".join(current_chunk_lines).strip()
                    })
                    current_chunk_lines = []
                    in_toc = False
                # If we have a previous non-TOC chunk, save it
                elif not in_toc and current_chunk_lines:
                    chunks.append({
                        "heading": current_item_heading or first_toc_item or "Table of Contents",
                        "text": "\n".join(current_chunk_lines).strip()
                    })
                    current_chunk_lines = []
                
                # Start new chunk
                current_chunk_lines = [line]
                current_item_heading = item_heading_info["full_heading"]
                found_forward_looking = False  # Reset when we hit a new item
            else:
                # This is a TOC entry, just add it to current chunk
                current_chunk_lines.append(line)
        else:
            # If we're after Forward-Looking Statements but before next item heading
            if found_forward_looking and not current_item_heading:
                current_item_heading = "Item 1. Business"
            
            # Add to current chunk
            current_chunk_lines.append(line)
    
    # Don't forget the last chunk
    if current_chunk_lines:
        chunks.append({
            "heading": current_item_heading or first_toc_item or "Table of Contents",
            "text": "\n".join(current_chunk_lines).strip()
        })
    
    return chunks

def should_ignore_heading(heading: str) -> bool:
    """
    Determine if a heading should be ignored for chunking purposes.
    """
    if not heading or not heading.strip():
        return True
        
    # Store original heading for case-sensitive checks
    original_heading = heading.strip()
    
    # Remove any markdown heading markers and clean the text
    heading = re.sub(r'^#+\s*', '', original_heading.strip()).lower()
    
    # Never ignore certain important financial statement headings
    financial_statement_patterns = [
        r'(?i)consolidated\s+statements?\s+of\s+(?:income|operations|comprehensive\s+income|financial\s+position|cash\s+flows|shareholders\'\s+equity)',
        r'(?i)report\s+of\s+independent\s+registered\s+public\s+accounting\s+firm',
        r'(?i)notes\s+to\s+(?:the\s+)?consolidated\s+financial\s+statements',
        r'(?i)opinions\s+on\s+the\s+financial\s+statements',
        r'(?i)basis\s+for\s+opinions',
        r'(?i)critical\s+audit\s+matters'
    ]
    
    for pattern in financial_statement_patterns:
        if re.search(pattern, heading, re.IGNORECASE):
            return False  # Don't ignore these important headings
    
    # Ignore "None" as a heading
    if heading == "none":
        return True
    
    # Ignore any variation of "Table of Contents" or "Index"
    if RE_TABLE_OF_CONTENTS.search(heading):
        return True
    
    # Ignore PART headings in any format (e.g., "PART I", "Part II", "PART 1", etc.)
    if re.match(r'^part\s*(?:[IVXivx]+|\d+)(?:\s|$)', heading, re.IGNORECASE):
        return True
    
    # Ignore if it's a standard item heading (these should be handled by item heading logic)
    if heading.startswith('item ') and any(h.lower().startswith(heading) for h in STANDARD_10K_HEADINGS):
        return True
        
    # Ignore if it's just a repetition of a standard item heading
    if re.match(r'^item\s+\d+[A-Za-z]?\.?\s+', heading):
        item_match = re.match(r'^item\s+(\d+[A-Za-z]?)\.?', heading)
        if item_match:
            item_num = item_match.group(1)
            for std_heading in STANDARD_10K_HEADINGS:
                std_heading_lower = std_heading.lower()
                if (std_heading_lower.startswith(f'item {item_num.lower()}') and 
                    original_heading.isupper() and 
                    heading.replace(' ', '') in std_heading_lower.replace(' ', '')):
                    return True
    
    # Ignore financial metadata patterns
    financial_metadata_patterns = [
        r'^\(in\s+(?:millions|thousands|billions)\)',
        r'^\(in\s+(?:millions|thousands|billions),\s+except.*\)',
        r'^see\s+accompanying\s+notes',
        r'^see\s+notes?\s+to',
        r'^weighted\s+average',
        r'^year[s]?\s+ended',
        r'^as\s+of\s+(?:and\s+for)?',
        r'^for\s+the\s+(?:three|six|nine|twelve)\s+months?\s+ended',
        r'^for\s+the\s+years?\s+ended',
        r'^for\s+the\s+periods?\s+(?:ended|presented)',
        r'^consolidated\s+balance\s+sheets?\s+data',
        r'^selected\s+(?:consolidated\s+)?financial\s+data',
        r'^supplementary\s+financial\s+information'
    ]
    
    if any(re.match(pattern, heading, re.IGNORECASE) for pattern in financial_metadata_patterns):
        return True
    
    # Ignore date patterns
    date_patterns = [
        r'^(?:january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2},?\s+\d{4}$',
        r'^(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\s+\d{1,2},?\s+\d{4}$',
        r'^\d{4}$',
        r'^(?:fiscal\s+year|fy)\s+\d{4}$'
    ]
    
    if any(re.match(pattern, heading, re.IGNORECASE) for pattern in date_patterns):
        return True
        
    # Ignore headings that start with specific phrases
    ignore_starts = [
        'the following table',
        'the following tables',
        'notes to',
        'note:',
        'notes:',
        'continued from',
        'continued on',
        'amount',
        'amounts',
        'reported as',
        'current portion',
        'balance at',
        'balance as of',
        'year ended',
        'period ended',
        'none',
        'for example',
        'such as',
        'including',
        'this section',
        'discussion of'
    ]
    
    for start in ignore_starts:
        if heading.startswith(start):
            return True
            
    # Ignore if it's just parenthetical content
    if heading.startswith('(') and heading.endswith(')'):
        return True
        
    # Ignore if it's just a separator
    if set(heading).issubset({'-', '_', '=', '*', '.'}):
        return True
        
    # Ignore headings that end with a colon
    if heading.endswith(':'):
        return True
        
    return False

def split_by_subheadings(text: str) -> List[Dict[str, str]]:
    """Split text into chunks based on markdown headings that are not TOC or Part headers."""
    chunks = []
    current_lines = []
    current_subheading = None
    in_table = False
    table_buffer = []
    
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for table start/end
        if line.startswith('|'):
            in_table = True
            table_buffer.append(lines[i])
        elif in_table and not line:
            # Empty line after table - check if table is complete
            if i + 1 < len(lines) and not lines[i + 1].strip().startswith('|'):
                in_table = False
                current_lines.extend(table_buffer)
                table_buffer = []
            else:
                table_buffer.append(lines[i])
        elif in_table:
            table_buffer.append(lines[i])
        # Handle headings
        elif line.startswith('#'):
            heading_text = line.strip('#').strip()
            if not should_ignore_heading(heading_text):
                # If we have content from a previous subheading, save it
                if current_lines or table_buffer:
                    # Include any buffered table content
                    if table_buffer:
                        current_lines.extend(table_buffer)
                        table_buffer = []
                        in_table = False
                    
                    chunks.append({
                        "subheading": current_subheading,
                        "text": '\n'.join(current_lines).strip()
                    })
                    current_lines = []
                
                # Set the new subheading
                current_subheading = heading_text
            else:
                # If it's an ignored heading, treat it as regular content
                current_lines.append(lines[i])
        else:
            # Regular content line
            current_lines.append(lines[i])
        i += 1
    
    # Don't forget the last chunk and any remaining table content
    if table_buffer:
        current_lines.extend(table_buffer)
    if current_lines:
        chunks.append({
            "subheading": current_subheading,
            "text": '\n'.join(current_lines).strip()
        })
    
    return chunks

def save_chunks_to_file(chunks: List[Dict[str, Any]], output_file: str):
    """Save chunks to a file in a readable format."""
    # Create output directory if needed
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Write chunks to file
    with open(output_file, "w") as f:
        f.write("================================================================================\n")
        f.write(f"TOTAL CHUNKS: {len(chunks)}\n")
        f.write("================================================================================\n\n")
        
        for i, chunk in enumerate(chunks, 1):
            f.write(f"\n######################################## CHUNK {i} ########################################\n\n")
            
            # Write metadata
            f.write("METADATA:\n")
            f.write("--------------------\n")
            f.write(f"Item Heading: {chunk['heading']}\n")
            f.write(f"Subheading: {chunk['subheading']}\n")
            
            # Write content
            f.write("\nCONTENT:\n")
            f.write("--------------------\n")
            f.write(chunk['text'])
            f.write("\n\n================================================================================\n")

def assign_missing_item_headings(chunks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Post-process chunks to assign missing item headings based on the next known item heading.
    """
    # First find the index of each standard heading in our ordered list
    heading_indices = {heading: i for i, heading in enumerate(STANDARD_10K_HEADINGS)}
    
    # Find the first chunk with a valid item heading
    next_heading = None
    next_heading_index = None
    
    # Scan forward to find the next valid item heading
    for i in range(len(chunks)):
        if chunks[i]['heading'] in heading_indices:
            next_heading = chunks[i]['heading']
            next_heading_index = i
            break
    
    # If we found a valid next heading, assign missing headings
    if next_heading and next_heading_index is not None:
        # Get the index of this heading in our standard list
        next_idx = heading_indices[next_heading]
        if next_idx > 0:
            # The previous heading in our standard list should be assigned to all
            # chunks between TOC and this heading
            prev_heading = STANDARD_10K_HEADINGS[next_idx - 1]
            for i in range(1, next_heading_index):  # Start from 1 to skip TOC
                if not chunks[i]['heading']:  # Only assign if heading is missing
                    chunks[i]['heading'] = prev_heading
    
    return chunks

def is_table_row(line: str) -> bool:
    """Check if a line is part of a markdown table."""
    return bool(line.strip().startswith('|') and line.strip().endswith('|'))

def count_tokens(text: str) -> int:
    """
    Estimate the number of tokens in a text.
    This is a simple approximation - actual token count may vary with the tokenizer.
    """
    # Simple approximation: split on whitespace and punctuation
    words = text.split()
    # Assume average of 1.3 tokens per word for multilingual text
    return int(len(words) * 1.3)

def split_chunk_preserve_tables(chunk: Dict[str, str], max_tokens: int = 300) -> List[Dict[str, str]]:
    """
    Split a chunk if it exceeds max_tokens while preserving table structures.
    Returns a list of new chunks, each with the same heading/subheading as the original.
    Prefers splitting at paragraph breaks and avoids splitting after colons.
    """
    # Skip empty chunks
    if not chunk['text'].strip():
        return []
        
    if count_tokens(chunk['text']) <= max_tokens:
        return [chunk]
    
    new_chunks = []
    paragraphs = chunk['text'].split('\n\n')
    current_paragraphs = []
    current_tokens = 0
    in_table = False
    table_lines = []
    
    i = 0
    while i < len(paragraphs):
        paragraph = paragraphs[i]
        
        # Skip empty paragraphs or separator-only paragraphs
        if not paragraph.strip() or paragraph.strip() == '---':
            i += 1
            continue
            
        # Check if this paragraph contains a table
        lines = paragraph.split('\n')
        if any(is_table_row(line) for line in lines):
            # Handle table paragraph
            table_tokens = count_tokens(paragraph)
            if current_tokens + table_tokens > max_tokens and current_paragraphs:
                # Create new chunk with accumulated paragraphs
                new_chunks.append({
                    'heading': chunk.get('heading'),
                    'subheading': chunk.get('subheading'),
                    'text': '\n\n'.join(current_paragraphs).strip()
                })
                current_paragraphs = []
                current_tokens = 0
            current_paragraphs.append(paragraph)
            current_tokens += table_tokens
        else:
            # Regular paragraph
            paragraph_tokens = count_tokens(paragraph)
            
            # Check if this paragraph ends with a colon
            ends_with_colon = paragraph.rstrip().endswith(':')
            
            # If adding this paragraph would exceed the limit
            if current_tokens + paragraph_tokens > max_tokens:
                if current_paragraphs:
                    # Don't split if last paragraph ended with a colon
                    last_para = current_paragraphs[-1] if current_paragraphs else ""
                    if last_para.rstrip().endswith(':'):
                        # Try to include this paragraph even if it exceeds the limit
                        current_paragraphs.append(paragraph)
                    else:
                        # Create new chunk with accumulated paragraphs
                        new_chunks.append({
                            'heading': chunk.get('heading'),
                            'subheading': chunk.get('subheading'),
                            'text': '\n\n'.join(current_paragraphs).strip()
                        })
                        current_paragraphs = [paragraph]
                        current_tokens = paragraph_tokens
                else:
                    # If a single paragraph is too large, we need to split it by sentences
                    sentences = re.split(r'(?<=[.!?])\s+', paragraph)
                    current_sentence_group = []
                    current_sentence_tokens = 0
                    
                    for j, sentence in enumerate(sentences):
                        sentence_tokens = count_tokens(sentence)
                        
                        # Check if this sentence ends with a colon
                        ends_with_colon = sentence.rstrip().endswith(':')
                        
                        if current_sentence_tokens + sentence_tokens > max_tokens and current_sentence_group:
                            # Don't split if last sentence ended with a colon
                            if not current_sentence_group[-1].rstrip().endswith(':'):
                                new_chunks.append({
                                    'heading': chunk.get('heading'),
                                    'subheading': chunk.get('subheading'),
                                    'text': ' '.join(current_sentence_group).strip()
                                })
                                current_sentence_group = []
                                current_sentence_tokens = 0
                        current_sentence_group.append(sentence)
                        current_sentence_tokens += sentence_tokens
                    
                    if current_sentence_group:
                        current_paragraphs = [' '.join(current_sentence_group)]
                        current_tokens = current_sentence_tokens
            else:
                current_paragraphs.append(paragraph)
                current_tokens += paragraph_tokens
                
                # If this paragraph ends with a colon, try to include the next paragraph
                if ends_with_colon and i + 1 < len(paragraphs):
                    next_paragraph = paragraphs[i + 1]
                    next_tokens = count_tokens(next_paragraph)
                    if current_tokens + next_tokens <= max_tokens * 1.2:  # Allow slight overflow
                        current_paragraphs.append(next_paragraph)
                        current_tokens += next_tokens
                        i += 1  # Skip the next paragraph since we included it
        
        i += 1
    
    # Don't forget the last chunk
    if current_paragraphs:
        new_chunks.append({
            'heading': chunk.get('heading'),
            'subheading': chunk.get('subheading'),
            'text': '\n\n'.join(current_paragraphs).strip()
        })
    
    # Filter out any empty chunks
    return [chunk for chunk in new_chunks if chunk['text'].strip()]

def is_related_table_content(text: str) -> bool:
    """
    Determine if a text block is related to table content by checking for:
    - Table rows
    - Financial statement line items
    - Numeric data
    - Table metadata
    """
    # Skip empty text
    if not text.strip():
        return False
        
    lines = text.strip().split('\n')
    
    # Quick check for obvious table markers
    has_table_marker = False
    table_row_count = 0
    header_separator_found = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Count table rows and check for header separator
        if line.startswith('|') and line.endswith('|'):
            table_row_count += 1
            has_table_marker = True
            if re.match(r'\|[\s\-:]+\|', line):
                header_separator_found = True
                
    # If we have a well-formed table (header, separator, and data rows)
    if has_table_marker and header_separator_found and table_row_count >= 3:
        return True
        
    # Check for financial statement patterns
    financial_patterns = [
        # Currency amounts
        r'\$\s*\d+(?:,\d{3})*(?:\.\d+)?',
        # Parenthetical amounts
        r'\(\$?\s*\d+(?:,\d{3})*(?:\.\d+)?\)',
        # Common financial statement headers
        r'(?i)^(?:assets|liabilities|equity|revenue|expenses|income|cash flows)',
        # Date ranges
        r'(?i)(?:year|quarter|period)s?\s+ended?\s+(?:january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2},\s+\d{4}',
        # Notes references
        r'\([0-9A-Z]\)',
        # Financial metrics
        r'(?i)(?:total|net|gross|operating|consolidated)\s+(?:revenue|income|loss|assets|liabilities|equity|earnings)'
    ]
    
    # Count how many lines match financial patterns
    financial_line_count = 0
    for line in lines:
        if any(re.search(pattern, line) for pattern in financial_patterns):
            financial_line_count += 1
            
    # If more than 30% of non-empty lines contain financial patterns
    non_empty_lines = len([l for l in lines if l.strip()])
    if non_empty_lines > 0 and financial_line_count / non_empty_lines > 0.3:
        return True
        
    return False

def should_merge_table_chunks(current_chunk: Dict[str, str], next_chunk: Dict[str, str]) -> bool:
    """
    Determine if two chunks should be merged based on their content and context.
    """
    # If they don't have the same item heading, don't merge
    if current_chunk.get('heading') != next_chunk.get('heading'):
        return False
        
    # If either chunk is empty, don't merge
    if not current_chunk.get('text').strip() or not next_chunk.get('text').strip():
        return False
        
    current_text = current_chunk['text']
    next_text = next_chunk['text']
    
    # Check if both chunks contain table-related content
    current_is_table = is_related_table_content(current_text)
    next_is_table = is_related_table_content(next_text)
    
    # If both are table-related, check if they're part of the same context
    if current_is_table and next_is_table:
        # If they share similar column headers, they're likely related
        current_headers = extract_table_headers(current_text)
        next_headers = extract_table_headers(next_text)
        if current_headers and next_headers and headers_are_similar(current_headers, next_headers):
            return True
            
        # If they're close together and have similar structure
        if len(current_text.split('\n')) < 20 and len(next_text.split('\n')) < 20:
            return True
            
        # If one appears to be a continuation of the other
        if is_table_continuation(current_text, next_text):
            return True
    
    # If one is a small chunk that looks like a table header or footer
    if len(current_text.split('\n')) < 4 or len(next_text.split('\n')) < 4:
        # Check if it contains table-related metadata
        metadata_patterns = [
            r'\([Ii]n (?:thousands|millions|billions)',
            r'[Nn]otes? to',
            r'[Cc]ontinued',
            r'[Yy]ear[s]? [Ee]nded',
            r'[Aa]s of',
            r'[Ss]ee accompanying notes'
        ]
        small_chunk = current_text if len(current_text.split('\n')) < 4 else next_text
        if any(re.search(pattern, small_chunk) for pattern in metadata_patterns):
            return True
    
    return False

def extract_table_headers(text: str) -> List[str]:
    """Extract column headers from a markdown table."""
    lines = text.strip().split('\n')
    for i, line in enumerate(lines):
        if line.startswith('|') and line.endswith('|'):
            headers = [col.strip() for col in line.strip('|').split('|')]
            # Check next line for separator
            if i + 1 < len(lines) and re.match(r'\|[\s\-:]+\|', lines[i + 1]):
                return headers
    return []

def headers_are_similar(headers1: List[str], headers2: List[str]) -> bool:
    """Check if two sets of table headers are similar."""
    if not headers1 or not headers2:
        return False
        
    # Normalize headers
    def normalize(headers):
        return [re.sub(r'\s+', ' ', h.lower().strip()) for h in headers if h.strip()]
        
    h1 = normalize(headers1)
    h2 = normalize(headers2)
    
    # If they're exactly the same
    if h1 == h2:
        return True
        
    # If one is a subset of the other
    if all(h in h1 for h in h2) or all(h in h2 for h in h1):
        return True
        
    # If they share significant overlap
    common = set(h1) & set(h2)
    return len(common) >= min(len(h1), len(h2)) * 0.5

def is_table_continuation(text1: str, text2: str) -> bool:
    """Check if text2 appears to be a continuation of text1's table."""
    lines1 = text1.strip().split('\n')
    lines2 = text2.strip().split('\n')
    
    # If either is empty, not a continuation
    if not lines1 or not lines2:
        return False
        
    # Check if the last line of text1 and first line of text2 have similar structure
    last_line = lines1[-1].strip()
    first_line = lines2[0].strip()
    
    if last_line.startswith('|') and first_line.startswith('|'):
        # Count pipes to check if they have the same number of columns
        pipes1 = last_line.count('|')
        pipes2 = first_line.count('|')
        return pipes1 == pipes2
        
    return False

def merge_related_chunks(chunks: List[Dict[str, str]], max_tokens: int = 300, min_tokens: int = 100) -> List[Dict[str, str]]:
    """
    Merge chunks that are part of the same table context while respecting the token limit.
    Also ensures that small chunks (below min_tokens) are merged with previous chunks if they share the same Item heading.
    """
    if not chunks:
        return chunks
        
    merged_chunks = []
    current_chunk = chunks[0]
    
    for next_chunk in chunks[1:]:
        should_merge = False
        
        # Check if chunks share the same item heading
        same_heading = current_chunk.get('heading') == next_chunk.get('heading')
        
        # Calculate token counts
        current_tokens = count_tokens(current_chunk['text'])
        next_tokens = count_tokens(next_chunk['text'])
        combined_tokens = count_tokens(current_chunk['text'] + '\n' + next_chunk['text'])
        
        # Determine if we should merge based on various conditions
        if same_heading:
            # Always merge if either chunk is very small and combined is within limit
            if (current_tokens < min_tokens or next_tokens < min_tokens) and combined_tokens <= max_tokens:
                should_merge = True
            # Merge if they're related table content
            elif should_merge_table_chunks(current_chunk, next_chunk) and combined_tokens <= max_tokens:
                should_merge = True
            # Merge if they're both small and sequential
            elif current_tokens < min_tokens and next_tokens < min_tokens and combined_tokens <= max_tokens:
                should_merge = True
        
        if should_merge:
            # Merge the chunks
            current_chunk['text'] = current_chunk['text'] + '\n' + next_chunk['text']
            # Keep the first meaningful subheading if it exists
            if (not current_chunk.get('subheading') or 
                current_chunk.get('subheading', '').lower() in ['none', 'no heading']) and next_chunk.get('subheading'):
                current_chunk['subheading'] = next_chunk['subheading']
        else:
            # If we're not merging and the current chunk is too small,
            # try to merge it with the previous chunk in merged_chunks
            if current_tokens < min_tokens and merged_chunks and current_chunk.get('heading') == merged_chunks[-1].get('heading'):
                prev_combined_tokens = count_tokens(merged_chunks[-1]['text'] + '\n' + current_chunk['text'])
                if prev_combined_tokens <= max_tokens:
                    merged_chunks[-1]['text'] = merged_chunks[-1]['text'] + '\n' + current_chunk['text']
                else:
                    merged_chunks.append(current_chunk)
            else:
                merged_chunks.append(current_chunk)
            current_chunk = next_chunk
    
    # Handle the last chunk
    if current_chunk:
        current_tokens = count_tokens(current_chunk['text'])
        if current_tokens < min_tokens and merged_chunks and current_chunk.get('heading') == merged_chunks[-1].get('heading'):
            # Try to merge with the previous chunk if they share the same heading
            prev_combined_tokens = count_tokens(merged_chunks[-1]['text'] + '\n' + current_chunk['text'])
            if prev_combined_tokens <= max_tokens:
                merged_chunks[-1]['text'] = merged_chunks[-1]['text'] + '\n' + current_chunk['text']
            else:
                merged_chunks.append(current_chunk)
        else:
            merged_chunks.append(current_chunk)
    
    return merged_chunks

def post_process_chunks(chunks: List[Dict[str, str]], max_tokens: int = 300) -> List[Dict[str, str]]:
    """
    Post-process chunks to ensure they don't exceed the token limit while preserving tables.
    Now also merges related table chunks while respecting the token limit.
    """
    # First split chunks that are too large
    processed_chunks = []
    for chunk in chunks:
        processed_chunks.extend(split_chunk_preserve_tables(chunk, max_tokens))
    
    # Then merge related table chunks while respecting the token limit
    processed_chunks = merge_related_chunks(processed_chunks, max_tokens)
    
    # Final verification that no chunk exceeds the limit
    final_chunks = []
    for chunk in processed_chunks:
        if count_tokens(chunk['text']) > max_tokens:
            # If a chunk somehow still exceeds the limit, split it again
            final_chunks.extend(split_chunk_preserve_tables(chunk, max_tokens))
        else:
            final_chunks.append(chunk)
    
    return final_chunks

def process_and_save_chunks(text: str, output_file: str = None) -> List[Dict[str, Any]]:
    """Process text into chunks and save to file if output_file is provided."""
    print(f"Total lines: {len(text.splitlines())}")
    
    # Find where content starts (after TOC)
    content_start_idx = find_start_of_content(text)
    lines = text.split('\n')
    content = '\n'.join(lines[content_start_idx:])
    
    # Process chunks
    chunks = []
    current_chunk_lines = []
    current_item_heading = None
    found_forward_looking = False
    
    for line in content.split('\n'):
        line_strip = line.strip()
        
        # Check for Forward-Looking Statements
        if line_strip.lower() == "# forward-looking statements":
            found_forward_looking = True
            if not current_item_heading:
                current_item_heading = "Item 1. Business"
        
        # Check if this is a new Item heading
        item_heading_info = detect_item_heading(line_strip)
        
        if item_heading_info and item_heading_info['full_heading'] in STANDARD_10K_HEADINGS:
            # If this is a real item heading (not just TOC entry)
            if len(line_strip.split()) > 3:
                # Save previous chunk if exists
                if current_chunk_lines:
                    chunks.append({
                        "heading": current_item_heading or "Item 1. Business",
                        "subheading": None,
                        "text": '\n'.join(current_chunk_lines).strip()
                    })
                    current_chunk_lines = []
                
                # Start new chunk
                current_chunk_lines = [line]
                current_item_heading = item_heading_info["full_heading"]
                found_forward_looking = False
            else:
                # This is a TOC entry, skip it
                continue
        else:
            # If we're after Forward-Looking Statements but before next item heading
            if found_forward_looking and not current_item_heading:
                current_item_heading = "Item 1. Business"
            
            # Add to current chunk
            current_chunk_lines.append(line)
    
    # Don't forget the last chunk
    if current_chunk_lines:
        chunks.append({
            "heading": current_item_heading or "Item 1. Business",
            "subheading": None,
            "text": '\n'.join(current_chunk_lines).strip()
        })
    
    # Split chunks by subheadings
    final_chunks = []
    for chunk in chunks:
        subheading_chunks = split_by_subheadings(chunk['text'])
        for subchunk in subheading_chunks:
            final_chunks.append({
                "heading": chunk['heading'],
                "subheading": subchunk['subheading'],
                "text": subchunk['text']
            })
    
    # Post-process to ensure chunks don't exceed token limit
    final_chunks = post_process_chunks(final_chunks)
    
    # Save to file if output file is provided
    if output_file:
        save_chunks_to_file(final_chunks, output_file)
        print(f"\nChunks also saved to file: {output_file}")
    
    return final_chunks

def get_sample_text():
    """
    Returns a sample 10-K text for testing the chunking functionality.
    """
    return '''
    LICE L. JOLLA|Corporate Vice President and Chief Accounting Officer (Principal Accounting Officer)|
'''

def print_chunks(chunks):
    """
    Print chunks in a clear, readable format to the console.
    """
    print("\n" + "="*80)
    print(f"TOTAL CHUNKS: {len(chunks)}")
    print("="*80 + "\n")

    for i, chunk in enumerate(chunks, 1):
        print(f"\n{'#'*40} CHUNK {i} {'#'*40}")
        print("\nMETADATA:")
        print("-"*20)
        metadata = chunk['metadata']
        print(f"Item Heading: {metadata['item_heading']}")
        print(f"Keywords: {', '.join(metadata['keywords']) if metadata['keywords'] else 'None'}")
        print(f"Type: {metadata['type']}")
        print(f"Company: {metadata['company']}")
        print(f"Document Type: {metadata['document_type']}")
        
        print("\nCONTENT:")
        print("-"*20)
        print(chunk["content"])
        print("\n" + "="*80 + "\n")

def test():
    """Run a test with sample data."""
    sample_text = get_sample_text()
    
    # Generate output filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join("chunking_results", f"10k_chunks_{timestamp}.md")
    
    # Process chunks and save to file
    chunks = process_and_save_chunks(sample_text, output_file)
    
    # Print some stats about the chunks
    print("\n================================================================================")
    print(f"TOTAL CHUNKS: {len(chunks)}")
    print("================================================================================\n")
    
    # Print metadata for each chunk
    for i, chunk in enumerate(chunks, 1):
        print(f"\n######################################## CHUNK {i} ########################################\n")
        print("METADATA:")
        print("--------------------")
        print(f"Item Heading: {chunk['heading']}")
        print(f"Subheading: {chunk['subheading']}")
        print("\nCONTENT:")
        print("--------------------")
        print(chunk['text'])
        print("\n================================================================================\n")

def main():
    import sys
    print("Starting main function...")
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Test with markdown file: python output_chunking.py <filename>.md")
        print("  Test with sample data:   python output_chunking.py --test")
        sys.exit(0)

    print(f"Arguments received: {sys.argv}")
    if sys.argv[1] == "--test":
        print("Running test mode...")
        test()
        return

    # Handle markdown file testing
    input_file = sys.argv[1]
    print(f"Processing input file: {input_file}")
    
    # Generate output filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join("chunking_results", f"{base_name}_chunks_{timestamp}.md")
    print(f"Output will be written to: {output_file}")
    
    # Read the input file
    try:
        with open(input_file, 'r') as f:
            content = f.read()
            print(f"Successfully read input file. Content length: {len(content)} characters")
    except Exception as e:
        print(f"Error reading input file: {e}")
        return
        
    # Process the content
    try:
        chunks = process_and_save_chunks(content, output_file)
        print(f"Successfully processed {len(chunks)} chunks")
    except Exception as e:
        print(f"Error processing chunks: {e}")
        return

if __name__ == "__main__":
    main()