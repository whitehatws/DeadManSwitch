import atexit
from datetime import datetime
from sched import scheduler
from flask import Flask, request, jsonify
from sendData import send
from config import Config
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

lastVerification = [datetime.now()]

def verifyCheck():
    tempDate = datetime.now() - lastVerification[0]
    if tempDate.days < 3:
        print('OK!')
    else:
        send()

schedule = BackgroundScheduler()
schedule.start()
schedule.add_job(
    func=verifyCheck,
    trigger=IntervalTrigger(hours=72),
    id='verifyJob',
    name='Verify dead man switch still active',
    replaceExisting=True)
atexit.register(lambda: schedule.shutdown())

app = Flask(__name__)

@app.route("/verify", methods=['POST'])
def verification():
    data = request.get_json()
    if data ["key"] == Config.secretKey:
        lastVerification[0] = datetime.now()
        return jsonify({"success": True})
    else:
        print('DENIED!')
        return jsonify({"success": False})

if __name__ == "__main__":
    app.run()
