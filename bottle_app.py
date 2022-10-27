from bottle import default_app, route, get, post, template, request, redirect
import sqlite3

connection = sqlite3.connect("games.db")

@route('/')
def hello_world():
    return 'Hello from nihash'

@route('/hi')
def hi_world():
    return 'Hi from nihash'

@route('/bye')
def bye_world():
    return 'Bye from nihash'

@route('/list')
def get_list():
    cursor = connection.cursor()
    rows = cursor.execute("select id, name from games")
    rows = list(rows)
    rows = [ {'id':row[0] ,'desc':row[1]} for row in rows ]
    return template("games.tpl", name="nihash", games=rows)

@get('/add')
def get_add():
    return template("add_item.tpl")

@post('/add')
def post_add():
    name = request.forms.get("name")
    cursor = connection.cursor()
    cursor.execute(f"insert into games (name) values ('{name}')")
    connection.commit()
    redirect('/list')

@route("/delete/<id>")
def get_delete(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from games where id={id}")
    connection.commit()
    redirect('/list')

@get("/edit/<id>")
def get_edit(id):
    cursor = connection.cursor()
    items = cursor.execute(f"select name from games where id={id}")
    items = list(items)
    if len(items) != 1:
        redirect('/list')
    name = items[0][0]
    return template("edit_item.tpl", id=id, name=name)

@post("/edit/<id>")
def post_edit(id):
    name = request.forms.get("name")
    cursor = connection.cursor()
    cursor.execute(f"update games set name='{name}' where id={id}")
    connection.commit()
    redirect('/list')


application = default_app()
