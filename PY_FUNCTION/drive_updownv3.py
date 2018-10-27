
DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

FILES = (
    ('hello.txt', None),
    ('hello.txt', 'application/vnd.google-apps.document'),
)

for filename, mimeType in FILES:
    body = {'name': filename}
    if mimeType:
         metadata['mimeType'] = mimeType
    res = DRIVE.files().create(body=metadata, media_body=filename).execute()
    filename = res['name']
    mimeType = res['mimeType']
    fileId = res['id']
    print('Uploaded "%s" (%s)' % (filename, mimeType))
    
 if res:
        print('Uploaded "%s" (%s)" % (filename, res['mimeType']))
        
 if res: 
    MIMETYPE = 'application/pdf'
    data = DRIVE.files().export(fileId=fileId, mimetype=MIMETYPE).execute() 
    if data:
        fn = '%s.pdf' % os.path.splitext(filename)[0]
        with open(fn, 'wb') as fh:
            fh.write(data)
        print('Downloaded "%s" (%s)' % (fn, MIMETYPE))
