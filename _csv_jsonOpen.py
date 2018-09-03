json_string = '{"first_name": "tom", "last_name":"maestas"}'
#file handle = open('json.json', 'r')
myfile = open('json.json')
print("1#myfile")
print(myfile)
text = myfile.read
print("2#myfile.read")
print(text)
text = myfile.read()
print("3#myfile.read()")
print(text)

print
print("#file handle = open('csv.csv', 'r')")
myfile = open('csv.csv')
print("1#myfile")
print(myfile)
text = myfile.read
print("2#myfile.read")
print(text)
text = myfile.read()
print("3#myfile.read()")
print(text)
print
w_text = open("jsonNew.json","a")
w_text.write('python')
w_text.write('class')
w_text = open(r'jsonNew.json','a')
print(w_text)
print
import json
parsed_json = json.loads(json_string)
print("##print(parsed_json['first_name'])")
print(parsed_json['first_name'])
 
jsonfile = {
    'first_name': 'tom',
    'second_name': 'maestas',
    'titles': ['job', 'Developer'],
}
print
print("##print(json.dumps(jsonfile))")
print(json.dumps(jsonfile))
