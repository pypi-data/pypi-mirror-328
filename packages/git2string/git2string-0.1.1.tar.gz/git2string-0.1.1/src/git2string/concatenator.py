from .ignore_handler import IgnoreHandler
from .file_handler import FileHandler
from .tokenizer import Tokenizer
from tqdm import tqdm
import os


class FileConcatenator:
    def __init__(
        self,
        repo_path,
        output_file,
        include_binary=False,
        encoding="utf-8",
        model="gpt2",
    ):
        """Initialize with paths and binary inclusion flag."""
        self.repo_path = repo_path
        self.output_file = output_file
        self.ignore_handler = IgnoreHandler(repo_path)
        self.file_handler = FileHandler(include_binary)
        self.encoding = encoding
        self.include_binary = include_binary        
        self.tokenizer = Tokenizer(model, output_file)

    def _get_files(self):
        """Get all files from the repo path."""
        output = []
        for root, dirs, files in os.walk(self.repo_path):
                    dirs[:] = [d for d in dirs if not d.startswith('.')]
                    files = [f for f in files if not f.startswith('.')]                
                    for file in files:
                        file_path = os.path.join(root, file)
                        if not self.ignore_handler.should_ignore(file_path):
                            if not self.file_handler.is_binary(file_path) or self.include_binary:
                                output.append(file_path)
        return output

    def concatenate(self):
        """Concatenate files from the repo path to the output file."""

        files = self._get_files()
        total_files = len(files)
        n_errors = 0
        with tqdm(total=total_files, desc="Concatenating") as pbar:
            with open(self.output_file, "w", encoding=self.encoding) as outfile:
                for file_path in self._get_files():
                            try:
                                content = self.file_handler.read_file(file_path)
                                if content is not None:
                                    relative_path = os.path.relpath(
                                        file_path, self.repo_path
                                    )
                                    outfile.write(f"--- START OF {relative_path} ---\n")
                                    outfile.write(content)
                                    outfile.write(f"\n--- END OF {relative_path} ---\n")
                                    outfile.write("\n\n")
                                pbar.update(1)
                            except:
                                 n_errors += 1

        return total_files, self.ignore_handler.n_ignored, self.tokenizer.count_tokens(), n_errors
