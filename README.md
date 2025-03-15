# crier
My OpenAI Assistant that sends me a daily pop science newsletter. 

Every day at 8 a.m.:
* Scrapes all r/machinelearning posts from previous day that contain an arXiv link (checking that the article was published in the last 5 days)
* Writes a pop-science style summary about each preserved article (using OpenAI agent)
* Sends me an email with links to the PDF's

To-do
* Find other subreddits that typically mention arXiv posts
* Incorporate other publication venues (besides arXiv)
* Other approach: just scrape from arXiv directly and have another assistant that chooses the coolest headline to focus on
* Improve the prompt so the article styles are cool. Alternative approach: write a list of prompts to choose from so style differs by day
* Allow the newsletter to send rich text
