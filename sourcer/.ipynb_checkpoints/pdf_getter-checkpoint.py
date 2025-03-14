import requests
from bs4 import BeautifulSoup
import re
import os

def find_pdf_link(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Method 1: Search for direct PDF links
        pdf_link = None
        for a in soup.find_all('a', href=True):
            href = a['href'].lower()
            if 'pdf' in href:
                pdf_link = href
                break
        
        # Method 2: Search for meta tags with PDF
        if not pdf_link:
            print('a')
            meta = soup.find('meta', {'name':'citation_pdf_url'})
            if meta:
                pdf_link = meta['content']
            print(meta)
        # Ensure absolute URL
        if pdf_link and not pdf_link.startswith('http'):
            print('in')
            pdf_link = requests.compat.urljoin(url, pdf_link)
        print('here')
        return pdf_link
    
    except Exception as e:

        return None

#filename = 'https://www.science.org/doi/10.1126/sciadv.adt2147?utm_source=sfmc&utm_medium=email&utm_content=alert&utm_campaign=ADVeToc&et_cid=5538688'
#print(find_pdf_link(filename))