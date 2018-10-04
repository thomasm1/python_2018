#SHUTIL MODULE
#Automate the Boring Stuff - chapters 9 - 10

# -*- coding: utf-8 -*- 
print('#chapter 9 copying, moving, zipping, managing files ') 
import shutil, os
print('''
#os.chidir('C:\\')
#shutil.copy('C:\\wamp64\www\juillet\a.txt','C:\\wamp64\www\juillet\docs\')
#shutil.copytree(source, destation_backup)
#shutil.move(s,d_backup)
#
#os.unlink(path) # deletes file at path
#os.rmdir(path)
#shutil.rmtree(path)
print('#')
#
#SEND2TRASH MODULE
#CMD: pip install send2trash
#pip --> USE Start Command Prompt with Ruby
#pwd is C:\Python27\Scripts
#pip upgrade: pip install --upgrade pip
import send2trash
baconFile = open('bacon.txt', 'a') #creates file
baconFile.write('Bacon is not ...')
baconFile.close()
send2trash.send2trash('bacon.txt')
#os.walk()
''')
import os
for folderName, subfolders, filenames in os.walk('C:\\test'):
    print('The current folder is '+ folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF' + folderName +':' + subfolder)
    for filename in filenames:
        print('FILE INSIDE' +folderName+':'+filename)
    print('')
print('#')
#ZIPFILE MODULE
'''
import zipfile, os
os.chdir('C:\\')
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
spamInfo.compress_size
'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2))
exampleZip.close()
#
#extraxtall()
    '''
print('#chapter 10-debugging & exceptions') 
print('#')
#RAISE EXCEPTION
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2')
    if height <= 2:
        raise Exception('Height must be greater than 2')
    print(symbol*width)
    for i in range(height-2):
        print(symbol+(''*(width-2))+symbol)
    print(symbol*width)
#
print('#1)Syntax Error\n #2 Runtime Error->try,try,except\n #3 Semantic (Logic) Error-->try,except,finally')
print('#1)Syntax Error')
for sym, w, h in (('*',4,4),('0',20,5),('x',1,3),('ZZ',3,3)):
    try:
        boxPrint(sym,w,h)
    except Exception as err:
        print('An exception hath happend:'+str(err))
            
#raise Exception('This is the error msg.')
print('#2 Runtime error- november 6, 2017')

try:
    n = float(raw_input("enter a number : "))
    z = float(raw_input("enter a 2nd numBER : "))
    n/z
except ValueError:
    print("#ValueError You have to enter an integer or floating point")
except ZeroDivisionError:
    print("tmm Note!  ZeroDivisionError: you cannot enter zero ")
#else:
 #   print("n/z: " + str(n/z)) 
finally:
    print("# Exception Handling Complete!")
    print("n/z: " + str(n/z)) 
    
