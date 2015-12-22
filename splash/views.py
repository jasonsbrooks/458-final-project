from flask import (Flask, render_template, Response, request, 
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for)
from splash.models import *
from splash import *
from flask import jsonify

splash = Blueprint('splash', __name__, template_folder="templates")

@splash.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@splash.route('/recommend', methods=['POST'])
def recommend():
	os = request.form.get('operating_system')
	battery = request.form.get('battery')
	harddrive = request.form.get('harddrive')
	budget = request.form.get('budget')
	memory = request.form.get('memory')
	size = request.form.get('size')
	prior_liked = request.form.getlist('prior-liked')
	prior_disliked = request.form.getlist('prior-disliked')
	user_data = {'os': os, 'battery': battery, 'harddrive': harddrive, 'budget': budget, 'memory': memory, 'size': size, 'prior_liked': prior_liked, 'prior_disliked': prior_disliked}
	results = whichpc(user_data)
	print results
	return render_template('recommend.html', results=results)


