import io 
import sys 

lang, origin_aid_file, inputfile, outputfile = sys.argv 

aid_list = io.load_list( origin_aid_file ) 

user_dict = io.load_user_dict( inputfile )

outf = open( outputfile , "w" )
for aid in aid_list :
	if not user_dict.has_key( aid ) : 
		print >> outf , aid 
outf.close() 
