'''
Lab 2, Task 2. Archakov Vsevolod.
'''
import requests


def twitter_get_friend_list(username: str) -> dict:
    """
    Get json with friends by username from twitter.
    """
    reqest_url = "https://api.twitter.com/1.1/friends/list.json"
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAEMUNAEAAAAALiiYRGBM1bAuk5SG3CcMokTqTCk%3DtrUF8xGO2dBSvMGiWWQlv5Vm0DvLcdibTMqyLv4zVv14a7Rze7"

    headers = {
        'Authorization': 'Bearer {}'.format(bearer_token)
    }

    params = {
        'screen_name': f'@{username}',
        'count': 15
    }

    response = requests.get(
        reqest_url, headers=headers, params=params)

    return response.json()['users']


def search_by_keys(search_item):
    if isinstance(search_item, dict):
        for key in search_item.keys():
            print(key + '\n')

        search_key = ''
        count = 0
        while search_key not in search_item:
            if count > 0:
                print('There is no such key!!!')
            count += 1
            search_key = input(
                'Enter one of the keys which you can see above: ')

        search_by_keys(search_item[search_key])

    elif isinstance(search_item, list):
        search_index = -1
        count = 0
        while search_index not in range(0, len(search_item)):
            if count > 0:
                print('Wrong index!!!')
            count += 1
            search_index_str = input(
                'Enter the index of element you want to see: ')
            try:
                search_index = int(search_index_str)
            except:
                search_index = -1

        search_by_keys(search_item[search_index])

    else:
        print(search_item)
        exit()


if __name__ == '__main__':
    username = input('Type a twitter nickname (without @) ')

    friend_list = twitter_get_friend_list(username)

    search_by_keys(friend_list)
