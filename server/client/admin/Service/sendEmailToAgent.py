from Mail.samples import HTMLSample
from Mail         import sendHTMLContentEmail

class SendEmailToAgent:
  @staticmethod
  def requestAgentEmail(username: str, request_id: str, email: str, ip: str, port: int = 8000):
    messageContent = {
      'username': username,
      'request_id': str(request_id),
      'host': ip + ":" + str(port)
    }
    
    sendHTMLContentEmail("New Sign Up", messageContent, [email], HTMLSample.NEW_AGENT_SAMPLE)
