import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')



def summarize_text(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Check if the text is too short to summarize
    if len(sentences) <= 2:
        return "Text is too short to summarize."
    
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.isalnum()]
    words = [word for word in words if word not in stop_words]
    
    # Calculate word frequency
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    # Calculate sentence scores based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_freq[word]
                else:
                    sentence_scores[sentence] += word_freq[word]
    
    # Select top 30% of sentences based on score
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:max(1, len(sentences) // 3)]
    summary = ' '.join(summary_sentences)
    return summary