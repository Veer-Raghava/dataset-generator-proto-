from playwright.sync_api import sync_playwright
import time
from pathlib import Path

def search_and_save_links(query: str):
    safe_name = query.replace(" ", "_").lower()
    out_file = Path("links") / f"{safe_name}.txt"
    out_file.parent.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("http://localhost:8080")
        page.wait_for_selector("input[name='q']")
        page.fill("input[name='q']", query)
        page.keyboard.press("Enter")

        page.wait_for_load_state("networkidle")
        time.sleep(2)

        links = page.eval_on_selector_all(
            "a[href]",
            "els => els.map(e => e.href)"
        )

        browser.close()

    # clean + dedupe
    clean_links = sorted({
        l for l in links
        if l.startswith("http")
        and "localhost" not in l
        and "web.archive.org" not in l
    })

    out_file.write_text("\n".join(clean_links), encoding="utf-8")

    print(f"✅ Saved {len(clean_links)} links → {out_file}")
    return clean_links
