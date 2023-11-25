from lib.HTTP import HTTP_REQUEST
from .business_logic    import LoginBusinessLayer
from administration.models import SuperAdmin as SuperAdminTable
    
class AuthenticationController:
  @staticmethod 
  def login(request: HTTP_REQUEST) -> SuperAdminTable | None:
    try:
      data = request.body

      (email, password) = LoginBusinessLayer.validate_login_data(
        password = data.get('password'),
        email    = data.get('email')
      )

      return LoginBusinessLayer.check_credentials(email, password)      

    except Exception as e:
      raise
  
