from datetime import datetime
import json
import bcrypt

def hashPassword(password: str):
    salt = bcrypt.gensalt(10)
    password = password.encode('utf-8')
    return bcrypt.hashpw(password, salt).decode('utf-8')


data = [
  {
    "model": "administration.superadmin",
    "pk": 1,
    "fields": {
      "email": "houssemwuerhani@gmail.com",
      "password": hashPassword("houssemwuerhani@gmail.com"),
      "phone_number": "56651363",
      "username": "Werhani Houssemeddine",
      "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
  },
  {
    "model": "administration.superadmin",
    "pk": 2,
    "fields": {
      "email": "mohamedhedigharbi101@gmail.com",
      "password": hashPassword("mohamedhedigharbi101@gmail.com"),
      "phone_number": "24038805",
      "username": "Mohamed Hedi Gharbi",
      "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
  }
]

with open('management/init_super_admin_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)