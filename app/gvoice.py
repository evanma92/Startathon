from flask import render_template, url_for, request, redirect
from app import app

import urllib
import urllib2

@app.route("/gvoice", methods = ["GET", "POST"])

def get_google_voice(phrase,lang,file_name):
    """
    Function that will send http request to google translate
    and save audio file from responce with voiced input phrase.
    Parameters:
    @phrase: phrase to voice.
    Returns:
    If ok - name of created file, else - returns None.
    """
    
    language=lang #Setting language.
    url = "http://translate.google.com/translate_tts" #Google translate url for getting sound.
    user_agent="Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5." 
    #file_name="temp.mp3" #Temp file for saving our voiced phrase.
 
    params = urllib.urlencode({'q':phrase, 'tl':language}) #query parameters.
    request = urllib2.Request(url, params) #http request.
    request.add_header('User-Agent', user_agent) #adding agent as header.
    response = urllib2.urlopen(request) 
    
    if response.headers["GET"] == 'audio/mpeg':
        with open(file_name, 'wb') as file:
            file.write(response.read())
        return file_name
    else:
        return None


