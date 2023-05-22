After having the code, and the .ico file in the same directory you can create a desktop icon for the application with the follow:

1. If you dont have installed the pip pyinstaller, on your terminal:
pip install pyinstaller

2. Now we create the app:
--onefile --noconsole --icon=YTD.ico main.py

3. A dist directory has been created inside your python's project:
inside the dist directory thats your app, now you can create a shortcut to your desktop and play with it
