from youtube_transcript_api import YouTubeTranscriptApi

# Initializing the title variable
title = []
# Initializing the description variable
transcript = []

jensen_data = {'title': title, 'transcript': transcript}


url = ['https://www.youtube.com/watch?v=cEg8cOx7UZk', 'https://www.youtube.com/watch?v=ytZcvwZxkrg' ]
print(url)

#extract video id for input for youtube scraping api
video_id = url.replace('https://www.youtube.com/watch?v=', '')
print(video_id)

transcript = YouTubeTranscriptApi.get_transcript(video_id)

#json format 

print(transcript)
print("hello")

#strip text value 
output=''
for x in transcript:
  sentence = x['text']
  output += f' {sentence}\n'


print(output)