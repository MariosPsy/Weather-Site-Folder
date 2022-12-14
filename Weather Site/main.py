import streamlit
import plotly.express as px
import backend
from backend import get_data

# Create basic site
streamlit.title("Weather Forecast for the Next Days")

place = streamlit.text_input("Place")

days = streamlit.slider("Forecast Days", max_value=1, min_value=5,
                        help="Select the number of days to forecast")

option = streamlit.selectbox("Select view",
                             ("Temperature", "Sky"))

streamlit.subheader(f"{option} for the next {days} days in {place}")

# Create the data for temperature and sky
if place: # This syntax mean that "place" variable has a value
    temperature, filtered_data = get_data(place, days, option)

    # Create a temperature plot
    if option == "Temperature" :
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperature,
                         labels={"x": "Date", "y": "Temperatuure (C)"})
        streamlit.plotly_chart(figure)



