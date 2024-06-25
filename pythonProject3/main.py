import requests
from bs4 import BeautifulSoup

def fetch_all_pypi_packages():
    packages = []
    url = "https://pypi.org/simple/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for anchor in soup.find_all('a'):
            packages.append(anchor.text)
    return packages

packages = fetch_all_pypi_packages()

# Write the packages to a file to avoid printing a huge list to the console
with open("all_pypi_packages.txt", "w", encoding="utf-8") as file:
    for package in packages:
        file.write(package + "\n")

print(f"Total packages fetched: {len(packages)}")
print("The list of all packages has been saved to 'all_pypi_packages.txt'.")
