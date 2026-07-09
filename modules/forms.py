import requests

from bs4 import BeautifulSoup


def find_forms(url):

    forms_data = []

    try:

        response = requests.get(
            url,
            timeout=5
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        forms = soup.find_all("form")

        for form in forms:

            method = form.get(
                "method",
                "GET"
            )

            action = form.get(
                "action",
                ""
            )

            inputs = []

            for input_tag in form.find_all(
                "input"
            ):

                inputs.append({

                    "name":
                    input_tag.get("name"),

                    "type":
                    input_tag.get("type")
                })

            forms_data.append({

                "method": method,

                "action": action,

                "inputs": inputs
            })

    except Exception as e:

        print(
            f"Form Error: {e}"
        )

    return forms_data