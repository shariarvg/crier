import sys, os
import openai

from sourcer import pdf_getter, pdf_downloader, reddit_scraper, arxiv_downloader
from writer import assistant_interact as aiai
from writer.summarize import Summarizer
from email_writer import send_strings_via_email

SUB = "machinelearning"
LIMIT = 100
KEYWORD = "arxiv"
TIME_FILTER = "DAY"

with open("../crier_doc_ids_used.txt", 'r') as f:
    doc_ids_used = f.readlines()

MAX_SUMMARIES = 1

SENDER = 'shariar.vaez@gmail.com'
APP_PASSWORD = os.getenv('EMAIL_APP_PASSWORD')
RECIPIENTS = ['shariar.vaez@gmail.com']

doc_ids = reddit_scraper.get_doc_ids_sub(SUB, LIMIT, KEYWORD, TIME_FILTER)
doc_ids = [d for d in doc_ids if d not in doc_ids_used]
doc_id = doc_ids[0]

with open("../crier_doc_ids_used.txt", "a") as file:
    file.write(doc_id)

arxiv_downloader.get_pdfs([doc_id])
summarizers = []

for doc_id in doc_ids:
    s = Summarizer('asst_dHVNmQY5xj6jIqbejjQpjkSb', doc_id + '.pdf')
    s.request_content()
    summarizers.append(s)
    
for s in summarizers:
    s.get_and_save_completed_content()
    
for recipient in RECIPIENTS:
    send_strings_via_email(SENDER, APP_PASSWORD, recipient, [s.content for s in summarizers])