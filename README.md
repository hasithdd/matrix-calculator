Matrix Calculator
Overview

Matrix Calculator is a simple web application built with Flask that allows users to perform basic matrix operations such as transpose and inverse. Users can input matrices in Python list format and select the desired operation to perform.
Features

    Transpose Operation: Transposes the input matrix.
    Inverse Operation: Calculates the inverse of the input matrix.
    User-friendly Interface: Provides a clean and intuitive user interface for inputting matrices and selecting operations.
    Result Display: Displays the result of the operation on the same page after form submission.

Deployment

The application is deployed using Azure App Service, making it accessible to users over the internet. The deployment process involves configuring the App Service and deploying the Flask application to the Azure cloud platform.
Usage

    Input the matrix in Python list format into the provided textarea.
    Select the desired operation from the dropdown menu.
    Click the "Calculate" button to perform the operation.
    View the result displayed on the same page.

Technologies Used

    Flask: Python web framework used for building the backend of the application.
    HTML/CSS: Frontend technologies used for designing the user interface.
    numpy: Python library used for matrix operations.

Development Setup

To set up the project locally for development, follow these steps:

    Clone the repository: git clone https://github.com/your-username/matrix-calculator.git
    Install dependencies: pip install flask
    Run the Flask application: python app.py
    Access the application in your web browser at http://localhost:5000

Contributing

Contributions to the project are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request. Be sure to follow the project's coding conventions and guidelines.
