import random
import RomanNum

class Card:
    def __init__(self, rank, suit, arcana):
        self.suit =  suit
        self.rank = rank
        self.arcana = arcana
    def __str__(self):
        if self.arcana == "minor" :
            return f"* {self.rank} of {self.suit} *"
        elif self.arcana == "major" :
            x = RomanNum.conv(self.rank)
            return f"* {x} {self.suit} {x} *"
        
class Deck:
    def __init__(self):
        self.cards = []
        self.major_arcana = []
        self.minor_arcana = []
        
        #Create Major Arcana Cards
        majors = [
            "The Fool",
            "The Magician",
            "The High Priestess",
            "The Empress",
            "The Emporer",
            "The Hierophant",
            "The Lovers",
            "The Chariot",
            "Strength",
            "The Hermit",
            "Wheel of Fortune",
            "Justice",
            "The Hanged Man",
            "Death",
            "Temperance",
            "The Devil",
            "The Tower",
            "The Star",
            "The Moon",
            "The Sun",
            "Judgement",
            "The World",
            ]
        n = 0
        for major in majors:
            card = Card(n, major, "major")
            self.major_arcana.append(card)
            n += 1
            
        #Create Minor Arcana Cards
        minor_suits = [
            "Cups", 
            "Wands", 
            "Pentacles", 
            "Swords"
            ]         
        minor_ranks = [
            "Ace",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Page",
            "Knight",
            "Queen",
            "King"
            ]
        for minor_suit in minor_suits:
            for minor_rank in minor_ranks:
                self.minor_arcana.append(Card(minor_rank, minor_suit, "minor"))
          
        #Add major and minor arcana to deck 
        self.cards = self.major_arcana + self.minor_arcana


    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self, number):
        self.spread = []
        for x in range(number):
            card = self.cards.pop()
            self.spread.append(card)
            
class Spreads:
    def threecard(self):
        print("\n You Chose a 3 Card Spread!")
        z = Reading()
        z.draw(3)
    def celtic(self):
        print("\n You Chose a 10 Card Celtic Cross Spread!")
        z = Reading()
        z.draw(10)
    def custom(self):
        x = int(input('A custom draw! How many cards would you like? \n'))
        z = Reading()
        z.draw(x)
        
  
class Reading:
    
    def begin(self):
        print("*" * 20)
        print('Welcome to Tahni\'s House of Tarot! \n')
        x = int(input(" For a 3 card Past / Present / Outcome spread, enter 1 \n For a Celtic Cross 10 card spread, enter 2 \n For a custom spread, enter 3 \n\n"))
        if x == 1:
            spread = Spreads().threecard()
        elif x == 2:
            spread = Spreads().celtic()
        else:
            spread = Spreads().custom()
    
    
    def draw(self, a):
        deck = Deck()       
        deck.shuffle()
        deck.deal(a)
        print()
        
        #initialize counters for suits and arcanas
        cmin = 0
        cmaj = 0
        cwands = 0
        ccups = 0
        cswords = 0
        cpent = 0
        for card in deck.spread:
            print(card)
            if card.arcana == "minor":
                cmin += 1
                if card.suit == "Wands":
                    cwands += 1
                elif card.suit == "Cups" :
                    ccups += 1
                elif card.suit == "Swords" :
                    cswords += 1
                elif card.suit == "Pentacles" :
                    cpent += 1
            else:
                cmaj += 1

        print()
        print("You got", cmin,"minor arcana cards and", cmaj, "major arcana cards! Interesting! ")
        #if (cwands > 1) or (ccups > 1) or (cswords > 1) or (cpent > 1):
        print( f"Of the minor arcana, there were {cwands} wands, {ccups} cups, {cswords} swords, and {cpent} pentacles")
        

         
r = Reading()
r.begin()