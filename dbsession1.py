Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: D:\Programs\Sublime Text 3\flaskblog.py ==============

Warning (from warnings module):
  File "C:\Python27\lib\site-packages\flask_sqlalchemy\__init__.py", line 774
    'Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. '
UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:".

Warning (from warnings module):
  File "C:\Python27\lib\site-packages\flask_sqlalchemy\__init__.py", line 794
    'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.

Traceback (most recent call last):
  File "D:\Programs\Sublime Text 3\flaskblog.py", line 72, in <module>
    app.run(debug=True)
  File "C:\Python27\lib\site-packages\flask\app.py", line 938, in run
    cli.show_server_banner(self.env, self.debug, self.name, False)
  File "C:\Python27\lib\site-packages\flask\cli.py", line 629, in show_server_banner
    click.echo(message)
  File "C:\Python27\lib\site-packages\click\utils.py", line 217, in echo
    file = _default_text_stdout()
  File "C:\Python27\lib\site-packages\click\_compat.py", line 621, in func
    rv = wrapper_func()
  File "C:\Python27\lib\site-packages\click\_compat.py", line 201, in get_text_stdout
    rv = _get_windows_console_stream(sys.stdout, encoding, errors)
  File "C:\Python27\lib\site-packages\click\_winconsole.py", line 261, in _get_windows_console_stream
    func = _stream_factories.get(f.fileno())
UnsupportedOperation: fileno
k
>>> from D:\Programs\Sublime Text 3\flaskblog.py import db
SyntaxError: invalid syntax
>>> from flaskblog import db

Warning (from warnings module):
  File "C:\Python27\lib\site-packages\flask_sqlalchemy\__init__.py", line 794
    'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
>>> db.create_all()
>>> from flaskblog import User, Post
>>> user_1 = User(username='Corey',email='c@demo.com',password='password')
>>> db.session.add(user_1)
>>> db.session.commit()
>>> User.query.all()
[User('{self.username)','{self.email}','{self.image_file}')]
>>> User.query.first()
User('{self.username)','{self.email}','{self.image_file}')
>>> User.query.filter_by(username='corey').all()
[]
>>> user = User.query.filter_by(username='Corey').first()
>>> user.id
1
>>> user
User('{self.username)','{self.email}','{self.image_file}')
>>> user = User.query.get(1)
>>> user
User('{self.username)','{self.email}','{self.image_file}')
>>> user.posts
[]
>>> post_1 = Post(title='Blog1',content='first post content!',user_id=user.id)
>>> db.session.add(post_1)
>>> db.session.commit()
>>> user.posts

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    user.posts
  File "D:\Programs\Sublime Text 3\flaskblog.py", line 30, in __repr__
    return "Post('{1)','{0}')".format(self.date_posted,self.title)
ValueError: unmatched '{' in format
>>> user.posts

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    user.posts
  File "D:\Programs\Sublime Text 3\flaskblog.py", line 30, in __repr__
    return "Post('{1)','{0}')".format(self.date_posted,self.title)
ValueError: unmatched '{' in format
>>> post = Post.query.first()
>>> post

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    post
  File "D:\Programs\Sublime Text 3\flaskblog.py", line 30, in __repr__
    return "Post('{1)','{0}')".format(self.date_posted,self.title)
ValueError: unmatched '{' in format
>>> post.author
User('{self.username)','{self.email}','{self.image_file}')
>>> db.drop_all()
>>> db.create_all()
>>> User.query.all()
[]
>>> Post.query.all()
[]
>>> 
