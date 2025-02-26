#!/usr/bin/env python3
import os
import subprocess
from datetime import datetime

# ----------------------------------------------------------------------------
# 1. Define your variables
# ----------------------------------------------------------------------------
# Location of your Git repository:
REPO_DIR = "/Users/your-username/path/to/your/repo"

# Desired start and end dates (YYYY-MM-DD):
START_DATE = "2025-01-11"
END_DATE = "2025-01-31"

# Location of the folder where you want to save the file:
OUTPUT_DIR = "/Users/your-username/path/to/your/output/folder"

# ----------------------------------------------------------------------------
# 2. Build your filename using the full dates
# ----------------------------------------------------------------------------
# For example: cf-2024-12-11-to-2025-01-10-git.txt
output_file = f"cf-{START_DATE}-to-{END_DATE}-git.txt"
output_path = os.path.join(OUTPUT_DIR, output_file)

# ----------------------------------------------------------------------------
# 3. Run git log in the target repo directory and write output to output_path
# ----------------------------------------------------------------------------
try:
    # Change to the repository directory
    original_dir = os.getcwd()
    os.chdir(REPO_DIR)

    # Prepare the git log command
    git_command = [
        "git", "log",
        f"--since={START_DATE}",
        f"--until={END_DATE}",
        "--pretty=format:%ad%n---------------------------%n%B%n%n==========================%n",
        "--name-only",
        "--date=format:%m/%d/%Y"
    ]

    # Run the command and capture output
    result = subprocess.run(git_command, capture_output=True, text=True)

    # Write the output to file
    with open(output_path, 'w') as f:
        f.write(result.stdout)

    print(f"Commit details have been saved to '{output_path}'")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Change back to original directory
    os.chdir(original_dir)

input("Press Enter to continue...")
