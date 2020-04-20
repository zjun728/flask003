from flask import Flask

# print("__init__:", __name__)  # __init__: apps
app = Flask(__name__)
app.debug = True

# 防止循环导入报错  app 在导入views之前创建成功（app = Flask(__name__)），
# 才能在views.py模块导入app(from apps import app)时正常导入
import apps.views

# 当前文件作为执行文件（运行）的时候__name__才会等于：__main__
# 当前文件作为包的一个模块导入到文件的时候当前文件的__name__为包名（此为__name__== apps）
# 如：启动runserver.py文件的时候 当前的文件 print( __name__) 输出结果为： apps
# 单独启动__init__.py文件的时候 当前的文件 print( __name__) 输出结果为： __main__
if __name__ == '__main__':
    app.run()
