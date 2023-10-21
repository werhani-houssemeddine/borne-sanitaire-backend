from datetime import datetime

#! This file will be the responsable of writing the HTML content

def getCurrentTime():
  current_time = datetime.now()
  second       = current_time.second
  minute       = current_time.minute
  month        = current_time.month
  year         = current_time.year
  hour         = current_time.hour
  day          = current_time.day

  return f"{hour}:{minute}:{second} {day}/{month}/{year}"

def generateCSS():
  return """
    <style>
      h3 {
        color: #0073e6;
        font-family: Arial, sans-serif;
      }
      h1 {
        color: #000;
        font-family: Arial, sans-serif;
      }
      .verification-code {
        font-weight: bold;
        font-family: Arial, sans-serif;
      }
      .button-link {
        text-decoration: none;
        color: #0073e6;
        border: 1px solid #0073e6;
        padding: 10px 20px;
        border-radius: 5px;
        display: inline-block;
        font-family: Arial, sans-serif;
        transition: background-color 0.3s, color 0.3s;
      }
      .button-link:hover {
        background-color: #0073e6;
        color: #fff;
      }
      .container {
        text-align: center;
        font-family: Arial, sans-serif;
      }
      .welcome-paragraph {
        text-align: justify;
        color: #333;
        font-family: Arial, sans-serif;
      }
    </style>
  """

def generateEmailContent(code, agent, current_time):
  return f"""
    <h2>Borne sanitaire</h2>
    <h1>Verification Code</h1>
    <p class="welcome-paragraph">
      Welcome, Admin, to the Borne Sanitaire application. 
      We have received your request to access our platform 
      from the device {agent} on {current_time}.
      Below, you'll find your verification code. 
      Please note that this code will remain valid for the next 15 minutes. 
      If you did not initiate this access request, 
      or if you have any concerns about the security of your account, 
      please click the button below to initiate our security process. 
      We also recommend that you change your password for enhanced security. 
      Your feedback and recommendations are valuable to us, 
      so please don't hesitate to share any insights or suggestions to help us 
      improve our service.
    </p>

    <p class="verification-code">{code}</p>
    <p>If you did not request this code, please click the button below:</p>
    <a href="#" class="button-link">Not Me</a>
  """

def generateVerificationCodeTemplate(code = "xXxXxXx", agent= 'Smart Phone xXx'):
  current_time    = getCurrentTime()
  getCssStyle     = generateCSS()
  getEmailContent = generateEmailContent(
    current_time = current_time,
    agent        = agent, 
    code         = code
  )

  return f"""
    <!DOCTYPE html>
    <html>
      <head>
        {getCssStyle}
      </head>
      <body>
        <div class="container">
          {getEmailContent}
        </div>
      </body>
    </html>
  """