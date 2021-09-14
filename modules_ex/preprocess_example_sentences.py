class PreprocessExampleSentences:
    def __init__(self, example_sentence_file_name):
        with open(example_sentence_file_name, 'r', encoding = 'utf-8') as f:
            self.__example_sentences_list = f.readlines()
        self.__removeNewLine()
        self.example_sentences = self.__addAllInList()
    
    def __removeNewLine(self):
        index = 0
        while index < len(self.__example_sentences_list):
            content = self.__example_sentences_list[index]
            if content.find('\n') != -1:
                content = content[:-1]
            self.__example_sentences_list[index] = content
            index += 1
    
    def __addAllInList(self):
        to_return = ""
        for oneLine in self.__example_sentences_list:
            to_return  = to_return + oneLine + " "
        to_return = to_return[:-1]
        return to_return
    
    def get(self):
        return self.example_sentences
    

def test():
    a = PreprocessExampleSentences('ex.txt')
    print(a.get())

if __name__ == "__main__":
    test()
