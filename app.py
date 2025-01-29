#To create a simple Flask app that brings my name

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
     return "My name is Musa Haulah"

if __name__ == '__main__':
       app.run(debug=True)
   

	
