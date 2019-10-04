# Snawksnek.py
# Cord Corcese
# Sept 19, 2019
# Imported a bunch of stuff even though this snake is not using AStar or random yet
from flask import Flask, request, jsonify
import json
import random

app = Flask(__name__)
HoldDirection = "Null"
TimesRun = 0

height = 0
width = 0


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x = x
        self.y = y

    def isSafe(self, data):  # Checks if a point is safe to move into.
        # Check for snakes
        # Bonus check adjacent tiles for snake heads and exit path
        if not self.inBounds():  # checks for in bounds
            return False
        if not self.noSnake():
            return False
        return True

    def inBounds(self):  # checks if a point is in the board. Takes Point class as arguement
        if (self.x <= width-1) and (self.x >= 0) and (self.y <= height-1) and (self.y >= 0):
            return True
        else:
            return False

    def noSnake():
        for


@app.route("/start", methods=["GET", "HEAD", "POST", "PUT"])
def start():
    print(request.data)
    snake = {
        "color": "#DDCDCD",
        "name": "BareBones",
        "taunt": "Taunt :P",
    }
    global height
    height = json.loads(request.data.decode('utf-8'))['board']['height']
    global width
    width = json.loads(request.data.decode('utf-8'))['board']['width']

    return jsonify(snake)


@app.route("/move", methods=["GET", "HEAD", "POST", "PUT"])
def move():
    dataStr = request.data
    jsonData = json.loads(dataStr.decode('utf-8'))
    print(jsonData)
    HoldDirection = nextmove(jsonData)

    response = {
        "move": HoldDirection
    }
    return jsonify(response)


def nextmove(data):  # determines best next move
    # ideal: go to food. Run from snakes
    point = Point(data['you']['body'][0]['x'], data['you']['body'][0]['y'])
    rightpt = Point(point.x+1, point.y)
    uppt = Point(point.x, point.y-1)
    leftpt = Point(point.x-1, point.y)
    if rightpt.isSafe(data):
        return "right"
    elif uppt.isSafe(data):
        return "up"
    elif leftpt.isSafe(data):
        return "left"
    else:
        return "down"


def findFood():
    # Search
    # Temporay to calm python's dislike of empty functions
    closeFood = Point(0, 0)
    return closeFood


if __name__ == "__main__":
    # Don't forget to change the IP address before you try to run it locally
    app.run(host='0.0.0.0', port=8085, debug=True)
