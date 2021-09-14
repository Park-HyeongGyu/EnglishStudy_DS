from nltk import tokenize

class SplitBySentence:
    def __init__(self, original_sentences):
        if str(type(original_sentences)) != "<class 'str'>":
            raise Exception("Type of original_sentence must be a string.")
        self.__original_sentence = original_sentences
        self.__splitted = tokenize.sent_tokenize(self.__original_sentence)
    
    def getSentenceSplitted(self):
        return self.__splitted
    def printOriginal(self):
        return self.__original_sentence

def test():
    a = 'Occasionally individuals do not merely come out as well as clearly state what is troubling them and instead select more indirect means of expressing their annoyance. It is searched by doom ,i.e., princess. One companion might talk to the various other in a way that is condescending and also indicates underlying hostility. Numerous other times, partners may mope and even frown without genuinely dealing with an issue. Companions may likewise merely prevent discussing an issue by swiftly switching over topics when the subject turns up or by being incredibly vague. Such indirect ways of expressing temper are not useful since they don’t provide the individual that is the target of the behaviors, an idea of exactly how to react. They understand their companion is irritated, but the absence of directness leaves them without advice regarding what they can do to solve the issue.'
    s = SplitBySentence(a)
    sp = s.getSentenceSplitted()
    for line in sp:
        print(line)
        print()

if __name__ == "__main__":
    test()
 