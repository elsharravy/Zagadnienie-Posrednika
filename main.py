from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)
OUTPUT_PATH = 'test_output.json'
INPUT_PATH = OUTPUT_PATH

@app.route('/', methods=['GET'])
def index():
    return render_template('Posrednik.html')

@app.route('/generate', methods=['POST'])
def index():
    return render_template('Posrednik.html')



if __name__ == '__main__':
    app.run(debug=True)
