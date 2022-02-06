from flask_apscheduler import APScheduler
from flask import Flask, render_template
from . import spoti
import requests
import random

app = Flask(__name__)

class Config:
    # App configuration.
    SCHEDULER_API_ENABLED = True
    SCHEDULER_TIMEZONE = "Europe/Istanbul" 


app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


# Define a class to pass trackID variable between routes
class VarStore():
    trackID = None

data = VarStore()



# Schedule an app to run once a day

@scheduler.task('cron', id="get_from_api", day='*')
def api_request():
    resp = requests.get('https://songs-i-like.herokuapp.com/api/songs').json()
    
    print("Request sended!")

    randomPick = random.choice(resp)
    
    artistOfTheDay = randomPick['artistName']
    songOfTheDay = randomPick['songName']

    print("Artist: "+ artistOfTheDay + " Song: "+ songOfTheDay)

    trackID = spoti.getSong(artistOfTheDay, songOfTheDay)
    data.trackID = trackID
    
    print("Artist2: "+ artistOfTheDay + " Song2: "+ songOfTheDay)
    
    return trackID


# Use trackID to embed spotify frame, if id is None use a predefined backup id
@app.route("/")
def homepage():
    if data.trackID is not None:
        return render_template('index.html', songID=data.trackID)
    else:
        return render_template('index.html', songID="01OcGaVUAyu3yckunQLhKF")