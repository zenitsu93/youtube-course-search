

---

# YouTube Video Search Script

This Python script uses the YouTube Data API to search for videos related to course titles and classes from an Excel file. It retrieves video titles and URLs and saves the results in another Excel file.

## Prerequisites

- Python 3.x
- `pandas` library (`pip install pandas`)
- Google API Client Library (`pip install google-api-python-client`)

## Getting Started

1. Obtain an API key for the YouTube Data API from the Google Developer Console.
2. Install the required Python libraries using pip.
3. Place your Excel file (`courses.xlsx`) containing course titles and classes in the same directory as the script.

## Usage

1. Replace the placeholder API key (`api_key = "YOUR_API_KEY"`) with your actual API key.
2. Update the Excel file name if necessary (`df = pd.read_excel("cent2.xlsx")` and `result_df.to_excel("resultats_videos3.xlsx", index=False)`).
3. Run the script to search for videos related to each course title and class.
4. The script will create a new Excel file (`resultats_videos3.xlsx`) with the search results.

## Notes

- You can modify the `max_results` parameter in the `search_videos` function to adjust the number of videos retrieved per search query.
- Ensure that your API key has the necessary permissions to access the YouTube Data API.

## Disclaimer

This script is provided as-is without any warranties. Use it responsibly and ensure compliance with [YouTube's API](https://developers.google.com/youtube/v3/getting-started?hl=fr) terms of service.

---
