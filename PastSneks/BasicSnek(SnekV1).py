# Imported a bunch of stuff even though this snake is not using AStar or random yet
from flask import Flask, request, jsonify
import json
import random

app = Flask(__name__)
HoldDirection = "Null"
TimesRun = 0

@app.route("/start", methods=["GET","HEAD","POST","PUT"])
def start():
    print(request.data)
    snake = {
        "color": "#C0C0C0",
        "name": "BareBones",
	"taunt": "Taunt :P",
    }
    
    return jsonify(snake) 

@app.route("/move", methods=["GET","HEAD","POST","PUT"])
def move():
    global TimesRun
    global HoldDirection
    dataStr = request.data
    jsonData = json.loads(dataStr.decode('utf-8'))
    SnekHeadX = jsonData['you']['body']['data'][0]['x']
    SnekHeadY = jsonData['you']['body']['data'][0]['y']    
    print(jsonData)
    print("X value Snek head +1:", SnekHeadX+1)
    print("X value Snek head:", SnekHeadX)
    HoldDirection = FindFood(SnekHeadX, SnekHeadY, jsonData)
    #Incoming block of safety checks
    if HoldDirection == "right":
        if isSafe(SnekHeadX+1, SnekHeadY, jsonData['width'], jsonData['height'], jsonData):
            HoldDirection = "right" 
        if not isSafe(SnekHeadX+1, SnekHeadY, jsonData['width'], jsonData['height'], jsonData):
            HoldDirection = "up"
    if HoldDirection == "up":
        if isSafe(SnekHeadX, SnekHeadY-1, jsonData['width'], jsonData['height'], jsonData):
            HoldDirection = "up"
        if not isSafe(SnekHeadX, SnekHeadY-1, jsonData['width'], jsonData['height'], jsonData):
            HoldDirection = "left"
    if HoldDirection == "left":
        if isSafe(SnekHeadX-1, SnekHeadY, jsonData['width'], jsonData['height'], jsonData):
            HoldDirection = "left"
        if not isSafe(SnekHeadX-1, SnekHeadY, jsonData['width'], jsonData['height'], jsonData):
            HoldDirection = "down"
    if HoldDirection =="down":
        if isSafe(SnekHeadX, SnekHeadY+1, jsonData['width'], jsonData['height'], jsonData):
            HoldDirection = "down"
        if not isSafe(SnekHeadX, SnekHeadY+1, jsonData['width'], jsonData['height'], jsonData):
            HoldDirection = "right"
    if HoldDirection == "right":
        if isSafe(SnekHeadX+1, SnekHeadY, jsonData['width'], jsonData['height'], jsonData):
            HoldDirection = "right" 
        if not isSafe(SnekHeadX+1, SnekHeadY, jsonData['width'], jsonData['height'], jsonData):
            HoldDirection = "up"
    if HoldDirection == "up":
        if isSafe(SnekHeadX, SnekHeadY-1, jsonData['width'], jsonData['height'], jsonData):
            HoldDirection = "up"
        if not isSafe(SnekHeadX, SnekHeadY-1, jsonData['width'], jsonData['height'], jsonData):
            HoldDirection = "left"
    if HoldDirection == "left":
        if isSafe(SnekHeadX-1, SnekHeadY, jsonData['width'], jsonData['height'], jsonData):
            HoldDirection = "left"
        if not isSafe(SnekHeadX-1, SnekHeadY, jsonData['width'], jsonData['height'], jsonData):
            HoldDirection = "down"
    Direction = HoldDirection


    TimesRun = TimesRun+1

            
    response = {
        "move": Direction
    }
    return jsonify(response)

def isSafe(x,y,width, height,json):
    if x >= width or x<0:
        return False
    if y >= height or y<0:
        return False    
    for snake in json['snakes']['data']: #not working yet. Intent is to iterate through all the snakes to see if next move is safe 
        for point in snake['body']['data']:
           if point['x'] == x and point['y'] == y:
               return False
    return True 

    
def FindFood(SnekX, SnekY, jasonData):
#Checks for food yo! 
    if SnekX > jasonData['food']['data'][0]['x']:
        return "left" 
    if SnekX < jasonData['food']['data'][0]['x']:
        return "right"
    if SnekY > jasonData['food']['data'][0]['y']:
        return "up"
    if SnekY < jasonData['food']['data'][0]['y']:
        return "down"

if __name__ == "__main__":
    # Don't forget to change the IP address before you try to run it locally
    app.run(host='10.0.2.15', port=8085, debug=True)
    
