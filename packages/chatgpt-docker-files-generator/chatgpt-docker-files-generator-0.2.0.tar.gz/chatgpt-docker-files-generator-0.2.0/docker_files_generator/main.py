from github_repo_files import GitHubRepoFiles
import re
import os
import openai
from prompt import prompt


class DockerFilesGenerator:
    """
    A class for generating Dockerfile and .dockerignore based on the contents of a GitHub repository.
    """

    def __init__(self, github_token: str, chat_gpt_token: str):
        """
        Initialising the Docker file generator.

        :param github_token: Token to access GitHub API.
        :param chat_gpt_token: Token to access OpenAI API.
        """
        self.GITHUB_TOKEN = github_token
        self.CHAT_GPT_TOKEN = chat_gpt_token
        openai.api_key = chat_gpt_token
        self.chatgpt_model = "gpt-4o-mini"

    @staticmethod
    def _split_content(input_string: str) -> dict:
        """
        Parses a string containing the generated files and extracts their contents.

        :param input_string: A string containing files in the format DONE(file_name)>>>(contents).
        :return: A dictionary with filenames as keys and their contents as values.
        """
        pattern = r"DONE\((.*?)\)>>>(\([\s\S]*?\))"
        matches = re.findall(pattern, input_string)

        result = {}
        for match in matches:
            file_name = match[0]
            content = match[1].strip("()").strip()
            result[file_name] = content

        return result

    def get_docker_files_in_json(self, repo_url: str, repo_branch: str) -> dict:
        """
        Retrieves a list of files from the repository and sends it to ChatGPT to generate Docker files.

        :param repo_url: URL of the GitHub repository.
        :param repo_branch: Repository branch.
        :return: JSON object with generated Dockerfile and .dockerignore.
        """
        try:
            repo = GitHubRepoFiles(repo_url, token=self.GITHUB_TOKEN, branch=repo_branch)
            repo_files_list = repo.get_files()
            repo_files_list_str = "\n".join(repo_files_list)

            messages = [
                {"role": "system", "content": prompt},
                {"role": "user", "content": repo_files_list_str}
            ]

            response = openai.chat.completions.create(
                model=self.chatgpt_model,
                messages=messages
            )
            res = response.choices[0].message.content

            requested_files = []

            while True:
                if res.startswith("DONE"):
                    final_files = self._split_content(res)
                    return {
                        "message": "ok",
                        "files": {
                            "Dockerfile": {"content": final_files.get("Dockerfile")},
                            ".dockerignore": {"content": final_files.get(".dockerignore")}
                        }
                    }
                elif res.startswith("yaRAK"):
                    return {
                        "message": "ChatGPT is sure that creating Docker files is impossible",
                        "files": {"Dockerfile": {"content": None}, ".dockerignore": {"content": None}}
                    }

                match = re.match(r"([A-Z_]+)\((.*?)\)", res)
                if match:
                    command = match.group(1)
                    content = match.group(2)

                    if command == "GET_FILE_DATA":
                        if content in requested_files:
                            messages.extend([
                                {"role": "assistant", "content": res},
                                {"role": "user", "content": "The file has already been requested"}
                            ])
                        else:
                            if content in repo_files_list:
                                requested_files.append(content)
                                messages.extend([
                                    {"role": "assistant", "content": res},
                                    {"role": "user", "content": repo.get_file_content(content)}
                                ])
                            else:
                                messages.extend([
                                    {"role": "assistant", "content": res},
                                    {"role": "user", "content": "File not found"}
                                ])

                        response = openai.chat.completions.create(
                            model=self.chatgpt_model,
                            messages=messages
                        )
                        res = response.choices[0].message.content

        except Exception as error:
            return {
                "message": str(error),
                "files": {"Dockerfile": {"content": None}, ".dockerignore": {"content": None}}
            }

    def get_docker_files_and_save(self, repo_url: str, repo_branch: str, path: str) -> dict:
        """
        Extracts Docker files in JSON format and saves them to the specified directory.

        :param repo_url: URL of the GitHub repository.
        :param repo_branch: The branch of the repository.
        :param path: The full path to the directory to save the files.
        :return: JSON object with the result of the operation.
        """
        response = self.get_docker_files_in_json(repo_url, repo_branch)

        if response["message"] == "ok":
            os.makedirs(path, exist_ok=True)

            with open(os.path.join(path, "Dockerfile"), "w") as file:
                file.write(response["files"]["Dockerfile"]["content"])

            with open(os.path.join(path, ".dockerignore"), "w") as file:
                file.write(response["files"][".dockerignore"]["content"])

        return response
