# Convert KOReader JSON to chaptered markdown

Takes a JSON exported from KOReader.  
The JSON has entries (highlights and notes).  
The script converts to Markdown.  
Markdown is grouped by chapters.  
Every sentence in an entry goes on an own line.  

**Usage**
`python3 koreader-json-to-markdown.py -i mortals.json -o mortals.md`

**Output format**
```md
# title - author

## chapter

text.

text.
```

**Caveats**
Highlights and own notes are not distinguishable.  
Line splitting is done by character (`.`) and will produce errors.
