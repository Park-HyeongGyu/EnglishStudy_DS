from .data_structure import CircularQueue

def IsStringContained(param_string, compare_list):
    for a in compare_list:
        if param_string.find(a) != -1:
            return True
    return False

def list_maker():
    QUEUE_SIZE = 3
    queue = CircularQueue(QUEUE_SIZE)

    list_to_return = list()

    COLUMN = 2
    print("새 단어를 입력합니다.")
    print("'end'라고 입력하면 입력 프로세스가 종료됩니다.")

    is_end = False
    is_delete = False
    while True:
        count = 0
        content_list = []
        while count < COLUMN:
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
            list_to_return.append(queue.Dequeue())

        line += 1
        print()

    while not queue.IsEmpty():
        list_to_return.append(queue.Dequeue())
    
    return list_to_return
#End of the maker

