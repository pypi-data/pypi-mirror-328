import tiktoken


class Tokenizer:
    def __init__(self, model_name="gpt2", file_path="llm_prompt.txt"):
        """Initialize tokenizer"""
        self.tokenizer = tiktoken.encoding_for_model(model_name)
        self.file_path = file_path
        self.tokens = None

    def _tokenize(self):
        """Tokenize the input file"""
        with open(self.file_path, "r", encoding="utf-8") as infile:
            text = infile.read()
            self.tokens = self.tokenizer.encode(text, disallowed_special=())

    def count_tokens(self):
        """Count the number of tokens"""
        self._tokenize()
        return len(self.tokens)
