import openai

with open("../../key.txt") as f:
    api_key = f.read().strip()

client = openai.OpenAI(api_key=api_key)

# Create an assistant with instructions
assistant = client.beta.assistants.create(
    name="Article Summarizer",
    instructions=(
        "You are an AI that writes pop science articles about new research. "
        "Given the PDF of an article, you are meant to provide an article that is both entertaining and accessible."
        "Your readers are generally interested in science, and are college-educated, but may not be knowledgeable about the exact discipline of the article. It's important to make use of the related work section of your article to provide an accessible background on the problem and past solutions"
    ),
    model="gpt-4-turbo",
    tools=[{"type": "file_search"}]  # Enables file searching
)

print("Assistant ID:", assistant.id)  # Store this ID for later reuse
