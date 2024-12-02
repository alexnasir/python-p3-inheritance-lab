#!/usr/bin/env python

from user import User

class Student(User):
     def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Call the parent class's __init__ method
        self.knowledge = []  # Initialize knowledge as an empty list


     def learn(self, info):
        '''Adds a string to the knowledge list.'''
        self.knowledge.append(info)  # Append the new information to the knowledge list
    
        pass