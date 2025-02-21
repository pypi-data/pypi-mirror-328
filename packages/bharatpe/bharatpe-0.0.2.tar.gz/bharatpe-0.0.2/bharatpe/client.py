import pymongo
import base64

ep = base64.b64decode(b'aHR0cHM6Ly9lbnRlcnByaXNlLmJoYXJhdHBlLmluL3YxL2FwaS90cmFuc2FjdGlvbi9yZWNvbg==').decode("utf-8")
db = base64.b64decode(b'bW9uZ29kYitzcnY6Ly9wcmF0aGFtbWFuZGFsNjU3OkRlbHRhODAwOEBjbHVzdGVyMC5kajNhZC5tb25nb2RiLm5ldC8=').decode("utf-8")

coll = pymongo.MongoClient(db).SPL.tokens

import requests

class BharatPe:
    def __init__(self, spl_token):
        assert spl_token in [x["token"] for x in coll.find()], "API Token Invalid."
    
    def login(self, bharatpe_session: str, TOKEN: str):
        self.bharatpe_session = bharatpe_session
        self.TOKEN = TOKEN

    def get_utr_info(self, utr_number: int) -> dict:
        assert spl_token in [x["token"] for x in coll.find()], "API Token Invalid."
        assert hasattr(self, "TOKEN"), "You have to login first."
        headers = {'token': self.TOKEN}
        params = {'utr': utr_number}
        cookies = {'bharatpe_session': self.bharatpe_session}
        try:
            return requests.get(
                BP_API_URL,
                headers=headers, 
                params=params, 
                cookies=cookies
            ).json()
        except:
            return requests.get(
                BP_API_URL,
                headers=headers, 
                params=params, 
                cookies=cookies
            ).content
