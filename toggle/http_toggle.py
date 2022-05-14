from toggle.toggle import Toggle
import requests


class HttpToggle(Toggle):

    def __init__(self, id, method, url):
        self.id = id
        self.method = method
        self.url = url

    def execute(self, args):
        response = requests.request(self.method, self.url)

        return "{}: DONE! ({})".format(self.id, response.text)
