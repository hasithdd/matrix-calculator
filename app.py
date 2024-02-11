from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    matrix_string = request.form['matrix']
    operation = request.form['operation']

    # Convert input string to numpy array
    matrix = np.array(eval(matrix_string))

    # Perform operation
    if operation == 'transpose':
        result = np.transpose(matrix)
    elif operation == 'inverse':
        result = np.linalg.inv(matrix)
    # Add more operations as needed...

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
