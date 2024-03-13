from flask import Flask

app =  Flask('name')

@app.route("/prueva1")
@app.route("/prueva1<name>")
@app.route("/prueva1<name>/<int:edad>")
def hello_word(name = None, edad =None):
    if edad == None :

        return f"<center><h1>Mi otro nombre es : {name}</h1></center>"
    else:
        return f"<center><h1>Mi otro nombre es : {name} y su edad es :{edad}</h1></center>"

if name == ('main'):
    app.run(debug=True)