#implement a class called player that represents a cricket player.the player class should have a method called play() which prints "the player is playing cricket".derive two classes, batsman and bowler, from the player class.override the play() method in each derived class to print "the batsman is batting "and "the bowler is bowling "respectively.write a program to create object of both the Batsman and bowler classes and call the play () method for each object
class player:
  def play (self):
    print ("the player is playing cricket ")
class Batsman(player):
  def play (self):
    print ("the batsman is batting  ")
class Bowler(player):
  def play (self):
    print ("the bowler is bowling   ")
batsman= Batsman()
bowler=Bowler()
batsman.play()
bowler.play()