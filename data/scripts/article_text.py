import sys
import json
import lxml.html


filename = sys.argv[1]

output = []

with open(filename) as f:
    data = json.load(f)

for article in data:
    html = lxml.html.fromstring(article['html'])

    article_title = html.xpath('//title/text()')

    article_text = html.xpath('//p/text()')
    article_text = []
    for div in html.cssselect('div.paragraph'):
        article_text.append(div.text_content())

    if article_text:
        output.append({
            'source_url': article['source_url'],
            'text': article_text,
            'title': article_title
        })

json.dump(output, sys.stdout)