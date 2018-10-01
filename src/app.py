"""Text Search Server
Usage: app.py [-d DOC]

-h --help    show this

-d DOC       specify input document [default: ./assets/king-i.txt]
"""

import json
from flask import Flask, Response
from docopt import docopt
from algorithm import SimpleSearch

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, add string to URL for getting a search result"


@app.route("/<string:string>", methods = ['GET'])
def search_text(string):
    if string == "":
        error_response = {
            "error": "Cannot search a null string"
        }
        return Response(
            json.dumps(error_response),
            status=400
        )

    search_result = document.search(string)

    return Response(
        json.dumps(search_result),
        status=200,
        mimetype='application/json'
    )


if __name__ == "__main__":

    args = docopt(__doc__, argv=None, help=True, version=0.1, options_first=False)
    with open(args["-d"]) as f:
        document = SimpleSearch(f)

    app.run(host="0.0.0.0", port=8080)
