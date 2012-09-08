import ast 

def load_user_table( filename ) :
	ret = list()
	f = open( filename )
	for l in f :
		ret.append( ast.literal_eval( l.strip() ) )
	return ret  
def load_user_dict( filename ):
	ret = dict()
	user_table = load_user_dict( filename )
	for user_row in user_table :
		ret[ user_row['uid'] ] = user_row 
	return ret 
def load_list( filename ):
	f = open( filename )
	ret = list()
	for l in f :
		ret.append( long( l.strip() ) )
	return ret 

