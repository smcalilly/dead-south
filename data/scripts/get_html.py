import sys
import json
import re
from urllib.parse import urljoin, urlparse
import requests
import lxml.html

filename = sys.argv[1]
with open(filename) as f:
    data = json.load(f)

sample_urls = data[0:10]

output = []

for i, url in enumerate(sample_urls):

    r = requests.get(url)
    source_url = urljoin(r.url, urlparse(r.url).path)
    html = lxml.html.fromstring(r.text)

    json_text = html.xpath('//script[@type="application/ld+json"]/text()')
    if json_text:
        food = re.search(r'"name": "food"', json_text[0])
        recipes = re.search(r'"name": "Recipes"', json_text[0])
        skip_content = [food, recipes]

        if any(skip_content):
            continue

    output.append({
                'source_url': source_url,
                'html': lxml.html.tostring(html).decode('utf-8')
            })

json.dump(output, sys.stdout, indent=4)