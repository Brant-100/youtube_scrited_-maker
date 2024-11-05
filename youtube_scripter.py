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

def save_transcript_to_file(transcript, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(transcript)
    print(f"Transcript saved to {filename}.")

# Example Usage
video_url = "https://www.youtube.com/watch?v=vinP4bGM8Pk"
transcript_text = get_youtube_transcript(video_url)

if transcript_text:
    print("Video Transcript:\n", transcript_text)
    
    # Prompt user for filename
    filename = input("Enter the filename to save the transcript (with .txt extension): ")
    save_transcript_to_file(transcript_text, filename)  # Save to a text file
else:
    print("Transcript not available.")