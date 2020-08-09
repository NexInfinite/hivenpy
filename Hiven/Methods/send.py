import requests


def send_message(message, room_id, token, restURL):
    headers = {
        'authorization': token,
        'user-agent': 'hiven.py',
        'content-type': 'application/json'
    }

    data = '{"content": \"' + message.replace("\n", "\\n") + '\"}'

    requests.post(f'{restURL}/rooms/{room_id}/messages', headers=headers, data=data)
