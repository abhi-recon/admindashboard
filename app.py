from flask import Flask, render_template
from flask import url_for
app = Flask(__name__)

app.debug = True

@app.route('/')
def dashboard():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)