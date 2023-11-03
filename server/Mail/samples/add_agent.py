from datetime import datetime
from pathlib  import Path

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
      h2 {
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

def generateEmailContent(full_name, link):
  return f"""
    <h2>Borne sanitaire</h2>
    <p class="welcome-paragraph">
      Hello! We are delighted that you've chosen our platform. 
      To get started with {full_name}, please complete your account creation process. 
      To access our platform, simply click the link below. 
      If you prefer to decline this invitation, just press the red button. 
      Please note that either of these actions will notify {full_name}. 
      Also, don't forget to sign up before the link expires in 7 days.
    </p>

    <p class="verification-code">
      <a href="#complete" class="complete-sign-up">complete</a>
    </p>
    <p>If you want to reject the invitation, please click the button below:</p>
    <a href="#reject" class="button-link">Reject</a>
  """



def generateAddAgentTemplate(full_name, link):
  current_time    = getCurrentTime()
  getCssStyle     = generateCSS()
  getEmailContent = generateEmailContent(
    full_name = "Werhani Houssemeddine",
    link      = ""
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