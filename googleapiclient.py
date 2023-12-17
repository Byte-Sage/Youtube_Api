from googleapiclient.discovery import build

api_key = 'AIzaSyDkYWm_tRMbwqkghzhFiTkAuAI1FFfVb4Y'
youtube = build('youtube', 'v3', developerKey=api_key)

channel_id = 'UCQYMhOMi_Cdj1CEAU-fv80A #NESO-ACADEMY CHANNEL ID'
# Get the video list from the channel
search_response = youtube.search().list(
    part='id',
    channelId=channel_id,
    type='video',
).execute()

# Extract video IDs from the search results
video_ids = [item['id']['videoId'] for item in search_response['items']]

# Get comments for each video
for vid in video_ids:
    comments_response = youtube.commentThreads().list(
        part='snippet',
        videoId=vid,
    ).execute()

    # Extract and print comments
    for item in comments_response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']