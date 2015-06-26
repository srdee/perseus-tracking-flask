from flask import render_template
from app import app

@app.route("/")
@app.route("/search")
def search():
	return render_template('search.html',
		title='Search')

@app.route("/browse")
def browse():
	return render_template('browse.html',
		title='Browse')

@app.route("/display")

def display():
	f =  {
        "epidoc_compliant": False, 
        "fully_unicode": True, 
        "git_repo": "canonical-greekLit", 
        "has_cts_metadata": False, 
        "has_cts_refsDecl": False, 
        "id": "1999.01.0227", 
        "last_editor": "", 
        "note": "", 
        "src": "texts/sdl/Apollonius/argo_gk.xml", 
        "status": "migrated", 
        "target": "canonical-greekLit/data/tlg0001/tlg001/tlg0001.tlg001.perseus-grc1.xml", 
        "valid_xml": True,
        "urn": "urn:cts:greekLit:tlg0001.tlg001.perseus-grc1"
    }
	
	return render_template('display.html', 
		title = "Testing", 
		f = f)