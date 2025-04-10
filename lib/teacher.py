#!/usr/bin/env python

from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # Initialize with some preset knowledge
        self.knowledge = [
            "Python basics",
            "Object-oriented programming",
            "Data structures",
            "Testing in Python"
        ]

    def teach(self):
        return random.choice(self.knowledge)
