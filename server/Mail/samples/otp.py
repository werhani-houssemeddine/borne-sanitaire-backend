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

def generateEmailContent(code):
  return f"""
    <h2>Borne sanitaire</h2>
    <p class="welcome-paragraph">
      Hello! We are delighted that you've chosen our platform. 
      To get started with Our Service, please complete your account creation process. 
      To access our platform, use this code {code}
    </p>
  """



def generateOTPTemplate(code):
  getCssStyle     = generateCSS()
  getEmailContent = generateEmailContent(code)

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