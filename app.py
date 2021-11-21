from flask import flask, render_template  
# from camera import video 

app = flask(__name__) 

@app.route('/') 
def index(): 
  return render_template('index.html') 

app.run(debug=True)   