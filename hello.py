from flask import Flask, request
app = Flask(__name__)

Entries = []

@app.route("/")
def hello():
    return "API de tonio (qui n'a pas honte)"

@app.route("/entry/create", methods=["POST"])
def createEntry():
    """Create Entry"""
    request_json = request.get_json()
    return 'bite'

@app.route("/<int:entry_id>", methods=["GET"])
def entry(entry_id):
    """test"""
    return "total %d %s" % (entry_id)