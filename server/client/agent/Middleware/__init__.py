from lib.Http.response_samples import RESPONSE_SAMPLE
from lib.Http                  import HTTP_REQUEST

from client.agent.Controller   import AgentController
from client.Repository         import RequestAgent

from Mail.samples import HTMLSample
from Mail         import sendHTMLContentEmail

class Agent:

  #?
    #? This method is not directly called from the agent endpoint it
    #? will be called from admin endpoint (admin request agent to have an account)
    #? this function will add a new requestAgent entity to complete the action the agent
    #? will receive an email to confirm the invitation and copmlete the necessary fields
    #? to have an account 
  #?
  @staticmethod
  def add(request: HTTP_REQUEST):
    try:
      email = AgentController.checkEmail(request)

      if email == None:
        return RESPONSE_SAMPLE.badRequest({ 'details': 'EMAIL IS ALREADY USED' })
      
      requestAgentId = str(RequestAgent.newRequestAgent(email = email , user_id = 2))
      sendHTMLContentEmail("New Sign Up", "Werhani Houssemeddine", [email], HTMLSample.NEW_AGENT_SAMPLE)
      
      return RESPONSE_SAMPLE.successfullyCreadted()

    except Exception as e:
      return RESPONSE_SAMPLE.badRequest({ 'details': str(e) })

  def edit(request: HTTP_REQUEST):
    pass

  def archieve(request: HTTP_REQUEST):
    pass

  def delete(request: HTTP_REQUEST):
    pass
  
