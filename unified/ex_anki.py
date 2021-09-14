from modules_csv.description import Convenients
from modules_csv.list_maker_add import list_maker
from modules_ex.preprocess_example_sentences import PreprocessExampleSentences
from modules_ex.find_sentence_include_word import FindSentenceIncludeWordNlp
from modules_ex.split_by_sentence import SplitBySentence
from modules_ex.anki_connecter import AnkiConnecter
from modules_ex.note_eng_example_sentence import NoteEngExampleSentence

def caution():
    print("*******주의사항*******")
    print("이 프로그램은 anki-connect가 설치되어있는 anki 프로그램이 동작중이어야 작동합니다.")
    input("anki 프로그램을 여십시오. 계속하려면 엔터를 누르십시오.")

def main():
    caution()

    print("예문이 있는 파일의 이름을 입력하십시오.")
    file_name_example_sentences = input("파일 이름 : ")

    file_name_example_sentences = "contents/" + file_name_example_sentences

    preprocess_example_sentence = PreprocessExampleSentences(file_name_example_sentences)
    example_sentences = preprocess_example_sentence.get()

    split_by_sentence = SplitBySentence(example_sentences)
    parsed_example_sentences = split_by_sentence.getSentenceSplitted()

    Convenients()
    new_words = list_maker()
    # structure of new_words = [english, korean]

    find_sentence_include_word = FindSentenceIncludeWordNlp(parsed_example_sentences)
    
    print()
    note_for_param = NoteEngExampleSentence()
    anki_connecter = AnkiConnecter()
    for line in new_words:
        example_to_append = ""
        english = line[0]
        meaning = line[1]
        print(english,"-", meaning)
        example_of_word = find_sentence_include_word.find(english)

        if len(example_of_word) == 0:
            print("예문 파일에 해당 단어를 포함한 예문이 없습니다")
            example_to_append = input("예문을 입력하십시오 : ")
        elif len(example_of_word) >= 1 and len(example_of_word) <= 3:
            for one_example in example_of_word:
                if example_to_append == "":
                    example_to_append = one_example
                else:
                    example_to_append = example_to_append + " / " + one_example
        elif len(example_of_word) > 3:
            print("<예문이 너무 많습니다. 어떤 예문을 등록할지 선택하십시오.>")
            print("만약 0을 입력하셨다면, 예문을 직접 입력할 수 있습니다..")
            count = 1 
            for one in example_of_word:
                print(count, ":", one)
                count += 1
            chosens = getChosenNumbers(len(example_of_word))
            if chosens == [0]:
                example_to_append = input("예문을 입력하십시오 : ")
            else:
                for one in chosens:
                    example_to_append = example_to_append + " / " + example_of_word[one-1]

        note_for_param.setEnglish(english)        
        note_for_param.setKorean(meaning)
        note_for_param.setExampleSentence(example_to_append)

        anki_connecter.stageNote(note_for_param)
        print()
    anki_connecter.addAllStagedNotes()
    anki_connecter.updateAllStagedDuplicatedNotes()
    input("프로그램을 종료하려면 엔터를 누르십시오......")

def getChosenNumbers(LIMIT):
    # This part should be modified to way that not uses while. But I don't have time now because I'm in school and doing Yaja.
    # I believe me in future will modify it.
    print("주의사항 : 숫자와 쉼표만으로 입력하십시오. ex)1,2,4")
    while True:
        chosed_numbers = input("넣을 예문의 숫자를 입력하십시오. : ")
        numbers = chosed_numbers.split(',')
        for x in range(len(numbers)):
            numbers[x] = int(numbers[x])
        cont = 0
        for one in numbers:
            if one < 0 or one > LIMIT:
                print("잘못된 입력입니다. 다시 입력해주십시오.\n")
                cont += 1
        if cont == 0:
            break

    return numbers

if __name__ == "__main__":
    main()
