import unittest

from automon.integrations.ollamaWrapper import OllamaClient
from automon.helpers.osWrapper import environ

from automon.helpers.loggingWrapper import LoggingClient

LoggingClient.logging.getLogger('httpx').setLevel(LoggingClient.ERROR)
LoggingClient.logging.getLogger('httpcore').setLevel(LoggingClient.ERROR)
LoggingClient.logging.getLogger('automon.integrations.ollamaWrapper.client').setLevel(LoggingClient.DEBUG)
LoggingClient.logging.getLogger('automon.integrations.ollamaWrapper.chat').setLevel(LoggingClient.ERROR)
LoggingClient.logging.getLogger('opentelemetry.instrumentation.instrumentor').setLevel(LoggingClient.ERROR)


class TestOllamaClient(unittest.TestCase):
    def test_chat(self):
        model = OllamaClient()
        model.STREAM = True

        if not model.is_ready() or not environ('RUN'):
            return

        RAG = open('RAG.txt', 'r').read()
        RESUME = open('RESUME.txt', 'r').read()

        model.add_chain(
            f"You are a user talking to a tech recruiter. "
            f"The user provides a resume: {RESUME}. \n\n"
            f"The recruiter provides a job: {RAG}, \n\n"
            f"Respond in first person as the user. "
            f"In one paragraph, give me the percentage of how relevant the user's resume is to the recruiter's job, and a short summary if you would apply for this job. "
            f"Include a link to my AVAILABILITY found in the resume. "
            f"Format the output in email format. "
            f"Give me three versions. "
        ).chat()


if __name__ == '__main__':
    unittest.main()
