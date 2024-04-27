import pandas as pd
from googleapiclient.discovery import build

# YouTube API Key (obtained from the developer console)
api_key = "YOUR_API_KEY"

# Read the Excel file containing course titles and classes
df = pd.read_excel("courses.xlsx")

# Create an instance of the YouTube API
youtube = build('youtube', 'v3', developerKey=api_key)

# List to store the results
results = []

# Function to search for videos on YouTube


def search_videos(query, max_results=3):
    search_response = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=max_results
    ).execute()

    videos = []

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            video_id = search_result['id']['videoId']
            title = search_result['snippet']['title']
            video_url = f"https://www.youtube.com/watch?v={video_id}"

            videos.append({
                'title': title,
                'video_url': video_url
            })

    return videos


# Iterate through each row of the dataframe
for index, row in df.iterrows():
    course_title = row['titre']
    course_class = row['classe']

    # Perform a search on YouTube
    query = f"{course_title} {course_class} cours"
    videos = search_videos(query)

    # Add the results to the list
    for video in videos:
        result = {
            'course_title': course_title,
            'course_class': course_class,
            'video_title': video['title'],
            'video_url': video['video_url']
        }
        results.append(result)

# Create a new DataFrame from the results
result_df = pd.DataFrame(results)

# Save the DataFrame to an Excel file
result_df.to_excel("results_videos.xlsx", index=False)
