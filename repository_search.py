import requests
import json

def search_repositories(query, per_page=100):
    
    url = "https://api.github.com/search/repositories"
    params = {"q": query, "per_page": per_page}
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        repositories = data["items"]
        return repositories
    else:
        print("Помилка під час пошуку репозиторіїв.")
        return None

def display_repositories(repositories):
    if repositories:
        for i, repo in enumerate(repositories):
            print(f"{i+1}. {repo['full_name']} ({repo['language']}) - {repo['description']}")

def get_repository_details(repository_url):
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(repository_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Помилка під час отримання інформації про репозиторій.")
        return None

if __name__ == "__main__":
    query = input("Пошук репозиторіїв: ")
    repositories = search_repositories(query)

    if repositories:
        display_repositories(repositories)

        choice = input("Виберіть номер репозиторія для перегляду деталей (або 0, щоб вийти): ")
        if choice.isdigit() and int(choice) > 0 and int(choice) <= len(repositories):
            selected_repo = repositories[int(choice) - 1]
            repo_details = get_repository_details(selected_repo["url"])

            if repo_details:
                print(json.dumps(repo_details, indent=4))
        else:
            print("Пошук завершено.")
