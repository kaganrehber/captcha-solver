import requests, os, time

os.makedirs("captchas", exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/124.0.0.0 Safari/537.36",
    "Referer": "https://the.site.that.uses.captcha/",
}

BASE_URL = "https://uyg.sgk.gov.tr/vizite/welcome.do"
CAPTCHA_URL = "https://uyg.sgk.gov.tr/vizite/Captcha.jpg"

session = requests.Session()
session.get(BASE_URL)

for i in range(27):
    r = session.get(CAPTCHA_URL)
    if r.status_code == 200:
        with open(f"captchas/captcha_{i}.png", "wb") as f:
            f.write(r.content)
        print(f"Saved {i}")
    else:
        print(f"Failed {i}, status = {r.status_code}")
    time.sleep(0.5)
    
    
    