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


class LinkedList():
    
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
        else:
            self._tail._link = new_node
        self._tail = new_node
        self._size+=1
    
    def add_first(self, element):
        new_node = LL_Node(element, None)
        if self.isempty():
            self._tail = new_node
        else:
            new_node._link = self._head
        self._head = new_node
        self._size+=1
    
    def add_any(self, element, target):
        new_node = LL_Node(element, None)
        if self.isempty():
            self._head = new_node
            self._tail = new_node
        else:
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
            #if self._size == 1:
            self._size-=1
            if self.isempty():
                self._tail = None
            #self._size-=1
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
            return last_element
    
    def remove_any(self, target):
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
            elif target == self._size-1:
                target_element = copy.deepcopy(self._tail._element)
                self._tail = trace._link
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
        while trace:#._link != None:
            print(trace._element, end="-->")
            trace = trace._link
        print()
    
    def search(self, key):
        trace = self._head
        index = 0
        while trace:
            if trace._element == key:
                return index
            trace = trace._link
            index+=1
        return -1
    
    def __repr__(self): # special method
        return "The linked-list element contains "#+str(self._element)+" and is linked to "+str(self._link)+"."
    
    def __str__(self): # special method
        return 'a linked-list'


if '__main__'.__eq__(__name__):
    
    # Initializing and Linking the nodes of a linked-list
    node_1 = LL_Node('DATA', None)
    print(node_1._element)
    node_2 = LL_Node('NEXT', None)
    print(node_2._element)
    node_1._link = node_2
    print(node_1._link._element)
    #print(ll_2._link._element)
    
    # Traversing the linked-list
    node_3 = LL_Node('TAIL', None)
    node_2._link = node_3
    head = node_1
    x = head
    print(repr(x))
    while(x._link != None):
        x = x._link
        print(repr(x))
    tail = x
    
    ll_1 = LinkedList()
    ll_1.add_last(7)
    ll_1.display()
    print("Length of linked-list is", len(ll_1))
    ll_1.add_last(5)
    ll_1.display()
    print("Length of linked-list is", len(ll_1))
    ll_1.add_last(3)
    ll_1.display()
    print("Length of linked-list is", len(ll_1))
    ll_1.add_last(1)
    ll_1.display()
    print("Length of linked-list is", len(ll_1))
    print(ll_1.search(9))
    print(ll_1.search(7))
    print(ll_1.search(5))
    print(ll_1.search(3))
    print(ll_1.search(1))
    ll_1.add_first(9)
    ll_1.display()
    print("Length of linked-list is", len(ll_1))
    ll_1.add_first(11)
    ll_1.display()
    print("Length of linked-list is", len(ll_1))
    ll_1.add_first(13)
    ll_1.display()
    print("Length of linked-list is", len(ll_1))
    ll_1.add_first(15)
    ll_1.display()
    print("Length of linked-list is", len(ll_1))
    ll_1.add_any(8, 4)
    ll_1.display()
    print("Length of linked-list is", len(ll_1))
    ll_1.add_any(6, 6)
    ll_1.display()
    print("Length of linked-list is", len(ll_1))
    ll_1.add_any(4, 8)
    ll_1.display()
    print("Length of linked-list is", len(ll_1))
    ll_1.add_any(2, 10)
    ll_1.display()
    print("Length of linked-list is", len(ll_1))
    ll_2 = LinkedList()
    ll_2.add_any(1, 0)
    ll_2.add_any(2, 1)
    ll_2.add_any(3, 2)
    ll_2.display()
    ll_2_copy = copy.deepcopy(ll_2)
    ll_2_copy_2 = copy.deepcopy(ll_2)
    print(ll_2.remove_first())
    ll_2.display()
    print("Length of linked-list is", len(ll_2))
    print(ll_2.remove_first())
    ll_2.display()
    print("Length of linked-list is", len(ll_2))
    print(ll_2.remove_first())
    ll_2.display()
    print("Length of linked-list is", len(ll_2))
    print(ll_2_copy.remove_last())
    ll_2_copy.display()
    print("Length of linked-list is", len(ll_2_copy))
    print(ll_2_copy.remove_last())
    ll_2_copy.display()
    print("Length of linked-list is", len(ll_2_copy))
    print(ll_2_copy.remove_last())
    ll_2_copy.display()
    print("Length of linked-list is", len(ll_2_copy))
    print(ll_2_copy_2.remove_any(0))
    ll_2_copy_2.display()
    print("Length of linked-list is", len(ll_2_copy_2))
    print(ll_2_copy_2.remove_any(1))
    ll_2_copy_2.display()
    print("Length of linked-list is", len(ll_2_copy_2))
    print(ll_2_copy_2.remove_any(0))
    ll_2_copy_2.display()
    print("Length of linked-list is", len(ll_2_copy_2))
