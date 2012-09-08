from sys import argv
from plurk_oauth.PlurkAPI import PlurkAPI
import json

plurk = PlurkAPI("TmJ2fUfRcy3X", "kuBsGZH8qBw34h9uytZgNWFC37PkYv66")
plurk.authorize("fqG3DURTDfvA", "EcpTJdGsxHEaCx4TxIMlKR1tksPEuf09")

script, filename= argv
infile = open(filename, "r")
total_length = len( infile.read().split("\n") )
infile.close()
infile = open(filename, "r")
#string = infile.read()
#string = string.split("\n")

#outfile = open("user_table", "w")


errorfile = open("error.txt", "w")
outf = open("total_user_table.txt", "w") 

#print >> outfile, (string[0] + "\tgender")


i= 0
for l in infile:
	tmp = l.strip().split("\t")
	userid = tmp[0]
	temp = plurk.callAPI("/APP/Profile/getPublicProfile", {"user_id": userid})
	print "[%.2f] %d/%d" %( ( float(i)/ float(total_length) ) , i, total_length )  
	i +=1 
	if not temp == None:
		userinfo = temp.get("user_info")
		print >>outf, userinfo
	else:
		print >> errorfile, (userid + " could not find!")
	

infile.close()
outf.close()
errorfile.close()

