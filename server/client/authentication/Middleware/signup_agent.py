from lib.Http     import HTTP_REQUEST, RESPONSE_SAMPLE
from lib.token    import Token

from client.authentication.Signup     import SignUpController

from client.Repository import User, RequestAgent

def SignupAgentMiddleware(request: HTTP_REQUEST):
  try:
    agent_id = request.query.get('agent')
    if agent_id == None:
      return RESPONSE_SAMPLE.notFound()
    
    #? CHECK IF THE REQUEST AGENT EXIST
    isRequestAgentEntityExist = RequestAgent.getRequestAgentById(agent_id, "PENDING")

    if isRequestAgentEntityExist == None:
      return RESPONSE_SAMPLE.badRequest({ 'request_agent': 'THIS REQUEST IS NO MORE VALID' })
    
    #? -> Add role to request body
    request.body['role']  = "AGENT"
    request.body['email'] =  isRequestAgentEntityExist.email
    (email, password, user_name, role) = SignUpController.validateUserData(request.body)
    
    #! WE ARE NOT CHECKING FOR EMAIL BECAUSE WE ALREADY 
    #! CHECKED IT BEFORE WE SENT TO REQUEST
    
    #? CREATE USER
    admin = isRequestAgentEntityExist.user_id
    user = SignUpController.createUser(email, password, user_name, role, user = admin)

    #? UPDATE REQUEST AGENT STATE
    isRequestAgentEntityExist.state = 'ACCEPT'
    isRequestAgentEntityExist.save()


    #? CREATE TOKEN
    token = Token.createToken({
      'email'    : email,
      'agent_id' : user.id,
    })

    return RESPONSE_SAMPLE.successfullyCreadted({ 'token': token })
  
  except Exception as e:
    return RESPONSE_SAMPLE.badRequest({ 'details': str(e) })