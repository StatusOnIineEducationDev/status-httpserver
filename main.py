from flask import Flask

from config.conf import *
from controllers.desktop.courseController import course
from controllers.desktop.userController import user

app = Flask(__name__)
# 注册蓝图
app.register_blueprint(blueprint=course, url_prefix='/course')
app.register_blueprint(blueprint=user, url_prefix='/user')


if __name__ == '__main__':
    app.run(host=HTTP_HOST, port=HTTP_PORT)
