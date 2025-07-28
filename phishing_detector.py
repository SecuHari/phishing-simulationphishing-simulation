import re
import requests
from bs4 import BeautifulSoup

def fetch_content(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response
    except Exception as e:
        print(f"[ERROR] Could not fetch URL: {e}")
        return None

def check_https(url):
    return not url.startswith('https://')

def check_ip_in_url(url):
    return bool(re.match(r'^https?://(?:\d{1,3}\.){3}\d{1,3}', url))

def check_suspicious_keywords(soup):
    text = soup.get_text().lower()
    keywords = ['login', 'password', 'account', 'credit card', 'social security number']
    return any(keyword in text for keyword in keywords)

def check_forms(soup):
    return any(form.get('method', '').lower() == 'post' for form in soup.find_all('form'))

def check_external_scripts(soup):
    return any(script.get('src') for script in soup.find_all('script', src=True))

def check_iframes(soup):
    return any(iframe.get('src') for iframe in soup.find_all('iframe', src=True))

def check_external_links(soup, domain):
    for link in soup.find_all('a', href=True):
        href = link['href']
        if not href.startswith(('/', '#')) and domain not in href:
            return True
    return False

def is_phishing(url):
    response = fetch_content(url)
    if not response:
        return False
    
    soup = BeautifulSoup(response.content, 'html.parser')
    domain = re.sub(r'^https?://(www\.)?', '', url).split('/')[0]

    checks = {
        'No HTTPS': check_https(url),
        'IP Address in URL': check_ip_in_url(url),
        'Suspicious Keywords': check_suspicious_keywords(soup),
        'Form with POST': check_forms(soup),
        'External Script': check_external_scripts(soup),
        'Iframe Tag': check_iframes(soup),
        'External Links': check_external_links(soup, domain),
    }

    phishing_detected = any(checks.values())

    print("\n=== Phishing Detection Report ===")
    for reason, triggered in checks.items():
        print(f"{reason}: {'⚠️ YES' if triggered else '✅ NO'}")

    if phishing_detected:
        print("⚠️ Phishing characteristics detected.\n")
    else:
        print("✅ Webpage is likely safe.\n")

    return phishing_detected
