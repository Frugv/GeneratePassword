from flask import Flask, render_template, request, redirect
from config_ import Config
from form import LoginForm
from formpass1 import FormPass1
from formpass2 import FormPass2
import sqlite3, random, math

app = Flask(__name__)
app.config.from_object(Config)

connect = sqlite3.connect('password.db')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS password 
    (id INTEGER,
    nameSN TEXT,
    loginSN TEXT,
    lengthpass INTEGER,
    password TEXT)""")
connect.commit()
cursor.close()

@app.route('/form', methods=['GET'])
def login():
    form = LoginForm()
    return render_template('LoginForm.html', title='Генерация пароля', form=form)

@app.route('/generation', methods=['POST', 'GET'])
def generation():
    if request.method == 'POST':
        connect = sqlite3.connect('password.db')
        cursor = connect.cursor()
        cursor.execute(''' INSERT INTO password (nameSN, loginSN, lengthpass) VALUES(?,?,?)''',
                       (request.form['Название соц.сети'], request.form['Логин соц.сети'], request.form['Длина пароля']))
        connect.commit()
        cursor.close()
        if (request.form['choice'] == 'Да'):
            if (request.form['specsimbol'] == 'Да'):
                form = FormPass1()
                return render_template('FormPass1.html', title='Данные для создания пароля', form=form)
            else:
                form = FormPass2()
                return render_template('FormPass2.html', title='Данные для создания пароля', form=form)
        if (request.form['choice'] == 'Нет'):
            if (request.form['specsimbol'] == 'Да'):
                return redirect('/generatess')
            else:
                return redirect('/generatewss')

@app.route('/generatess', methods=['POST', 'GET'])
def generatess():
    form = FormPass1()
    if request.method == 'GET':
        connect = sqlite3.connect('password.db')
        cursor = connect.cursor()
        cursor.execute("""SELECT id, lengthpass FROM password ORDER BY id DESC LIMIT 1;""")
        for i in cursor.fetchall():
            id = i[0]
            length = i[1]
        specsimbol = '+-/*!&$#?=@<>'
        bigletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        litletters = 'abcdefghijklnopqrstuvwxyz'
        number = '1234567890'
        for n in range(length):
            password = ''
            for i in range(math.floor(length/4)):
                password += random.choice(specsimbol)
            for i in range(math.floor(length/4)):
                password += random.choice(bigletters)
            for i in range(math.floor(length/4)):
                password += random.choice(litletters)
            for i in range(length - math.floor(length/4)*3):
                password += random.choice(number)
        password = "".join(random.sample(password, len(password)))
        cursor.execute('''UPDATE password SET password=? WHERE id=?''', (password, id,))
        cursor.execute("""SELECT nameSN,loginSN,password FROM password ORDER BY id DESC LIMIT 1;""")
        value = []
        for i in cursor.fetchall():
            value.append(i[0])
            value.append(i[1])
            value.append(i[2])
        connect.commit()
        cursor.close()
        return render_template('result.html', list=value)

    if request.method == 'POST':
        connect = sqlite3.connect('password.db')
        cursor = connect.cursor()
        cursor.execute("""SELECT id, lengthpass FROM password ORDER BY id DESC LIMIT 1;""")
        for i in cursor.fetchall():
            id = i[0]
            length = i[1]
        specsimbol = '+-/*!&$#?=@<>'
        bigletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        litletters = 'abcdefghijklnopqrstuvwxyz'
        number = '1234567890'
        quatityss = int(request.form["Количество спецсимволов"])
        quatitybl = int(request.form["Количество больших букв"])
        quatitysl = int(request.form["Количество маленьких букв"])
        quatityn = int(request.form["Количество чисел"])
        S = quatityn + quatitysl + quatitybl + quatityss
        print(S)
        print(length)
        if S != length:
            message = "Вы ввели неверное количество символов,букв и чисел. Проверьте еще раз и повторите попытку!"
            return render_template('FormPass1.html', message=message, form=form)
        else:
            for n in range(length):
                password = ''
                for i in range(quatityss):
                    password += random.choice(specsimbol)
                for i in range(quatitybl):
                    password += random.choice(bigletters)
                for i in range(quatitysl):
                    password += random.choice(litletters)
                for i in range(quatityn):
                    password += random.choice(number)
            password = "".join(random.sample(password, len(password)))
            cursor.execute('''UPDATE password SET password=? WHERE id=?''', (password, id,))
            cursor.execute("""SELECT nameSN,loginSN,password FROM password ORDER BY id DESC LIMIT 1;""")
            value = []
            for i in cursor.fetchall():
                value.append(i[0])
                value.append(i[1])
                value.append(i[2])
            connect.commit()
            cursor.close()
            return render_template('result.html', list=value)

@app.route('/generatewss', methods=['POST', 'GET'])
def generatewss():
    form = FormPass2()
    if request.method == 'GET':
        connect = sqlite3.connect('password.db')
        cursor = connect.cursor()
        cursor.execute("""SELECT id, lengthpass FROM password ORDER BY id DESC LIMIT 1;""")
        for i in cursor.fetchall():
            id = i[0]
            length = i[1]
        bigletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        litletters = 'abcdefghijklnopqrstuvwxyz'
        number = '1234567890'
        for n in range(length):
            password = ''
            for i in range(math.floor(length/3)):
                password += random.choice(bigletters)
            for i in range(math.floor(length/3)):
                password += random.choice(litletters)
            for i in range(length - math.floor(length/3)*2):
                password += random.choice(number)
        password = "".join(random.sample(password, len(password)))
        cursor.execute('''UPDATE password SET password=? WHERE id=?''', (password, id,))
        cursor.execute("""SELECT nameSN,loginSN,password FROM password ORDER BY id DESC LIMIT 1;""")
        value = []
        for i in cursor.fetchall():
            value.append(i[0])
            value.append(i[1])
            value.append(i[2])
        connect.commit()
        cursor.close()
        return render_template('result.html', list=value)

    if request.method == 'POST':
        connect = sqlite3.connect('password.db')
        cursor = connect.cursor()
        cursor.execute("""SELECT id, lengthpass FROM password ORDER BY id DESC LIMIT 1;""")
        for i in cursor.fetchall():
            id = i[0]
            length = i[1]
        bigletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        litletters = 'abcdefghijklnopqrstuvwxyz'
        number = '1234567890'
        quatitybl = int(request.form["Количество больших букв"])
        quatitysl = int(request.form["Количество маленьких букв"])
        quatityn = int(request.form["Количество чисел"])
        S = quatityn + quatitysl + quatitybl
        print(S)
        print(length)
        if S != length:
            message = "Вы ввели неверное количество букв и чисел. Проверьте еще раз и повторите попытку!"
            return render_template('FormPass2.html', message=message, form=form)
        else:
            for n in range(length):
                password = ''
                for i in range(quatitybl):
                    password += random.choice(bigletters)
                for i in range(quatitysl):
                    password += random.choice(litletters)
                for i in range(quatityn):
                    password += random.choice(number)
            password = "".join(random.sample(password, len(password)))
            cursor.execute('''UPDATE password SET password=? WHERE id=?''', (password, id,))
            cursor.execute("""SELECT nameSN,loginSN,password FROM password ORDER BY id DESC LIMIT 1;""")
            value = []
            for i in cursor.fetchall():
                value.append(i[0])
                value.append(i[1])
                value.append(i[2])
            connect.commit()
            cursor.close()
            return render_template('result.html', list=value)


if __name__ == "__main__":
    app.run()