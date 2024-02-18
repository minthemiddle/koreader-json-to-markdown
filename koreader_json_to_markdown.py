import click
import json
import re
import os

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
def process_json(input_file):
    """
    Processes a JSON file to extract 'text' and 'chapter' from each entry,
    and outputs the result in a specified Markdown format.
    """
    with open(input_file, 'r') as file:
        data = json.load(file)

    author = data['author']
    title = data['title']
    entries = data['entries']

    # Group entries by chapter
    chapters = {}
    for entry in entries:
        chapter = entry['chapter']
        text = entry['text']
        # Split text into sentences using regular expressions
        sentences = re.split(r'(?<=[.!?:]) +', text)
        formatted_text = '\n'.join(f"> {sentence}" for sentence in sentences)
        if chapter in chapters:
            chapters[chapter].append(formatted_text)
        else:
            chapters[chapter] = [formatted_text]

    # Prepare Markdown output
    markdown_output = f"# {title} - {author}\n\n"
    for chapter, texts in chapters.items():
        markdown_output += f"## {chapter}\n\n"
        for text in texts:
            markdown_output += f"{text}\n\n"
            
    # Remove duplicate empty lines
    markdown_output = re.sub(r'\n{2,}', '\n\n', markdown_output)
    
    # Determine the output file name based on the input file name
    base = os.path.splitext(input_file)[0]
    output_file = f"{base}.md"

    # Write to output file or overwrite input file if no output file is specified
    with open(output_file, 'w') as file:
        file.write(markdown_output)

    print(f"Processed file saved to {output_file}")

if __name__ == '__main__':
    process_json()
