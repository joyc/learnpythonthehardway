#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1.dict style
# mystuff['apples']

# 2.module style
# mystuff.apples()
# print mystuff.yinru

# 3.class style
# thing = MyStuff()
# thing.apples()
# print thing.yinru

# print '-' * 10
# 
# import mystuff
# mystuff.apple()
# print mystuff.yinru

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])					
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	