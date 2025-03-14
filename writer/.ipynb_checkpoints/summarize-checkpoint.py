import openai
import sys

with open("../../key.txt", 'r') as f:
    api_key = f.read().strip()

client = openai.OpenAI(api_key=api_key)


class Summarizer():
    def __init__(self, assistant_id, filepath):
        self.assistant_id = assistant_id
        self.filepath = filepath
        self.assistant = client.beta.assistants.retrieve(assistant_id)
        self.thread, self.file = self.start_thread()
        self.info = {"thread_id": self.thread.id, "file_id": self.file.id, "assistant_name": self.assistant.name, "assistant_instructions": self.assistant.instructions}
        self.content = None


    def start_thread(self, root = "../"):
        file = client.files.create(
            file=open(root + f"crier_input_pdfs/{self.filepath}", "rb"),
            purpose="assistants"
        )

        thread = client.beta.threads.create()

        return thread, file

    def send_messages(self, prompts_filepath = "writer/prompts.txt"):

        with open(prompts_filepath, 'r') as f:
            prompts = f.read().splitlines()

        messages = []
        
        message = client.beta.threads.messages.create(
                thread_id=self.thread.id,
                role="user",
                content=prompts[0],
                attachments=[{"file_id": self.file.id, "tools": [{"type": "file_search"}]}]  # Attach the uploaded PDF
            )
        messages.append(message)

        for prompt in prompts[1:]:
            message = client.beta.threads.messages.create(
                thread_id=self.thread.id,
                role="user",
                content=prompt,
            )
            messages.append(message)

        return self.info
    
    def request_content(self, prompts_filepath = "writer/prompts.txt"):
        info = self.send_messages(prompts_filepath)
        run = client.beta.threads.runs.create_and_poll(
            thread_id=self.thread.id,
            assistant_id=self.assistant_id
        )
        
        if run.status == 'completed':
            # Retrieve all messages (including assistant's responses)
            messages = client.beta.threads.messages.list(thread_id=self.thread.id)

            # Print assistant responses
            for msg in messages.data:
                if msg.role == 'assistant':
                    print(msg.content[0].text.value)
        else:
            print(f"Run failed or incomplete. Status: {run.status}")
            
    def get_completed_content(self):
        messages = client.beta.threads.messages.list(thread_id=self.thread.id)
        out = ""
        # Print assistant responses
        for msg in reversed(messages.data):
            if msg.role == 'assistant':
                out += msg.content[0].text.value
        self.content = out
        
    def save_completed_content(self, root = "../"):
        with open(root+f"crier_output_summaries/completed_{self.filepath}", 'w') as f:
            f.write(self.content)
            
    def get_and_save_completed_content(self):
        self.get_completed_content()
        self.save_completed_content()
