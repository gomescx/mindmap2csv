# Markdown to CSV Converter

## Overview

This Python program reads a Markdown file containing project task data and converts it into a CSV file. Each column in the CSV file represents a level of depth in the task hierarchy, starting from Level 2.

### Motivation

The primary purpose of this program is to allow the author to quickly convert a mindmap from iThoughts exported as a Markdown file format into a tasks CSV file for tools like JIRA.
The primary purpose of this program is to allow the author to quickly convert a mindmap from iThoughts exported as a Markdown file format into a tasks CSV file for JIRA.

## Features

- **Parse Markdown Data**: Reads tasks from a Markdown file.
- **Hierarchical Levels**: Organizes tasks into columns based on their outline levels.
- **CSV Output**: Outputs the organized tasks into a CSV file for easy import into JIRA or other tools.

## Prerequisites

- Python 3.x

## Usage

1. Save the Markdown file you want to convert (e.g., `source.markdown`) in the `data` directory.
2. Ensure the `data` directory exists and contains the necessary Markdown file.
3. Run the script using Python:
```sh
python markdown_to_csv_converter.py
```

## Output

The script will generate a CSV file (`output.csv`) in the `data` directory with the following structure:
- Each column represents a level of depth in the task hierarchy, starting from Level 2.
- Each row corresponds to a task or sub-task at the appropriate level.

## Notes

- Ensure that the Markdown file follows the structure expected by the script, with tasks organized under appropriate heading levels (e.g., `##`, `###`, `####`, `#####`).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

