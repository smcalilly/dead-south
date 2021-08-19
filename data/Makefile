DATE:=$(shell date '+%Y-%m-%d')

all : output/$(DATE).json
	docker-compose run --rm app python manage.py save_the_zobot --file $<

output/$(DATE).json : intermediate/articles/article_text/$(DATE).json
	mkdir -p $(dir $@)
	python3 scripts/zobot.py $< > $@

intermediate/articles/article_text/%.json : intermediate/articles/raw_html/%.json
	mkdir -p $(dir $@)
	python3 scripts/article_text.py $< > $@

intermediate/articles/raw_html/%.json : intermediate/articles/links/%.json
	mkdir -p $(dir $@)
	python3 scripts/get_html.py $< > $@

intermediate/articles/links/%.json : intermediate/tweets/content/%.json
	mkdir -p $(dir $@)
	python3 scripts/get_links.py $< > $@

intermediate/tweets/content/%.json : intermediate/tweets/json/%.json
	mkdir -p $(dir $@)
	cat $< | jq '.[].content' | jq -s '.'  > $@

intermediate/tweets/json/$(DATE).json : 
	mkdir -p $(dir $@)
	snscrape --jsonl --since $(DATE) twitter-user Southern_Living | jq -s '.' > $@
