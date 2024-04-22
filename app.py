from flask import Flask, json

from flask_cors import CORS


from youtube_transcript_api import YouTubeTranscriptApi as yt
# from transformers import pipeline # This is library from internet 
# Importing my own library
from summary import summarizer


app = Flask(__name__)

CORS(app)
 
def plain_transcript(x) :
    ans = ""
    for i in x :
        ans += i['text']
        if ans[-1] != ' ' :
            ans += " "
    return ans;


@app.route('/<ytid>')
def hello_world(ytid):
    # Obtaining the transcript 
    transcript_list = yt.list_transcripts(ytid)
    transcript = transcript_list.find_transcript(language_codes=['de', 'en', 'hi'])
    
    # obtaining the summary
    # summarization = pipeline("summarization", model="pszemraj/led-large-book-summary") # model="model_name" needs to be decided
    # truncation = True for the normal model
    # summary_text = summarization(plain_transcript(transcript.fetch()))# Add this to get the plain_text of the summary [0]['summary_text']
    # truncation is used so that there will be not index out of the bound
    # truncation = True

    # This is summarizing using my own library
    summary_text = summarizer(plain_transcript(transcript.fetch()))
    json_format = json.dumps(summary_text)
    return json_format
    # return plain_transcript(transcript.fetch())
    
if __name__ == "__main__":
    app.run(debug=True)