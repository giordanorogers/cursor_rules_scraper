import os
import math

# Directory containing the rule files
input_dir = "cursor_directory_code"
files = sorted([f for f in os.listdir(input_dir) if f.startswith("rule_") and f.endswith(".txt")])

# Calculate files per group
total_files = len(files)
num_groups = 19
files_per_group = math.floor(total_files / num_groups)

print(f"Found {total_files} files, combining into {num_groups} groups of {files_per_group} files each...")

# Process files in groups
for group_num in range(num_groups):
    start_idx = group_num * files_per_group
    end_idx = min((group_num + 1) * files_per_group, total_files)
    group_files = files[start_idx:end_idx]
    
    # Create combined content with clear separators
    combined_content = []
    for filename in group_files:
        with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as f:
            content = f.read()
            combined_content.append(f"=== {filename} ===\n{content}\n\n")
    
    # Write combined content to new file
    output_filename = f"combined_rules_{group_num + 1}.txt"
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(combined_content))
    
    print(f"Created {output_filename} with {len(group_files)} rules")

print("Combination complete!") 