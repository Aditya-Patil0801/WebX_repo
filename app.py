#WebX Exp11: Feedback Form using Flask

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    feedback = request.form['feedback']

    return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)