from lib.Http import HTTP_REQUEST, RESPONSE_SAMPLE

from administration.account.Controller import updateSuperAdminPhonenumber
from administration.account.Controller import updateSuperAdminUsername
from administration.account.Controller import updateSuperAdminPassword


def UpdateSuperAdminMiddleware(request: HTTP_REQUEST):
  data = request.body
  
  if data.get('password'):
    updateSuperAdminPassword()

  elif data.get('phone_number'):
    updateSuperAdminPhonenumber()

  elif data.get('username'):
    updateSuperAdminUsername()

  return RESPONSE_SAMPLE.notFound()