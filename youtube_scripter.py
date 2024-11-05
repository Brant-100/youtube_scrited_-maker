from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_transcript(video_url):
    try:
        # Extract video ID from the URL
        video_id = video_url.split("v=")[-1]
        
        # Fetch transcript
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Combine transcript into a single string
        transcript = " ".join([item['text'] for item in transcript_list])
        print("Transcript retrieved successfully.")
        return transcript

    except Exception as e:
        print(f"Error retrieving transcript: {e}")
        return None

# Example Usage
video_url = "https://www.youtube.com/watch?v=HdEr6edDdeA"
transcript_text = get_youtube_transcript(video_url)

if transcript_text:
    print("Video Transcript:\n", transcript_text)
else:
    print("Transcript not available.")