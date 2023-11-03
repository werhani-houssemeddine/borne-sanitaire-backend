def validateAgentData(email = None) -> str:
  try:
    if email == None:
      raise Exception('Email is required')
    
    if not isinstance(email, str) or '@' not in email:
      raise Exception('email must be a valid email address \'str\' type and contains @ characters')
    
    return email.lower()

  except Exception as e:
    raise