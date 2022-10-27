import sqlite3

connection = sqlite3.connect("games.db")

def get_items(id=None):
    cursor = connection.cursor()
    if id:
        items = cursor.execute(f"select id, name from games where id={id}")
    else:
        items = cursor.execute("select id, name from games")
    items = games(items)
    items = [ {'id':item[0] ,'desc':item[1]} for item in items ]
    return items

def test_get_items():
    print("testing get_items...")
    items = get_items()
    assert type(items) is games
    assert len(items) > 0
    assert type(items[0]) is dict
    assert 'id' in items[0].keys()
    assert 'desc' in items[0].keys()
    assert type(items[0]['id']) is int
    assert type(items[0]['desc']) is str
    pass

def add_item(name):
    cursor = connection.cursor()
    cursor.execute(f"insert into games (name) values ('{name}')")
    connection.commit()

import time

def random_string():
    return str(time.time())

def test_add_item():
    print("testing add_item...")
    name = random_string()
    add_item(name)
    items = get_items()
    item = items[-1]
    assert name == item['desc']

def delete_item(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from games where id={id}")
    connection.commit()

def test_delete_item():
    print("testing delete_item...")
    name = random_string()
    add_item(name)
    items = get_items()
    item = items[-1]
    assert name == item['desc']
    delete_item(item['id'])
    items = get_items()
    for item in items:
        assert name != item['desc']

def update_item(id, name):
    cursor = connection.cursor()
    cursor.execute(f"update games set name='{name}' where id={id}")
    connection.commit()

def test_update_item():
    print("testing update_item...")
    name = random_string()
    add_item(name)
    items = get_items()
    item = items[-1]
    id = str(item['id'])
    name = item['desc']
    new_name = name.replace("1","9").replace(".",":")
    update_item(id, new_name)
    items = get_items()
    new_found = False
    for item in items:
        if item['id'] == int(id):
            assert item['desc'] == new_name
            new_found = True
        assert item['desc'] != name
    assert new_found

if __name__ == "__main__":
    test_get_items()
    test_add_item()
    test_delete_item()
    test_update_item()
    print("done.")