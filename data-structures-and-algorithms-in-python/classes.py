# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:10:27 2022

@author: ksandeep
"""

import os

class example:
    
    """ This is a doc-string"""
    
    static_var1 = 'LOL' # Static var created within the class
    
    def __init__(myself, var3): # Constructor, special method
        myself.var1 = 13
        myself.var2 = 'abc'
        myself.var3 = var3
    
    def __str__(self): # special method
        return 'This is an example class.'
    
    def display(self):
        local_var1 = False
        print('static_var1 is ', example.static_var1)
        print('var1 is ', self.var1)
        print('var2 is ', self.var2)
        print('var3 is ', self.var3)
        print('static_var2 is ', example.static_var2)
        print('local_var1 is ', local_var1) #example.local_var1)
        print('(static)local_var1 is ', example.local_var1) #example.local_var1)
    
    # object is an instance of class
    # contains data attributes and methods:
    # attributes can be instance vars, static vars or local vars
    # methods can be instance methods, static methods or class methods (py excl.)
    # instance vars/methods are object-level, static vars/methods are class-level and local vars are method-level.
    # self var is implicitly created upon obj creation, first var in __init__ is always a alias for self
    # Please note self is not reserved/keyword
    

if '__main__'.__eq__(__name__):
    
    print(example.__doc__)
    #obj_eg = example()
    example.static_var2 = 'ROFL' # Static var created outside the class
    obj_eg = example(35)
    #print(obj_eg.var1)
    #print(obj_eg.var2)
    #print(obj_eg.__doc__)
    #print(obj_eg) # calls the __str__ in-built method.
    #obj_eg.display()
    #obj_eg_2 = example(50)
    #obj_eg_2.display()
    #obj_eg_3 = example(65)
    #obj_eg_3.display()
    obj_eg.__init__(135)
    example.local_var1 = True # Actually a static var and not a local var.
    obj_eg.display()
    
    eg = 1