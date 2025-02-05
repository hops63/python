
class B:
	m_List = []
	m_Val = 0
	def __init__( self, val):
		B.m_Val = val		# changes class variable (static)
		self.m_Val = val	# initializes a new declared instance variable that hides the class variable	

		
b = B( 4)
print b.m_Val

b2 = B( 5)

print b.m_Val
print b2.m_Val
		

