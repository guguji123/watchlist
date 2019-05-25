from app import User,Movie
'''
user = User(name = 'Grey Li')
m1 = Movie(title = 'Leon',year = '1994')
m2 = Movie(title = 'Mahjong',year = '1996')

user.save()
m1.save()
m2.save()
'''
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
for m in movies:
    movie = Movie(title = m.get('title'),year = m.get('year'))
    movie.save()