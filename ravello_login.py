
import os
from ravello_sdk import *

client = RavelloClient()
client.login(username=os.environ['RAVELLO_USER'],
             password=os.environ['RAVELLO_PASS'],
             identify_domain=os.environ['RAVELLO_DOMAIN'])
             
# Find all apps.
for app in client.get_applications():
	print ('Found Application: {0}'.format(app['name']))
  
