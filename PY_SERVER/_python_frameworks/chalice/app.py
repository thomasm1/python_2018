from os import path
from chalice import Chalice, Response

app = Chalice(app_name='Chalice Example')

index_path = path.join(
    # Grab the parent directory path
    path.dirname(__name__),
    "chalicelib",
    "template",
    "index.html"
)


@app.route('/')
def index():
    with open(index_path, 'r') as fstream:
        output = fstream.read()
    return Response(
        body=output,
        status_code=200,
        headers={'Content-Type': 'text/html'}
    )


@app.route('/json')
def json_index():
    return {"key": "value"}
