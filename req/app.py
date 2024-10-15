from flask import Flask, render_template,request

app= Flask(__name__)
@app.route('/')
def index():
    return render_template('h.html')

@app.route('/submit',methods=['POST'])
def submit():
    name=request.form['name']
    age=request.form['age']
    email=request.form['email']
    return render_template("h2.html",name=name,age=age,email=email)
if __name__ == '__main__':
    app.run(debug=True,port=5500)

