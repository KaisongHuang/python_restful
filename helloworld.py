from flask import Flask, request, jsonify
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'flask'
app.config['MYSQL_PASSWORD'] = 'flask'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)


@app.route('/')
def hello_world():
	return 'Hello world!'


@app.route('/hello', methods=['GET'])
def hello():
	return 'hello'


@app.route('/world', methods=['GET'])
def world():
	return 'world'


@app.route('/student', methods=['GET', 'POST'])
def student():
	if request.method == "POST":
		firstName = request.json['First name']
		lastName = request.json.get('Last name', "")
		age = int(request.json.get('Age', "18"))
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO students(firstname, lastname, age) VALUES (%s, %s, %i)", (firstName, lastName, age))
		mysql.connection.commit()
		cur.close()
		student = {
			'Firt name': firstName,
			'Last name': lastName,
			'Age': age
		}
		return jsonify({'student': student})
	else:
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM students")
		res = cur.fetchall()
		cur.close()

		students = []
		for row in res:
			student = {
				'id': row[0],
				'Firt name': row[1],
				'Last name': row[2],
				'Age': row[3]
			}
			students.append(student)

		return jsonify({'students': students})


if __name__ == '__main__':
	app.run()
