# git2string
git2string is a powerful tool that can quickly convert an entire Git repository to a prompt that can be fed to any large language model (LLM).

It will automatically ignore all binary files. Additionally, it will respect your **.gitignore**.

## Usage

```
git2string <url of repository>
```

For example:

```
git2string https://github.com/mozilla/experimenter
```

If you have cloned your desired repository already, you can just specify its path.

```
git2string <repo root directory>
```

By default, the prompt will be generated in a file called **llm_prompt.txt**.

You can specify a different filename as follows:

```
git2string <repo root directory> --output-file <filename>
```

## Additional Features

- Can count tokens for most OpenAI models
