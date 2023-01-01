from flask import Flask, send_file, request
from pipelines import k

app = Flask(__name__)

@app.route('/')
def indexPage():
    return send_file('../dist/index.html')

@app.route('/<path:p>')
def staticAssets(p):
    return send_file('../dist/'+p)

@app.route('/api/generate', methods=['POST'])
def generate():
    res = request.json
    if(res['flag'] == 'k'):
        return k(res['prompt'])
    else:
        return res['prompt']+'测试测试测试测试'

if __name__ == '__main__':
    app.run(port=8439, debug=True)