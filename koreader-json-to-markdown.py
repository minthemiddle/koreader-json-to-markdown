import click
import json

@click.command()
@click.option('--input_file', '-i', type=click.Path(exists=True))
@click.option('--output_file', '-o', type=click.Path())
def process_json(input_file, output_file):
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
        text = entry['text'].replace('.', '.\n')
        if chapter in chapters:
            chapters[chapter].append(text)
        else:
            chapters[chapter] = [text]

    # Prepare Markdown output
    markdown_output = f"# {title} - {author}\n\n"
    for chapter, texts in chapters.items():
        markdown_output += f"## {chapter}\n\n"
        for text in texts:
            markdown_output += f"{text}\n\n"

    # Write to output file or overwrite input file if no output file is specified
    output_path = output_file
    with open(output_path, 'w') as file:
        file.write(markdown_output)

    print(f"Processed file saved to {output_path}")

if __name__ == '__main__':
    process_json()
