from flask import Flask, jsonify, abort
import pytest

app = Flask(__name__)

persons = [
    {
        "name":"Вася Пупкин",
        "phone":"88005553535",
        "address":"Нижний Новгород, пр. Гагарина д.3",
        "id":1
     },
    {
        "name":"Марфа Петровна",
        "phone":"88009996767",
        "address":"Иваново, Ивановская д.4",
        "id":2
    }
]

@app.route('/')
def index():
    return '<h1>Hell<h1>'

@app.route('/pers/api/v1/list/int:pers_id', methods=['GET'])
def  list_person(pers_id):
    persona = filter(lambda t: t['id'] == pers_id, persons) #лямбда неправильно отрабатывает
    if persona == 0:
        abort(404)
    return jsonify({'persons' : persons[0]})
    # return jsonify({'persons': persons})

if __name__ == '__main__':
    app.run(port=8882)