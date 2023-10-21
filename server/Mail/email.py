from django.core.mail import send_mail
from django.conf      import settings

from .samples import HTMLSample

class InvalidInputException(Exception):
  pass

# This function will raise an exception if the arguments
# are not valid or return the email propeties 
def check_arguments(subject, message, recipients):
  if subject is None or isinstance(subject, str) == False:
    raise InvalidInputException('Invalid subject parameter')
  
  if message is None or isinstance(message, str) == False:
    raise InvalidInputException('Invalid message parameter')
  
  if isinstance(recipients, str):
    return (subject, message, [recipients])
  
  elif isinstance(recipients, list):
    for recipient in recipients:
      if isinstance(recipient, str) == False:
        raise InvalidInputException('Invalid recipients parameter List<str>')
      
  else:
    raise InvalidInputException('Invalid recipients parameter str')
  
  return (subject, message, recipients)


# This email will sent the email
def sendEmail(subject, message, recipients):
  try:
    subject, message, recipients = check_arguments(subject, message, recipients)
    send_mail(
      recipient_list = recipients,
      html_message   = None, #"<button>" + message + "</button>",
      from_email     = settings.EMAIL_HOST_USER,
      subject        = subject,
      message        = message,
    )

  except Exception as e:
    print(e)
    raise


#! this function will be responsable of sending 
#! an email with html content
def sendHTMLContentEmail(subject, message, recipients, html_message_sample):
  send_mail(
    recipient_list = recipients,
    html_message   = html_message_sample(message),
    from_email     = settings.EMAIL_HOST_USER,
    subject        = subject,
    message        = message,
  )