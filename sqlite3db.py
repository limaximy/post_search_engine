import sqlite3 as s3

ALLOWED_TABLES = ["main_table"]
ALLOWED_ROWS = ["page_id", "name", "surname", "gender", "birth_data", "matching_by_date", "matching_by_end"]


class Sqlite3DB:
    def __init__(self, db_name:str):
        self.name:str = db_name
        self.con: s3.Connection = s3.connect(self.name, check_same_thread=False)
        self.cur: s3.Cursor = self.con.cursor()


    def __del__(self):
        if self.con:
            self.con.commit()
            self.con.close()


    def is_connection(self)->bool:
        if self.con:
            return True
        return False


    def disconnect_by_hand(self):
        if self.con:
            self.con.commit()
            self.con.close()


    def create_table(self, table_name:str):
        if table_name not in ALLOWED_TABLES:
            raise ValueError("Недопустимое название таблицы")

        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (page_id INTEGER, name TEXT, surname TEXT, gender INTEGER, birth_data TEXT, matching INTEGER)")
        self.con.commit()


    def add_row_to_table(self, table_name:str, columns_values:tuple):
        if table_name not in ALLOWED_TABLES:
            raise ValueError("Недопустимое название таблицы")

        self.cur.execute(f"INSERT INTO {table_name} VALUES (?,?,?,?,?,?)", columns_values)
        self.con.commit()


    def delete_row_from_table(self, table_name:str, column_name:str, row_value:str):
        if table_name not in ALLOWED_TABLES:
            raise ValueError("Недопустимое название таблицы")
        if column_name not in ALLOWED_ROWS:
            raise ValueError("Недопустимое название столбца")

        self.cur.execute(f"DELETE FROM {table_name} WHERE {column_name} = ?", (row_value,))
        self.con.commit()


    def update_row_from_table(self, table_name:str, column_name:str, column_for_search_name:str, update_element, element_for_search):
        if table_name not in ALLOWED_TABLES:
            raise ValueError("Недопустимое название таблицы")
        if column_name not in ALLOWED_ROWS or column_for_search_name not in ALLOWED_ROWS:
            raise ValueError("Недопустимое название столбца")

        self.cur.execute(f"UPDATE {table_name} SET {column_name} = ? WHERE {column_for_search_name} = ?", (update_element, element_for_search,))
        self.con.commit()


    def select_row_from_table(self, table_name:str, column_for_take_name:str, column_for_search_name:str, element_for_search):
        if table_name not in ALLOWED_TABLES:
            raise ValueError("Недопустимое название таблицы")
        if column_for_take_name not in ALLOWED_ROWS or column_for_search_name not in ALLOWED_ROWS:
            raise ValueError("Недопустимое название столбца")

        response = self.cur.execute(f"SELECT {table_name} FROM {column_for_take_name} WHERE {column_for_take_name} = ?", (element_for_search,))
        return response.fetchall()


    def select_id_from_position(self, table_name:str, column_for_take_name:str, limit:int, shift:int)->list:
        if table_name not in ALLOWED_TABLES:
            raise ValueError("Недопустимое название таблицы")
        if column_for_take_name not in ALLOWED_ROWS:
            raise ValueError("Недопустимое название столбца")

        response_count = self.cur.execute(f"SELECT COUNT(*) FROM {table_name}")
        count:int = response_count.fetchone()[0]

        if limit < 1:
            raise ValueError(f"Запрашиваемое количество не может быть меньше нуля")
        if shift < 0:
            raise ValueError(f"Сдвиг не может быть отрицательным")
        if (count - shift) < limit:
            raise ValueError(f"Недопустимый сдвиг или получаемое количество. Количество строк в таблице = {count}")

        response = self.cur.execute(f"SELECT {column_for_take_name} FROM {table_name} LIMIT ? OFFSET ?", (limit, shift,))
        return response.fetchall()



if __name__ == "__main__":
    db_object = Sqlite3DB("tutorial.db")
    db_object.create_table("proba")
    rp = db_object.select_id_from_position("proba", "page_id", -191, -1)

    print(rp)
    print(type(rp))

    rp2 = db_object.select_id_from_position("proba", "page_id", 192, 0)
    print(rp2)
    print(type(rp2))

    print(rp == rp2)