import pandas as pd
import requests

# Function to check if a website is active
def check_website_status(url):
    try:
        response = requests.get(url, timeout=5)  # Send a GET request with a timeout
        if response.status_code == 200:
            return "Active"
        else:
            return f"Not Active (Status Code: {response.status_code})"
    except requests.exceptions.RequestException as e:
        return f"Not Active (Error: {str(e)})"

# Read the CSV file
csv_file = "websites.csv"   # Replace with your CSV file path
df = pd.read_csv(r"C:\Users\MORRIS CAPT\Documents\LuxDev Academy\Website URLs.csv", encoding='latin1')

# Ensure the CSV has a column named 'Website' (adjust as needed)
if 'Website' not in df.columns:
    raise ValueError("CSV file must contain a 'Website' column.")

# Check the status of each website and store the result in a new column
df['Status'] = df['Website'].apply(check_website_status)

# Save the updated DataFrame to a new CSV file
output_file = "websites_with_status.csv"
df.to_csv(output_file, index=False)

print(f"Website statuses have been saved to {output_file}")