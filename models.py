import time

from init import db


class ModelHelper(object):
    def __repr__(self):
        """
        __repr__ 是一个魔法方法
        简单来说, 它的作用是得到类的 字符串表达 形式
        比如 print(u) 实际上是 print(u.__repr__())
        """
        classname = self.__class__.__name__
        properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)
        return '< {}\n{} \n>\n'.format(classname, s)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Todo(db.Model, ModelHelper):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)

    def __init__(self, form):
        self.task = form.get('task', '')
        self.created_time = int(time.time())


class User(db.Model, ModelHelper):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)

    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.created_time = int(time.time())

    def valid(self):
        return len(self.username) > 2 and len(self.password) > 2

    def validate_login(self, u):
        return u.username == self.username and u.password == self.password


class Weibo(db.Model, ModelHelper):
    __tablename__ = 'weibos'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    content = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)

    def __init__(self, form):
        self.content = form.get('content', '')
        self.created_time = int(time.time())


class Comment(db.Model, ModelHelper):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    weibo_id = db.Column(db.Integer)
    content = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)

    def __init__(self, form):
        self.content = form.get('content', '')
        self.created_time = int(time.time())
        self.weibo_id = form.get('weibo_id', None)


def init_db():
    db.drop_all()
    db.create_all()
    print('rebuild database')


if __name__ == '__main__':
    init_db()
