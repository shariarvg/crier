import praw

reddit = praw.Reddit(
    client_id='KLBeMAiqwWYtnZV9k0LI4Q',
    client_secret='ZAZbrGYK8hti4ISSZOZ3INq9Y3bgCg',
    user_agent='arxiv_scraper'
)

subreddit = reddit.subreddit('science')

for post in subreddit.top(time_filter='day', limit=500):
    if 'arxiv' in post.url:
        print(post.url)
