import json


def save_json_report(data):

    with open(
        "reports/report.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def save_html_report(data):

    html = f"""
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">

<title>
Python Web Scanner Report
</title>

<style>

body {{

    font-family: Arial;
    margin: 40px;
}}

table {{

    border-collapse: collapse;
    width: 100%;
}}

th, td {{

    border: 1px solid #cccccc;
    padding: 8px;
}}

th {{

    background-color: #eeeeee;
}}

</style>

</head>

<body>

<h1>Python Web Scanner Report</h1>

<h2>Target</h2>

<p>{data['target']}</p>

<h2>Statistics</h2>

<ul>
<li>Total Links: {data['total_links']}</li>
<li>Security Score: {data['security_score']}/5</li>
</ul>

<h2>Security Headers</h2>

<table>

<tr>
<th>Header</th>
<th>Status</th>
</tr>
"""

    for header, status in data["headers"].items():

        result = (
            "Present"
            if status
            else "Missing"
        )

        html += f"""
<tr>
<td>{header}</td>
<td>{result}</td>
</tr>
"""

    html += """
</table>

<h2>Forms</h2>
"""

    if not data["forms"]:

        html += """
<p>No forms detected.</p>
"""

    else:

        for index, form in enumerate(
            data["forms"],
            start=1
        ):

            html += f"""
<h3>Form #{index}</h3>

<ul>
<li>Method: {form['method']}</li>
<li>Action: {form['action']}</li>
</ul>
"""

    html += """
</body>
</html>
"""

    with open(
        "reports/report.html",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)