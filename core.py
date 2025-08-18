from sqlite3db import Sqlite3DB, ALLOWED_TABLES
from searchconfig import SearchConfig
from vk_api_worker import VKAPIRequester
import additional_functions
import time

DB_NAME = "main_db.db"
TABLE_NAME = ALLOWED_TABLES[0]


class CoreObject:
    def __init__(self):
        self.db:Sqlite3DB = Sqlite3DB(DB_NAME)
        self.db.create_table(TABLE_NAME)
        self.config:SearchConfig = SearchConfig()
        self.requester:VKAPIRequester = VKAPIRequester(self.config)


    def is_sex_match(self, sex:int)->bool:
        if self.config.sex == sex:
            return True
        return False


    def is_can_write_private_message_match(self, can_write_private_message:int)->bool:
        if self.config.can_write_private_message == can_write_private_message:
            return True
        return False


    def is_current_age_match(self, current_age:int)->bool:
        if (current_age <= self.config.max_age) and (current_age >= self.config.min_age):
            return True
        return False


    def is_relation_match(self, relation:int)->bool:
        if (relation == 0) or (relation == 1) or (relation == 6):
            return True
        return False


    def is_user_match(self, response_users_get)->bool:
        info_get = response_users_get.json().get('response')[0]
        d = {'sex': self.is_sex_match(info_get.get('sex')),
                'can_write_private_message': self.is_can_write_private_message_match(info_get.get('can_write_private_message')),
                'current_age': self.is_current_age_match(additional_functions.take_age(info_get.get('bdate'), self.config.current_year, self.config.min_age)),
                'relation': self.is_relation_match(info_get.get('relation'))
                }

        if d == {'sex':True, 'can_write_private_message': True, 'current_age':True, 'relation':True}:
            return True
        if d == {'sex':True, 'can_write_private_message': True, 'current_age':False, 'relation':True}:
            return True
        return  False


    def all_ids_scan_and_record(self, id_owner, id_item):
        response_likes_getlist, count_post_people = self.requester.request_to_post_likes_getlist(id_owner, id_item)
        for i in range(count_post_people):
            user_id = response_likes_getlist.json().get('response').get('items')[i]
            response_users_get = self.requester.request_to_post_users_get(user_id)
            time.sleep(0.1)

            if self.is_user_match(response_users_get):
                now_id = int(response_users_get.json().get('response')[0].get('id'))
                first_name = str(response_users_get.json().get('response')[0].get('first_name'))
                last_name = str(response_users_get.json().get('response')[0].get('last_name'))
                sex = int(response_users_get.json().get('response')[0].get('sex'))
                bdate = str(response_users_get.json().get('response')[0].get('bdate'))

                data = (now_id, first_name, last_name, sex, bdate, 0)
                print(data)
                self.db.add_row_to_table(TABLE_NAME, data)


    def launch_select_id_from_position(self, limit:int, shift:int)->list:
        return self.db.select_id_from_position(TABLE_NAME, "page_id", limit, shift)


if __name__ == "__main__":
    co = CoreObject()
    co.config.set_default_settings(str(input("Введите пароль:")))
    owner_id, item_id = additional_functions.enter_source_and_take_owner_and_item_ids(str(input("Введите ссылку:")))
    co.all_ids_scan_and_record(owner_id, item_id)



