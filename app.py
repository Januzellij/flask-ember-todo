from flask import Flask, jsonify, send_file, request
from flask.ext.restful import Api, Resource
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug=True
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/todos.db'
db = SQLAlchemy(app)

class TodoModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	isCompleted = db.Column(db.Boolean)

	def __init__(self, title, isCompleted=False):
		self.title = title
		self.isCompleted = isCompleted

	@property
	def to_json(self):
		return {
			"id": self.id,
			"isCompleted": self.isCompleted,
			"title": self.title
		}

# write a module to handle this

class Todos(Resource):
	def get(self):
		todos = TodoModel.query.all()
		return jsonify({ "todos" : [t.to_json for t in todos] })

	def post(self):
		t = request.json['todo']['title']
		new_todo = TodoModel(t)
		db.session.add(new_todo)
		db.session.commit()
				

class Todo(Resource):
	def put(self, id):
		todo = TodoModel.query.get(id)
		req = request.json['todo']
		todo.title = req['title']
		todo.isCompleted = req['isCompleted']
		db.session.commit()

	def delete(self, id):
		todo = TodoModel.query.get(id)
		db.session.delete(todo)
		db.session.commit()
	

api.add_resource(Todos, '/api/todos', methods=['GET','POST'])
api.add_resource(Todo, '/api/todos/<int:id>', methods=['GET','POST','PUT', 'DELETE'])

@app.route('/')
def index():
	return send_file('templates/index.html')

if __name__ == '__main__':
	db.create_all()
	"""db.session.add(TodoModel("Test"))
	db.session.commit()"""
	app.run()
