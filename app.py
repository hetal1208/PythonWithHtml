from flask import Flask, render_template
from flask import request
app= Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html", name="Hetal")
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    return f'Hello, {username}! {password}'
    
if __name__ == "__main__":
    app.run(debug=True)
