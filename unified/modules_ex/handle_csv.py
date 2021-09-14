import csv

class HandleCsv:
    def __init__(self):
        pass

    def setFileNameToWrite(self, file_name_):
        self.file_name_to_write = file_name_
        if self.file_name_to_write[-4:] != '.csv':
            if self.file_name_to_write.find('.') != -1:
                raise Exception("file extension should be '.csv'.")

            self.file_name_to_write = self.file_name_to_write + '.csv'
    
    def read(self, file_name):
        to_return = list()
        with open(file_name, 'r', encoding = 'utf-8') as f:
            rdr = csv.reader(f)
            for line in rdr:
                to_return.append(line)
        return to_return

    def read_tsv(self, file_name):
        to_return = list()
        with open(file_name, 'r', encoding = 'utf-8') as f:
            rdr = csv.reader(f, delimiter = '\t')
            for line in rdr:
                to_return.append(line)
        return to_return

   
    def write(self, to_write):
        if str(type(to_write)) != "<class 'list'>":
            raise Exception("type of to_write should be two dimension list.")
        for content in to_write:
            if str(type(content)) != "<class 'list'>":
                raise Exception('type of to_write should be two dimension list.')
        with open(self.file_name_to_write, 'w', encoding = 'utf-8', newline = '') as f:
            wr = csv.writer(f)
            wr.writerows(to_write)
    
    def appendOne(self, to_append):
        if str(type(to_append)) != "<class 'list'>":
            raise Exception("type of to_append should be one dimension list.")
        with open(self.file_name_to_write, 'a', encoding = 'utf-8', newline = '') as f:
            wr = csv.writer(f)
            wr.writerow(to_append)

def test():
    cs = HandleCsv() 
    cs.setFileNameToWrite('test')
    cs.appendOne(['a', 'b', 'c'])
    cs.appendOne(['dd', 'e'])

if __name__=="__main__":
    test()
