import io
import json                    
import base64                  
import logging 
import cv2    
import pickle        
import numpy as np
import os
import requests
from PIL import Image

import flask


app = flask.Flask(__name__,static_folder='assets/')          
app.logger.setLevel(logging.DEBUG)

jpg_original=None

@app.route("/")
def home():
    # url = 'https://www.youtube.com/channel/UC5E4oGepJOyBHpv6447f3tQ/live'
    # youtube_url=""
    # html = requests.get(url)
    # req = str(html.content)
    # youtube_url = req.split("link rel=\"canonical\" href=\"")[1].split("\"")[0].split("watch?v=")[1]
    # with open('assets/url.txt', 'w') as f:
    #     #f.write('<iframe width="560" height="315" src="https://www.youtube.com/embed/'+youtube_url+'?controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
    #     f.write(youtube_url)
    return flask.render_template('home.html')

@app.route("/info", methods=['GET'])
def info():
    rain = flask.request.args.get('rain')
    soil = flask.request.args.get('soil')
    accX = flask.request.args.get('accX')
    accY = flask.request.args.get('accY')
    accZ = flask.request.args.get('accZ')
    with open('assets/info.txt', 'w') as f:
        f.write(rain+'\n')
        f.write(soil+'\n')
        f.write(accX+'\n')
        f.write(accY+'\n')
        f.write(accZ+'\n')
    return flask.render_template('info.html')


  
def run_server_api():
    app.run(host='0.0.0.0', port=5123)
  
  
if __name__ == "__main__":     
    run_server_api()
    print