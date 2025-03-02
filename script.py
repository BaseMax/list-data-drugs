import requests
import json
import yaml
from bs4 import BeautifulSoup

def extract_drug_list():
    url = "https://www.talktofrank.com/drugs-a-z"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch page, status code: {response.status_code}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    drug_items = []
    
    for li in soup.find_all("li", class_="list-item list-item--underlined"):
        a_tag = li.find("a", class_="list-link cursor-pointer")
        if a_tag:
            drug_name = a_tag.find("h3", class_="list-link__title").get_text(strip=True)
            drug_type = a_tag.find("p", class_="grey d-inline-block").get_text(strip=True).replace("(", "").replace(")", "")
            link = a_tag["href"]
            drug_items.append({"name": drug_name, "type": drug_type, "link": f"https://www.talktofrank.com{link}"})
    
    return drug_items

drug_list = extract_drug_list()

with open("drugs.json", "w", encoding="utf-8") as json_file:
    json.dump(drug_list, json_file, ensure_ascii=False, indent=4)

with open("drugs.yaml", "w", encoding="utf-8") as yaml_file:
    yaml.dump(drug_list, yaml_file, allow_unicode=True, default_flow_style=False)

for drug in drug_list:
    print(drug)