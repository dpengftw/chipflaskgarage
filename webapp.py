from flask import Flask
from flask import render_template
from flask import jsonify
import CHIP_IO.GPIO as GPIO
import time

app = Flask(__name__)

@app.route('/api/passcode/<int:key>')
def gatekepper(key):
        if key == 9999:
                return jsonify({ 'status': 'ok', 'user': 'root', 'pwd': 'password' })
        else:
                return jsonify({ 'status': 'failed' })

@app.route('/api/garage/open/<int:key>')
def garageopen(key):
        if key == 9999:
                # send out GPIO to open or close garage
                GPIO.setup("XIO-P0", GPIO.OUT)
                GPIO.output("XIO-P0", GPIO.LOW)
                time.sleep(1)
                GPIO.output("XIO-P0", GPIO.HIGH)
                GPIO.cleanup()
                return jsonify({ 'status': 'ok' })
        else:
                return jsonify({ 'status': 'failed' })
