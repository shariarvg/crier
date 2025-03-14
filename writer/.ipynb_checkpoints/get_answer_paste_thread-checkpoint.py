import openai

with open("../../key.txt") as f:
    api_key = f.read().strip()

client = openai.OpenAI(api_key=api_key)

messages = client.beta.threads.messages.list(thread_id="thread_BnBtmPyfKE29n4hJRUK0u9RN")

# Get the latest assistant response
assistant_messages = [msg for msg in messages.data if msg.role == "assistant"]

if assistant_messages:
    print(len(assistant_messages))
    assistant_messages = sorted(assistant_messages, key=lambda msg: msg.created_at)  # Sort by timestamp
    for message in assistant_messages:
        print(message.content[0].text.value)
else:
    print("No response from assistant yet.")
