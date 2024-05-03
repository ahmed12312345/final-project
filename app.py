from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/project1')
def project1():
    return render_template('project1.html', project_number=1)

@app.route('/project2')
def project2():
    return render_template('project2.html', project_number=2)

@app.route('/project3')
def project3():
    return render_template('project3.html', project_number=3)

if __name__ == '__main__':
    app.run(debug=True)
