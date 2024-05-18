import requests
import json

def search_repositories(query, per_page=50):    #Searches for repositories on GitHub based on the given query. 
    url = "https://api.github.com/search/repositories"
    params = {"q": query, "per_page": per_page}
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        repositories = data["items"]
        return repositories
    else:
        print("Error searching for repositories.")
        return None

def display_repositories(repositories):    #Displays a numbered list of the found repositories.
    if repositories:
        for i, repo in enumerate(repositories):
            print(f"{i+1}. {repo['full_name']} ({repo['language']}) - {repo['description']}")

def get_repository_details(repository_url):    #Gets detailed information about the selected repository.
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(repository_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error getting repository information.")
        return None

if __name__ == "__main__":
    query = input("Search for repositories: ")
    repositories = search_repositories(query)

    if repositories:
        display_repositories(repositories)

        choice = input("Select the repository number to view details (or 0 to exit): ")
        if choice.isdigit() and int(choice) > 0 and int(choice) <= len(repositories):
            selected_repo = repositories[int(choice) - 1]
            repo_details = get_repository_details(selected_repo["url"])

            if repo_details:
                print(json.dumps(repo_details, indent=4))
        else:
            print("Search complete.")
