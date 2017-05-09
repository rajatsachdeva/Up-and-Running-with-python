'''
Created on 09-May-2017

@author: Rajat Sachdeva
'''
'''
symmetric_difference()
The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
The set is immutable to the .symmetric_difference() operation (or ^ operation).

>>> s = set("Hacker")
>>> print s.symmetric_difference("Rank")
set(['c', 'e', 'H', 'n', 'R', 'r'])

>>> print s.symmetric_difference(set(['R', 'a', 'n', 'k']))
set(['c', 'e', 'H', 'n', 'R', 'r'])

>>> print s.symmetric_difference(['R', 'a', 'n', 'k'])
set(['c', 'e', 'H', 'n', 'R', 'r'])

>>> print s.symmetric_difference(enumerate(['R', 'a', 'n', 'k']))
set(['a', 'c', 'e', 'H', (0, 'R'), 'r', (2, 'n'), 'k', (1, 'a'), (3, 'k')])

>>> print s.symmetric_difference({"Rank":1})
set(['a', 'c', 'e', 'H', 'k', 'Rank', 'r'])

>>> s ^ set("Rank")
set(['c', 'e', 'H', 'n', 'R', 'r'])
Task
Students of District College have subscriptions to English and French newspapers. 
Some students have subscribed to English only, some have subscribed to French only,
and some have subscribed to both newspapers.You are given two sets of student roll numbers.
One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.
'''

def main():
    _ = raw_input()
    eng = set(map(int, raw_input().split()))
    _ = raw_input()
    frn = set(map(int, raw_input().split()))
    total = len(eng.symmetric_difference(frn))
    print total
if __name__ == '__main__':
    main()