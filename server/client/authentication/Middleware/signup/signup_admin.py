from lib.Http     import HTTP_REQUEST, RESPONSE_SAMPLE
from lib.token    import Token

from client.Repository import User, Device
from client.authentication.Controller.Signup     import SignUpController

def SignupAdminMiddleware(request: HTTP_REQUEST):
  try:
    device_id = request.query.get('device')
    if device_id == None:
      return RESPONSE_SAMPLE.notFound()

    #? CHECK IF THE DEVICE EXIST
    if Device.getDeviceById(device_id) == None:
      return RESPONSE_SAMPLE.badRequest({ 'device': 'THIS DEVICE ID IS NO MORE VALID' })

    #? -> Add role to request body
    request.body['role'] = "ADMIN"
    (email, password, user_name, role) = SignUpController.validateUserData(request.body)

    #? CHECK IF THE USER EXIST
    if User.getUserByEmail(email) != None: # User exist
      return RESPONSE_SAMPLE.badRequest({ 'email': 'THIS PROPERTY IS ALREADY USED' })

    #? CREATE USER AND DEVICE
    user   = SignUpController.createUser(email, password, user_name, role)

    #! WE HAVE TO PASS USER TO DEVICE 
    device = Device.addDevice(device_id, user)

    #? CREATE TOKEN
    token = Token.createToken({
      'email'    : email,
      'admin_id' : user.id,
      'device_id': str(device.device_id)
    })

    return RESPONSE_SAMPLE.successfullyCreadted({ 'token': token })

  except Exception as e:
    return RESPONSE_SAMPLE.badRequest({ 'details': str(e) })