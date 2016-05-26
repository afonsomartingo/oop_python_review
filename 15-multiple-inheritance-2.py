#!/usr/bin/env python

# multiple-inheritance-2.py

# Python supports multiple inheritance
# and uses a depth-first order when searching for methods.

# This search pattern is call MRO (Method Resolution Order)

# This is a second example, which shows the lookup of 'dothis()'.
# Both A and C contains 'dothis()'. Let's trace how the lookup happens.

# As per the MRO output, it starts in class D, then B, A, and lastly C.
# Starts looking in D, then moves to B, then to A.
# A defines 'dothat' which is not what we're looking for.
# Hence it goes back to D, then C, and finds it there.


class A(object):

    def dothat(self):
        print("Doing this in A")

class B(A):
    pass

class C(object):

    def dothis(self):
        print("\nDoing this in C")

class D(B, C):
    """Multiple Inheritance,
    D inheriting from both B and C"""
    pass

d_instance = D()

d_instance.dothis()

print("\nPrint the Method Resolution Order")
print(D.mro())