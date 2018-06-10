"""
create by gaowenfeng on 
"""

from flask import Flask, current_app

__author__ = "gaowenfeng"

app = Flask(__name__)

# 获取AppContext，里面的代码很简单，就是：return AppContext(self)
ctx = app.app_context()
# 将AppContext入栈
ctx.push()
# 断点调试这里显示current_app=[LocalProxy]<LocalProxy unbound>
a = current_app

# RuntimeError: Working outside of application context.
b = current_app.config["DEBUG"]
print(b)
ctx.pop()
