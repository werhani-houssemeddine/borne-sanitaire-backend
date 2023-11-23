from .verification_code import generateVerificationCodeTemplate
from .add_agent         import generateAddAgentTemplate  

# This class will have a couple of examples of 
# an email with HTML content, we will add others for 
# future version, at this moment (21/10/2023) we only have 
# an exemple of a verification code sample 
class HTMLSample:

  @staticmethod
  def VERIFICATION_CODE_SAMPLE(code):
    return generateVerificationCodeTemplate(code)
  
  @staticmethod
  def NEW_AGENT_SAMPLE(message):
    link = message['host'] + '/agent-request/?agent=' + message['request_id']
    return generateAddAgentTemplate(full_name = message['username'], link = link)
