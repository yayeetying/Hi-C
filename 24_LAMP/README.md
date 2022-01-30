# how-to :: Create a Droplet with Ubuntu and Apache2
---
## Overview
  Guide to creating a DigitalOcean Droplet (Virtual Machine) equipped with Ubuntu 20.04 and Apache2

### Estimated Time Cost: 30 mins

### How-To

1. Create the Droplet on DigitalOcean, with prerequisites below:
- Ubuntu 20.04
- Basic Shared CPU
- Regular Intel (with SSD)
- $5/month plan
- A data center in the area you are closest in
2. Authenticate device with ssh, not password
3. Access Droplet by launching Droplet console
- Annabel tips!: if you want to launch Droplet in regular computer instead of opening console everytime, run `ssh [user]@[droplet_ip]`

#### Deploying Flask app with Virtual Host
4. Enable mod_wsgi
```
sudo apt-get install libapache2-mod-wsgi-py3 python-dev
```
```
sudo a2enmod wsgi
```
5. Create flask app (with static and templates folder)
```
cd /var/www/
```
```
sudo mkdir <FlaskApp>
cd <FlaskApp>
sudo mkdir <FlaskApp>
cd <FlaskApp>
sudo mkdir static templates
```
6. Add contents of flask app into init.py
```
sudo nano __init__.py
```
7. Install python3-pip, virtualenv, and Flask
8. Configure and enable virtual host
```
sudo nano /etc/apache2/sites-available/<FlaskApp>.conf
```
Change mywebsite.com to the IPV4 addy, and FlaskApp to the name of your app
```
<VirtualHost *:80>
 	ServerName mywebsite.com
 	ServerAdmin admin@mywebsite.com
 	WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
 	<Directory /var/www/FlaskApp/FlaskApp/>
 		Order allow,deny
 		Allow from all
 	</Directory>
 	Alias /static /var/www/FlaskApp/FlaskApp/static
 	<Directory /var/www/FlaskApp/FlaskApp/static/>
 		Order allow,deny
 		Allow from all
 	</Directory>
 	ErrorLog ${APACHE_LOG_DIR}/error.log
 	LogLevel warn
 	CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
Enable Virtual Host
```
sudo a2ensite <FlaskApp>
```
9. Create WSGI file
```
cd /var/www/<FlaskApp>
```
```
sudo nano <flaskapp>.wsgi
```
```
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application
application.secret_key = 'Add your secret key'
```
10. Apply changes
```
sudo service apache2 restart
```
HINT: If Apache shows default webpage instead of Flask app, run:
```
sudo a2dissite 000-default.conf
```
then apply changes again :)
