# Drug List Scraper

This Python script scrapes drug-related information from the "Talk to Frank" website and saves the extracted data in both JSON and YAML formats. It utilizes the `requests` library to fetch the webpage, `BeautifulSoup` for HTML parsing, and `json` and `yaml` libraries for data storage.

## Features

- Scrapes drug names, types, and links from the Talk to Frank website.
- Saves extracted data in `drugs.json` (JSON format) and `drugs.yaml` (YAML format).
- Uses a user-agent header to mimic a browser request.
- Handles request failures gracefully.

## Requirements

Ensure you have Python installed (Python 3.x recommended). Install the required dependencies using:

```sh
pip install requests beautifulsoup4 pyyaml
```

## Usage
1. Clone or download this repository.
2. Run the script using:

```sh
python script.py
```

3. The script will:
   - Scrape drug information from the website.
   - Save the data to `drugs.json` and `drugs.yaml`.
   - Print the extracted information in the console.

## Output Files

- `drugs.json`: Contains the extracted drug data in JSON format.
- `drugs.yaml`: Contains the extracted drug data in YAML format.

## Code Explanation

- Sends an HTTP GET request to `https://www.talktofrank.com/drugs-a-z`.
- Parses the HTML content to extract drug names, types, and links.
- Saves the extracted data to `drugs.json` and `drugs.yaml`.
- Uses exception handling to manage request failures.

## Example Output

A sample JSON entry:

```json
[
    {
        "name": "A2",
        "type": "Piperazines",
        "link": "https://www.talktofrank.com/drug/piperazines?a=A2"
    }
]
```

## License

This project is licensed under the MIT License.

Copyright 2025, Max Base
