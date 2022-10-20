<<<<<<< HEAD
# front end vartotojo sąsaja, kai varototjas manipuliuoja objektais, tikinter yra front end
# back end yra darbas su duomenų baze, duomenų ištraukimas

from flask import Flask, request, render_template

# susikuriam savo app ir jį pavadiname leidžiamo failo instancija
app = Flask(__name__)

# bus homepage, kuriamas puslapis
# dekoratorius route nurodo adresą; į route nurodome adresą, vienas "/"" yra pagridininio katalogo vienas puslapis
=======
from flask import Flask, render_template, request

app = Flask(__name__)

>>>>>>> 00a5619cc09cf501c2a29b355bce3b77ea7f157c
@app.route("/")
def home():
    return "Veikia!"

<<<<<<< HEAD
# sukuriam kitą puslapį, galima paduoti į adresą kintamaji "name"
# %20 padaro tarpą
@app.route("/sveikas/<name>")
def user(name):
    return f"Sveikas, {name}."
=======
@app.route("/sveikas/<name>")
def user(name):
    return f"Sveikas, {name}"
>>>>>>> 00a5619cc09cf501c2a29b355bce3b77ea7f157c

@app.route("/grazi_diena")
def grazi_diena():
    return render_template("grazi_diena.html")

<<<<<<< HEAD

@app.route("/zmones")
def zmones():
    zmones = [
        'Rasa', 'Mantas', 'Ana', 
        'Laima', 'Lina', 'Darius'
    ]
    return render_template("zmones.html", zmones = zmones)
=======
@app.route("/zmones")
def zmones():
    zmones = [
        'Justina', 'Darius', 'Ingrida', 'Linas', 
        'Ana', 'Simas', 'Arnoldas', 'Sergejus',
    ]
    return render_template("zmones.html", zmones=zmones)
>>>>>>> 00a5619cc09cf501c2a29b355bce3b77ea7f157c

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/hello")
def hello():
    return render_template("hello.html", **request.args)


if __name__ == "__main__":
<<<<<<< HEAD
    # debug rodys klaidas browseryje ir komandinej eilutej
    app.run(debug=True)

# <ul> unordered list
# <ol> ordered list
# <li> listas
# ! ir enter padarys basic htmlo file
=======
    app.run(debug=True)
>>>>>>> 00a5619cc09cf501c2a29b355bce3b77ea7f157c
