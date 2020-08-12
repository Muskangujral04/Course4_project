VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer():
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    def goBankrupt(self):
        self.prizeMoney = 0
    def addPrize(self, prize):
        self.prizes.append(prize)
    def addMoney(self,amt):
        self.prizeMoney = self.prizeMoney + amt
    def __str__(self):
        return "{} (${})".format(self.name,self.prizeMoney)
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def getMove(self,category, obscuredPhrase, guessed):
        print("{} has a ${}".format(self.name,self.prizeMoney))
        print("Category: {}".format(category))
        print("Phrases: {}".format(obscuredPhrase))
        print("Guessed: {}".format(guessed))
        n=input("Guess a letter, phrase, or type 'exit' or 'pass':")
        return n


# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.prizeMoney = 0
        self.prizes = []
    
    def smartCoinFlip(self):
        if random.randint(1, 10) > self.difficulty:
            return True
        else: 
            return False
    
    def getPossibleLetters(self, guessed):
        l = []
        if self.prizeMoney >= 250: 
            for i in LETTERS:
                l.append(i)
        else:
            for i in LETTERS:
                if i not in VOWELS and i not in guessed:
                    l.append(i)
        return l

    def getMove(self, category, obscuredPhrase, guessed):
        lst = self.getPossibleLetters(guessed)
        FlipResult = self.smartCoinFlip()
        if len(lst) == 0:
            return 'pass'
        else:
            if FlipResult==True:
                for l in self.SORTED_FREQUENCIES:
                    if l in lst:
                        return l
            elif FlipResult==False:
                return random.choice(lst)
