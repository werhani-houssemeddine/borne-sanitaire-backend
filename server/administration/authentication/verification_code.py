import random

class VerificationCode:

  @staticmethod
  def generateCode(length = 8):
    listOfCharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    random_string = ''

    for _ in range(length):
      random_index = random.randint(0, len(listOfCharacters) - 1)
      random_string += listOfCharacters[random_index]

    return random_string
  
  @staticmethod
  def getCode(length = 8):
    VerificationCode.generateCode(length)
  
  @staticmethod
  def saveCode(code, ip):
    pass

  @staticmethod
  def loadCode(ip):
    pass