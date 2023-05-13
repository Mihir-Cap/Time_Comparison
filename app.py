from flask import Flask, render_template, request
import requests
import pytz
from datetime import datetime

app = Flask(__name__)

def get_timezone_for_country(country_code):
    response = requests.get(f'https://restcountries.com/v3.1/alpha/{country_code}')
    country_data = response.json()

    # Check if the response is a list and get the first element
    if isinstance(country_data, list):
        country_data = country_data[0]

    timezones = country_data['timezones']
    if isinstance(timezones, list):
        timezone = timezones[0]
    else:
        timezone = timezones

    # Convert UTC offset to timezone name
    if timezone.startswith('UTC'):
        hours = int(timezone[4:].split(':')[0]) if timezone else 0
        minutes = int(timezone[4:].split(':')[1])
        tz = pytz.FixedOffset(hours * 60 + minutes)
    else:
        tz = pytz.timezone(timezone)

    return tz

@app.route('/')
def index():
    response = requests.get('https://restcountries.com/v3.1/all')
    countries = response.json()
    country_list = [(country['name']['common'], country['cca2']) for country in countries]
    return render_template('index.html', country_list=country_list)

@app.route('/get_time', methods=['POST'])
def get_time():
    first_country_code = request.form['first_country']
    first_country_time_str = request.form['first_country_time']
    second_country_code = request.form['second_country']

    first_country_tz = get_timezone_for_country(first_country_code)
    second_country_tz = get_timezone_for_country(second_country_code)

    # Convert string to datetime object
    first_country_time = datetime.strptime(first_country_time_str, '%Y-%m-%dT%H:%M')

    # Convert first country time to second country time
    second_country_time = first_country_time.astimezone(first_country_tz).astimezone(second_country_tz).strftime('%Y-%m-%d %H:%M:%S')

    return {'time': second_country_time}

if __name__ == '__main__':
    app.run(debug=True)
