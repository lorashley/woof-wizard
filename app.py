from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def slash():
    return "Hello World!"
    
@app.route("/hello")
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route("/woofwizard", methods=['GET', 'POST'])
def woofwizard():
    if request.method == 'GET':
    	return render_template('woofwizard.html')   
    
if __name__ == "__main__":
    app.run(debug=True, port=5001)