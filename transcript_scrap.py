from youtube_transcript_api import YouTubeTranscriptApi
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
import anthropic

# Initializing the jensen_data dictionary
jensen_data = {}

urls = ['https://www.youtube.com/watch?v=cEg8cOx7UZk', 'https://www.youtube.com/watch?v=ytZcvwZxkrg']

  
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def insert_new_lines(s, interval=1300, separator='\n\n'):
    """
    Inserts a separator into the string after every specified interval of characters.

    :param s: The original string.
    :param interval: The interval of characters after which to insert the separator.
    :param separator: The separator to insert.
    :return: The modified string with separators inserted.
    """
    # Use a list comprehension to break the string into chunks
    chunks = [s[i:i+interval] for i in range(0, len(s), interval)]
    
    # Join the chunks together with the separator
    return separator.join(chunks)

def get_completion(client, prompt):
        return client.messages.create(
            model= 'claude-3-opus-20240229',
            max_tokens=2048,
            messages=[{
                "role": 'user', "content":  prompt
            }]
        ).content[0].text
        
        
for url in urls:
    video_data = {'id': None, 'segments': []}    

    # Extract video id for input for YouTube scraping API
    video_id = url.replace('https://www.youtube.com/watch?v=', '')
    video_data['id'] = video_id
    # Store this video's data in the main dictionary
    
    try:
        # Attempt to fetch the video title
        session = HTMLSession()
        response = session.get(url)
        response.html.render(timeout=20)
        soup = bs(response.html.html, "html.parser")
        title = soup.find("meta", itemprop="name")["content"]
        video_data['title'] = title
        print(title)
    except Exception as e:
        print(f"An error occurred while fetching the page title for {video_id}: {e}")
        video_data['title'] = "Title fetch failed"

    try:
        # Attempt to fetch the video transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        output = '\n'.join(x['text'] for x in transcript)
        video_data['transcript'] = output
    except Exception as e:
        print(f"An error occurred while fetching the transcript for {video_id}: {e}")
        #video_data['transcript'] = "Transcript fetch failed"
    
  
    for x in transcript:
      sentence = x['text']
      output += f' {sentence}\n'

    segments = get_completion(client,
         f"""Here is an interview transcript: <transcript>{output}</transcript>
        
         Please split the transcript with '\n\n' for more efficient retrieval and include all content, Each segment acts as a more focused piece of information, allowing the retriever to match queries with segments that are highly relevant to the specific question or prompt. 

    # """
    )
    # segments = insert_new_lines(output)
    segments = segments.split('\n\n')
    for s in segments:
      segment_data = {
          'text': s,
          'metadata': {
              'video_title': video_data['title'],
              # Add more metadata as needed
          }
      }
      video_data['segments'].append(segment_data)
      
    jensen_data[url] = video_data

    

# Output the data to see the structure

for video_url, data in jensen_data.items():
    print(f"URL: {video_url}")
    print(f"ID: {data['id']}")
    # print(f"Transcript: {data['transcript'][:10000]}...") 
    print("Segments:")
    for segment in data['segments']:
        print(f"Segment: {segment['text']}\n")
        print(f"Segment Metadata: Video Title: {segment['metadata']['video_title']}\n")
     

