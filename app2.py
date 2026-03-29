#exp12:Design a Portfolio Website using Flask including Education, Professional Skills, and Contact Form.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    print("----- New Contact Form Submission -----")
    print("Name:", name)
    print("Email:", email)
    print("Message:", message)
    print("--------------------------------------")

    return "<h3 style='color:green;text-align:center;'>Form Submitted Successfully!</h3>"

if __name__ == '__main__':
    app.run(debug=True)