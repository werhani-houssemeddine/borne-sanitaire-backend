from lib.Http.response_samples import RESPONSE_SAMPLE
from lib.Http                  import HTTP_REQUEST

from client.agent.Controller   import AgentController
from client.Repository         import RequestAgentRepository

from Mail.samples import HTMLSample
from Mail         import sendHTMLContentEmail

from client.utils import CurrentUser
class Agent:

  #?
    #? This method is not directly called from the agent endpoint it
    #? will be called from admin endpoint (admin request agent to have an account)
    #? this function will add a new requestAgent entity, to complete the action the agent
    #? will receive an email to confirm the invitation and copmlete the necessary fields
    #? to have an account 
  #?
  @staticmethod
  def add(request: HTTP_REQUEST):
    try:
      email = AgentController.checkEmail(request)

      currentUser: CurrentUser = request.session['__currentUser__']

      if email == None:
        return RESPONSE_SAMPLE.badRequest({ 'details': 'EMAIL IS ALREADY USED' })
      
      #? This function create a new request agent object in the database
      #? it also returns the request_id
      request_id = RequestAgentRepository.newRequestAgent(
        user_id = currentUser.getId(),
        email   = email,
      )

      messageContent = {
        'username': currentUser.getUsername(),
        'request_id': str(request_id),
        'host': request.ip + ":8000"
      }

      sendHTMLContentEmail("New Sign Up", messageContent, [email], HTMLSample.NEW_AGENT_SAMPLE)
      
      return RESPONSE_SAMPLE.successfullyCreadted()

    except Exception as e:
      return RESPONSE_SAMPLE.badRequest({ 'details': str(e) })
    
  def checkRequestAgent(request: HTTP_REQUEST):
    agent_id = request.query.get('agent')
    if agent_id == None:
      return RESPONSE_SAMPLE.notFound()
    
    #? CHECK IF THE REQUEST AGENT EXIST
    isRequestAgentEntityExist = RequestAgentRepository.getRequestAgentById(agent_id, "PENDING")

    if isRequestAgentEntityExist == None:
      return RESPONSE_SAMPLE.badRequest({ 'request_agent': 'THIS REQUEST IS NO MORE VALID' })
    
    return RESPONSE_SAMPLE.ok()

  def edit(request: HTTP_REQUEST):
    pass

  def archieve(request: HTTP_REQUEST):
    pass

  def delete(request: HTTP_REQUEST):
    pass

  def rejectRequest(reqest: HTTP_REQUEST):
    print(reqest.params)
    pass
  
