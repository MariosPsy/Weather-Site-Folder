from flask import Flask, render_template
import pandas



app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    path = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pandas.read_csv(path, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[]
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__" :
    app.run(debug=True)
