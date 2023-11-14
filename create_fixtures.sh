#!/bin/bash

# This file will load the necessary data for our application



count=$(python server/manage.py shell -c "from administration.models import SuperAdmin; print(SuperAdmin.objects.count())")

if [ "$count" -eq 0 ]; then
  # Create the data
  python management/generate_super_admin_data.py

  # Initialize the database
  python server/manage.py loaddata management/init_super_admin_data.json
else
  echo "The database is already not empty";
fi