from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# 任务：为7个景点介绍页设置动态路由
@app.route('/<name>')
def detail(name):
    return render_template(name + '.html')
app.run(port=5980,debug=True)