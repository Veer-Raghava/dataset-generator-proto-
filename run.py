from search.browser_search import search_and_save_links
from scraper.page_scraper import scrape_links_to_jsonl

query = input("What do you want? > ")

links = search_and_save_links(query)
scrape_links_to_jsonl(query, links)
