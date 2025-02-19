import os
import requests


class GnistAI:
    def __init__(self, api_key: str | None = None):
        if api_key:
            self.api_key = api_key
        else:
            self.api_key = os.environ["GNISTAI_API_KEY"]
    
    def health_check(self):
        return requests.get("https://gnist.ai/api/health-check").json()
