from lib.HTTP     import HTTP_REQUEST, RESPONSE_SAMPLE
from lib.token    import Token

from client.Repository import UserRepository, DeviceRepository
from client.authentication.Controller.Signup     import SignUpController

def SignupAdminMiddleware(request: HTTP_REQUEST):
  try:
    device_id = request.query.get('device')
    
    #! This ckeck is already made in SignupMiddleware 
    # if device_id == None:
    #   return RESPONSE_SAMPLE.notFound()

    #? CHECK IF THE DEVICE EXIST
    if DeviceRepository.getDeviceById(device_id) == None:
      return RESPONSE_SAMPLE.badRequest({ 'device': 'THIS DEVICE ID IS NO MORE VALID' })

    #? -> Add role to request body
    request.body['role'] = "ADMIN"
    (email, password, user_name, role) = SignUpController.validateUserData(request.body)

    #? CHECK IF THE USER EXIST
    if UserRepository.getUserByEmail(email) != None: # User exist
      return RESPONSE_SAMPLE.badRequest({ 'email': 'THIS PROPERTY IS ALREADY USED' })

    #? CREATE USER AND DEVICE
    user   = SignUpController.createUser(email, password, user_name, role)

    #! WE HAVE TO PASS USER TO DEVICE 
    device = DeviceRepository.addDevice(device_id, user)

    #? CREATE TOKEN
    token = Token.createToken({
      'email'    : email,
      'id' : user.id,
      'device_id': str(device.device_id)
    })

    return RESPONSE_SAMPLE.successfullyCreadted({ 'token': token })

  except Exception as e:
    return RESPONSE_SAMPLE.badRequest({ 'details': str(e) })