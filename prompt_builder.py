import os
import argparse
from typing import List, Optional, Dict
from pathlib import Path
from datetime import datetime

def find_file_in_workspace(filename: str, start_path: str = None) -> Optional[str]:
    """
    Search for a file in the workspace and its subdirectories.
    Returns the full path if found, None otherwise.
    """
    if start_path is None:
        start_path = os.getcwd()

    # Convert filename to Path object for better path handling
    filename = Path(filename).name
    
    print(f"Searching for {filename}...")
    
    # Walk through directory tree
    for root, dirs, files in os.walk(start_path):
        if filename in files:
            full_path = os.path.join(root, filename)
            print(f"Found {filename} at: {full_path}")
            return full_path
            
    # If not found in current directory tree, try parent directory
    parent_dir = os.path.dirname(start_path)
    if parent_dir and parent_dir != start_path:
        return find_file_in_workspace(filename, parent_dir)
    
    print(f"Could not find {filename} in workspace")
    return None

def resolve_file_paths(files: List[str]) -> Dict[str, str]:
    """
    Resolve all file paths and return a dictionary mapping original paths to found paths.
    """
    resolved_paths = {}
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    for file_path in files:
        # First try direct path
        if os.path.exists(file_path):
            resolved_paths[file_path] = file_path
            continue
            
        # Then try relative to script location
        script_relative = os.path.join(script_dir, file_path)
        if os.path.exists(script_relative):
            resolved_paths[file_path] = script_relative
            continue
            
        # Finally, try to find it in workspace
        found_path = find_file_in_workspace(file_path)
        if found_path:
            resolved_paths[file_path] = found_path
            
    return resolved_paths

def read_file_content(file_path: str) -> str:
    """Read content from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Warning: Could not read file {file_path}: {e}")
        return ""

def read_notepad_content(notepad_name: str) -> str:
    """Read content from a notepad file."""
    try:
        # Try both .txt and .md extensions
        for ext in ['.txt', '.md']:
            notepad_path = notepad_name + ext
            found_path = find_file_in_workspace(notepad_path)
            if found_path:
                return read_file_content(found_path)
        
        print(f"Warning: Could not find notepad {notepad_name} with any supported extension")
        return ""
    except Exception as e:
        print(f"Warning: Could not read notepad {notepad_name}: {e}")
        return ""

def combine_content(files: List[str], notepads: List[str], output_file: str = None, format: str = "markdown") -> None:
    """Combine content from files and notepads into a single output file."""
    combined_content = []
    
    # Create o1_prompts directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "o1_prompts")
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate default output name if none provided
    if not output_file:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"prompt_{timestamp}"
    
    # If output_file doesn't have a directory path, put it in o1_prompts
    if not os.path.dirname(output_file):
        output_file = os.path.join(output_dir, output_file)
    
    print("\nStarting content combination process...")
    
    # Add prompt_builder.md to files list if not already present
    default_prompt = "prompt_builder.md"
    if default_prompt not in files:
        print(f"\nAutomatically adding {default_prompt} to the file list...")
        files = [default_prompt] + files
    
    print(f"\nProcessing files in order: {', '.join(files)}")
    
    # First resolve all file paths
    print("\nResolving file paths...")
    resolved_paths = resolve_file_paths(files)
    
    if not resolved_paths:
        print("Warning: No files were found to process!")
        return
    
    # Process default prompt first if found
    if default_prompt in resolved_paths:
        print(f"\nProcessing default prompt: {default_prompt}")
        content = read_file_content(resolved_paths[default_prompt])
        if content:
            print(f"Successfully read {default_prompt}")
            combined_content.append(f"<filepath>{default_prompt}</filepath>\n")
            combined_content.append(content)
            combined_content.append("\n---\n")
        del resolved_paths[default_prompt]
    
    # Process notepads
    if notepads:
        print("\nProcessing notepads...")
        for notepad in notepads:
            print(f"Reading notepad: {notepad}")
            content = read_notepad_content(notepad)
            if content:
                combined_content.append(content)
                combined_content.append("\n---\n")
    
    # Process remaining files
    if resolved_paths:
        print("\nProcessing remaining files...")
        for original_path, resolved_path in resolved_paths.items():
            print(f"Reading file: {original_path}")
            content = read_file_content(resolved_path)
            if content:
                combined_content.append(f"<filepath>{original_path}</filepath>\n")
                combined_content.append(content)
                combined_content.append("\n---\n")
    
    # Write combined content to output file
    output_extension = ".md" if format.lower() == "markdown" else ".txt"
    output_path = output_file if output_file.endswith(output_extension) else output_file + output_extension
    
    if not combined_content:
        print("\nWarning: No content was collected to write!")
        return
        
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(combined_content))
        print(f"\nSuccessfully created combined file: {output_path}")
        print(f"Total files processed: {len(files)}")
    except Exception as e:
        print(f"Error creating output file: {e}")

def main():
    parser = argparse.ArgumentParser(
        description='Combine content from files and notepads into a single file. Always includes prompt_builder.md if available.',
        usage='%(prog)s [files...] [-- notepad1 notepad2...]'
    )
    parser.add_argument('files', nargs='*', help='Additional files to combine')
    parser.add_argument('--', dest='notepads', nargs='*', help='List of notepads to combine', default=[])
    
    # Hide these options from the main help display since they're rarely used
    parser.add_argument('--output', help=argparse.SUPPRESS)
    parser.add_argument('--format', choices=['txt', 'markdown'], default='markdown', help=argparse.SUPPRESS)
    
    args = parser.parse_args()
    
    if not args.files and not args.notepads:
        print("Error: Please specify at least one file or notepad to combine")
        parser.print_help()
        return
    
    print(f"Current working directory: {os.getcwd()}")
    print(f"Script location: {os.path.dirname(os.path.abspath(__file__))}")
    combine_content(args.files, args.notepads, args.output, args.format)

if __name__ == "__main__":
    main() 