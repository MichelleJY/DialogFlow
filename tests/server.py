#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from urllib import unquote_plus
import json
import re


app = Flask(__name__)


def parse_request(req):
    """
    Parses application/json request body data into a Python dictionary
    """
    payload = req.get_data()
    payload = unquote_plus(payload)
    payload = re.sub('payload=', '', payload)
    payload = json.loads(payload)

    return payload


@app.route('/', methods=['GET'])
def index():
    """
    Go to localhost:5000 to see a message
    """
    return ('This is a website.', 200, None)


@app.route('/api/print', methods=['POST'])
def print_test():
    """
    Send a POST request to localhost:5000/api/print with a JSON body with a "p" key
    to print that message in the server console.
    """
    payload = parse_request(request)
    print(payload['p'])
    return ("", 200, None)


@app.route('/api/sum', methods=['POST'])
def sum():
    """
    Send a POST request to localhost:5000/api/sum with a JSON body with an "a" and "b" key
    to have the app add those numbers together and return a response string with their sum.
    """
    print("Processing request...")
    payload = parse_request(request)
    print("Receieved following paylod:")
    print(payload)

    print("Adding sum...")
    summation = payload['a'] + payload['b']
    print("Found sum: %s" % summation)

    print("Creating response string...")
    resp = '%s + %s = %s' % (payload['a'], payload['b'], summation)
    print("Sending the following response:")
    print(resp)

    return (resp, 200, None)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)