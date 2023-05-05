import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.msn.com/en-us/news"
    response = requests.get(url)

    print(response)


if __name__ == "__main__":
    main()
