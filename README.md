# Financial Data Extractor and Updater

This project provides a comprehensive solution for extracting financial data from Google Finance, updating a Google Sheet with the extracted data, and sending an SMS notification if new data is added. The project is implemented as a Google Cloud Function that can be triggered via HTTP requests.

## Features

- Extracts financial data for key indices and stocks from Google Finance.
- Updates a Google Sheet with the latest financial data.
- Sends an SMS notification using Twilio API when new data is added.
- Handles HTTP requests to trigger the data update process.

## Prerequisites

- Python 3.7+
- Google Cloud account
- Google Cloud SDK
- Twilio account

## Libraries Used

- `pandas==2.2.2`
- `numpy==1.21.2`
- `google-auth==2.28.0`
- `google-auth-httplib2==0.2.0`
- `google-auth-oauthlib==1.2.0`
- `google-api-python-client==2.132.0`
- `oauthlib==3.2.2`
- `requests==2.31.0`
- `beautifulsoup4==4.12.2`
- `lxml==4.9.3`
- `json`
- `datetime==5.5`
- `twilio==9.1.1`

## Getting Started

### Setup

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/Bacchus2333/google_cloud_scrapping_function.git
   cd google_cloud_scrapping_function
   ```

2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Google Cloud Setup:**
   - Enable Google Sheets API and Google Drive API on your Google Cloud project.
   - Download the service account credentials file and save it as `credentials.json` in the project directory.

4. **Twilio Setup:**
   - Sign up for a Twilio account and obtain your Account SID and Auth Token.
   - Set up a Twilio phone number.

### Configuration

1. **Update Parameters:**
   Edit the script to update the following parameters with your values:
   - `file_id`: Google Sheets file ID.
   - `scope`: Scope for accessing Google Drive.
   - `service_account_json_key`: Path to the service account credentials file.
   - `ACCOUNT_SID`, `AUTH_TOKEN`, `TWILIO_PHONE_NUMBER`, `TO_PHONE_NUMBER`: Twilio credentials and phone numbers.

### Deploying the Cloud Function

1. **Deploy the Cloud Function:**
   ```sh
   gcloud functions deploy final_func --runtime python37 --trigger-http --allow-unauthenticated
   ```

### Usage

- To trigger the function and update the Google Sheet, send an HTTP request to the deployed Cloud Function URL.

## Code Overview

### Main Functions

- `get_ticker_data()`: Fetches and parses financial data from Google Finance.
- `extract_new_data(df)`: Extracts specific data points from the DataFrame.
- `test_add(old_data, added_data)`: Checks for new data and updates the DataFrame.
- `send_sms(body)`: Sends an SMS notification using Twilio.
- `reply_to_request(request)`: Handles HTTP requests and returns a response.
- `update_google_sheet(request, spreadsheet_id, scope, service_account_json_key, sheet_name)`: Updates the Google Sheet with new data and sends an SMS notification if needed.
- `final_func(request)`: Entry point for the Cloud Function.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

RichardrahciR

## Acknowledgements

- [Google Finance](https://www.google.com/finance)
- [Google Cloud](https://cloud.google.com/)
- [Twilio](https://www.twilio.com/)

---
Why don't stock market experts ever read novels?

Because the only numbers that matter to them are the ones in the stock ticker! 
