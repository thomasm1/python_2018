def remove_duplicates(countries):
    replist = []
    for i in countries:
        if i not in replist:
            replist.append(i)
    print(replist)
   # return replist 
r = ['t','t','o','o','m','a','a','s','_','_','']
remove_duplicates(r)
