# Markdown File Renamer

This Python script `process_files()` helps in renaming markdown files in the current directory to a standardized date format (`YYYY-MM-DD.md`). It's particularly useful when dealing with markdown files named in a different format, specifically with dates as part of their filenames.

## How it Works

1. **File Identification**: The script scans the current directory and identifies all files with the `.md` extension.
2. **Date Extraction**: It extracts the date part from the filenames, assuming they follow the pattern `YYYYMMDD [optional text]`.
3. **Date Conversion**: Using the extracted date, it converts the format to `YYYY-MM-DD`.
4. **Renaming**: The script renames the files to the new standardized format.

## Code Details

- The `process_files()` function uses Python's `os` and `datetime` libraries.
- It iterates through the markdown files in the current directory, parsing their filenames to extract dates and transform them into the desired format.
- If a filename doesn't match the expected date format, it prints an error message and continues to the next file.

## How to Use

1. Copy the script into a Python file.
2. Run the script in the directory containing the markdown files you want to rename.
3. Check the terminal/console output for the renaming details.
4. The markdown files should now be updated to the `YYYY-MM-DD.md` format.

**Note**: Ensure that the files you intend to rename follow the format `YYYYMMDD [optional text]` to guarantee successful renaming.
