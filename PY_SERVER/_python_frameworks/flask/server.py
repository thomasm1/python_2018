import argparse
from os import path
from flask import Flask, request, redirect, url_for
from jinja2 import Template
from werkzeug.contrib.fixers import ProxyFix
from flask_sqlalchemy import SQLAlchemy
app = Flask("demo flask server")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/flask_db.db'
db = SQLAlchemy(app)

index_path = path.join(
    # Grab the parent directory path
    path.dirname(path.abspath(path.dirname(__name__))),
    "template",
    "index.html"
)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(250), unique=True, nullable=False)

    def __repr__(self):
        return self.note


@app.route("/", methods=["GET"])
def index():
    with open(index_path, 'r') as fstream:
        template = Template(fstream.read())
    output = template.render(
        title="Flask Server",
        description="Flask, the python (micro)framework",
        notes=[str(note) for note in Note.query.all()],
        has_notes=True
    )
    return output.encode('ascii')


@app.route("/", methods=["POST"])
def create_note():
    note = request.form.get("note", None)
    if note is None:
        return redirect(url_for('.index'))
    new_note = Note(note=note)
    # Add note to the database session
    db.session.add(new_note)
    # Commit changes in session to the database
    db.session.commit()
    return redirect(url_for('.index'))


def run_flask(app):
    parser = argparse.ArgumentParser(
        description='Example Flask server'
    )
    parser.add_argument(
        "-port",
        "--port",
        default=8000,
        help="Port to run server on"
    )
    parser.add_argument(
        "-host",
        "--host",
        default="localhost",
        help="Host to run server on"
    )
    parser.add_argument(
        "--debug",
        default=False,
        help="Debug Mode"
    )

    args = parser.parse_args()
    app.logger.info(
        "Demo Flask server running at {0}:{1}".format(
            args.host,
            args.port
        )
    )
    app.run(
        host=args.host,
        port=int(args.port),
        debug=bool(args.debug),
        threaded=True
    )


app.wsgi_app = ProxyFix(app.wsgi_app)

if not path.isfile("/tmp/flask_db.db"):
    db.create_all()

if __name__ == '__main__':
    run_flask(app)
