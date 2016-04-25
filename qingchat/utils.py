import requests



def get(address):
    return requests.get(address)


def post(address, data):
    return requests.post(address,data)
