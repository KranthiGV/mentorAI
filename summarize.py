from youtube_transcript_api import YouTubeTranscriptApi
import anthropic
import os



url = 'https://www.youtube.com/watch?v=cEg8cOx7UZk'
print(url)

video_id = url.replace('https://www.youtube.com/watch?v=', '')
print(video_id)

transcript = YouTubeTranscriptApi.get_transcript(video_id)

output=''
for x in transcript:
  sentence = x['text']
  output += f' {sentence}\n'
  
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


def get_completion(client, prompt):
    return client.messages.create(
        model= 'claude-3-opus-20240229',
        max_tokens=2048,
        messages=[{
            "role": 'user', "content":  prompt
        }]
    ).content[0].text
    
completion = get_completion(client,
    f"""Here is an interview transcript: <transcript>{output}</transcript>

Please do the following:
1. Summarize the abstract as a journalist (In <summary> tags.)
2. Create a comprehensive list of tags representing the all topics discusses by the main speaker in this transcript and output them in a python list such as ['item1', 'item2','item3']" (In <categories> tags.)

"""
)
print(completion)


# print('>>>SUMMARY:')
# print(summary)
# print('>>>TAGS:')
# print(tag)
# print('>>>OUTPUT:')
#print(output)

