'''

https://www.reddit.com/r/dailyprogrammer/comments/53ijnb/20160919_challenge_284_easy_wandering_fingers/

Input
Given the following input strings, find all possible output words 5 characters or longer.

'qwertyuytresdftyuioknn'

'gijakjthoijerjidsdfnokg'

Output
Your program should find all possible words (5+ characters) that can be derived from the strings supplied.

'''

class ReadMe:
    count = 0
    def __init__(self,filename):
        self.filename = filename
        self.words = []
    
    def open_file(self):
        try:
            with open(self.filename, encoding = 'utf-8') as f:
                contents = f.read()
        except FileNotFoundError:
            print(f"Sorry, the file{filename} cannot be found")
        else:
            self.words = contents.split()
            #num_words = list(words)
    
    def update_file(self,new_f):
        self.filename = new_f
        ReadMe.open_file(self)
    
    
    def word_count(self,word):
        ReadMe.count = 0
        self.word = word
        for x in self.words:
            if x == self.word:
                ReadMe.count += 1
        print(ReadMe.count)
        
    def all_words(self,sample):
        self.almost = []
        self.there = []
        self.sample = [sample[x] for x in range(1,len(sample)-1)]
        for x in self.words:
            if x[0] == sample[0] and x[-1] == sample[-1]:
                self.almost.append(x)
        for x in self.almost:
            if all(elem in self.sample for elem in [y for y in x[1:-1]]) == True:
                self.there.append(x)
        print(self.there)
