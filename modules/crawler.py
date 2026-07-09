import requests

from bs4 import BeautifulSoup

from urllib.parse import urljoin


def get_links(url):

    try:

        response = requests.get(
            url,
            timeout=5
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        links = []

        for tag in soup.find_all("a"):

            href = tag.get("href")

            if href:

                absolute_url = urljoin(
                    url,
                    href
                )

                links.append(
                    absolute_url
                )

        return list(set(links))

    except Exception as e:

        print(
            f"Error: {e}"
        )

        return []