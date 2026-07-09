from modules.crawler import crawl_site
from modules.forms import find_forms
from modules.headers import (
    check_headers,
    calculate_score
)
from modules.reporter import (
    save_json_report,
    save_html_report
)
print("=" * 50)
print("PYTHON WEB SCANNER")
print("=" * 50)

target = input("\nTarget URL: ").strip()

print("\n[+] Crawling website...")

links = crawl_site(
    target,
    max_pages=20
)

print("\n" + "=" * 50)
print("DISCOVERED LINKS")
print("=" * 50)

for link in links:
    print(link)

print(f"\nTotal Links Found: {len(links)}")

print("\n[+] Checking security headers...")

headers = check_headers(target)

print("\n" + "=" * 50)
print("SECURITY HEADERS")
print("=" * 50)

for header, status in headers.items():

    result = "Present" if status else "Missing"

    print(
        f"{header:<35} {result}"
    )

score = calculate_score(headers)

print("\n" + "=" * 50)
print(f"SECURITY SCORE: {score}/5")
print("=" * 50)

print("\n[+] Discovering forms...")

forms = find_forms(target)

print("\n" + "=" * 50)
print("FORMS FOUND")
print("=" * 50)

if not forms:

    print("No forms detected.")

else:

    for index, form in enumerate(
        forms,
        start=1
    ):

        print(f"\nForm #{index}")

        print(
            f"Method : {form['method']}"
        )

        print(
            f"Action : {form['action']}"
        )

        print("Inputs:")

        for input_field in form["inputs"]:

            print(
                f"  - {input_field['name']} "
                f"({input_field['type']})"
            )
report = {

    "target": target,

    "total_links": len(
        links
    ),

    "links": links,

    "security_score": score,

    "headers": headers,

    "forms": forms
}
save_json_report(
    report
)
save_html_report(
    report
)
print(
    "\nReports saved:"
)

print(
    "reports/report.json"
)

print(
    "reports/report.html"
)
print("\nScan completed.")