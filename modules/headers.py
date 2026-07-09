import requests


SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy"
]


def check_headers(url):

    results = {}

    try:

        response = requests.get(
            url,
            timeout=5
        )

        for header in SECURITY_HEADERS:

            results[header] = (
                header in response.headers
            )

    except Exception as e:

        print(
            f"Header Error: {e}"
        )

    return results


def calculate_score(results):

    score = 0

    for value in results.values():

        if value:
            score += 1

    return score