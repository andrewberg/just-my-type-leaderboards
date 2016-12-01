# Leaderboards back end by Andrew Berg written with Flask

from flask import Flask, request, render_template, jsonify
import sqlite3 as sql
app = Flask(__name__)

"""Page to enter scores into the leaderboards based on numbers
	by POST"""
@app.route("/jmt/typingtest/enter", methods = ['POST', 'GET'])
def ttEnterScore():
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

@app.route("/jmt/basketball/enter", methods = ['POST', 'GET'])
def bbEnterScore():
    if request.method == 'POST':
    	try:
    		name = request.form['name'] # grab name
    		score = request.form['score'] # score

	    	with sql.connect('jmtleaderboards.db') as con: # open connection
	    		cur = con.cursor() # get the current spot for executing
	    		cur.execute("INSERT INTO basketballleader (name, score) VALUES (?, ?)", 
	    			(name, score)) # execute insert to add the score and name
	    		con.commit() # commit the query
    			msg = "Score entered" # open the return message
    	except:
    		con.rollback()
    		msg = "error"
    	finally:
    		return render_template("result.html", msg = msg) # renders page
    		con.close()

@app.route("/jmt/racecar/enter", methods = ['POST', 'GET'])
def rcEnterScore():
    if request.method == 'POST':
    	try:
    		name = request.form['name'] # grab name
    		score = request.form['score'] # score

	    	with sql.connect('jmtleaderboards.db') as con: # open connection
	    		cur = con.cursor() # get the current spot for executing
	    		cur.execute("INSERT INTO racecarleader (name, score) VALUES (?, ?)", 
	    			(name, score)) # execute insert to add the score and name
	    		con.commit() # commit the query
    			msg = "Score entered" # open the return message
    	except:
    		con.rollback()
    		msg = "error"
    	finally:
    		return render_template("result.html", msg = msg) # renders page
    		con.close()

@app.route("/jmt/balloon/enter", methods = ['POST', 'GET'])
def blEnterScore():
    if request.method == 'POST':
    	try:
    		name = request.form['name'] # grab name
    		score = request.form['score'] # score

	    	with sql.connect('jmtleaderboards.db') as con: # open connection
	    		cur = con.cursor() # get the current spot for executing
	    		cur.execute("INSERT INTO balloonleader (name, score) VALUES (?, ?)", 
	    			(name, score)) # execute insert to add the score and name
	    		con.commit() # commit the query
    			msg = "Score entered" # open the return message
    	except:
    		con.rollback()
    		msg = "error"
    	finally:
    		return render_template("result.html", msg = msg) # renders page
    		con.close()

@app.route("/jmt/ant/enter", methods = ['POST', 'GET'])
def agEnterScore():
    if request.method == 'POST':
    	try:
    		name = request.form['name'] # grab name
    		score = request.form['score'] # score

	    	with sql.connect('jmtleaderboards.db') as con: # open connection
	    		cur = con.cursor() # get the current spot for executing
	    		cur.execute("INSERT INTO antleader (name, score) VALUES (?, ?)", 
	    			(name, score)) # execute insert to add the score and name
	    		con.commit() # commit the query
    			msg = "Score entered" # open the return message
    	except:
    		con.rollback()
    		msg = "error"
    	finally:
    		return render_template("result.html", msg = msg) # renders page
    		con.close()

# ------------- list functions

@app.route('/jmt/typingtest/list')
def ttList():
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

@app.route('/jmt/racecar/list')
def rcList():
	con = sql.connect("jmtleaderboards.db")
	con.row_factory = sql.Row 

	cur = con.cursor()
	cur.execute("SELECT * from racecarleader") # grabs all rows from ttleader

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

@app.route('/jmt/basketball/list')
def bbList():
	con = sql.connect("jmtleaderboards.db")
	con.row_factory = sql.Row 

	cur = con.cursor()
	cur.execute("SELECT * from basketballleader") # grabs all rows from ttleader

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

@app.route('/jmt/balloon/list')
def blList():
	con = sql.connect("jmtleaderboards.db")
	con.row_factory = sql.Row 

	cur = con.cursor()
	cur.execute("SELECT * from balloonleader") # grabs all rows from ttleader

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

@app.route('/jmt/ant/list')
def agList():
	con = sql.connect("jmtleaderboards.db")
	con.row_factory = sql.Row 

	cur = con.cursor()
	cur.execute("SELECT * from antleader") # grabs all rows from ttleader

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

@app.route('/jmt/racecar/updatescore', methods = ['POST', 'GET'])
def rcUpdateScore():
    if request.method == 'POST':
    	name = request.form['name'] # grab name
    	con = sql.connect('jmtleaderboards.db') # open connection
    	cur = con.cursor() # get the current spot for executing
    	cur.execute("SELECT * FROM racecarleader WHERE name = (?)", (name,))
    	rows = cur.fetchall()
    	cur = con.cursor()
    	if (len(rows) == 0):
    		cur.execute("INSERT INTO racecarleader (name, score) VALUES (?,?)", 
	    			(name,1))
    		con.commit()
    		msg = "insert"
    	else:
    		msg = "updated"
    		cur.execute("UPDATE racecarleader SET score = score + 1 WHERE name = (?)", (name,))
    		con.commit()

    	return msg # renders page


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True) # debug mode true and broadcasts