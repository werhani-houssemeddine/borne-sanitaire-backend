import bcrypt


#! Bcrypt class is to hash and compare values
#! calling hash to hash instannce and compare to 
#! compare instances

class Bcrypt:
  rounds: int = 12

  # In other language we may make it private and will
  # be called from hash and compare functions
  @staticmethod
  def generateSalt(rounds: int = 12) -> bytes:
     return bcrypt.gensalt(rounds)


  @staticmethod
  def compare(instance1: str, instance2: str) -> bool:
    try:
      if isinstance(instance1, str):
        instance1 = instance1.encode('utf-8')

      if isinstance(instance2, str):
        instance2 = instance2.encode('utf-8')

      return bcrypt.checkpw(
        hashed_password = instance2,
        password        = instance1
      )
    
    except Exception as e:
      if e == "Invalid salt":
        return bcrypt.checkpw(
          hashed_password = instance1,
          password        = instance2
        )
  

  @staticmethod
  def hash(instance: bytes) -> bytes:
    if isinstance(instance, str):
      instance = instance.encode('utf-8')

    return bcrypt.hashpw(
      password = instance,
      salt     = Bcrypt.generateSalt(Bcrypt.rounds) 
    )
