import mouse_custom as mouse

def key_1():
	mouse.overtake_1()
	mouse.high_fuel_1()
	mouse.attack_1()
def key_2():
	pass
def key_3():
    mouse.overtake_1()
    mouse.high_fuel_1()
    mouse.attack_1()
	
def key_4():
	pass

def key_5():
	mouse.overtake_2()
	mouse.high_fuel_2()
	mouse.attack_2()
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
    
   
    