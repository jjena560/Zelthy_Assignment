import requests
import json
from urllib.parse import quote

# api-endpoint


def dict(language_code, word):

    # lc = quote(language_code)
    # w = quote(word)
    url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/hello"

    # url_template = "{}{}".format(language_code, word)

    # I DON't knwo why dynamic params are not working with this api

    response = requests.get(url)

    result = json.loads(response.content)
    meaning = ''

    for i in result:
        mean = (i['meanings'])

    for j in mean:
        meaning = j['definitions'][0]

    return meaning


en_us = 'en_US'
print(dict('en_US', 'hello'))
