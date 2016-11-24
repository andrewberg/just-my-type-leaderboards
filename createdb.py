# Leaderboards back end by Andrew Berg written with Flask

import sqlite3

conn = sqlite3.connect('jmtleaderboards.db')
print "Opened database successfully";

conn.execute("CREATE TABLE IF NOT EXISTS "
	"typingtestleader (name TEXT, score TEXT)")
conn.execute("CREATE TABLE IF NOT EXISTS "
	"ballonleader (name TEXT, score TEXT)")
conn.execute("CREATE TABLE IF NOT EXISTS "
	"basketballleader (name TEXT, score TEXT)")
print "Table created successfully";
conn.close()