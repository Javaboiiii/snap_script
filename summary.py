import spacy

from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = """Samsung canceled in-person attendance of MWC 2021, committing only to an online presence.
 Today the company made it official and set the time and date for the Samsung Galaxy MWC Virtual 
 Event, which will be held on June 28 at 17:15 UTC. It will be livestreamed on YouTube, so everyone can attend.

The press release announcing the event is pretty terse – the company will will talk about the “ever-expanding Galaxy device ecosystem” 
and will present a “vision for the future of smartwatches”. What Galaxy devices?"""
def summarizer(rawdocs) :
    stopwords = list(STOP_WORDS)
    # print(stopwords)

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    # print(doc)

    tokens = [token.text for token in doc]
    # print(tokens)

    word_freq = {}

    for word in doc :
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys() :
                word_freq[word.text] = 1
            else :
                word_freq[word.text] += 1

    # print(word_freq)

    max_freq = max(word_freq.values())
    # print(max_freq)

    for word in word_freq.keys() :
        word_freq[word] = word_freq[word]/max_freq

    # print(word_freq)

    sent_tokens = [sent for sent in doc.sents]
    # print(sent_tokens)

    sent_scores = {}
    for sent in sent_tokens : 
        for word in sent : 
            if word.text in word_freq.keys() :
                if sent not in sent_scores.keys() :
                    sent_scores[sent] = word_freq[word.text]
                else :
                    sent_scores[sent] += word_freq[word.text]

    # print(sent_scores)

    select_len = int(len(sent_tokens) * 0.3)
    # print(select_len)
    summary = nlargest(select_len, sent_scores, key = sent_scores.get)
    
    # print(summary)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    # print(text)
    # print(summary)
    # print("Lenght of the original text",len(text.split(' ')))
    # print("Lenght of the summarized text",len(summary.split(' ')))

    

    return rawdocs, summary, len(rawdocs.split(' ')), len(summary.split(' '))