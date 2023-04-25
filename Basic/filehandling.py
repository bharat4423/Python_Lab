try:
    with (open('file.txt','r')as fh):
        print("Agodarcha Code:.......",fh.read())
except FileNotFoundError:
    print("file not found")

finally:

    with ( open('file.txt',"a+") as fh):
        fh.write("\n I was created with default text")
        # print(fh.read())
        
        before_write=fh.tell()
        fh.write("\n I am appended data")
        fh.seek(before_write)
        print("appended data-------",fh.read())
        fh.seek(0)
        print("Data Completed-------",fh.read())
        
    