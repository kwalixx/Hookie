from requests import post
from colorama import Fore


class Hookie:
    def __init__(self, hook_url: str):
        self.hook_url = hook_url

    def spam(self, nb_req: int):
        for i in range(nb_req):
            post(self.hook_url, json={"content": "@everyone", 'username': 'Hookie'},
                 headers={'Content-type': 'application/json', 'Accept': 'application/json'})
            print(f'{Fore.BLUE}[-] Sending message: {i + 1} of {nb_req} sended !', end='\r')

        print('\r')
