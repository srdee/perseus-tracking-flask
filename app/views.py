from flask import render_template, flash, redirect, session, url_for, request, g, jsonify
from app import app
from .forms import SearchForm
import json

@app.route("/")
@app.route("/search", methods =["GET", "POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash("Retrieving data for %s" % form.urn.data)
        with open("../canonical-greekLit/canonical-greekLit.tracking.json","r") as f:
            TrackingData = json.loads(f.read())
        tracking_data = TrackingData[form.urn.data]
        return render_template("display.html", 
            title="Tracking information for " + form.urn.data,
            urn = form.urn.data,
            f = tracking_data)
    return render_template('search.html',
        form = form,
		title='Search')

@app.route("/browse")
def browse():
	return render_template('browse.html',
		title='Browse')

@app.route("/display/<urn>")
def display(urn):
    with open("../canonical-greekLit/canonical-greekLit.tracking.json","r") as f:
          TrackingData = json.loads(f.read())
    tracking_data = TrackingData[urn]
    if tracking_data == None:
        flash('Tracking data for %s not found.' % urn)
        return redirect(url_for('search'))
    return render_template('display.html', 
        title = "Tracking information for " + urn,
        urn = urn, 
        f = tracking_data)

@app.route("/api/<urn>.json")
def api(urn):
    with open("../canonical-greekLit/canonical-greekLit.tracking.json","r") as f:
          TrackingData = json.loads(f.read())
    tracking_data = TrackingData[urn]
    if tracking_data == None:
        flash('Tracking data for %s not found.' % urn)
        return redirect(url_for('search'))
    return render_template('api.html', 
       json =  "{'"+ urn + "':" + json.dumps(TrackingData[urn], sort_keys=True, indent=4) + "}")
