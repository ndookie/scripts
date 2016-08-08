#!/bin/python

# Importing integer base converter.
from base_converter import base_conversion

import sqlite3 as lite

# ASCII to INT Map


# Database set up
con = None

con = lite.connect('shortener.db');

cur = con.cursor()

def insert_url(url):
	cur.execute("INSERT INTO url_table VALUES(NULL,'%s',NULL)" % (url))

	cur.execute("SELECT id FROM url_table WHERE url='%s'" % (url));

	url_id = cur.fetchone()

	return url_id

def generate_hash(id):
	new_hash = base_conversion(id[0],62)

	return new_hash

def update_shortened_url(id, hash):
	print id
	cur.execute("UPDATE url_table SET shortened_url='" + hash + "' WHERE id=%i" % (id));

	con.commit()

def url_generator(url):
	new_id = insert_url(url)
	#print new_id

	shortened_url = generate_hash(new_id)
	print new_id
	update_shortened_url(new_id, shortened_url)

	con.close()

	return



url_generator('friendssdfdsfdhip.com')

