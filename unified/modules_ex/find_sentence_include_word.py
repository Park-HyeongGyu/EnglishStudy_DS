import nltk
from nltk.stem.wordnet import WordNetLemmatizer
#https://stackoverflow.com/questions/3753021/using-nltk-and-wordnet-how-do-i-convert-simple-tense-verb-into-its-present-pas

class FindSentenceIncludeWord:
    def __init__(self, sentences_list_):
        if str(type(sentences_list_)) != "<class 'list'>":
            raise Exception("type of sentences_list should be list.")
        self.SENTENCES_LIST = sentences_list_
        self.LEN_SENTENCES_LIST = len(self.SENTENCES_LIST)
    
    def find(self, word_to_find):
        to_return = list()
        index = 0
        lower_word_to_find = word_to_find.lower()
        while index < self.LEN_SENTENCES_LIST:
            sentence = self.SENTENCES_LIST[index]
            lower_sentence = sentence.lower()
            if lower_sentence.find(lower_word_to_find) != -1:
                to_return.append(sentence)
            index += 1
        return to_return

class FindSentenceIncludeWordNlp:
    def __init__(self, sentences_list):
        if str(type(sentences_list)) != "<class 'list'>" and str(type(sentences_list)) != "<class 'tuple'>":
            raise Exception("type of sentences_list should be list or tuple.")
        self.SENTENCE_DICT = dict() 
        for one_sentence in sentences_list:
            self.SENTENCE_DICT[self.__divideSentenceBasedOnPOS(one_sentence)] = one_sentence 
    
    def __divideSentenceBasedOnPOS(self, one_sentence): # POS - Parts of speech
        one_sentence = one_sentence.lower()
        pos_list = nltk.pos_tag(nltk.word_tokenize(one_sentence)) # https://medium.com/@gianpaul.r/tokenization-and-parts-of-speech-pos-tagging-in-pythons-nltk-library-2d30f70af13b
        sent_preprocessed = list()
        for one_word in pos_list:
            word = one_word[0]
            parts_of_speech = one_word[1] # parts_of_speech == 품사
            sent_preprocessed.append(word)
            if parts_of_speech == "NNS": # noun plural
                sent_preprocessed.append(self.__getSingularNoun(word))
            elif parts_of_speech == "JJR": #adjective comparative
                sent_preprocessed.append("-er")
                sent_preprocessed.append("~er")
            elif parts_of_speech == "JJS": # adjective, surperlative
                sent_preprocessed.append("-est")
                sent_preprocessed.append("~est")
            elif parts_of_speech == "POS": # possesive ending
                sent_preprocessed.append("one's")
            elif parts_of_speech == "PRP$": # posessive pronoun
                sent_preprocessed.append("one's")
            elif parts_of_speech == "VBD": # verb, past tense
                sent_preprocessed.append(self.__getNon3rdPresentTense(word))
            elif parts_of_speech == "VBG": # gerund/present participle ex.taking
                sent_preprocessed.append("-ing")
                sent_preprocessed.append("~ing")
                sent_preprocessed.append(self.__getNon3rdPresentTense(word))
            elif parts_of_speech == "VBN": # past participle
                sent_preprocessed.append(self.__getNon3rdPresentTense(word))
                sent_preprocessed.append("pp")
                sent_preprocessed.append("p.p")
                sent_preprocessed.append("p.p.")
                sent_preprocessed.append("-ed")
                sent_preprocessed.append("~ed")
            elif parts_of_speech == "VBP": # non 3rd person present
                sent_preprocessed.append(self.__getNon3rdPresentTense(word))
            elif parts_of_speech == "VBZ": # 3rd person present
                sent_preprocessed.append(self.__getNon3rdPresentTense(word))
            sent_preprocessed_lower = list() 
            for one in sent_preprocessed:
                sent_preprocessed_lower.append(one.lower())
        return tuple(sent_preprocessed_lower)
    
    def __getSingularNoun(self, word):
        return WordNetLemmatizer().lemmatize(word)
    def __getNon3rdPresentTense(self, word):
        return WordNetLemmatizer().lemmatize(word, 'v')
    
    def find(self, word_to_find):
        splitted_word = word_to_find.split()
        if len(splitted_word) == 1: # In case of there is no space in word_to_find
            return self.__findWordWithNoSpace(word_to_find.lower())
        elif len(splitted_word) != 1:
            splitted_word_lower = list()
            for one in splitted_word:
                splitted_word_lower.append(one.lower())
            return self.__findWordWithSpace(tuple(splitted_word_lower))

    def __findWordWithNoSpace(self, word_to_find):
        if str(type(word_to_find)) != "<class 'str'>":
            raise Exception("type of word_to_find should be str.")
        sentences_finded = list()
        divided_sentences = self.SENTENCE_DICT.keys()
        for one_divided_sentence in divided_sentences:
            if word_to_find in one_divided_sentence:
                unsplitted_sentence = self.SENTENCE_DICT[one_divided_sentence]
                sentences_finded.append(unsplitted_sentence)
        return tuple(sentences_finded)
    
    def __findWordWithSpace(self, word_to_find):
        if str(type(word_to_find)) != "<class 'tuple'>" and str(type(word_to_find)) != "<class 'list'>":
            raise Exception("Type of word_to_find_tupe should be tuple or list.")
        preprocessed_word_to_find = self.__removeExceptions(word_to_find)
        sentences_finded = list()
        divided_sentences = self.SENTENCE_DICT.keys()
        for one_divided_sentence in divided_sentences:
            count_finded_word = 0
            for one_word in preprocessed_word_to_find:
                if one_word in one_divided_sentence:
                    count_finded_word += 1
            if count_finded_word == len(preprocessed_word_to_find):
                unsplitted_sentence = self.SENTENCE_DICT[one_divided_sentence]
                sentences_finded.append(unsplitted_sentence)
        return tuple(sentences_finded)
    
    def __removeExceptions(self, word_list):
        if str(type(word_list)) != "<class 'tuple'>" and str(type(word_list)) != "<class 'list'>":
            raise Exception("Type of word_list should be tuple or list")
        exceptions = ('...', '~', 'A', 'B')
        word_list_copied = list(word_list)
        for one_word in word_list:
            if one_word in exceptions:
                word_list_copied.remove(one_word)
        return word_list_copied

def test():
    pass

if __name__=="__main__":
    test()

