from Mail.samples import HTMLSample
from Mail         import sendHTMLContentEmail

class sendOTPCode:
  @staticmethod
  def send(code: int, email: str):    
    sendHTMLContentEmail("New Sign Up", code, [email], HTMLSample.OTP_SAMPLE)
