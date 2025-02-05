class A:
	def f( cls):
		print "In class method of ", cls
	
	def f2():
		print "In static method of A"
		
	f = classmethod(f)
	f2 = staticmethod(f2)
	
class B( A):
	pass

if __name__ == "__main__":
	A.f()
	B.f()
	
	A.f2()
	B.f2()
	
	A().f()
	B().f()
	
	A().f2()
	B().f2()


	
