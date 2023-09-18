# #bubble sorting
# list1 = [23,456,37,6,45,3,87,30,54,88]
# for i in range(len(list1)):
#     print("i is in first loop", list1[i] )
#     for j in range(0,len(list1)-i-1):
#         print("j is in second loop", list1[j])
#         if list1[j] > list1[j+1]:
#             list1[j], list1[j+1] = list1[j+1], list1[j]
# print(list1)

#bubble sorting reverse
# list1 = [23,456,37,6,45,3,87,30,54,54,88]
# for i in range(len(list1)-1):
#     print("i is in first loop", list1[i] )
#     for j in range(0,len(list1)-i-1):
#         print("j is in second loop", list1[j])
#         if list1[j] < list1[j+1]:
#             list1[j], list1[j+1] = list1[j+1], list1[j]
# print(list1)


#selection sort
# list1 = [23,456,37,6,45,3,87,30,54,54,88]
# for i in range(0,len(list1)-1):
#     for j in range(i+1,len(list1)):
#         if list1[i] > list1[j]:
#             var = list1[i]
#             list1[i] = list1[j]
#             list1[j] = var
# print(list1)


#sorting
# list1 = [10,45,23,75,22,88,12,7]
# for i in range(len(list1)):
#     for j in range(len(list1)-i-1):
#         if list1[j] > list1[j+1]:
#             list1[j], list1[j+1] = list1[j+1], list1[j]
# print(list1)


'''selection sort'''
# list1 = [10,45,23,75,22,88,12,7]
# for i in range(len(list1)-1):
#     for j in range(i+1, len(list1)):
#         if list1[i] < list1[j]:
#             var = list1[i]
#             list1[i] = list1[j]
#             list1[j] = var
# print(list1)

'''factorial'''
# x = int(input("enter any number"))
# fact = 1
# while(x>0):
#     fact = x * fact
#     x = x-1
# print(fact)

'''insertion sort'''
# list1 = [10,45,23,75,22,88,12,7]
# for i in range(1,len(list1)):
#     var1 = i
#     while var1>0 and list1[var1] > list1[var1-1]:
#         var2 = list1[var1]
#         list1[var1] = list1[var1-1]
#         list1[var1-1] = var2
#         var1 = var1 - 1
# print(list1)

'''bubble sort'''
# list1 = [10,45,23,75,22,88,12,7]
# for i in range(len(list1)):
#     for j in range(len(list1)-i-1):
#         if list1[j] > list1[j+1]:
#             list1[j], list1[j+1] = list1[j+1],list1[j]
# print(list1)

'''selection sort'''
# list1 = [10,45,23,75,22,88,12,7]
# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i] > list1[j]:
#             var = list1[i]
#             list1[i] = list1[j]
#             list1[j]=var
# print(list1)

'''factorial'''
# x = int(input("enter any number :"))
# fact = 1
# while(x>0):
#     fact = fact * x
#     x = x-1
# print(fact)

'''selection sort'''
# list1 = [10,45,23,75,22,88,12,7]
# for i in range(1,len(list1)):
#     var1 = i
#     while var1>0 and list1[var1] < list1[var1-1]:
#         x = list1[var1]
#         list1[var1] = list1[var1-1]
#         list1[var1-1] = x
#         var1= var1-1
# print(list1)

# my_list = [1, 2, 3, 4, 5, "anuj" ,"nnhh" ]
# my_list.reverse()
# print(my_list)

# my_list = [1, 2, 3,"pp",4, 5,"aa","ff"]
# reversed_list = my_list[::-1]
# print(reversed_list)

# my_list = [1, 2,"rr", 3, 4, 5,"aa"]
# reversed_list = list(reversed(my_list))
# print(reversed_list)

'''decorator'''
# def abc(aa):
#     def bb():
#         print("good morning")
#         aa()
#         print("thanks for using !!")
#     return bb
# @abc
# def hello():
#     print("hello world !!")
# hello()

'''decorator'''
# def abc(a,b,c):
#     return a(b(c))
# abc(print,len,"kumar anuj")


'''closure'''
# def outer_function(x):
#     # This is the enclosing function
#     def inner_function(y):
#         # This is the nested function
#         print("x is ",x)
#         print("y is ",y)
#         return x + y
#     return inner_function
# closure = outer_function(10)
# print(closure(20))
# result = closure(5)
# print(result)

'''args and kwargs'''
# def abc(a, *b, **c):
#     print(a)
#     for i in b:
#         print(i)
#     for j in c.values():
#         print(j)
# abc("anuj", {'a':10} ,{'b':20},one = "abc", two="def")


'''coroutine'''
# import asyncio
# async def greet(name):
#     print(f"Hello, {name}!")
#     await asyncio.sleep(1)  # Simulate some asynchronous work
#     print(f"Goodbye, {name}!")
# async def main():
#     await greet("Alice")
#     await greet("Bob")
# # Create an event loop and run the main coroutine
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.close()

'''counter'''
# from collections import Counter
#
# # Create a counter from a list
# my_list = [1, 2,6,8,4,10,20,76]
# counter = Counter(my_list)
# print(counter)


'''iterator'''
# my_list = [4, 7, 0, 3]
# my_iter = iter(my_list)
# print(next(my_iter))
# print(next(my_iter))
# print(my_iter.__next__())
# print(my_iter.__next__())
# print(my_iter.__next__())

'''generator'''
# def my_generator():
#     for i in range(4):
#         print("aa")
#         yield i
# for item in my_generator():
#     print(item)


# my_list = ["apple", "banana", "cherry"]
# for i, j in enumerate(my_list):
#     print(f"{i}: {j}")

'''pickling and unpickling'''
