import openai
import sys

def request_content(client, thread_id, prompt):
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=prompt
    )
    return message

def poll_done(client, thread_id, run_id):
    run_status = client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id
    )
    if run_status.status == "completed":
        return True
    else:
        return False

def get_content(client, thread_id, run_id, check_finished = True):
    if check_finished:
        assert poll_done(client, thread_id, run_id) == True, "Still waiting for responses to complete"
    return client.beta.threads.messages.list(thread_id=thread_id)

