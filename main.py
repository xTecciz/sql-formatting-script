import os
import sqlparse
import re


def manual_align(formatted_sql: str) -> str:
    # Split the formatted SQL into separate lines
    lines = formatted_sql.split('\n')

    # Remove trailing spaces from each line
    lines = [line.rstrip() for line in lines]

    # Define top-level keywords which should start at the beginning of a line
    # This helps ensure that statements like SELECT, FROM, WHERE, etc. are aligned.
    top_keywords = {
        'SELECT', 'FROM', 'WHERE', 'ORDER', 'GROUP', 'HAVING', 'LIMIT', 'JOIN', 'LEFT', 'RIGHT', 'INNER',
        'OUTER', 'UPDATE', 'DELETE', 'INSERT', 'CREATE', 'DROP', 'VALUES', 'ON'
    }

    aligned_lines = []
    for line in lines:
        stripped_line = line.lstrip()
        first_word = stripped_line.split(' ', 1)[0].upper() if stripped_line else ''
        # If the line starts with a top-level keyword, align it to the start of the line (no extra indentation)
        if first_word in top_keywords:
            aligned_lines.append(stripped_line)
        else:
            aligned_lines.append(line)

    # Replace multiple spaces with a single space to avoid cases like "ORDER     BY"
    single_spaced_lines = []
    for line in aligned_lines:
        if line.strip():
            line = re.sub(r' {2,}', ' ', line)  # Compress multiple spaces into one
        single_spaced_lines.append(line)

    # Remove consecutive empty lines, leaving at most one empty line in a row
    cleaned_lines = []
    prev_empty = False
    for line in single_spaced_lines:
        if line.strip() == '':
            if not prev_empty:
                cleaned_lines.append(line)
            prev_empty = True
        else:
            cleaned_lines.append(line)
            prev_empty = False

    # Ensure there is exactly one empty line at the end of the file
    if cleaned_lines and cleaned_lines[-1].strip() != '':
        cleaned_lines.append('')

    return '\n'.join(cleaned_lines)


def format_sql_file(file_path: str):
    # Read the original SQL content from the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Use sqlparse to perform initial formatting
    formatted = sqlparse.format(
        content,
        reindent=True,
        reindent_aligned=False,  # Disable aligned reindentation to rely on manual adjustments
        indent_width=4,          # Indent width: 4 spaces
        indent_char=' ',         # Use spaces (not tabs) for indentation
        keyword_case='upper',    # Convert all keywords to uppercase
        identifier_case=None,
        strip_comments=False,    # Keep comments intact
        strip_whitespace=False,
        use_space_around_operators=True
    )

    # Perform additional manual alignment to better match sqlstyle.guide conventions
    formatted = manual_align(formatted)

    # Write the formatted SQL back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(formatted)


def process_directory(root_dir: str):
    # Recursively process all .sql files in the specified directory, skipping directories that start with '.'
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for filename in filenames:
            if filename.lower().endswith('.sql'):
                file_path = os.path.join(dirpath, filename)
                try:
                    format_sql_file(file_path)
                    print(f"Formatted file: {file_path}")
                except Exception as e:
                    print(f"Error formatting file {file_path}: {e}")


if __name__ == '__main__':
    # Start processing from the current directory
    current_dir = os.path.abspath('.')
    process_directory(current_dir)
