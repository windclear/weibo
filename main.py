from init import app
from todo import main as todo_routes
from user import main as user_routes
from weibo import main as weibo_routes
import errors


app.register_blueprint(todo_routes, url_prefix='/todo')
app.register_blueprint(user_routes, url_prefix='/user')
app.register_blueprint(weibo_routes, url_prefix='')


if __name__ == '__main__':
    app.run(debug=True, port=3000)
