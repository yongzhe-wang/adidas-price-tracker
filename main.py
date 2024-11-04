import requests
from bs4 import BeautifulSoup
headers = {
    "Cache-Control": "max-age=0, no-cache, no-store",
    "Content-Encoding": "gzip",
    "Content-Type": "text/html; charset=utf-8",
    "Date": "Mon, 04 Nov 2024 15:12:41 GMT",
    "Expires": "Mon, 04 Nov 2024 15:12:41 GMT",
    "Pragma": "no-cache",
    "Remaining-Edge-TTL": "-1085",
    "Server-Timing": 'cdn-cache; desc=HIT, edge; dur=182, origin; dur=0, intid;desc=18896f46a4656ea0, ak_p; desc="1730733160994_398664778_1267949746_18240_53275_14_19_255";dur=1',
    "Set-Cookie": 'geo_country=US; path=/; geo_state=PA; path=/; geo_coordinates=lat=39.9524, long=-75.1642; expires=Tue, 04-Nov-2024 15:12:41 GMT; path=/; secure',
    "Strict-Transport-Security": "max-age=31536000 ; includeSubDomains ; preload",
    "Vary": "Accept-Encoding",
    "X-Akamai-Transformed": "9 1402972 0 pmb=mRUM,2",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "SAMEORIGIN",
    "X-Request-Id": "186a96ce92321b04b3b78af69a5c6f31",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Priority": "u=0, i",
    "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}
original_class_tag = ["gl-price-item gl-price-item--crossed notranslate",
                      "gl-price gl-price--horizontal notranslate"]
def get_soup(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def get_price_original(soup):
    price_found = 0
    for tag in original_class_tag:
        original_price = soup.find('div', class_=tag)
        if original_price:
            price_found = original_price.text.strip()
            break
    return price_found

def get_price_discount(soup):
    price_found = 0
    sale_price = soup.find('div', class_='gl-price-item gl-price-item--sale notranslate')
    if sale_price:
        price_found = sale_price.text.strip()
    return price_found

def get_html(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open("adidas_grand_court_shoes.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("HTML content saved as 'adidas_grand_court_shoes.html'")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

def get_sold_out_state(soup):
    state = "Not Found"
    sale_price = soup.find('h2', class_='sold-out-callout_title___1u2ms')
    if sale_price:
        state = sale_price.text.strip()
    return state

urls_list =["https://www.adidas.com/us/racer-tr23-shoes/IH2329.html"]

if __name__ == '__main__':
    for url in urls_list:
        soup_adidas = get_soup(url, headers)
        price_original = str(get_price_original(soup_adidas))
        price_discount = str(get_price_discount(soup_adidas))
        soldout = str(get_sold_out_state(soup_adidas))

        print(price_original + "  " + price_discount + "   " + soldout)
        get_html(url,headers)