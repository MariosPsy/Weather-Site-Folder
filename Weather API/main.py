from flask import Flask, render_template
import pandas



app = Flask(__name__)

stations = pandas.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    path = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pandas.read_csv(path, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"]== date]["   TG"].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}


@app.route("/api/v1/<station>")
def subpage(station):
    path = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    certain_station = pandas.read_csv(path, skiprows=20, parse_dates=["    DATE"])
    return certain_station.to_dict(orient="records")

@app.route("/api/v1/yearly/<station>/<year>")
def subpage2(station, year):
    path = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    certain_station = pandas.read_csv(path, skiprows=20)
    certain_station["    DATE"] = certain_station["    DATE"].astype(str)
    certain_year = certain_station[certain_station["    DATE"].str.startswith(str(year))]
    print(certain_year)
    return certain_year.to_dict(orient="records")



if __name__ == "__main__" :
    app.run(debug=True)
