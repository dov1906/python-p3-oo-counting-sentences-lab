#!/usr/bin/env python3

class MyString:
  def __init__(self , value = ""):
    self.value = value
    
  @property
  def value(self):
    return self._value 
  
  @value.setter
  def value(self, val):
    if type(val) == str:
      self._value = val
    else:
      print("The value must be a string.")
    
  def is_sentence(self):
    if self.value[len(self.value) -1] == '.':
      return True
    else:
      return False
  
  def is_question(self):
    if self.value[len(self.value) -1] == '?':
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value[len(self.value) -1] == '!':
      return True
    else:
      return False
    

  def count_sentences(self):
    # Replacing multiple sentence ending punctuations with a period
    sentences = self.value.replace('!', '.').replace('?', '.').split('.')
    # Filtering out empty strings from the list      
    sentences = [s.strip() for s in sentences if s.strip()]        
    return len(sentences)
    