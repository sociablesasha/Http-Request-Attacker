import requests
import urllib

def get(json):
    requests.get("url~~~", urllib.urlencode(json))

def post(json):
    requests.post("url~~~", data=json)


attacks = {"idx": "19"}
get(attacks)
attacks = {"prdcode": "1808310004", "likeCnt": "5"}
post(attacks)