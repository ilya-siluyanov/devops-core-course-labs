# Miscellaneous

## Code quality

In order to lint the project there are `ruff` and `markdownlint`:

```bash
ruff main.py
markdownlint PYTHON.md README.md
```

### Examples

```bash
> ruff main.py
main.py:20:89: E501 Line too long (90 > 88 characters)
Found 1 error.
```

```bash
> markdownlint PYTHON.md README.md
PYTHON.md:3 MD022/blanks-around-headings/blanks-around-headers
    Headings should be surrounded by blank lines
    [Expected: 1; Actual: 0; Below] [Context: "## Code quality"]
PYTHON.md:5 MD031/blanks-around-fences
    Fenced code blocks should be surrounded by blank lines [Context: "```bash"]
PYTHON.md:10 MD022/blanks-around-headings/blanks-around-headers
    Headings should be surrounded by blank lines 
    [Expected: 1; Actual: 0; Below] [Context: "### Examples:"]
PYTHON.md:10:13 MD026/no-trailing-punctuation
    Trailing punctuation in Headings
    [Punctuation: ':']
PYTHON.md:11 MD031/blanks-around-fences
    Fenced code blocks should be surrounded by blank lines
    [Context: "```bash"]
PYTHON.md:15 MD031/blanks-around-fences
    Fenced code blocks should be surrounded by blank lines
    [Context: "```"]
PYTHON.md:16 MD031/blanks-around-fences
    Fenced code blocks should be surrounded by blank lines
    [Context: "```bash"]
README.md:10 MD032/blanks-around-lists
    Lists should be surrounded by blank lines
    [Context: "1. Install [npm](https://docs...."]
```

## Unit tests

Unit tests check test a repository to persist notes (`test_repo.py`) and endpoints correct work (`test_endpoints.py`)

### Best practices

We use the base pattern for tests:

1. Prepare environment
1. Perform actions
1. Make assertions and validate them

We also make unit-tests as lightweight as we can:

1. We use `InMemoryNoteRepo`, because we don't care where notes will be persisted during testing
1. We split tests based on components responsibility in order to eradicate fragile tests
