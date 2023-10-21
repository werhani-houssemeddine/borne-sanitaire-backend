from .verification_code import generateVerificationCodeTemplate

# This class will have a couple of examples of 
# an email with HTML content, we will add others for 
# future version, at this moment (21/10/2023) we only have 
# an exemple of a verification code sample 
class HTMLSample:

  @staticmethod
  def VERIFICATION_CODE_SAMPLE(code):
    return generateVerificationCodeTemplate(code)
  
  @staticmethod
  def ANOTHER_CODE_SAMPLE():
    pass
