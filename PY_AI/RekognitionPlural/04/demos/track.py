import json

personlasttime = {}

with open('people.json', 'r') as f:
    nullcount = 0
    tracking = json.load(f)
    allitems = tracking['Persons']
    for item in allitems:
        person = item['Person']
        timestamp = item['Timestamp']
        try:
            face = person['Face']
            confidence = float(face['Confidence'])
            index = int(person['Index'])
            if( confidence > 10.0 ):    
                try:
                    lasttime = personlasttime[index] 
                    if( lasttime < 0 ):
                        print('person %d appears at %d' % (index,timestamp))
                    personlasttime[index] = timestamp
                except:
                    personlasttime[index] = timestamp
                    print('person %d appears at %d' % (index,timestamp))
        except:
            nullcount = nullcount + 1
        for personindex, stamp in personlasttime.items():
            if( stamp > 0 ):
                if( (timestamp - stamp) > 1000 ):
                    print('person %d leaves at %d' % (personindex,timestamp))
                    personlasttime[personindex] = -100
        

