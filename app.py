from flask import Flask,render_template
from flask_mongoengine import MongoEngine
from datetime import datetime
import click
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'web',
    'host': '127.0.0.1',
    'port': 27017
}

db = MongoEngine(app)

@app.cli.command()
def forge():
    name = 'Yao'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]
    user = User(name=name)
    user.save()
    for m in movies:
        movie = Movie(title=m.get('title'), year=m.get('year'))
        movie.save()
    click.echo('Done')

class User(db.Document):
    meta = {
        'collection': 'user',
        'ordering': ['-create_at'],
        'strict': False,
    }
    name = db.StringField()
    create_at = db.DateTimeField(default=datetime.now)

class Movie(db.Document):
    meta = {
        'collection': 'movie',
        'ordering': ['-create_at'],
        'strict': False,
    }
    title = db.StringField()
    year = db.StringField()
    create_at = db.DateTimeField(default=datetime.now)

@app.route('/')
def index():
    user = User.objects().first()  # 读取用户记录
    movies = Movie.objects().all()  # 读取所有电影记录
    return render_template('index.html', user=user, movies=movies)
