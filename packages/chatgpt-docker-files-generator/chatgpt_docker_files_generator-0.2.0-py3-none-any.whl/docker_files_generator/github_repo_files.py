import requests
import base64
import re


class GitHubRepoFiles:
    def __init__(self, repo_url_or_name, token=None, branch=None, skip_token_check=False):
        self.repo_full_name = self.extract_repo_name(repo_url_or_name)
        self.headers = self.build_auth_header(token) if token else {}

        if token and not skip_token_check and not self.validate_token():
            raise Exception("Invalid GitHub token or not enough permissions.")

        self.branch = branch if branch else self.get_default_branch()
        self.api_url = f"https://api.github.com/repos/{self.repo_full_name}/contents/"

    @staticmethod
    def extract_repo_name(repo_url_or_name):
        if re.match(r"https://github.com/.+/.+\.git", repo_url_or_name):
            return repo_url_or_name.rstrip(".git").split("github.com/")[1]
        return repo_url_or_name

    @staticmethod
    def build_auth_header(token):
        return {"Authorization": f"token {token}"}

    def validate_token(self):
        response = requests.get("https://api.github.com/user", headers=self.headers)
        return response.status_code == 200

    def get_default_branch(self):
        repo_info_url = f"https://api.github.com/repos/{self.repo_full_name}"
        response = requests.get(repo_info_url, headers=self.headers)
        if response.status_code == 200:
            return response.json().get("default_branch", "main")
        else:
            raise Exception(f"Error while getting repository information: {response.status_code} - {response.text}")

    def get_files(self, path=""):
        url = f"{self.api_url}/{path}" if path else self.api_url
        response = requests.get(f"{url}?ref={self.branch}", headers=self.headers)
        if response.status_code == 200:
            files = response.json()
            result = []
            for file in files:
                if file["type"] == "file":
                    result.append(file["path"])
                elif file["type"] == "dir":
                    result.extend(self.get_files(file["path"]))
            return result
        else:
            raise Exception(f"Error while getting the list of files: {response.status_code} - {response.text}")

    def find_file(self, filename):
        files = self.get_files()
        for file in files:
            if file == filename:
                return {"path": file, "url": f"{self.api_url}{file}?ref={self.branch}"}
        return None

    def get_file_content(self, filename):
        file = self.find_file(filename)
        if not file:
            raise Exception(f"File '{filename}' not found in repository {self.repo_full_name} on branch {self.branch}.")

        response = requests.get(file["url"], headers=self.headers)
        if response.status_code == 200:
            file_data = response.json()
            if file_data.get("encoding") == "base64":
                return base64.b64decode(file_data["content"]).decode("utf-8")
            return file_data["content"]
        else:
            raise Exception(f"Error while downloading a file: {response.status_code} - {response.text}")
