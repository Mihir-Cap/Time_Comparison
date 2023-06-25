# Time Zone Converter

This is a Flask web application that allows users to convert the time from one country to another. It utilizes the REST Countries API to retrieve country information and time zone data.

## Setup

1. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

2. Start the Flask server by executing the following command:

   ```
   python app.py
   ```

3. Open your web browser and navigate to `http://localhost:5000`.

## Usage

1. On the homepage, you will see a dropdown list containing various countries. Select the country from which you want to convert the time.

2. Enter the time in the format `YYYY-MM-DDTHH:MM` for the selected country.

3. Choose the destination country to which you want to convert the time.

4. Click the "Convert" button.

5. The converted time will be displayed below the button.

## API Endpoints

- `GET /`: Renders the homepage with a dropdown list of countries.

- `POST /get_time`: Accepts a POST request containing the selected countries and the time to convert. It returns the converted time in JSON format.

## External APIs

- REST Countries API: This application fetches country information and time zone data from the REST Countries API. The API provides data on countries, including their time zones.

## Dependencies

- Flask: A micro web framework used to develop this application.

- Requests: A library used to send HTTP requests and handle API responses.

- Pytz: A library used to handle time zone conversions and retrieve time zone information.

Feel free to explore and use this application to convert times between different countries. If you have any questions or suggestions, please feel free to reach out. Happy time zone conversions!
