# Git Log to Invoicing Notes

This repository contains a simple Windows Batch script that generates a text file summarizing Git commit logs between two specified dates. IT consultancies can use this output to improve or streamline their invoicing notes by tracking project work directly from commit history.

---

## Overview

When working on client projects, IT consultancies often need to provide detailed activity logs for invoicing purposes. This script extracts commits (including commit messages, dates, and associated changed files) from a Git repository within a given date range. It then outputs the commit details into a single text file.

The resulting file can be sent to clients or used internally for billing and reporting purposes. I personally curate the entries a bit more before inputing them into my invoicing system, [Harvest](https://www.getharvest.com/).

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
6. **Double-click** or **run** the script from your command prompt:

   ```batch
   @echo off

   rem ----------------------------------------------------------------------------
   rem 1. Define your variables
   rem ----------------------------------------------------------------------------
   rem Location of your Git repository:
   set "REPO_DIR=C:\_Projects\[your client git repository]"

   rem Desired start and end dates (YYYY-MM-DD):
   set "START_DATE=2025-01-11"
   set "END_DATE=2025-01-31"

   rem Location of the folder where you want to save the file:
   set "OUTPUT_DIR=C:\_Projects\[your client time report output folder]"

   rem ----------------------------------------------------------------------------
   rem 2. Build your filename using the full dates
   rem ----------------------------------------------------------------------------
   rem For example: cf-2024-12-11-to-2025-01-10-git.txt
   set "OUTPUT_FILE=cf-%START_DATE%-to-%END_DATE%-git.txt"

   rem Construct the full path to the output file:
   set "OUTPUT_PATH=%OUTPUT_DIR%\%OUTPUT_FILE%"

   rem ----------------------------------------------------------------------------
   rem 3. Run git log in the target repo directory and write output to OUTPUT_PATH
   rem ----------------------------------------------------------------------------
   pushd "%REPO_DIR%"
   git log --since="%START_DATE%" ^
           --until="%END_DATE%" ^
           --pretty=format:"%%ad%%n--------------------------%%n%%B%%n%%n==========================%%n" ^
           --name-only ^
           --date=format:"%%m/%%d/%%Y" ^
           > "%OUTPUT_PATH%"
   popd

   echo Commit details have been saved to "%OUTPUT_PATH%".
   pause
   ```

7. **Check** the `OUTPUT_DIR` folder for the generated text file named something like `cf-2025-01-11-to-2025-01-31-git.txt`.
8. **Review** or **share** this file with your finance/invoicing team.

---

## Example Output

Below is a simplified example of what the output might look like:

```
01/11/2025
--------------------------
Refactor user login logic
- Consolidated legacy auth flow
- Fixed #123

==========================
src/auth/login.js
tests/auth/login.test.js

01/11/2025
--------------------------
Update README with new instructions

==========================
README.md
```

Each commit is separated by a line of `==========================`, ensuring clarity between each commit's details.

---

## Customizing the Script

- **File naming**: Modify `OUTPUT_FILE` if you need a different naming convention (for instance, `CLIENTNAME-YYYY-MM-DD.txt`).
- **Date format**: Adjust the `--date=format:"%%m/%%d/%%Y"` flag if you want a different date format (e.g., ISO or localized).
