from flask import Flask, render_template, request
from weather_service import get_location_key, get_weather_forecast

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        location_key = get_location_key(city)
        if location_key:
            weather_data = get_weather_forecast(location_key)
    return render_template('index.html', weather=weather_data)


if __name__ == "__main__":
    app.run(debug=True)
