from openai import OpenAI

from core.tools.logger import Logger
from core.tools.get_token import get_token

log = Logger()

class Chatbot:


    def __init__(self):
        self.model = 'gpt-4o'
        self.base_url = 'https://api.proxyapi.ru/openai/'
        self._conversation_history = {}

    def trim_history(self, history: dict = None, max_length=4096) -> dict:
        current_length = sum(len(message["content"]) for message in history)
        while history and current_length > max_length:
            removed_message = history.pop(0)
            current_length -= len(removed_message["content"])

        return history

    def clear(self, user_id):
        self._conversation_history = []

    def send_message(self, message, user_id):
        if user_id not in self._conversation_history:
            self._conversation_history[user_id] = []

        self._conversation_history[user_id].append({"role": 'user', "content": message})
        self._conversation_history[user_id] = self.trim_history(self._conversation_history[user_id])

        gpt_response = None
        chat_history = self._conversation_history[user_id]
        print(chat_history)
        try:
            client = OpenAI(
                api_key=get_token('ProxyAPI', 'token'),
                base_url=self.base_url + 'v1'
            )
            response = client.chat.completions.create(model=self.model, messages=chat_history, max_tokens=3000)
            gpt_response = response
            print(gpt_response)
        except Exception as e:
            log.error(e)
        self._conversation_history[user_id].append(dict(role="assistant", content=gpt_response))
        return gpt_response
