DATE:=$(shell date '+%Y-%m-%d')

all : data/output/$(DATE).json
	python manage.py save_the_zobot --file $<

data/output/$(DATE).json : data/intermediate/articles/article_text/$(DATE).json
	mkdir -p $(dir $@)
	python3 data/scripts/zobot.py $< > $@

data/intermediate/articles/article_text/%.json : data/intermediate/articles/raw_html/%.json
	mkdir -p $(dir $@)
	python3 data/scripts/article_text.py $< > $@

data/intermediate/articles/raw_html/%.json : data/intermediate/articles/links/%.json
	mkdir -p $(dir $@)
	python3 data/scripts/get_html.py $< > $@

data/intermediate/articles/links/%.json : data/intermediate/tweets/content/%.json
	mkdir -p $(dir $@)
	python3 data/scripts/get_links.py $< > $@

data/intermediate/tweets/content/%.json : data/intermediate/tweets/json/%.json
	mkdir -p $(dir $@)
	cat $< | jq '.[].content' | jq -s '.'  > $@

data/intermediate/tweets/json/$(DATE).json : 
	mkdir -p $(dir $@)
	snscrape --jsonl --since $(DATE) twitter-user Southern_Living | jq -s '.' > $@
