#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 在运行前或运行后替换
class Parent(object):

	def override(self):
		print "PARENT override()"
		
	def implicit(self):
		print "PARENT implicit()"

	def altered(self):
		print "PARENR altered()"
		
class Child(Parent):
	
	def override(self):
		print "CHILD override()"
	
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"
		
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()