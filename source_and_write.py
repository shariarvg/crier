import sys, os
import openai

from sourcer import pdf_getter, pdf_downloader, reddit_scraper, arxiv_downloader
from writer import assistant_interact as aiai
from writer.summarize import Summarizer

SUB = "machinelearning"
LIMIT = 100
KEYWORD = "arxiv"
TIME_FILTER = "DAY"

MAX_SUMMARIES = 1


doc_ids = reddit_scraper.get_doc_ids_sub(SUB, LIMIT, KEYWORD, TIME_FILTER)
doc_ids = doc_ids[:MAX_SUMMARIES]

arxiv_downloader.get_pdfs(doc_ids)
summarizers = []

for doc_id in doc_ids:
    s = Summarizer('asst_dHVNmQY5xj6jIqbejjQpjkSb', doc_id + '.pdf')
    s.request_content()
    summarizers.append(s)
    
for s in summarizers:
    s.get_and_save_completed_content()