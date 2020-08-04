import requests


class GetUser:
    def __init__(self, username, outer):
        headers = {
            'user-agent': 'hiven.py',
        }

        r = requests.get(f'{outer.restURL}/users/{username.lower()}', headers=headers).json()
        if r['success']:
            data = r['data']
            self.success = True
            self.id = data['id']
            self.name = data['name']
            self.username = data['username']
            self.user_flags = data['user_flags']
            self.bot = data['bot']
            self.location = data['location']
            self.website = data['website']
            self.bio = data['bio']
        else:
            self.success = False
