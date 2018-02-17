from flask import Flask, jsonify, json, request, render_template

app = Flask(__name__)

@app.route("/my_route/",methods=['POST'])
def my_route():
    print('Received POST request at /my_route/')
    return 'Received POST request at /my_route/'

@app.route('/')
def render_main():
    return render_template('main.html')

if __name__ == '__main__':
  app.run()