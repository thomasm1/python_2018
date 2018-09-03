book = {}
book['tom'] = {
    'name': 'tom',
    'address': '2300 Calle de Real, NM',
    'phone': '505-508-7707'
}
book['tom2'] = {
    'name': 'tom',
    'address': '2300 Calle de Real',
    'phone': '505-508-????'
}

import json
s=json.dumps(book)

with open("c://xampp//htdocs//juillet//data//book.txt","w") as f:
    f.write(s)
with open('text.txt', 'r') as f:
    
f = open('test.txt', 'r')
print(f.mode)
f.close()
