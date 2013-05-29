#!/usr/bin/env python
# -*- coding: utf-8 -*-
# nagios_check_xmpp_login - Nagios plugin for check authorization on xmpp server

# Copyright © 2013 Denis 'Saymon21' Khabarov
# E-Mail: saymon at hub21 dot ru (saymon@hub21.ru)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3
# as published by the Free Software Foundation.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys, argparse
try:
	import xmpp
except ImportError as errmsg:
	print >> sys.stderr, str(errmsg)
	sys.exit(3)
  
cliparser = argparse.ArgumentParser(description='Plugin for nagios. Nagios plugin for check authorization on xmpp server\nLicence: GNU GPLv3')
cliparser.add_argument("--jid",metavar="VALUE",help="Jabber ID",required=True)
cliparser.add_argument("--passwd",metavar="VALUE",help="Password for jid",required=True)
cliargs = cliparser.parse_args()

def main():
	jid=xmpp.protocol.JID(cliargs.jid)
	client=xmpp.Client(jid.getDomain(),debug=[])
	con=client.connect()
	if not con:
		print('CRITICAL Unable to connect xmpp server at ' +jid.getDomain())
		sys.exit(2)
	auth=client.auth(jid.getNode(),cliargs.passwd)
	if not auth:
		print('CRITICAL XMPP auth unsuccessful for ' + cliargs.jid)
		sys.exit(2)
	else:
		print('OK XMPP ' +cliargs.jid +' authorization successfully')
		client.disconnect()
		sys.exit(0)

if __name__ == "__main__":
	main()
