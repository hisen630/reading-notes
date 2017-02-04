
def mydecorator(f):
    print 'decorate!'
    return f

@mydecorator
def myfunc():
    print 'myfunc'
	
