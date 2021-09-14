import csv
from .data_structure import CircularQueue

class csvs:
    def __init__(self, filename):
        self.file_name = filename
    def reader(self):
        line_numbers = 0
        try:
            f = open(self.file_name, 'r', encoding = 'utf-8')
            line_numbers = len(f.readlines())
            f.close()
        except:
            line_numbers = 0
        return line_numbers
    def adder(self, content):
        with open(self.file_name, 'a+', encoding = 'utf-8', newline='') as f:
            wr = csv.writer(f)
            wr.writerow(content)

def IsStringContained(param_string, compare_list):
    for a in compare_list:
        if param_string.find(a) != -1:
            return True
    return False

def list_maker(filename_with_path_ended_with_csv):
    QUEUE_SIZE = 3
    queue = CircularQueue(QUEUE_SIZE)

    for_csv = csvs(filename_with_path_ended_with_csv) 
    column = 2
    line = for_csv.reader() + 1
    print("if you input 'end' then the input proceds end")

    is_end = False
    is_delete = False
    while True:
        count = 0
        content_list = []
        while count < column:
            if count == 0:
                tem = input(str(line)+"_"+"English : ")
            elif count == 1:
                tem = input(str(line)+"_"+"뜻 : ")

            if tem == "end":
                is_end = True
                break
            elif IsStringContained(tem, ['이거 삭제', '이거삭제', 'Dths']):
                print("Delete current.")
                print()
                is_delete = True
                break
            elif IsStringContained(tem, ['위 삭제', '위삭제', 'Dpr']):
                print("Delete prior.")
                print(queue.Pop(), "is deleted")
                line -= 1
                print()
                is_delete = True
                break
            elif IsStringContained(tem, ['위 복사', '위복사', 'Cpr']):
                print("Copying prior.")
                print("Copied :" , queue.Top()[count])
                tem = queue.Top()[count]
            
            content_list.append(tem)
            count += 1

        if is_end:
            break
        if is_delete:
            is_delete = False
            continue

        queue.Enqueue(content_list)
        if queue.IsFull():
            for_csv.adder(queue.Dequeue())

        line += 1
        print()

    while not queue.IsEmpty():
        for_csv.adder(queue.Dequeue())
#End of the maker

