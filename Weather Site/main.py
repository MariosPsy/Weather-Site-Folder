import streamlit
import plotly.express as px
from backend import get_data

streamlit.title("Weather Forecast for the Next Days")

place = streamlit.text_input("Place")

days = streamlit.slider("Forecast Days", max_value=1, min_value=5,
                        help="Select the number of days to forecast")

option = streamlit.selectbox("Select view",
                             ("Temperature", "Sky"))

streamlit.subheader(f"{option} for the next {days} days in {place}")

get_data(place, days, option)

# dates = ["day1", "day2", "day3"]
# temperatures = [10, 8, 12]
figure = px.line(x=dates, y=temperatures,
                 labels={"x": "Date", "y": "Temperatuure (C)"})
streamlit.plotly_chart(figure)


