# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:10:27 2022

@author: ksandeep
"""


import os
import copy


# Limitation of array:
# 1 - Same type of element.
# 2 - Fixed size of array a.k.a immutable.
# 3 - Data is stored sequentially in memory.


# Linked list is an collection with elements represented as nodes.
# A node is comprised of 'data' and 'link'.
# The data can contain any object whereas the link contains address of the next node (null be default).
# Linked list need not have fixed size i.e., flexible size.
# The elements of linked list need not be stored sequentially in memory i.e., efficient memory storage.


class LL_Node:
    
    __slots__ = '_element', '_link' # in-built class member for instance var generation to save space without dict().
    
    def __init__(self, element, link):
        self._element = element
        self._link = link
    
    def __repr__(self): # special method
        return "This node contains "+str(self._element)+" and is linked to "+str(self._link)+"."
    
    def __str__(self): # special method
        return 'a node'


class CircularLinkedList():
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0
    
    def add_last(self, element):
        new_node = LL_Node(element, None)
        if self.isempty():
            self._head = new_node
            new_node._link = new_node # Added new here.
        else:
            self._tail._link = new_node
            #new_node._link = self._head # Added new here.
            new_node._link = self._tail._link # Added new here.
        self._tail = new_node
        self._size+=1
    
    def add_first(self, element):
        new_node = LL_Node(element, None)
        if self.isempty():
            self._tail = new_node
            new_node._link = new_node # Added new here.
        else:
            new_node._link = self._head
            self._tail._link = new_node # Added new here.
        self._head = new_node
        self._size+=1
    
    def add_any(self, element, target):
        new_node = LL_Node(element, None)
        if self.isempty():
            self._head = new_node
            self._tail = new_node
            new_node._link = new_node # Added new here.
        else: # No change here.
            index = 0
            trace = self._head
            while index < target-1:
                trace = trace._link
                index+=1
            #if index == 0:
            #    new_node._link = self._head
            #    self._head = new_node
            #elif index == self._size-1:
            #    self._tail._link = new_node
            #    self._tail = new_node
            #else:
            #    new_node._link = self.trace._link
            #    self.trace._link = new_node
            new_node._link = trace._link
            trace._link = new_node
        self._size+=1
    
    def remove_first(self): # No de-allocation of memory required in Python but is required in C/C++
        if self.isempty():
            print("List is empty.")
            return None
        else:
            first_element = self._head._element
            self._head = self._head._link
            self._tail._link = self._head # Added new here.
            #if self._size == 1:
            self._size-=1
            if self.isempty():
                self._tail = None
                self._head = None
        return first_element
    
    def remove_last(self):
        if self.isempty():
            print("List is empty.")
            return None
        else:
            trace = self._head
            index = 0
            while index < self._size-2:
                trace = trace._link
                index+=1
            self._size-=1
            if self.isempty():
                last_element = trace._element
                self._head = self._tail = None
            else:
                #last_element = self._tail._element # Can't use this due to python's assignment
                last_element = copy.deepcopy(trace._link._element)
                trace._link = None
                self._tail = trace
                self._tail._link = self._head # Added new here.
            return last_element
    
    def remove_any(self, target):
        if self.isempty():
            target_element = None
            print("List is empty.")
        trace = self._head
        i=0
        while i < target-1:
            trace = trace._link
            i+=1
        target_element = trace._link._element
        trace._link = trace._link._link
        self._size-=1
        return target_element
    
    def remove_any_ext(self, target):
        if self.isempty():
            target_element = None
            print("List is empty.")
        elif self._size == 1:
            target_element = self._head._element
            self._head = self._tail = None
            self._size-=1
        else:
            trace = self._head
            if target == 0:
                target_element = copy.deepcopy(self._head._element)
                self._head = trace._link
                self._tail._link = self._head # Added new here.
            elif target == self._size-1:
                target_element = copy.deepcopy(self._tail._element)
                self._tail = trace._link
                self._tail._link = self._head # Added new here.
            else:
                index = 0
                while index < target-1:
                    trace = trace._link
                    index+=1
                target_element = copy.deepcopy(trace._link._element)
                trace._link = trace._link._link
                if index == self._size-1:
                    self._tail = trace
            self._size-=1
        return target_element
    
    def display(self):
        trace = self._head
        #while trace:#._link != None:
        for i in range(self._size):
            print(trace._element, end="-->")
            trace = trace._link
        print()
    
    def search(self, key):
        trace = self._head
        index = 0
        #while trace:
        for i in range(self._size):
            if trace._element == key:
                return index
            trace = trace._link
            index+=1
        return -1
    
    def __repr__(self): # special method
        return "The linked-list element contains "#+str(self._element)+" and is linked to "+str(self._link)+"."
    
    def __str__(self): # special method
        return 'a circular linked-list'


if '__main__'.__eq__(__name__):
    
    cll_1 = CircularLinkedList()
    cll_1.add_last(7)
    cll_1.display()
    print("Length of linked-list is", len(cll_1))
    cll_1.add_last(5)
    cll_1.display()
    print("Length of linked-list is", len(cll_1))
    cll_1.add_last(3)
    cll_1.display()
    print("Length of linked-list is", len(cll_1))
    cll_1.add_last(1)
    cll_1.display()
    print("Length of linked-list is", len(cll_1))
    print(cll_1.search(9))
    print(cll_1.search(7))
    print(cll_1.search(5))
    print(cll_1.search(3))
    print(cll_1.search(1))
    cll_1.add_first(9)
    cll_1.display()
    print("Length of linked-list is", len(cll_1))
    cll_1.add_first(11)
    cll_1.display()
    print("Length of linked-list is", len(cll_1))
    cll_1.add_first(13)
    cll_1.display()
    print("Length of linked-list is", len(cll_1))
    cll_1.add_first(15)
    cll_1.display()
    print("Length of linked-list is", len(cll_1))
    cll_1.add_any(8, 4)
    cll_1.display()
    print("Length of linked-list is", len(cll_1))
    cll_1.add_any(6, 6)
    cll_1.display()
    print("Length of linked-list is", len(cll_1))
    cll_1.add_any(4, 8)
    cll_1.display()
    print("Length of linked-list is", len(cll_1))
    cll_1.add_any(2, 10)
    cll_1.display()
    print("Length of linked-list is", len(cll_1))
    cll_2 = CircularLinkedList()
    cll_2.add_any(1, 0)
    cll_2.add_any(2, 1)
    cll_2.add_any(3, 2)
    cll_2_copy = copy.deepcopy(cll_2)
    cll_2_copy_2 = copy.deepcopy(cll_2)
    cll_2.display()
    print(cll_2.remove_first())
    cll_2.display()
    print("Length of linked-list is", len(cll_2))
    print(cll_2.remove_first())
    cll_2.display()
    print("Length of linked-list is", len(cll_2))
    print(cll_2.remove_first())
    cll_2.display()
    print("Length of linked-list is", len(cll_2))
    print(cll_2_copy.remove_last())
    cll_2_copy.display()
    print("Length of linked-list is", len(cll_2_copy))
    print(cll_2_copy.remove_last())
    cll_2_copy.display()
    print("Length of linked-list is", len(cll_2_copy))
    print(cll_2_copy.remove_last())
    cll_2_copy.display()
    print("Length of linked-list is", len(cll_2_copy))
    print(cll_2_copy_2.remove_any(0))
    cll_2_copy_2.display()
    print("Length of linked-list is", len(cll_2_copy_2))
    print(cll_2_copy_2.remove_any(1))
    cll_2_copy_2.display()
    print("Length of linked-list is", len(cll_2_copy_2))
    print(cll_2_copy_2.remove_any(0))
    cll_2_copy_2.display()
    print("Length of linked-list is", len(cll_2_copy_2))
    