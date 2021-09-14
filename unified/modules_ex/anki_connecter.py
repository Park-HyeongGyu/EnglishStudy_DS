import json
import urllib.request
from modules.note_eng_example_sentence import NoteEngExampleSentence

class AnkiConnecter:
    def __init__(self):
        with open('modules/param_fields.json', 'r') as f:
            param_field = json.load(f)
        self.__DECK_NAME = param_field['deckName']
        self.__FIRST_FIELD = param_field['fields'][0]
        self.__ORIGIN_NOTE_INFOS = self.__getNoteInfos()
        self.__ORIGIN_NOTES = self.__getNotes(self.__ORIGIN_NOTE_INFOS)
        self.__staged_notes = list()
        self.__staged_notes_duplicated = dict() # {ID : card, ...}
        self.__ORIGIN_NOTES_DUPLICATED = dict()
    
    def __printProcess(self, message):
        if str(type(message)) != "<class 'str'>":
            raise Exception("Type of message should be str.")
        print("*",message)
   
    def __getNotes(self, note_infos):
        notes = list()
        for note in note_infos:
            notes.append(note['fields'][self.__FIRST_FIELD]['value'])
        self.__printProcess("getting notes......")
        return tuple(notes)

    def __getNoteInfos(self):
        self.__printProcess("getting note infos......")
        return self.__invoke("notesInfo", {"notes": self.__getNoteIDs()})['result']

    def __getNoteIDs(self):
        param = {'query': "deck:"+self.__DECK_NAME}
        note_ids = self.__invoke('findNotes', param)['result']
        self.__printProcess("getting note Ids......")
        return note_ids

    def __invoke(self, action, params):
        requestJson = json.dumps(self.__request(action, params)).encode('utf-8')
        response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', requestJson)))
        if len(response) != 2:
            raise Exception('response has an unexpected number of fields')
        if 'error' not in response:
            raise Exception('response is missing required error field')
        if 'result' not in response:
            raise Exception('response is missing required result field')
        if response['error'] is not None:
            raise Exception(response['error'])
        return response
    def __request(self, action, params):
        return {'action': action, 'params': params, 'version': 6}
    
    def stageNote(self, note):
        note_copied = NoteEngExampleSentence()
        note_copied.setEnglish(note.getEnglish())
        note_copied.setKorean(note.getKorean()) 
        note_copied.setExampleSentence(note.getExampleSentence())
        note_copied.setTagList(note.getTags())
        # I don't know why I should do a action of copying like it.
        # When I used this function while not copying note, there was an error.
        # I think there will be a more good answer.
        # But I don't have time now because I'm doing Yaja.
        # So I will give a mission to solve this problem to me of future.
        if self.__is_duplicated(note_copied.getEnglish()):
            self.__stageNoteToDuplicateds(note_copied.getJson())
        else:
            self.__staged_notes.append(note_copied.getJson())

    def __is_duplicated(self, word):
        if word in self.__ORIGIN_NOTES:
            return True
        else:
            return False
    
    def __stageNoteToDuplicateds(self, note):
        if str(type(note)) != "<class 'dict'>":
            raise Exception("Type of note should be dict.")
        eng = note['fields'][self.__FIRST_FIELD]
        finded_note = self.__findNote(eng)
        self.__ORIGIN_NOTES_DUPLICATED[finded_note['noteId']] = finded_note['note']
        self.__staged_notes_duplicated[finded_note['noteId']] = note
       
    def __findNote(self, first_field):
        note_to_return = NoteEngExampleSentence()
        for one in self.__ORIGIN_NOTE_INFOS:
            if one['fields'][self.__FIRST_FIELD]['value'] == first_field:
                note_to_return.setEnglish(one['fields']['English']['value'])
                note_to_return.setKorean(one['fields']['Korean']['value'])
                note_to_return.setExampleSentence(one['fields']['example-sentence']['value'])
                note_to_return.setTagList(one['tags'])
                note_id = one['noteId']
                return {"noteId": note_id, "note": note_to_return.getJson()}
 
    def addAllStagedNotes(self):
        self.__invoke("addNotes", {'notes': self.__staged_notes})
        self.__printProcess("adding all staged notes......")
    
    def updateAllStagedDuplicatedNotes(self):
        duplicated_note_ids = tuple(self.__staged_notes_duplicated.keys())
        quantity_total_cards = len(duplicated_note_ids)

        self.__printEngsOfStagedDuplicatedNotes(duplicated_note_ids)
        self.__printProcess("updating all staged duplicated notes......")
        print()

        count = 1
        for duplicated_note_id in duplicated_note_ids:
            eng = self.__staged_notes_duplicated[duplicated_note_id]['fields']['English']
            print("(" + str(count) + "/" + str(quantity_total_cards) + ") : " + eng)
            self.__updateNoteFields(duplicated_note_id)
            tag = self.__staged_notes_duplicated[duplicated_note_id]['tags'][0]
            self.__updateTags(tag, duplicated_note_id)
            self.__forgetNote(duplicated_note_id)
            count += 1
    
    def __printEngsOfStagedDuplicatedNotes(self, duplicated_note_ids):
        print("<List of duplicated notes>")
        count = 1
        for duplicated_note_id in duplicated_note_ids:
            print(str(count) + " : " + self.__staged_notes_duplicated[duplicated_note_id]['fields']['English'])
            count += 1
    
    def __updateNoteFields(self, duplicated_note_id):
        param = dict()
        param['note'] = dict()
        # new / old
        eng = self.__staged_notes_duplicated[duplicated_note_id]['fields']['English']
        new_kor = self.__staged_notes_duplicated[duplicated_note_id]['fields']['Korean'] + " / " + self.__ORIGIN_NOTES_DUPLICATED[duplicated_note_id]['fields']['Korean']
        new_example_sentence = self.__staged_notes_duplicated[duplicated_note_id]['fields']['example-sentence'] + "<br>/<br>" + self.__ORIGIN_NOTES_DUPLICATED[duplicated_note_id]['fields']['example-sentence']
        param['note']['id'] = duplicated_note_id
        param['note']['fields'] = dict()
        param['note']['fields']['English'] = eng
        param['note']['fields']['Korean'] = new_kor
        param['note']['fields']['example-sentence'] = new_example_sentence
        self.__invoke('updateNoteFields', param) 
        self.__printProcess("updating note fields......")
    
    def __updateTags(self, tag, duplicated_note_id):
        if str(type(tag)) != "<class 'str'>":
            raise Exception("Type of tag should be str.")
        param = dict()    
        param['notes'] = [duplicated_note_id]
        param['tags'] = tag
        self.__invoke('addTags', param)
        self.__printProcess("updating tags......")
    
    def __forgetNote(self, duplicate_note_id):
        cards = self.__findCards(duplicate_note_id) 
        param = {"cards":cards}
        self.__invoke("forgetCards", param)
        self.__printProcess("forgetting notes......")
    
    def __findCards(self, duplicate_note_id):
        param = {"query": "nid:"+str(duplicate_note_id)} #nid : note id
        result = self.__invoke("findCards", param)
        self.__printProcess("finding cards......")
        return result['result']

def test():
    a = NoteEngExampleSentence()
    connect = AnkiConnecter()
    for count in range(10):
        a.setEnglish(str(count)+" eng")
        a.setKorean(str(count)+" kor")
        a.setExampleSentence(str(count)+ "example")
        a.setTag('connect_testing')
        connect.stageNote(a)
    b = NoteEngExampleSentence()
    b.setEnglish('invest')
    b.setKorean('ddd')
    b.setExampleSentence('newddfdasfdafda')
    b.setTag("dd")
    connect.stageNote(b)

    connect.addAllStagedNotes()
    connect.updateAllStagedDuplicatedNotes()

if __name__ == "__main__":
    test()
