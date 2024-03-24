from youtube_transcript_api import YouTubeTranscriptApi
import anthropic
import os

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
)

def get_completion(client, prompt):
    return client.messages.create(
        model= 'claude-3-opus-20240229',
        max_tokens= 4096,
        messages=[{
            "role": 'user', "content":  prompt
        }]
    ).content[0].text

segments = []

urls = ['https://www.youtube.com/watch?v=cEg8cOx7UZk','https://www.youtube.com/watch?v=lXLBTBBil2U&t=13s', 'https://www.youtube.com/watch?v=USlE2huSI_w','https://www.youtube.com/watch?v=h5xY_kRKHxE', 'https://www.youtube.com/watch?v=MwiM_nPyx5Y','https://www.youtube.com/watch?v=ytZcvwZxkrg', 'https://www.youtube.com/watch?v=GI4Tpi48DlA']

for url in urls:
    video_id = url.replace('https://www.youtube.com/watch?v=', '')
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    
    current_segment = ''
    
    char_count = 0 
    
    for x in transcript:
        sentence = x['text']
        if char_count < 300:
        # If the total character count hasn't reached 1000 yet, add the length of the current sentence
            char_count += len(sentence)
            if char_count > 300:
                # If adding this sentence exceeds 1000 characters, include the part of the sentence that goes beyond 1000 characters
                excess_chars = char_count - 300
                # Calculate the starting index of the part of the sentence to be included
                start_index = len(sentence) - excess_chars
                current_segment += f'{sentence[start_index:]}\n'
            continue 
    
        # Check if adding the next sentence would exceed the 10,000 character limit.
        if len(current_segment) + len(sentence) + 1 > 2000:  # +1 for the newline character
            # If it would, add the current segment to the list of segments and start a new one.
            segments.append(current_segment)
            current_segment = f'{sentence}\n'
        else:
            # If not, just add the sentence to the current segment.
            current_segment += f'{sentence}\n'

    # Don't forget to add the last segment if it's not empty.
    if current_segment:
        segments.append(current_segment)
            
count = 0
for i in segments:
    count += 1

print (count)

question  = "What is the most profitable area in AI"
completion = get_completion(client,
    f"""Here is a large database of interview transcript segments from many interviews done by the same person: <transcript>{segments}</transcript>

    Please do the following:
        1.Please answer the question solely based on the responses by the same interviewee in the transcript segments provided and imitate the tone of the interviewee<question>{question}</question>, only output your answer and limit the answer to 100-250 words 

    """
)
    
print(completion)



    




