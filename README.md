# Git Log to Invoicing Notes

This repository contains a simple Windows Batch script that generates a text file summarizing Git commit logs between two specified dates. IT consultancies can use this output to improve or streamline their invoicing notes by tracking project work directly from commit history.

---

## Overview

When working on client projects, IT consultancies often need to provide detailed activity logs for invoicing purposes. This script extracts commits (including commit messages, dates, and associated changed files) from a Git repository within a given date range. It then outputs the commit details into a single text file.

The resulting file can be sent to clients or used internally for billing and reporting purposes.

---

## Prerequisites

- **Windows** environment (the script is a `.bat` file).
- **Git** installed and accessible via the command line (`git` command should be in your PATH).
- **Write access** to the output directory you specify.

---

## Usage

1. **Clone or download** this script into your working folder.
2. **Open** the script in a text editor.
3. **Set** the following environment variables to reflect your own setup:
   - `REPO_DIR`  
     The path to the local Git repository you want to extract logs from.

   - `START_DATE` and `END_DATE`  
     The date range in `YYYY-MM-DD` format. Commits after `START_DATE` (inclusive) and before `END_DATE` (inclusive) will be retrieved.

   - `OUTPUT_DIR`  
     The path to the folder where you want the output text file saved.

4. **Optional**: Adjust the default filename structure by editing `OUTPUT_FILE` if you prefer a different naming convention.
5. **Save** the script.
