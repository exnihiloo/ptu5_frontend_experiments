# front end vartotojo sąsaja, kai varototjas manipuliuoja objektais, tikinter yra front end
# back end yra darbas su duomenų baze, duomenų ištraukimas

from flask import Flask, request, render_template

# susikuriam savo app ir jį pavadiname leidžiamo failo instancija
app = Flask(__name__)

# bus homepage, kuriamas puslapis
# dekoratorius route nurodo adresą; į route nurodome adresą, vienas "/"" yra pagridininio katalogo vienas puslapis
@app.route("/")
def home():
    return "Veikia!"

# sukuriam kitą puslapį, galima paduoti į adresą kintamaji "name"
# %20 padaro tarpą
@app.route("/sveikas/<name>")
def user(name):
    return f"Sveikas, {name}."

@app.route("/grazi_diena")
def grazi_diena():
    return render_template("grazi_diena.html")


@app.route("/zmones")
def zmones():
    zmones = [
        'Rasa', 'Mantas', 'Ana', 
        'Laima', 'Lina', 'Darius'
    ]
    return render_template("zmones.html", zmones = zmones)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/hello")
def hello():
    return render_template("hello.html", **request.args)


if __name__ == "__main__":
    # debug rodys klaidas browseryje ir komandinej eilutej
    app.run(debug=True)

# <ul> unordered list
# <ol> ordered list
# <li> listas
# ! ir enter padarys basic htmlo file