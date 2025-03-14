import arxiv
from datetime import datetime, timedelta

def get_pdf_urls(doc_ids, days = 5):
    recent_pdfs = []
    recent_dates = []
    cutoff_date = datetime.now() - timedelta(days=days)

    for doc_id in doc_ids:
        search = arxiv.Search(id_list=[doc_id])
        paper = next(search.results())
        if paper.published >= cutoff_date:
            recent_pdfs.append(paper.pdf_url)
            recent_dates.append(paper.published)

    return recent_pdfs, recent_dates

import requests

def download_pdf(pdf_url, save_path):
    # Send HTTP GET request to the PDF URL
    response = requests.get(pdf_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Save PDF content to the specified file
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"PDF downloaded successfully: {save_path}")
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}")

def get_pdfs(doc_ids, root = "../"):
    urls, dates = get_pdf_urls(doc_ids)
    urls = urls[dates > 
    filenames = [root+'crier_input_pdfs/' + doc_id + '.pdf' for doc_id in doc_ids]
    for url, filename in zip(urls, filenames):
        download_pdf(url, filename)