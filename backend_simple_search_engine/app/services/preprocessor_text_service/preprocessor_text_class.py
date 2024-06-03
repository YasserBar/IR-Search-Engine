
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag
class Preprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def get_wordnet_pos(self, tag):
        tag_dict = {
            "J": wordnet.ADJ,
            "N": wordnet.NOUN,
            "V": wordnet.VERB,
            "R": wordnet.ADV
        }
        return tag_dict.get(tag[0].upper(), wordnet.NOUN)

    def lemmatization(self, tagged_doc_text):
        return [self.lemmatizer.lemmatize(word, pos=self.get_wordnet_pos(tag)) for word, tag in tagged_doc_text]
    
    def preprocess(self, text):
        tokens = word_tokenize(text.lower())
        tokens = [token.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))) for token in tokens]
        tokens = [subtoken for token in tokens for subtoken in token.split()]
        tokens = [token for token in tokens if token.strip() and len(token) > 1]        
        tokens = [word for word in tokens if word not in self.stop_words]
        tagged_tokens = pos_tag(tokens)
        tokens = self.lemmatization(tagged_tokens)
        return tokens