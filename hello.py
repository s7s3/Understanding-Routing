from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World!"
    
@app.route('/dojo')
def dojo():
  return "Dojo" 

@app.route('/say/<name>')
def hello(name):
    print(name)
    return "Hi " + name +'!'


@app.route('/repeat/<num>/<n>')
def repeat(n,num):
    
    return render_template('index.html', _n=n ,_num=int(num))



if __name__=='__main__':
 app.run(debug=True)

