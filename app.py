from datetime import datetime
from flask import Flask, render_template, request, make_response, redirect
import sqlite3


# Steps with commands for creating table "posts":
# 1. ./env/Scripts/activate
# 2.sqlite3 blog.sqlite
# 3.CREATE TABLE POSTS(Id integer primary key AUTOINCREMENT, Title text, Description text, Date text);

app = Flask(___name___)

@app.route('/')
@app.route('/show')
def show():
    """Страница для отображения всех сообщений в блоге. Он отображается в шаблоне
    вся информация о каждом посте (должности). Информация включает
    ID, титул, описание, время, когда этот пост был отредактирован."""
    connection = sqlite3.connect("blog.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM posts")
    fields = cursor.fetchall()
    connection.close()
    return render_template('show.html', fields=fields)

@app.route('/add', methods=['GET', 'POST'])
def get_title():
    """На странице отображается форма для ввода титула и описания новой должности.
    Система добавляет созданную позицию в блог под новым эксклюзивным идентификатором.
    После добавления новой позиции с идентификатором, названием, описанием и текущим временем,
    система перенаправляет пользователя на обновленную страницу со всеми сообщениями в блоге."""
    if request.method == 'GET':
        response = make_response(render_template('add.html'))
    elif request.method == 'POST':
        tittle = request.form['Tittle']
        description = request.form['Description']
        if not tittle:
            return 'Sorry, you should insert tittle'
        if not description:
            return 'Sorry, you should insert description'
        now = datetime.now()
        date = now.strftime("%d/%m/%Y %H:%M:%S")
        connection = sqlite3.connect("blog.sqlite")
        cursor = connection.cursor()
        values = (tittle, description, date)
        cursor.execute("""insert into POSTS ( Title,Description,Date)
                   VALUES               (  ?,             ?,             ? )""",
                       values)
        connection.commit()
        connection.close()
        response= redirect("/show")
    return response

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    """TЭта страница предоставит пользователю доступ к обновлению названия и описания любой существующей позиции в блоге.
    На странице отображается форма для ввода существующего идентификатора блога и формы для обновления названия и описания.
    Если введенный идентификатор имеет соответствующую позицию в блоге, система обновит информацию о публикации и перенаправит пользователя
    на обновленную страницу со всеми сообщениями в блоге."""
    if request.method == 'GET':
        response = make_response(render_template('edit.html'))
    elif request.method == 'POST':
        tittle = request.form['Tittle']
        description = request.form['Description']
        id = request.form['ID']
        now = datetime.now()
        date = now.strftime("%d/%m/%Y %H:%M:%S")
        connection = sqlite3.connect("blog.sqlite")
        cursor = connection.cursor()
        values = (tittle, description, date, id)
        cursor.execute("""UPDATE POSTS SET Title = ?,Description = ?,Date= ? WHERE id = ?;""",
                       values)
        connection.commit()
        connection.close()
        response= redirect("/show")
    return response

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    """Эта страница удалит сообщение со всей информацией под существующим идентификатором этого пользователя.
    войдет в форму. После удаления сообщений система перенаправит пользователя в обновленный
    страница со всеми сообщениями в блоге."""
    if request.method == 'GET':
        response = make_response(render_template('delete.html'))
    elif request.method == 'POST':
        id = request.form['ID']
        connection = sqlite3.connect("blog.sqlite")
        cursor = connection.cursor()
        cursor.execute('''DELETE FROM POSTS WHERE Id = ?''', (id))
        connection.commit()
        connection.close()
        response= redirect("/show")
    return response



if __name__ == '__main__':
    app.run(debug=True,)