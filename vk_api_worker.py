import requests as rq
from searchconfig import SearchConfig


class VKAPIRequester:
    def __init__(self, config:SearchConfig):
        self.config:SearchConfig = config


    def request_to_post_likes_getlist(self, owner_id, item_id):
        source_metod = "https://api.vk.com/method/likes.getList"
        response = rq.get(source_metod,
                            params = {
                                'access_token': self.config.token,
                                'v': self.config.version,
                                'owner_id': owner_id,
                                'item_id': item_id,
                                'count': self.config.count,
                                'type':"post",
                            })
        print(response.json())
        count_post_people = response.json().get('response').get('count')
        if count_post_people > self.config.count: # если количество всех людей больше указанного количества
            count_post_people = self.config.count # то приравниваем максимальное кол-во к указанному
                                      # после цикл идет по максимальному кол-ву
        return response, count_post_people


    def request_to_post_users_get(self, user_id:int):
        source_metod = "https://api.vk.com/method/users.get"
        response = rq.get(source_metod,
                      params={
                          'access_token': self.config.token,
                          'v': self.config.version,
                          'user_ids': user_id,
                          'fields': 'bdate, sex, relation, can_write_private_message, friends, counters'
                      })
        return response