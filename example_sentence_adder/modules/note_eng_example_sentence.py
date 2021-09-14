import json

class NoteEngExampleSentence:
    def __init__(self):
        with open('modules/param_fields.json', 'r') as f:
            param_fields = json.load(f)
        self.note = dict()
        self.note = dict()
        self.note['deckName'] = param_fields['deckName']
        self.note['modelName'] = param_fields['modelName']
        self.note['fields'] = dict()
        for field in param_fields['fields']:
            self.note['fields'][field] = ""
        self.note['options'] = dict()
        self.note['options']['allowDuplicate'] = param_fields['allowDuplicate']
        self.note['options']['duplicateScope'] = 'deck'
        self.note['options']['duplicateScopeOptions'] = dict()
        self.note['options']['duplicateScopeOptions']['deckName'] = param_fields['deckName']
        self.note['options']['duplicateScopeOptions']['checkChildren'] = param_fields['checkChildren']
        self.note['tags'] = list()
    
    def setEnglish(self, word):
        self.note['fields']['English'] = word
    def setKorean(self, word):
        self.note['fields']['Korean'] = word
    def setExampleSentence(self, sentence):
        self.note['fields']['example-sentence'] = sentence
    def setTag(self, tag):
        if str(type(tag)) != "<class 'str'>":
            raise Exception("Type of tag should be a str.")
        self.note['tags'] = [tag]
    def setTagList(self, tag_list):
        if str(type(tag_list)) != "<class 'list'>" and str(type(tag_list)) != "<class 'tuple'>":
            raise Exception("Type of tag_list should be a list or a tuple.")
        self.note['tags'] = tag_list
    def addTag(self, *tags):
        for tag in tags:
            self.note['tags'].append(tag)
    
    def getEnglish(self):
        return self.note['fields']['English']
    def getKorean(self):
        return self.note['fields']['Korean']
    def getExampleSentence(self):
        return self.note['fields']['example-sentence']
    def getTags(self):
        return self.note['tags']
    
    def getJson(self):
        return self.note

def test():
    a = NoteEngExampleSentence()
    a.setEnglish("eng")
    a.setKorean("kor")
    a.setExampleSentence("example")

    with open('tes.json', 'w') as f:
        json.dump(a.getNoteJson(), f, indent = '\t')

if __name__ == "__main__":
    test()
