import environ
import jwt

env = environ.Env()
environ.Env.read_env()
            
JWT_SECRET_KEY = env('JWT_SECRET_KEY')

class Token:
  @staticmethod
  def createToken(payload: bytes | dict) -> bytes:

    if isinstance(payload, bytes) or isinstance(payload, dict):
      return jwt.encode(payload, JWT_SECRET_KEY, 'HS256')

    raise Exception('INVALID PAYLOAD TYPE')
  
  @staticmethod
  def getTokenPayload(jwt_payload):
    if isinstance(jwt_payload, str):
      return jwt.decode(jwt, JWT_SECRET_KEY, algorithms=['HS256'])
    
    raise Exception('INVALID PAYLOAD TYPE')