from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("styling/home.html")


@app.route("/poezija")
def poezija():
    return render_template("styling/poezija.html")

@app.route("/containers")
def containers():
    return render_template("styling/containers.html")

@app.route("/grid")
def grid():
    return render_template("styling/grid.html")

@app.route("/page")
def fullpage():
    return render_template("styling/fullpage2.html")

@app.route("/gyvunai")
def gyvunai():
    return render_template("styling/gyvunai.html")

@app.route("/flex")
def flex():
    return render_template("styling/flex.html")

if __name__ == "__main__":
    app.run(debug = True)


# padding: 1rem; atitraukia nuo remelio teksta
# vh ekrano ausktis
# vw plotis
# margin jei keturi aprametrai eina pagal laikrodzio rodykle
# jei tik du parametrai tai tik virus-apacia, antras - sonai