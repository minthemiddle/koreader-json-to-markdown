import json
import os
import unittest
from click.testing import CliRunner
from koreader_json_to_markdown import process_json

class TestProcessJson(unittest.TestCase):
    def test_process_json(self):
        # Create a test JSON file
        input_file = "test.json"
        with open(input_file, "w") as f:
            json.dump(
                {
                    "author": "John Doe",
                    "title": "Test Book",
                    "entries": [
                        {
                            "chapter": "Chapter 1",
                            "text": "This is a test. It contains multiple sentences. Each sentence should be quoted.",
                        }
                    ],
                },
                f,
            )

        # Use Click's CliRunner to simulate command-line interface
        runner = CliRunner()
        result = runner.invoke(process_json, [input_file])

        # Check that the script executed successfully
        self.assertEqual(result.exit_code, 0)

        # Check the output Markdown file
        base = os.path.splitext(input_file)[0]
        output_file = f"{base}.md"
        with open(output_file, "r") as f:
            markdown_output = f.read()

        expected_output = "# Test Book - John Doe\n\n## Chapter 1\n\n> This is a test.\n> It contains multiple sentences.\n> Each sentence should be quoted.\n\n"
        self.assertEqual(markdown_output, expected_output)

        # Clean up the test files
        os.remove(input_file)
        os.remove(output_file)

if __name__ == "__main__":
    unittest.main()
