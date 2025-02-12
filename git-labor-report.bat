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
