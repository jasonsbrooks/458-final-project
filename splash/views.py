from flask import (Flask, render_template, Response, request, 
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for)


from flask import jsonify

splash = Blueprint('splash', __name__, template_folder="templates")

@splash.route('/')
def home():
    return render_template('home.html')
