# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
def index():
  return render_template('index.html')
# def hello_world():
#     return 'Hello World'

def sumOf2(num1, num2):
    print(num1 +num2)


@app.route('/next-page/')
def my_link():
  sumOf2(2,3)
  return render_template('index2.html')

@app.route('/hello/')
def hello_name():
    print('I got clicked!')
    return 'Hello!'


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()