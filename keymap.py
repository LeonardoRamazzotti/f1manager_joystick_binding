import mouse_custom as m

def key_1():
	m.overtake_1()
	m.high_fuel_1()
	m.attack_1()
def key_2():
	pass
def key_3():
    m.overtake_1()
    m.high_fuel_1()
    m.attack_1()
	
def key_4():
	pass

def key_5():
	m.overtake_2()
	m.high_fuel_2()
	m.attack_2()
def key_6():
	pass
def key_7():
	pass
def key_8():
	pass
	
def key_9():
	pass
def key_10():
	pass
def key_11():
	pass
def key_12():
	pass

def key_13():
	pass
def key_14():
	pass
def key_15():
	pass
def key_16():
	pass


def key_fun(input):
   
    
    globals()['key_'+str(input)]()
    
   
    