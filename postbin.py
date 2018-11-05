import requests


APIBASE = 'http://postb.in/api/'


class PostBin:
    def __init__(self):
        self.binId = requests.post(APIBASE + 'bin').json()['binId']

    def popRequest(self):
        resp = requests.get(APIBASE + 'bin/' + self.binId + '/req/shift')
        resp = resp.json()
        q = resp['query'] if 'query' in resp else {}
        b = resp['body'] if 'body' in resp else {}
        return q, b

    def delete(self):
        resp = requests.delete(APIBASE + 'bin/' + self.binId)
        return resp.json()['msg']

    def getBinURL(self):
        return 'http://postb.in/{}'.format(self.binId)

    def getWebURL(self):
        return 'http://postb.in/b/{}'.format(self.binId)


if __name__ == '__main__':
    b = PostBin()
    print('Created bin {}'.format(b.getWebURL()))

    url = b.getBinURL()
    requests.get(url, params={'text': 'GET Request'})
    requests.post(url, data={'text': 'POST Request'})

    for i in range(0, 3):
        line = b.popRequest()
        print(line)

    print(b.delete())
