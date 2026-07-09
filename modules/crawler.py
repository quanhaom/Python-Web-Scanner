import requests

from bs4 import BeautifulSoup

from urllib.parse import (
    urljoin,
    urlparse
)


def extract_links(url):

    links = set()

    try:

        response = requests.get(
            url,
            timeout=5
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        for tag in soup.find_all("a"):

            href = tag.get("href")

            if href:

                absolute = urljoin(
                    url,
                    href
                )

                links.add(
                    absolute
                )

    except Exception:

        pass

    return links


def crawl_site(
    start_url,
    max_pages=20
):

    visited = set()

    to_visit = [
        start_url
    ]

    base_domain = (
        urlparse(
            start_url
        ).netloc
    )

    while (
        to_visit
        and
        len(visited)
        < max_pages
    ):

        current = (
            to_visit.pop(0)
        )

        if current in visited:

            continue

        visited.add(
            current
        )

        print(
            f"[+] Crawling: {current}"
        )

        links = extract_links(
            current
        )

        for link in links:

            domain = (
                urlparse(
                    link
                ).netloc
            )

            if (
                domain
                ==
                base_domain
            ):

                if (
                    link
                    not in visited
                    and
                    link
                    not in to_visit
                ):

                    to_visit.append(
                        link
                    )

    return list(
        visited
    )