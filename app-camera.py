#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Author : sosorry
# Date   : 05/31/2015
# Origin : http://blog.miguelgrinberg.com/post/video-streaming-with-flask

from flask import Flask, render_template, Response
from camera_pi import Camera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('stream.html')
    
@app.route('/f1')
def f1():
    return render_template('func1.html')
    
@app.route('/f2')
def f2():
    return render_template('func2.html')
    
@app.route('/f3')
def f3():
    return render_template('func3.html')
    
@app.route('/f4')
def f4():
    return render_template('func4.html')
    
@app.route('/f5')
def f5():
    return render_template('func5.html')
    
@app.route('/f6')
def f6():
    return render_template('func6.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen2(camera):
    while True:
        frame = camera.get_frame2()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen3(camera):
    while True:
        frame = camera.get_frame3()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen4(camera):
    while True:
        frame = camera.get_frame4()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen5(camera):
    while True:
        frame = camera.get_frame5()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen6(camera):
    while True:
        frame = camera.get_frame6()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/video_feed2')
def video_feed2():
    return Response(gen2(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/video_feed3')
def video_feed3():
    return Response(gen3(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/video_feed4')
def video_feed4():
    return Response(gen4(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/video_feed5')
def video_feed5():
    return Response(gen5(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/video_feed6')
def video_feed6():
    return Response(gen6(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
