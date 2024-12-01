import os
import re

# Replace this path with the actual path to your YeastGenesA folder
folder_path = r"./YeastGenes/YeastGenes"

# Define your regex pattern
pattern = re.compile(r"ATG[ATCG]{3}TAA")

output_file = "pattern_matches.txt"

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Write a header line (optional)
    outfile.write("Gene_Name\tMatch_Count\n")
    
    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        # Construct full file path
        file_path = os.path.join(folder_path, filename)
        
        # Check if it's a file (not a folder)
        if os.path.isfile(file_path):
            # Open and read the gene file
            with open(file_path, 'r') as infile:
                # Read all lines from the file
                lines = infile.readlines()
                
                # Skip empty files
                if len(lines) < 2:
                    continue
                
                # Extract the gene name from the filename or content
                # Assuming filename is the ORF name, e.g., 'YBL020W.txt'
                gene_name = os.path.splitext(filename)[0]
                
                # The DNA sequence is usually on the second line
                sequence = lines[1].strip()
                
                # Search for the pattern in the sequence
                matches = pattern.findall(sequence)
                
                # Count the number of matches
                match_count = len(matches)
                
                # Write the results to the output file
                outfile.write(f"{gene_name}\t{match_count}\n")