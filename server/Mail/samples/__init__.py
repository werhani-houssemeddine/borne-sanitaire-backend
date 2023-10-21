from .verification_code import generateVerificationCodeTemplate

# this calss will have a couple of exemple of 
# an email with a HTML content, we will add other for 
# future version, at this moment (21/10/2023) we only have 
# an exemple of a verification code sample 
class HTMLSample:

  @staticmethod
  def VERIFICATION_CODE_SAMPLE(code):
    return generateVerificationCodeTemplate(code)
  
  @staticmethod
  def ANOTHER_CODE_SAMPLE():
    pass
