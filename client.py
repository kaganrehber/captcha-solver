import requests
import base64
import time

# Example endpoints (switch as needed)
BASE_URL = "https://uyg.sgk.gov.tr/vizite/welcome.do"
CAPTCHA_URL = "https://uyg.sgk.gov.tr/vizite/Captcha.jpg"

SOLVER_URL = "http://127.0.0.1:8000/solve"

def fetch_captcha(session):
    resp = session.get(CAPTCHA_URL)
    if resp.status_code != 200:
        print("Failed to fetch captcha:", resp.status_code)
        exit(1)
    return base64.b64encode(resp.content).decode("utf-8")

def main(n = 10):
    session = requests.Session()
    session.get(BASE_URL) #set cookies
    
    success = 0
    failures = 0
    results = []
    
    start = time.time()
    for i in range(n):
        img_b64 = fetch_captcha(session)
        if not img_b64:
            print("Error fetching")
            failures += 1
            continue
        
        payload = {"image_base64": img_b64}
        try:
            res = requests.post(SOLVER_URL, json=payload, timeout=10)
            if res.status_code == 200:
                text = res.json().get("text", "")
                results.append(text)
                success+=1
                print("Correct:", text)
            else:
                failures += 1
                print("False")
        except Exception as e:
            print("Error:", e)
            failures += 1
        time.sleep(1)
    
    end = time.time()
    
    print(f"\nTotal: {n}")
    print(f"Success: {success}")
    print(f"Failures: {failures}")
    print(f"Success rate: {success/n*100:.2f}%")
    print(f"Time taken: {end-start:.2f}s")
    
if __name__ == "__main__":
    main(100)
            
    
