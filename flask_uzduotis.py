from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def statinis_psl():
    return "Čia pagal užduotį reikėjo parašyti tekstą, tai va tekstas jums."


@app.route("/<zodis>")
def url(zodis):
    return (zodis + " ") * 5 


@app.route("/keliamieji")
def keliamieji_metai():
    keliamieji_m = []
    metai = range(1900, 2101)
    for i in metai:
        if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
            keliamieji_m.append(i)
    return render_template("keliamieji.html", **request.args, keliamieji = keliamieji_m) 

@app.route("/metai")
def metai():
    return render_template("metai.html")

@app.route("/atsakymas")
def atsakymas():
    ivesti_metai = int(request.args["metai"])
    if ivesti_metai % 4 == 0 and (ivesti_metai % 100 != 0 or ivesti_metai % 400 == 0):
        atsakymas = "keliamieji"
    else:
        atsakymas = "nekeliamieji"
    return render_template("atsakymas.html", **request.args, atsakymas = atsakymas)


@app.route("/koksskaicius")
def koks_skaicius():
    return render_template("koks_skaicius.html")

@app.route("/atsakymassk")
def sk_atsakymas():
    ivestas_sk = int(request.args["skaicius"])
    if ivestas_sk % 2 == 0:
        atsakymas = "lyginis"
    else:
        atsakymas = "nelyginis"
    return render_template("sk_atsakymas.html", **request.args, atsakymas = atsakymas)


if __name__ == "__main__":
    app.run(debug = True)