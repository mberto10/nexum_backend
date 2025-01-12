from import_2_chunking import process_and_save_chunks
from datetime import datetime
import os

def test_chunking_on_file(input_file: str):
    """Test chunking logic on a specific markdown file."""
    print(f"\nTesting chunking on file: {input_file}")
    
    # Read the input file
    try:
        with open(input_file, 'r') as f:
            content = f.read()
            print(f"Successfully read input file. Content length: {len(content)} characters")
    except Exception as e:
        print(f"Error reading input file: {e}")
        return
    
    # Generate output filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join("chunking_results", f"{base_name}_chunks_{timestamp}.md")
    
    print(f"Output will be written to: {output_file}")
    
    # Process the content
    try:
        chunks = process_and_save_chunks(content, output_file)
        print(f"\nSuccessfully processed {len(chunks)} chunks")
        
        # Print first few chunks for inspection
        print("\nFirst few chunks for inspection:")
        for i, chunk in enumerate(chunks[:3], 1):
            print(f"\n{'='*80}")
            print(f"CHUNK {i}")
            print(f"{'='*80}")
            print("METADATA:")
            print(f"Item Heading: {chunk['heading']}")
            print(f"Subheading: {chunk['subheading']}")
            print("\nFirst 200 chars of content:")
            print(chunk['text'][:200] + "...")
            
    except Exception as e:
        print(f"Error processing chunks: {e}")
        import traceback
        traceback.print_exc()
        return

if __name__ == "__main__":
    # Test on NVIDIA parsed document
    test_chunking_on_file("parsed_results/NVDA_parsed_20250104_204819.md") 