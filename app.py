from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/email')
# def email():
#     return redirect('http://127.0.0.1:8081/')

# @app.route('/chat')
# def chat():
#     return redirect('http://127.0.0.1:8065/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
