#any_all.py

####################################################################
#any test
####################################################################
# 1. Returns true if any of the items is True.
# 2. It returns False if empty or all are false.
# 3. Any can be thought of as a sequence of OR operations on the provided iterables.
# 4. It short circuit the execution i.e. stop the execution as soon as the result is known.

####################################################################
# all
####################################################################
# 1. Returns true if all of the items are True (or if the iterable is empty).
# 2. All can be thought of as a sequence of AND operations on the provided iterables.
# 3. It also short circuit the execution i.e. stop the execution as soon as the result is known.
####################################################################


####################################################################
#any
####################################################################
# print (any([False, False, False, False]))
# print (any([False, True, False, False]))
# print (any([True, False, False, False]))
# print(any([]))
#False
#True
#True
#False


####################################################################
# print (any({False, False, False, False}))
# print (any((False, True, False, False)))
# print (any([True, False, False, False]))
# False
# True
# True

####################################################################
#all
# print (all([True, True, True, True]))
# print (all([False, True, True, False]))
# print (all([False, False, False]))
# print(all([]))
#True
#False
#False
#True

####################################################################
# l = [1, 3, 4, 0]
# print(any(l))
#true

# l = [0, False] #0 --> False
# print(any(l))
# False

# l = [0, False, 5]
# print(any(l))
# true

# l = [False]
# print(any(l))
# false

# l = []
# print(any(l))
# False

####################################################################
# s = "This is good"
# print(any(s))
# true

# # 0 is False
# # '0' is True

# s = '000'
# print(any(s))
# true

# s = ''
# print(any(s))
# false

#It takes key. It will false when key = 0(int) | False(Boolean)


####################################################################
# d = {0: 'False'}
# print(any(d))
# false

# d = {0: 'False', 1: 'True'}
# print(any(d))
# true

# d = {0: 'False', False: 0}
# print(any(d))
# false

# d = {}
# print(any(d))
# false

# # 0 is False
# # '0' is True
# d = {'0': 'False'}
# print(any(d))



####################################################################
#The all() method returns True when all elements in the given iterable are true. If not, it returns False.
####################################################################
# all values true
# l = [1, 3, 4, 5]
# print(all(l))
# true

# # all values false
# l = [0, False]
# print(all(l))
# false

# # one false value
# l = [1, 3, 4, 0]
# print(all(l))
# false

# # one true value
# l = [0, False, 5]
# print(all(l))
# false

# # empty iterable
# l = []
# print(all(l))
# true

####################################################################
# s = "This is good"
# print(all(s))
# true

# # 0 is False
# # '0' is True
# s = '000'
# print(all(s))
# true

# s = '' # s = " "  it will also return true
# print(all(s))
# true

####################################################################
# s = {0: 'False', 1: 'False'}
# print(all(s))
# false

# s = {1: 'True', 2: 'True'}
# print(all(s))
# true

# s = {1: 'True', False: 0}
# print(all(s))
# false

# s = {}
# print(all(s))
# true

# # 0 is False
# # '0' is True
# s = {'0': 'True'}
# print(all(s))
# true



####################################################################
# s = " "
# print(any(s))
# true

# s = ""
# print(any(s))
# false

####################################################################
# s = " "
# print(all(s))
# s = ""
# print(all(s))
# True
# True

###################################################################
#close any all
#close any all




