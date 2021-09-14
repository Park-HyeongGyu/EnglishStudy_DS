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
    
    def setEnglish(self, word):
        self.note['fields']['English'] = word
    def setKorean(self, word):
        self.note['fields']['Korean'] = word
    def setExampleSentence(self, sentence):
        self.note['fields']['example-sentence'] = sentence
    
    def getEnglish(self):
        return self.note['fields']['English']
    def getKorean(self):
        return self.note['fields']['Korean']
    def getExampleSentence(self):
        return self.note['fields']['example-sentence']
    
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
