import os
from werkzeug import secure_filename
from flask import *


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/upcoming_act')
def upcoming_act():
    return render_template('upcoming_act.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/active_members')
def active_members():
    return render_template('active_members.html')

@app.route('/photo_gallery/october15_jaisalmer')
def october15_jaisalmer():
    return render_template('october15_jaisalmer.html')

@app.route('/photo_gallery/september15_old_delhi')
def aseptember15_old_delhi():
    return render_template('september15_old_delhi.html')

@app.route('/photo_gallery/august15_lodhi_garden')
def august15_lodhi_garden():
    return render_template('august15_lodhi_garden.html')


@app.route('/photo_gallery')
def photo_gallery():
    return render_template('photo_gallery.html')






# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

