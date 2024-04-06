#  работа с ягпт

import requests
import json
import os
from pprint import pprint

from config import IAM_TOKEN, APY_KEY

with open('gpt/body.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
f.close()
data['modelUri'] = "gpt://" + IAM_TOKEN + "/yandexgpt-lite"
with open('gpt/body.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
f.close()


headers = {
    'Authorization': f'Api-Key {APY_KEY}',
}

def gpt(text):
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
    with open('gpt/body.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    f.close()
    data['messages'][3]['text'] = text
    with open('gpt/body.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    f.close()
    with open('gpt/body.json', 'r', encoding='utf-8') as f:
        data = json.dumps(json.load(f))
    resp = requests.post(url, headers=headers, data=data)

    if resp.status_code != 200:
        raise RuntimeError(
            'Invalid response received: code: {}, message: {}'.format(
                {resp.status_code}, {resp.text}
            )
        )
    return resp.json()['result']['alternatives'][0]['message']['text']
