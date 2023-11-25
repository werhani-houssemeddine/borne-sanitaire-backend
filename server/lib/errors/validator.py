import re

class ValidationError(Exception):
  def __init__(self, field=None, message=None):
    super().__init__(message)
    
    self.message = message
    self.field   = field

class Validator:
  def __init__(self, data: dict) -> 'Validator':
    self.data = data

  def check_not_null(self, field) -> 'Validator':
    if self.data.get(field) is None:
      raise ValidationError(
        field   = field, 
        message = "This property is required"
      )
    
    return self
  
  def check_not_empty(self, field) -> 'Validator':
    value = self.data.get(field)
    if isinstance(value, str):
      if len(value.strip()) != 0:
        return self
      
    raise ValidationError(
      field   = field, 
      message = "This property is required"
    )
  
  def check_email(self, field) -> 'Validator':
    value = self.data.get(field)
    
    email_regex = re.compile(r'^\S+@\S+\.\S+$')
    if not email_regex.match(value):
      raise ValidationError(
        field   = field, 
        message = "Invalid email format"
      )
    
    return self
  
  def check_min_length(self, field, min_length=None) -> 'Validator':
    value = self.data.get(field)

    if min_length is not None and len(value) < min_length:
      raise ValidationError(
        field   = field, 
        message = f"Field length must be at least {min_length} characters"
      )
    
    return self

  def check_max_length(self, field, max_length=None) -> 'Validator':
    value = self.data.get(field)

    if max_length is not None and len(value) > max_length:
      raise ValidationError(
        field   = field, 
        message = f"Field length must not exceed {max_length} characters"
      )
    
    return self

  def check_custom_async(self, field, callback) -> 'Validator':
    value = self.data.get(field)
    callback(value)
    return self