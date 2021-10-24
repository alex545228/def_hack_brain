import requests
from time import sleep

token = 'токен'


def search_groups(category, count=5):
    """Поиск групп по ключевому слову.
    Параметром count задается необходимое число групп.
    Возвращается словарь"""

    response = requests.get('https://api.vk.com/method/groups.search',
                            params={
                                'q': category,
                                'count': count,
                                'access_token': token,
                                'v': 5.81
                            })
    data = response.json()['response']['items']
    return data


def get_group_info(group_id):
    """Возвращает информацио о сообществе.
    Fields возможно расширить, получив больше инормации о сообществе"""
    
    response = requests.get('https://api.vk.com/method/groups.getById',
                            params={
                                'group_id': group_id,
                                'fields': 'activity',
                                'access_token': token,
                                'v': 5.81
                            })
    data = response.json()['response'][0]['activity']
    return data


def get_max_offset(group):
    """Возвращает количество участников сообщества. Истользуется запрос к API, результат делим
    на 1000, т.к. это максимальное число участников, чьи данные можно получить.
    Может произойти слующая ситуация:
    - у сообщества заккрыты участники, соответственно получаем ошибку."""

    count = requests.get('https://api.vk.com/method/groups.getMembers',
                         params={
                             'group_id': group,
                             'sort': 'id_desc',
                             'offset': 0,
                             'fields': 'last_seen, activity',
                             'access_token': token,
                             'v': 5.81
                         })
    data = count.json()['response']['count']
    print(data)
    sleep(0.34)
    return data // 1000


def get_members(group_id):
    """Возвращает данные всех участников сообщества. Собираем по 1000 пользователей, потом обновляем
    offset. Максимальный offset находится по функции get_max_offset. Возвращается список со словарями."""

    main_data = []
    offset = 0
    count = 1000
    max_offset = get_max_offset(group_id)
    while offset < max_offset:
        response = requests.get('https://api.vk.com/method/groups.getMembers',
                                params={
                                    'group_id': group_id,
                                    'offset': offset,
                                    'count': count,
                                    'fields': 'first_name, last_name, sex, bdate, country, city, contacts',
                                    'access_token': token,
                                    'v': 5.81
                                })
        mean_data = response.json()['response']
        main_data.append(mean_data)
        sleep(0.34)
        offset += 1000
    return main_data
