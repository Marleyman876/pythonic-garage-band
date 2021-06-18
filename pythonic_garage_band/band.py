from attr import mutable
import re

class Band:
    
    instances = []
    
    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
      return  f"The band {self.name}" 
   
    def __repr__(self):
      return f'Band instance. name={self.name}, members={self.members}'
    
    def play_solos(self):
      return [member.play_solo() for member in self.members]
    
    @classmethod
    def to_list(cls):
      return cls.instances  
      
       
   
      
   

class Musician:
    def __init__(self, name, type, instrument, solo):
      self.name = name
      self.type = type
      self.instrument = instrument
      self.solo = solo
  
  
    def __repr__(self):
      return f"{self.type} instance. Name = {self.name}"
   
    def __str__(self):
      return f"My name is {self.name} and I play {self.instrument}" 
    
    def get_instrument(self):
      return f"{self.instrument}"
     
    def play_solo(self):
      return f"{self.solo}"


class Guitarist(Musician):
  def __init__(self, name):
    super().__init__(name,"Guitarist", "guitar", "face melting guitar solo")
    

class Bassist(Musician):
  def __init__(self, name):
    super().__init__(name,"Bassist", "bass", "bom bom buh bom")
      
 
class Drummer(Musician):
  def __init__(self, name):
    super().__init__(name,"Drummer", "drums", "rattle boom crash")
  


  
  