from lib.HTTP     import HTTP_REQUEST, HTTP_RESPONSE, RESPONSE_SAMPLE
from lib.errors   import ValidationError

from client.authentication.Controller import SignupControllerAgent

def SignupAgentMiddleware(request: HTTP_REQUEST) -> HTTP_RESPONSE:
  try:
    #? In the agent case we can omit sending the token, the agent is requested
    #? this endpoint from a web page and the app is delivred by a mobile app
    
    agent_signup = SignupControllerAgent(request)
    if agent_signup:
      token = SignupControllerAgent.generateToken(agent_signup.agent.agent_id)
      return RESPONSE_SAMPLE.OK(data = { 'token': token })
    
    else:
      return RESPONSE_SAMPLE.faillureBuild(
        status_code = 401,
        message     = "UNAUTHORIZED",
        data        = { 'User': 'WRONG CREDENTIALS' }
      )

  except ValidationError as ve:
    print(f"AN ERROR OCCURED {ve}")
    return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
  except Exception as e:
    print(f'SignupAgentMiddleware {e}')
    return RESPONSE_SAMPLE.BAD_REQUEST()
  