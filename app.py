from flask import Flask, render_template, request
import numpy as np
import ast
from numpy.linalg import LinAlgError

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        matrix_string = request.form['matrix']
        operation = request.form['operation']

        # Safely evaluate the input matrix string
        matrix = np.array(ast.literal_eval(matrix_string))

        determinant = np.linalg.det(matrix)

        if operation == 'transpose':
            result = np.transpose(matrix)
        elif operation == 'inverse':
            try:
                result = np.linalg.inv(matrix)
            except LinAlgError:
                error_message = "The matrix is singular and does not have an inverse."
                return render_template('error.html', error_message=error_message)

        return render_template('result.html', result=result, determinant=determinant)

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
