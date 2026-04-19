#!/usr/bin/python3

import sys
import os

def convert_tabs_to_spaces(filename):
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return

    output_lines = []
    
    with open(filename, 'r') as f:
        for line in f:
            # We only want to target leading tabs
            content = line.lstrip('\t')
            tab_count = len(line) - len(content)
            
            if tab_count > 0:
                # Replicating your step-process: 
                # Each tab is replaced by 8 spaces.
                # This preserves your 'alignment spaces' in the content.
                leading_spaces = ' ' * (tab_count * 8)
                output_lines.append(leading_spaces + content)
            else:
                output_lines.append(line)

    # Save to a temporary file for your review
    output_filename = filename + ".modernized"
    with open(output_filename, 'w') as f:
        f.writelines(output_lines)
    
    print(f"Processed {filename} -> {output_filename}")
    print(f"Tabs handled as 8-space blocks. Alignment preserved.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tab_peeler.py <file.java>")
    else:
        convert_tabs_to_spaces(sys.argv[1])
