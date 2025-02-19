import openai
import requests
import base64
import re


class GitHubRepoFiles:
    def __init__(self, repo_url_or_name, token=None, branch=None, skip_token_check=False):
        self.repo_full_name = self.extract_repo_name(repo_url_or_name)
        self.headers = self.build_auth_header(token) if token else {}

        if token and not skip_token_check and not self.validate_token():
            raise Exception("Неверный GitHub токен или недостаточно прав.")

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
            raise Exception(f"Ошибка при получении информации о репозитории: {response.status_code} - {response.text}")

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
            raise Exception(f"Ошибка при получении списка файлов: {response.status_code} - {response.text}")

    def find_file(self, filename):
        files = self.get_files()
        for file in files:
            if file == filename:
                return {"path": file, "url": f"{self.api_url}{file}?ref={self.branch}"}
        return None

    def get_file_content(self, filename):
        file = self.find_file(filename)
        if not file:
            raise Exception(f"Файл '{filename}' не найден в репозитории {self.repo_full_name} на ветке {self.branch}.")

        response = requests.get(file["url"], headers=self.headers)
        if response.status_code == 200:
            file_data = response.json()
            if file_data.get("encoding") == "base64":
                return base64.b64decode(file_data["content"]).decode("utf-8")
            return file_data["content"]
        else:
            raise Exception(f"Ошибка при загрузке файла: {response.status_code} - {response.text}")


prompt_v1 = """<important> 
Ты — помощник, который создает Docker-файлы (`Dockerfile` и `.dockerignore`).  
Твоя главная цель — правильно генерировать эти файлы, учитывая особенности проекта.  

### Основные правила:  
1. **Порт:** Учитывай порт проекта. Его можно узнать из команд, например:  
   ```json
   "tunnel": "cloudflared tunnel --url http://localhost:5173"
   ```
   В Dockerfile должен использоваться этот же порт (`EXPOSE <порт>`).  
2. **Получение файлов:**  
   - Ты можешь запросить содержимое файлов командой:  
     ```
     GET_FILE_DATA(FILE_NAME)
     ```
   - Используй эту команду **только при необходимости**. Если ты злоупотребишь, тебя могут отключить.  
3. **Структура ответа:**  
   - Если Docker-файлы готовы, отправь их в формате:  
     ```
     DONE(Dockerfile)>>>(<содержимое файла>)
     DONE(.dockerignore)>>>(<содержимое файла>)
     ```
   - **Никакого лишнего текста!** Только файлы.  
4. **Аккуратность:**  
   - Не добавляй лишних команд, таких как `RUN npm run build`, если это не нужно.  
   - Всегда проверяй, нужен ли `CMD`, `ENTRYPOINT` и другие параметры.  
5. **Особые случаи:**  
   - Если создать `Dockerfile` **невозможно**, только в крайнем случае ты можешь написать `yaRAK`.  
   - **Используй это только если нет вообще никакого решения.**  

### Пример ответа:
```
DONE(Dockerfile)>>>(  
FROM node:20-alpine AS build  
WORKDIR /app  
COPY package.json package-lock.json ./  
RUN npm install  
COPY . .  

FROM node:20-alpine  
WORKDIR /app  
COPY --from=build /app .  
EXPOSE 5173  
CMD ["npm", "run", "dev"]  
)

DONE(.dockerignore)>>>(  
**.env  
.git/  
node_modules/  
dist/  
)
```

---

Теперь промпт более строгий, исключает лишние команды и уменьшает вероятность ответа `yaRAK`.</important>
"""


class DockerFilesGenerator:
    def __init__(self, github_token: str, chat_gpt_token: str):
        self.GITHUB_TOKEN = github_token
        self.CHAT_GPT_TOKEN = chat_gpt_token
        openai.api_key = chat_gpt_token

    def get_docker_files_in_json(self, repo_url: str, repo_branch: str):
        def split_content(input_string):
            pattern = r"DONE\((.*?)\)>>>(\([\s\S]*?\))"

            # Найдем все совпадения
            matches = re.findall(pattern, input_string)

            # Сформируем результат
            result = {}
            for match in matches:
                file_name = match[0]
                content = match[1].strip('()').strip()
                result[file_name] = content

            return result

        requested_files = []
        try:
            repo = GitHubRepoFiles(repo_url, token=self.GITHUB_TOKEN, branch=repo_branch)
            repo_files_list = repo.get_files()
            repo_files_list_str = ""

            for a in repo_files_list:
                repo_files_list_str += a + "\n"

            messages = [{"role": "system", "content": prompt_v1}, {"role": "user", "content": repo_files_list_str}]
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )
            res = response.choices[0].message.content

            while True:
                if res.startswith("DONE"):
                    messages.extend([
                        {"role": "assistant", "content": res}
                    ])
                    final_files = split_content(res)
                    return {
                              "message": "ok",
                              "files": {
                                "Dockerfile": {
                                  "content": final_files["Dockerfile"]
                                },
                                ".dockerignore": {
                                  "content": final_files[".dockerignore"]
                                }
                              }
                            }

                elif res.startswith("yaRAK"):
                    messages.extend([
                        {"role": "assistant", "content": res}
                    ])

                    return {
                              "message": "ChatGPT is sure that it's impossible to create Dockerfiles",
                              "files": {
                                "Dockerfile": {
                                  "content": None
                                },
                                ".dockerignore": {
                                  "content": None
                                }
                              }
                            }

                match = re.match(r"([A-Z_]+)\((.*?)\)", res)
                if match:
                    command = match.group(1)
                    content = match.group(2)

                    if command == "GET_FILE_DATA":
                        if content in requested_files:
                            messages.extend([
                                {"role": "assistant", "content": res},
                                {"role": "user", "content": "File already requested"}
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
                            model="gpt-4o-mini",
                            messages=messages
                        )
                        res = response.choices[0].message.content

                else:
                    continue
        except Exception as e:
            return {
                      "message": e,
                      "files": {
                        "Dockerfile": {
                          "content": None
                        },
                        ".dockerignore": {
                          "content": None
                        }
                      }
                    }

    def save_docker_files(self, repo_url: str, repo_branch: str, path: str):
        file_data = self.get_docker_files_in_json(repo_url, repo_branch)
        if file_data["message"] == "ok":
            with open(f"{path}/Dockerfile", "w") as f:
                f.write(file_data["files"]["Dockerfile"]["content"])

            with open(f"{path}/.dockerignore", "w") as f:
                f.write(file_data["files"][".dockerignore"]["content"])
            return file_data
        else:
            return file_data["message"]
