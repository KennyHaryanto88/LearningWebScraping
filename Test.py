import requests
from bs4 import BeautifulSoup

url = 'https://www.tokopedia.com/corsair-official?product_id=316427368&source=pdp&t_id=1726817574819&t_st=5&t_pp=product_detail&t_efo=search_pure_goods_card&t_ef=goods_search&t_sm=&t_spt=search_result'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

timeout = 10

response = requests.get(url, headers=headers, timeout=timeout)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Gagal mendapatkan halaman, kode status: {response.status_code}")