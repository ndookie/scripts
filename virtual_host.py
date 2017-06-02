#!/usr/bin/python

# Replace the elements of the string to produce a virtual host file 
import string
import sys

if (len(sys.argv) == 1 or sys.argv[1] == 'help'):
	print """
Usage: ./virtual_host.py website email 
"""
	sys.exit()

if len(sys.argv) == 3:
	website = sys.argv[1]
	email = sys.argv[2]
else:
	website = raw_input('Website Name (excluding www): ')
	email = raw_input ('Admin E-Mail: ')

virtual_host_text="""
<VirtualHost *:80>
	# The ServerName directive sets the request scheme, hostname and port that
	# the server uses to identify itself. This is used when creating
	# redirection URLs. In the context of virtual hosts, the ServerName
	# specifies what hostname must appear in the request's Host: header to
	# match this virtual host. For the default virtual host (this file) this
	# value is not decisive as it is used as a last resort host regardless.
	# However, you must set it for any further virtual host explicitly.
	#ServerName www.example.com

	ServerAdmin EMAIL
	ServerName WEBSITE
	ServerAlias www.WEBSITE 
	DocumentRoot /var/www/WEBSITE/public_html

	# Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
	# error, crit, alert, emerg.
	# It is also possible to configure the loglevel for particular
	# modules, e.g.
	#LogLevel info ssl:warn

	ErrorLog ${APACHE_LOG_DIR}/WEBSITE.error.log
	CustomLog ${APACHE_LOG_DIR}/WEBSITE.access.log combined

	# For most configuration files from conf-available/, which are
	# enabled or disabled at a global level, it is possible to
	# include a line for only one particular virtual host. For example the
	# following line enables the CGI configuration for this host only
	# after it has been globally disabled with "a2disconf".
	#Include conf-available/serve-cgi-bin.conf
</VirtualHost>"""

virtual_host_text = virtual_host_text.replace("WEBSITE", website, 10)
virtual_host_text = virtual_host_text.replace("EMAIL", email, 10)

print virtual_host_text
