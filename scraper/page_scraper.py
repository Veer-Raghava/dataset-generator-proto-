import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_links_to_jsonl(query: str, links: list[str]):
    safe_name = query.replace(" ", "_").lower()
    out_file = Path("data") / f"{safe_name}.jsonl"
    out_file.parent.mkdir(exist_ok=True)

    with out_file.open("w", encoding="utf-8") as f:
        for url in links:
            try:
                r = requests.get(url, headers=HEADERS, timeout=10)
                soup = BeautifulSoup(r.text, "html.parser")

                text = " ".join(
                    p.get_text(strip=True)
                    for p in soup.find_all("p")
                )

                if len(text) < 300:
                    continue  # trash page

                record = {
                    "source": url,
                    "query": query,
                    "text": text[:8000]  # cap for sanity
                }

                f.write(json.dumps(record, ensure_ascii=False) + "\n")
                print(f"🟢 scraped: {url}")

            except Exception as e:
                print(f"🔴 failed: {url} | {e}")
