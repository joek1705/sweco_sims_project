import nltk as nlp


class TextProcessor:

    # extract keywords from a piece of text
    def extract_keywords(self, text, language):

        # split the text into a list of tokens
        tokens = self.clean_text(text)

        # identify most frequently occurring words in a given language
        if language == "sv":
            stop_words = nlp.corpus.stopwords.words('swedish')

        # english is default
        else:
            stop_words = nlp.corpus.stopwords.words('english')

        # filter out non-keywords
        keywords = [word.lower() for word in tokens if word not in stop_words]

        # set used in order to remove multiple occurrences of a given word
        return set(keywords)

    # clean up a textstring by specified rules
    def clean_text(self,textstring):

        # punctuations to remove from the textstring
        punctuations = ['(', ')', ';', ':', '[', ']', ',', '.',"'","-","..","''","—","/"]

        # some sequences of characters should be replaced by other sequences of characters
        replacements = {"- eller":" eller", "- och":" och","- ":""}

        # remove unnecessary whitespace
        textstring = " ".join(textstring.split())

        # perform specified replacements
        for char in replacements:
            textstring = textstring.replace(char,replacements[char])

        tokens = nlp.word_tokenize(textstring)

        # remove all tokens that are classified as punctuations
        words = [word.lower() for word in tokens if word not in punctuations]

        return words

