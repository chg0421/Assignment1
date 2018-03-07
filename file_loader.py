class FileLoader:

    def read_file(filename):
        fo = open(filename, "r+")
        data = fo.read(1000000)
        print("Read String is : ", data)
        print("Name of the file: ", fo.name)
        print("File Status - Closed or not : ", fo.closed)
        print("File Opening mode : ", fo.mode)
        position = fo.tell()
        print("Current file position : ", position)
        fo.close()


test = FileLoader
test.read_file("test.txt")