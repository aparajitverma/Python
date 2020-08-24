import _io
f=open(r"Z:\npr.txt","r")
print(type(f))
m=f.read(5)
print(m)
m=f.read(3)
print(m)
'''modes r if file existe, data will be read from startof file,elif error
        w` if file exists, firstly file will be truncated, elif file doesnt exist then a new file will be created
        a   if file exists, then data will be written at end of file,elif if file doesnt exist,then a new file will be created
        a+read and append   r and w but if file doesnt exist a new file will be created
        r+read and write    both read and write file, if file doesnt exist,then error
        w+                  both and read write, if file doesnt exist then new file will be created
        
binary mode     rb
        wb
        ab
        rb+ read and write binary
        wb+
        ab+
        
        
'''
t=f.readable()
print(t)
f.close()
f=open('Z://heya.txt','rb')
m=f.read(10)
n=f.tell() # current cursor pos
print(n)

f.seek(-10,2)#whence   0--> starting of file  1--> current cursor position 2--> end of file
m=f.read(10) # b in run tells file is opened in binary mode
print(m)        #if we give 2 in whence argument, if files in text mode, it wont run.....only in binary mode
#converting list into strings



