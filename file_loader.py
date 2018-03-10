import time as t
from os import path


class Filer:

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

    def create_file(dest):
        answer = input("Do you want to save file? ")

        if answer =='yes' or answer =='Yes' or answer == 'Y' or answer == 'y':
            """ The script create a text file at the passed in location name file based on date"""
            date = t.localtime(t.time())
            # file name = month_day_year

            name = "{:d}{:d}{:d}.txt".format(date[1],date[2],(date[0]%100))
            if not (path.isfile(dest + name)):
                f = open(dest + name,'w')
                f.write("derewrewrweerwe")
                f.close()

            destination ="F:\Ara3\Python\Assignment\test"
            # create_file(destination)
            input("File Saved!!!")
        else:
            print("Cancelled")

test = Filer
test.read_file("test.txt")
test.create_file("test_save")