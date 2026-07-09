# Python Web Scanner

A Python-based web assessment tool for website inventory and security posture analysis.

## Features

* Website Crawling
* Recursive Link Discovery
* Form Discovery
* Security Header Analysis
* Security Score Calculation
* JSON Report Generation
* HTML Report Generation

## Project Structure

```text
python-web-scanner/
│
├── scanner.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── crawler.py
│   ├── forms.py
│   ├── headers.py
│   └── reporter.py
│
└── reports/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/python-web-scanner.git

cd python-web-scanner
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the scanner:

```bash
python scanner.py
```

Example:

```text
Target URL:
https://example.com
```

## Output

The scanner generates:

```text
reports/
├── report.json
└── report.html
```

### JSON Report

Contains:

* Target URL
* Discovered Links
* Security Headers
* Security Score
* Forms

### HTML Report

Provides a browser-friendly report with:

* Statistics
* Header Analysis
* Form Discovery Results

## Technologies Used

* Python 3
* Requests
* BeautifulSoup4
* JSON

## Learning Objectives

This project was developed to improve knowledge of:

* HTTP Fundamentals
* Web Crawling
* HTML Parsing
* Python Automation
* Web Security Concepts
* Secure Development Practices

## Roadmap

Planned improvements:

* robots.txt parsing
* sitemap.xml discovery
* Endpoint collection
* Technology fingerprinting
* Multi-threaded crawling
* Advanced reporting

## Disclaimer

This tool is intended for educational purposes and authorized security assessment activities only.
