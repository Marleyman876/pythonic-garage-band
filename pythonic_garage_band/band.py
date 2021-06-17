from attr import mutable
import re

class Band:
    
    all_band_mates = []
    
    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        self.__class__.all_band_mates.append(self) #(https://stackoverflow.com/questions/9610993/python-type-or-class-or-is) found explnantion on how to use this on stack over flow in the demo roger user count class.count.

    def __str__(self):
      results = f"The band {self.name}" 
      
      return results 

    def __repr__(self):
        results = f'Band instance. name={self.name}, members={self.members}'
        return results 
    def solo(self):
      output = ''
      for person in self.members:
        output += person.play_solo() + ' '
        return output

class Musician:
    def __init__(self, name, type, instrument, members=[]):
      self.name = name
      self.type = type
      self.instrument = instrument
      self.member = members
  
    def __repr__(self):
      return f"{self.type} instance. Name = {self.name}"
   
    def __str__(self):
      output = f"My name is {self.name} and I play {self.instrument}" 
      return output
    
    def play_solo(self):
      solos = ''
      for each_solo in self.members:
        solos += f"{each_solo.play_solo()}\n"
        return solos
      # return f"{self.name} is playing solo on the {self.instrument}"
    
    def get_instrument(self):
      return f"{self.instrument}"
      
# @staticmethod
# def new_data(data):
#   data_split = re.findall(r"\S.*", data)
#   print(data)
  

class Guitarist(Musician):
  def __init__(self, name):
    super().__init__(name,"Guitarist", "guitar")

class Bassist(Musician):
   def __init__(self, name):
      super().__init__(name,"Bassist", "bass")
 
class Drummer(Musician):
   def __init__(self, name):
      super().__init__(name,"Drummer", "drums")
     
  

if __name__ == "__main__":
  x = Musician('C')
  print(x.play_solo)
  
  band = """
  The Roots
  AOwen Bibble, Guitarist
  Mark Kelly, Bass
  Quest Love, Drums
  """ 