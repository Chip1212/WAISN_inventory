# WAISN_inventory_web_app
WAISN Fellowship coding assignment


This is the requested web app created by Timothy Holt as a part of the application process for the WAISN fellowship.

The application was created using Django and SQLite as described in the spec.

This is a very basic Django application as I have never really worked with a web framework before this. 
This proved to be a challenging and fun assignment.

**Acessing the application**

To get the application up and running, download and unzip this file. Ensure that django is installed on your machine. 

Use terminal to navigate to the "mysite" directory within the downloaded folder.

Next, Utilize the "python manage.py createsuperuser" command to create an admin user. 

Follow the prompts using an email you have access to in order to create your user credentials.

Use "python3 ./manage.py runserver" in the command line to begin running the server.

Next, open a browser and navigate to "http://127.0.0.1:8000/inventory".

This should take you to the application, where you can login with the credentials you provided earlier.

You can now use the application to add items to the inventory, delete items from the inventory, and change the quantity of items in the inventory.

Once you set an item's quantity to 0 (when not in the new_item page), you should recieve an email at the address provided earlier,
notifying you that you have run out of that item.
