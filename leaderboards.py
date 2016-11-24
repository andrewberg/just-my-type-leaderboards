# Leaderboards back end by Andrew Berg written with Flask

from flask import Flask, request, render_template, jsonify
import sqlite3 as sql
app = Flask(__name__)

"""Page to enter scores into the leaderboards based on numbers
	by POST"""
@app.route("/jmt/typingtest/enter", methods = ['POST', 'GET'])
def enterScore():
    if request.method == 'POST':
    	try:
    		name = request.form['name'] # grab name
    		score = request.form['score'] # score

	    	with sql.connect('jmtleaderboards.db') as con: # open connection
	    		cur = con.cursor() # get the current spot for executing
	    		cur.execute("INSERT INTO typingtestleader (name, score) VALUES (?, ?)", 
	    			(name, score)) # execute insert to add the score and name
	    		con.commit() # commit the query
    			msg = "Score entered" # open the return message
    	except:
    		con.rollback()
    		msg = "error"
    	finally:
    		return render_template("result.html", msg = msg) # renders page
    		con.close()

@app.route('/jmt/typingtest/list')
def list():
	con = sql.connect("jmtleaderboards.db")
	con.row_factory = sql.Row 

	cur = con.cursor()
	cur.execute("SELECT * from typingtestleader") # grabs all rows from ttleader

	rows = cur.fetchall() # grabs a list of rows
	rows.sort(key = lambda x: x[1], reverse = True) # sorts based on score

	jsonlist = []
	scores = {} # init empty scores list
	for row in rows: # iterates and adds to scores
		score_json = {}
		score_json['name'] = row[0]
		score_json['score'] = row[1]

		jsonlist.append(score_json)

	return jsonify({'score_list':jsonlist})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True) # debug mode true and broadcasts





