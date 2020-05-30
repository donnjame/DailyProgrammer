'''
Challenge from https://www.reddit.com/r/dailyprogrammer/wiki/challenges
[2015-12-23] Challenge # 246 [Intermediate] Letter Splits
This problem is a simplified version of Text Segmentation in Natural Language Processing.

Description

Given a positive integer, return all the ways that the integer can be represented by letters using the mapping:

1 -> A
2 -> B
3 -> C

...

25 -> Y
26 -> Z

For example, the integer 1234 can be represented by the words :

ABCD -> [1,2,3,4]
AWD -> [1,23,4]
LCD -> [12,3,4]

'''
#Solution with OOP

import string
import copy
alpha_dict = dict(enumerate(string.ascii_lowercase,1))

class StrNum:
    
    def __init__(self,number):
        self.number = [y for y in number]
        self.copyy = []
        self.fin = []
    
    def build(self):
        self.copyy = copy.deepcopy(self.number)
        
    def uhh(self):
        for y in range(len(self.number)):
            self.number[y:y+2] = [''.join(self.number[y:y+2])]
            self.fin.append(self.number)
            self.number = copy.deepcopy(self.copyy)
        
    def converttoLetter(self):
        for x in self.fin:
            for y in range(len(x)):
                if int(x[y]) in alpha_dict.keys():
                    x[y] = alpha_dict[int(x[y])]
        print(self.fin)
        
    def final_convert(self):
        for x in self.fin:
            if str(''.join(x)).isalpha():
                print(''.join(x))
        