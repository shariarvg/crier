import requests
from bs4 import BeautifulSoup
import re
import os

def download_pdf(pdf_url, filename):
    response = requests.get(pdf_url, headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f'Downloaded: {filename}')
    else:
        print(f'Failed to download {pdf_url}')
