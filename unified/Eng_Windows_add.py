from modules.description import *
from modules.list_maker_add import list_maker

def GetFilename():
    a = input("Input file name : ")
    to_return = a + ".csv"
    return to_return

#From here, int main()
def main():
    print("제작자:박형규")
    print("제작일:2020년4월30일")
    print("예문 모듈 제작일:2020년 11월 29일")
    print("append 수정일:2021년2월1일")
    print("입력받은 텍스트들을 csv파일로 만들어주는 프로그램.")
    print("저장 경로:현재경로")
    print("위의 폴더 안에 자동으로 .csv가 붙은 파일을 만들어줍니다.")
    print()
    Convenients()
    HowMakeTag()
    list_maker(GetFilename())
    print("Press enter to exit program......", end="")
    input()

if __name__ == "__main__":
    main()
