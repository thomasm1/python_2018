import os
import re
from flask import Flask, jsonify, render_template, request, url_for
from flask_jsglue import JSGlue

# configure application
app = Flask(__name__)
JSGlue(app)

@app.route("/<string:filename>")
def main(filename):
    """Render file."""
    return render_template(filename)