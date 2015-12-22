from flask import (Flask, render_template, Response, request, 
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for)
from splash.models import *
from flask import jsonify

splash = Blueprint('splash', __name__, template_folder="templates")

@splash.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@splash.route('/recommend', methods=['POST'])
def recommend():
	print request.form
	print request.form.getlist('prior')
	return "hi"
