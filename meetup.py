import json, requests

url = 'https://api.meetup.com/activity.json'

params = dict(
    member_id='206692101',
    key=meetup_key
)

def extract_meetup_group_names():
    resp = requests.get(url=url, params=params)
    json_object = resp.json()

    groups = []
    for result in json_object['results']:
        groups.append(result['group_name'])
    new_list = list(set(groups))
    return new_list

print extract_meetup_group_names()
