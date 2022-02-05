from app.main import app
from flask_apscheduler import APScheduler

if __name__ == "__main__":
    
    app.run(debug=True)