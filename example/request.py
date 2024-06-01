import requests

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()  # Parse the response as JSON
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

data = fetch_data()
print(data)