# -*- coding: utf-8 -*-
"""
Created on Wed Oct 04 00:12:07 2017

@author: thomas
"""
print ('')
print ('')
print ('')

html = '''<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>'''
data = {'title': 'TMM', 'text': 'Well, Hello World'}
print html % data
#
print('#')
datum = ['first string','second string']
def html_list(data):
    for d in data:
        html = '<ul>\n<li>' + d + '</li>\n<li>' + d + '</li>\n</ul>'
    print(html)
html_list(datum)
