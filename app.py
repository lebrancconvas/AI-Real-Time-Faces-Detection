from flask import flask 

app = flask(__name__) 

@app.route('/') 
def index(): 
  return render_template('index.html') 

app.run(debug=False)  