# bookbot
---

This CLI tool will extract useful data from a text file like word count and character count.
This project is a straight forward version of ‘wc’ command, because it outputs word count and character count by default. This is useful for piping commands and it follows the Unix Philisophy of one tool with specific goal.

## Motivation

At first I thought 'this seems a weird project'
but after learning how to parse each characters, read them and putting them into a loop dictionary
It's cool, it can count words, and all recurring characters.
I know that `wc` command exist, but why not?

## (>w<) Quick Start

Python 3.8 or higher is required

### 1. Clone the repo

```bash
git clone https://github.com/tianchongfengsula/bookbot.git
```

### 2. Test it using the example txts (thanks gutenberg!)

```bash
python3 bookbot/main.py bookbot/books/prideandprejudice.txt
```

## (0w0) Usage

```bash
python3 bookbot/main.py <your-book's-location>
```

## (>v<) Contributing

### 1. Clone the repo

```bash
git clone https://github.com/tianchongfengsula/bookbot.git
```

### Submit a pull request

If you'd like to contribute, please fork the repository and open a pull request to the `main` branch.
