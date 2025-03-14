import praw

reddit = praw.Reddit(
    client_id='KLBeMAiqwWYtnZV9k0LI4Q',
    client_secret='ZAZbrGYK8hti4ISSZOZ3INq9Y3bgCg',
    user_agent='arxiv_scraper'
)

def get_posts_sub(sub, limit, keyword, time_filter = 'day'):
    subreddit = reddit.subreddit(sub)

    all_text = []
    query = 'flair:"Research"'
    for post in subreddit.search(query=query, sort='relevance', limit=limit):
        if keyword in post.selftext:
            all_text.append(post.selftext)

    return all_text

def get_doc_id_from_text(text):
    ind = text.index('https://arxiv.org/abs/')
    start = ind + len('https://arxiv.org/abs/')
    return text[start:start + 10]

def get_doc_ids_sub(sub, limit, keyword, time_filter = 'day'):
    all_posts = get_posts_sub(sub, limit, keyword, time_filter)
    all_ids = []
    for post in all_posts:
        try:
            all_ids.append(get_doc_id_from_text(post))
        except:
            pass
    return all_ids