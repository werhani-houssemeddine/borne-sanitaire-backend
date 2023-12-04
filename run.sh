#!/bin/bash

# This file will load the necessary data for our application

# Get variable from command line
if [ -z "$1" ]; then
  echo "---- SERVER RUNNING IN LOCAL ENVIRONMENT ----";
fi

# Store the variable
ip_address="$1"

# Run python environment 
source .env/Scripts/activate

# Add the administrator actors if not exist 
count=$(python server/manage.py shell -c "from administration.models import SuperAdmin; print(SuperAdmin.objects.count())")

if [ "$count" -eq 0 ]; then
  # Create the data
  python management/generate_super_admin_data.py

  # Initialize the database
  python server/manage.py loaddata management/init_super_admin_data.json
else
  echo "The database is already not empty";
fi

# Run the server 
python server/manage.py runserver "$ip_address"