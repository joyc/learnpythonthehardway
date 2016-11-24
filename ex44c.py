#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 在运行前或运行后替换
class Parent(object):

	def altered(self):
		print "PARENR altered()"
		
class Child(Parent):
	
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"
		
dad = Parent()
son = Child()

dad.altered()
son.altered()