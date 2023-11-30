from .request_agent_controller import RequestAgentController
from .agent_controller         import AgentController 

# from lib.HTTP.http_request     import HTTP_REQUEST
# from .bussinessLayer           import validateAgentData
    
# from client.Repository import UserRepository, RequestAgentRepository

# class AgentController:
#   #? checkEmail function will validate the email than will check
#   #? check if the email is used by other user
#   #? or a requestAgent used it 
#   #? the method return the email if the email is used otherwise
#   #? it return None and raise an error if it's not valid
#   @staticmethod
#   def checkEmail(request: HTTP_REQUEST):
#     try:
#       email = validateAgentData(request.body["email"])
#       isEmailUsed = UserRepository.getUserByEmail(email)
#       isEmailUsedToRequestAgent = RequestAgentRepository.getRequestAgentByEmail(email)
      
#       checkingEmailResult = isEmailUsed or isEmailUsedToRequestAgent

#       #? If the email is used return NULL
#       #? otherwise return the email
#       return email if checkingEmailResult == None else None

#     except Exception as e:
#       raise