from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()
    
setup(
   name = 'brain_scan',
   version = '0.1.0',
   description = 'A brain scan tumor classification model.',
   license = 'MIT',
   long_description = long_description, 
   author = 'DATA 515 Brain Scan Classification Team',
   author_email = 'aaliyahfiala42@gmail.com', 
   url = "http://aaliyahhanni.pythonanywhere.com/"
   packages = ['brain_scan'],
   install_requires = ['tensorflow', 'urllib3'] #NOTE: Need to list ALL dependencies we use in final project
)
