from sqlite3db import Sqlite3DB

def test_select_id_from_position():
    db_object = Sqlite3DB("tutorial.db")
    db_object.create_table("proba")
    with pytest.raises(ValueError, match = "Запрашиваемое количество не может быть меньше нуля"):
        assert db_object.select_id_from_position("proba", "page_id", -191, -1)

    assert db_object.select_id_from_position("proba", "page_id", 191, 1)
    assert db_object.select_id_from_position("proba", "page_id", 193, 1)


