from git import Repo
import tempfile
from .console import Console


class RepoDownloader:
    def __init__(self, repo_url, repo_path=None):
        self.repo_url = repo_url
        self.repo_path = repo_path

    def download_repo(self):
        console = Console()
        if self.repo_path is None:
            temp_dir = tempfile.mkdtemp(dir=".")
            self.repo_path = temp_dir

        console.print(f"ℹ Cloning repository to {self.repo_path}")
        Repo.clone_from(self.repo_url, self.repo_path)

    def get_repo(self):
        return Repo(self.repo_path)

    def get_repo_path(self):
        return self.repo_path

    def get_repo_url(self):
        return self.repo_url
