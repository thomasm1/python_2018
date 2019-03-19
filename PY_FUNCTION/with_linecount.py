with open('Alone.txt', encoding='utf-8') as file:
    file.seek(16)
    char = file.read(1)
    print(char)
    
    # 16
    # o 
    
# line.py
lineCount = 0
with open('Daffodils.txt', encoding='utf-8') as file:
    for line in file:
        lineCount += 1
        print('{:<5} {}'.format(lineCount, line.rstrip()))
