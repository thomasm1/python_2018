 
### Feb. 2019

###### VIRTUAL ENV ###########
##### PYTHON SERVERS ############### 
###### IOT TWYTHON TWITTER ###
###### HARDWARE.  ############# 
###### IOT  RASPBERRY SETUP ###
###### PY MATHEMATICS ########### 


#KEY differences between Py3 and Py2
https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html
https://www.geeksforgeeks.org/important-differences-between-python-2-x-and-python-3-x-with-examples

ITERATIONS:     in 2.7 if iterating, keys
                while 3 if iterating, 
                Next key word for iterating .. (turned into key word instead of method, .method). 
DIVISION OPERATOR: 
        # https://www.geeksforgeeks.org/division-operator-in-python/ 
        Integers --> print 7 / 5   ;   print -7 / 5	 
        Output in Python 2.x -->   1     ;  -2 
        Output in Python 3.x -->  1.4    ;  -1.4 
PRINT: print 'Hello, Geeks'   # Python 3.x doesn't support no parens
TEXT:   Python 2: Implicit str type is ASCII, i.e. 8-bit
        Python 3: Implicit str type is Unicode.
print(type('default string ')) 
print(type(u'string with b ')) 
''' 
Output in Python 2.x (Unicode and str are different) 
<type 'str'> 
<type 'unicode'> 
Output in Python 3.x (Unicode and str are same) 
<class 'str'> 
<class 'str'>  
''' 
Reduce no longer exists in 3.x
Map and Filter are still in 3.x
use list comprehensions! if can't you
###########################33
from requests_html import HTMLSession
site="https://www.meetup.com/AbqPython/"
session = HTMLSession()
r = session.get(site)


 # IoT 
###  RPI RASPBIAN UNIX Setup  ################ 
 Py Graphic
	From pygraph-->python graphics_dem.py
 
 ####  SHELL--RASPBIAN
raspi-config 
 expand file system
 localizaiton

sudo apt-get update
sudo apt-get upgrade  

pip
sudo -i 
$ apt-get install python-pip
$ exit
############## VIRTUAL ENV 1 ####################

## Virtual ENV 2  ####################
sudo -i
$ pip install virtualenv
$ exit
$ cd my_project_folder
$ virtualenv venv
source venv/bin/activate
pip install virtualenvwrapper
$ export WORKON_HOME=~/Envs
$ source /usr/local/bin/virtualenvwrapper.sh
export WORKON_HOME=~/
mkvirtualenv venv
$ workon venv
$ deactivate
sudo pip3 install twython
pip install pyperclip  # or pip3
pip install requests
pip install bs4
pip install gpiozero 
 

###     Anaconda ###  
cat > <filename> # places standard input into file

##Anaconda shell:
conda upgrade conda
conda upgrade --all
	#error
conda create -n my_root --clone="C:\ProgramData\Anaconda3"
conda search --canonical | grep -v 'py\d\d' #lists non-python packages


pip install pipenv
pipenv --three
pipenv --two
jupyter notebook
pip install pendulum
## IF USING PYTHON 3.5 ##
conda install python=3.5

 ##### [in Anaconda prompt]


conda list
conda upgrade conda
conda upgrade --all
conda clean --packages
# 
If   "conda command not found" and are using ZShell 
Add ||| export PATH="/Users/username/anaconda/bin:$PATH" |||| to your .zsh_config file.
conda install numpy scipy pandas pyperclip requests bs4 
#
conda create -n py2 python=2.7
conda create -n py3 python=3
activate py3
deactivate
source activate py3  #  bash, OSX
deactivate
pip install --upgrade pip
(py3)pip install requests bs4 pyperclip
# Apache Beam
pip install --upgrade virtualenv
pip install --upgrade setuptools
virtualenv /path/to/directory
. /path/to/directory/bin/activate   

############ PYTHON SERVERS ##################
##############################################
python3 -m pip install pylint

p = 'parsimony and the pythonic way'
print(p)
print(p.title())
#############
C exists to port a binary to a new machine
if C compiler on device, 
it's just pipeline to pass keyboard strokes to libPython. 
So any binary from libPython can run on any device.
Once you have a running interpreter, you want to access
the C library You can access C functions like Python does on C:/
CPython does not require CLI,
C type caling convention is well defined, (so don't need to use C, 
any tool can produce machine readable code, regardless of language 
delivering it
 
https://ngrok.com/####heroku
####AWS-Lambda with: github.com/Miserlou/Zappa
###github.com/atbaker/five-ways-to-deploy
	
### simple-server ###########
activate py2
python3 -m pip install pylint
python3 -m pip install pylint
python -m SimpleHTTPServer   # in r-view
############## python 3 ######################333
python3 -m pip install pylint
python3 -m pip install 
  
### pure_python   
github/AbqPy/python_frameworks ##  forrest.york@gmail.com
 accpts requests   	
Building up a response via the GET method
	Flushing in ordet that buffer not be torn down 
hey localhost:8000
hey -n 2000 ...
### CHALICE  chalice server [serverless Python framework built on AWS Lambda 
	https://github.com/aws/chalice.git
	#DJANGO
pip install Django==1.11.7 

python -m SimpleHTTPServer
yarn http-server // :8080
_JS/03d3_data



###### First Steps:::  DJANGO -> MODEL, TEMPLATE (html), VIEW(ctrl)
Django Best Practices:: 
    http://goo.gl/PRrEMe     
    http://www.djangoproject.com
mkdir dj-fun-course
cd dj-fun-course
# python3 -m venv my_venv_name
python3 -m venv my_venv_name
[linux-mac] . my_venv_name/bin/activate
[win] my_venv_name\Scripts\activate.bat
EXIT: deactivate

pip install django
pip install django==1.9
django-admin startproject tictactoe
django-admin.py startproject tictactoe
cd tictactoe/
python manage.py runserver



npm init # inside django project # install node packages, learn REDUX
# make server.js   # make webpack.config.js    
# webpack.config.jsx  
# index.jsx
# AppRoot.jsx
# App.jsx
pip install django-webpack-loader # add 'webpack_loader', to INSTALLED_APPS
index.html  {% load staticfiles %} ...


### FLASK ########################################################
pip install Flask
pip install Flask-PyMongo
pip install SQLAlchemy  # use flask-restful/flask-restful.git #cd fla* #python setup.py develop
pip install Flask-Mail
pip install flask-restful # use flask-restful/flask-restful.git #cd fla* #python setup.py develop #
from flask import Flask
app = Flask(__name__)
@app.route('/tom\Login')
def NewLogin():
	return 'new item'
if __name__ == '__main__':
	#app.run(debug=True)
	app.run(host='0.0.0.0', port=4000)
	# ROUTING 
@app.route('/tom/<string:name>')# example.com/hello/t
def NewLogin(name):
	return 'Welcome ' + name + '
#Allowed Request Methods
@app.route('/test')
@app.route('/test/, methods=['GET', 'POST])
@app.route('/test', methods=['PUT'])
#Configuration
app.config['CONFIG_NAME'] = 'config value'
app.config.from_envvar('ENV_VAR_NAME') # import from exported env var w pth to config
#Templates
from flask import render_template
@app.route('/')
def index():
	return render_template('template_file.html', var1=value1)
#JSON Resonponses
import jsonify
@app.route('/A')
def A():
	num_list = [1,2,3,4,5]
	num_dict = {'number' : num_list, 'name' : 'Numbers')}
	return jsonify({'output' : num_dict})
##set session
import session
app.config['SECRET_KEY'] = 'Any random string'
@app.route('/login_success')
def login_success():
	session['key_name'] = 'key_value'
	return redirect(url_for('index'))
#read session@app.route('/')
def index():
	if 'key_name' in session:  #session exist and has key
		session_var = session[key_value']
	else: #session does not exist...

def index():
	if 'key_name' in session: 
		session_var = session['key_value']
	

#####Data Models in Flask - 2017 Djangocon.us Spokane
#Flask: Templating, URL Routing, Error Handling, and a Debugger
#### 
##Flask 1
#flaskhello.py
from flask import Flask 
app = Flask(__name__)

@app.route("/")
def flaskhello():
	return "Hello FLASKworld!"

#  $FLASK_APP=flaskhello.py flask run
#pip install Flask-SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:////tmp/test/db'
db = SQLAlchemy(app)
#### 
##Flask 2
sudo apt-get install sqlite3
sqlite3 login.db
>>.tables
>>.exit
python
from app1 import db
db.create_all()
from app1 import db, User
thomas = User(username='tom')
db.session.add(thomas)
db.session.commit()
 
sudo pip install flask_SQLAlchemy
sudo pip install flask_bootstrap
sudo pip install jinja2
sudo pip install flask_security
sudo pip install flask_restful
sudo pip install flask_login

## Flask 3. ########  
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
#
pip install Flask
FLASK_APP=hello.py flask run
	* Running on http://localhost:5000/
	Web app dev, staging, production, deploy
	FLASK-
	Postgres Database
	Application Code
	automatic server configuration
	Platform As A Service
	elastic
	heroku 
	beanstock 
Web app dev, staging, production, deploy

### FLASK 4 
python3 _pyFlask.py #_Python
from flask import Flask 

app = Flask(__name__) 
@app.route("/")
def div1():
    return """<h2>TM Flask Webpage</h2><br />
<h3>Welcome from Tom</h3>"""
if __name__ == "__main__":
    app.run(debug=True)


### DJANGO ##########
#pip install django
django-admin startproject djangproject  #cd djproject
python manage.py startapp djhello
#settings.py  # be careful, add into it.
INSTALLED_APPS = [	'djhello',]
#hello/views.py
from django.http import HttpResponse

def djhello(request):
	return HttpResponse("hellooodjan")
 
#urls py
from django.conf.urls import url
from djhello import views

urlpatterns = [
    url(r'^$', views.djhello),
]     #  then run: >>python manage.py runserver

#models.py
from django.db import models
'''
# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max__length=200)
	content = models.TextField()
	pub_date = models.DateTimeField()

##### IOT TWYTHON TWITTER #######
 
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
gh_url = 'https://api.github.com'
req = urllib2.Request(gh_url)
password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, gh_url, 'user', 'pass')
auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
opener = urllib2.build_opener(auth_manager)

urllib2.install_opener(opener)
handler = urllib2.urlopen(req)
print handler.getcode()
print handler.headers.getheader('content-type') 
# ------
# 200
# 'application/json'

Web pages:
	1) Raspberry Twitter API
https://projects.raspberrypi.org/en/projects/getting-started-with-the-twitter-api
2) Sensehat Streamer:
https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat
3) Website Hosting 
https://readwrite.com/2014/06/27/raspberry-pi-web-server-website-hosting/
   
python --version or python2 –version 
sudo apt-get install python2
sudo dnf install python2
python -m pip install -U pip setuptools
9/20/17
Print   #  %s  %1f   %5d
 #

#### requests ###  
auth_url="https://api.twitter.com/oauth2/token"
from requests_html import HTMLSession
site="https://www.thomasmaestas.net” 
r = session.get(site)ß
"https://www.thomasmaestas.net”
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code
	200
r.headers['content-type']
			'application/json; charset=utf8'
r.encoding
			'utf-8'
r.text
			u'{"type":"User"...'
r.json()
			{u'private_gists': 419, u'total_private_repos': 77, ...}
 
 #### PIP3 list
## python3 -m pip install pyperclip requests

from requests_html import HTMLSession
site="https://www.meetup.com/AbqPython/"
session = HTMLSession()
r = session.get(site)

## pip3 install 
astroid (1.6.5)
automationhat (0.1.0)
beautifulsoup4 (4.6.0) 
bs4 (0.0.1) 
cryptography (1.7.1)
drumhat (0.1.0)
envirophat (1.0.0)
ExplorerHAT (0.4.2)
Flask (0.12.1) 
gpiozero (1.4.1)  
numpy (1.12.1)
oauthlib (2.0.1) 
pgzero (1.2) 
picamera (1.13) 
pigpio (1.38) 
pip (9.0.1) 
pycrypto (2.6.1)
pygame (1.9.3) 
pyperclip (1.6.2) 
requests (2.12.4)
requests-oauthlib (0.7.0) 
scrollphat (0.0.7)
scrollphathd (1.2.1)
SecretStorage (2.3.1)
sense-emu (1.0)
sense-hat (2.2.0)
setuptools (33.1.1)
simplejson (3.10.0) 
touchphat (0.0.1)
twython (3.4.0) 
urllib3 (1.19.1)
Werkzeug (0.11.15) 

# HARDWARE.  ######################### 
SD cards bigger than 32GB using FAT32. However it is possible using third party tools. If you try to format a 64GB (or larger) USB flash drive or SD card under Windows you will have to choose between NTFS and exFAT.May 9, 2016

###  SD   RASPBERRY PI SETUP OPTIONS  
sudo swapoff --all.  # this makes OS write to all instead of more More RAM, more writes.
Swapping is the process of using part of the SD card as volatile memory. This will increase the amount of RAM available, but it will result in a high number of read/writes. It is unlikely to increase performance significantly.

SD cards bigger than 32GB using FAT32. However it is possible using third party tools. If you try to format a 64GB (or larger) USB flash drive or SD card under Windows you will have to choose between NTFS and exFAT.May 9, 2016
 
########## Directories  external Hard Disk   #########################
The Raspberry Pi can also boot it's root partition from an external drive. This could be via USB or Ethernet and means that the SD card will only be used to delegate to different device during boot. This requires a bit of kernel hacking to accomplish, as I don't think the default kernel supports USB storage. You can find more information at this question, or this external blog post. 
Highly used directories such as /var/tmp/ and possibly /var/log can be relocated to RAM in /etc/fstab like this: 
tmpfs /var/tmp tmpfs nodev,nosuid,size=50M 0 0
 
These directories are probably the culprits: 
/home/
/var/
/tmp/

You are able to mount partitions on your external hard drive to these directories automatically at boot. Let's say your HDD is /dev/sdb, and it has four partitions. You can append your /etc/fstab to look something like this: 
/dev/sdb1       /var        ext4   defaults    0  1
/dev/sdb2       /home       ext4   defaults    0  1
/dev/sdb3       /tmp        ext4   defaults    0  1
/dev/sdb4       none        swap   sw          0  0 

##### IOT  RASPBERRY SETUP ########################################## 
 
boot: Linux kernel aand other pkgs
bin: OS-related binary files, like those requireed to run the GUI 
dev: Virtual directory, which doesn't actually exist on the SD. 
	Devices connected to system accessed here
etc: This stores miscellaneous config files, 
	including the list of users and their encrypted passwords
lib: This is a storage space for libraries, 
	which are shared bits of code requireed by different applications##VIM settings ## file called .vimrc
mnt: External hard drives.
opt: New, or optional software goes here
proc: (like dev) Another virtual directory, containing	
	information about running processes
selinux: Files related to Security Enhanced Linux, a suite of security utilities
sbin: Stores special binary files, primarily used by the root account for system maintenance.
sys: Where special OS files are stored
usr: user accessible programs
var: This is vritual directory that programs use to store changing values/variables

	# Shell Bash vim Python
sudo apt-get install apache2 php5 php5-mysql mysql-server
sudo apt-get install vim
sudo apt-get install trash-cli
trash-put somefile.txt
trash-restore
trash-empty
	# test
vim test
set number
syntax on
set tabstop=4
set autoindent
hostname -I
	#find software
apt-cache search emacs  
sudo apt-get install emacs
sudo apt-get remove - emacs
sudo apt-get purge emacs (removes all, incl configs)

sudo apt-get upgrade 
	#A/V RaspiCam
Sudo apt-get install python3-gpiozero libav-tools
python3 -c "import gpiozero"
avconv
raspistill -k
ls
---
raspi-config
Internationalisation:  locale: en_GB.UTF-8 UTF-8
	# save in home directory in file called .vimrc
sudo vi /etc/default/keyboard
#scp
pc->pi: scp myfile.txt pi@10.0.0.226:Public/
pc<-pi: scp pi@10.0.0.226:myfile.txt
#multiple
scp myfile.txt myfile2.txt pi@1
sudo apt-get install ssh
sudo /etc/init.d/ssh start
#to start ssh server at boot:
sudo update-rc.d ssh defaults
#extract file
#http://jdk8.java.net/fxarmpreview/
tar -zxvf fileToExtract.tar.gz #ouput: jdk1.8.0
#put jdk1.8.0 in /home/pi 
#open /etc/profile
PATH=$PATH:/home/pi/jdk1.8.0/bin
export PATH
sudo reboot

##################  RASPBIAN  ################### 
apt-get update:### Synchronizes the list of packages on your system to the list in the repositories. Use it before installing new packages to make sure you are installing the latest version.
apt-get upgrade: ###Upgrades all of the software packages you have installed.
clear: ###Clears previously run commands and text from the terminal screen.
date: ###Prints the current date.
find / -name example.txt: ###Searches the whole system for the file example.txt and outputs a list of all directories that contain the file.
nano example.txt: ###Opens the file example.txt in the Linux text editor Nano.
poweroff: ###To shutdown immediately.
raspi-config: ###Opens the configuration settings menu.
reboot: ###To reboot immediately.
shutdown -h now: ###To shutdown immediately.
shutdown -h 01:22: ###To shutdown at 1:22 AM.
startx: ###Opens the GUI (Graphical User Interface).
FILE AND DIRECTORY CsOMMANDS
cat example.txt: ###Displays the contents of the file example.txt.
cd /abc/xyz: ###Changes the current directory to the /abc/xyz directory.
cp XXX: ###Copies the file or directory XXX and pastes it to a specified location; i.e. cp examplefile.txt /home/pi/office/ copies examplefile.txt in the current directory and pastes it into the /home/pi/ directory. If the file is not in the current directory, add the path of the file’s location (i.e. cp /home/pi/documents/examplefile.txt /home/pi/office/ copies the file from the documents directory to the office directory).
ls -l: ###Lists files in the current directory, along with file size, date modified, and permissions.
mkdir example_directory: ###Creates a new directory named example_directory inside the current directory.
mv examplefile.txt /home/pi/office/ ###  moves examplefile.txt in the current directory to the /home/pi/office directory. If the file is not in the current directory, add the path of the file’s location (i.e. cp /home/pi/documents/examplefile.txt /home/pi/office/ moves the file from the documents directory to the office directory). This command can also be used to rename files (but only within the same directory). For example, mv examplefile.txt newfile.txt renames examplefile.txt to newfile.txt, and keeps it in the same directory.
rm example.txt: ###Deletes the file example.txt.
rmdir example_directory: ###Deletes the directory example_directory (only if it is empty).
scp user@10.0.0.32:/some/path/file.txt: ###Copies a file over SSH. Can be used to download a file from a PC to the Raspberry Pi. user@10.0.0.32 is the username and local IP address of the PC, and /some/path/file.txt is the path and file name of the file on the PC.
touch example.txt: ###Creates a new, empty file named example.txt in the current directory.
NETWORKING AND INTERNET COMMANDS
ifconfig: ###To check the status of the wireless connection you are using  (to see if wlan0 has acquired an IP address).
iwconfig: ###To check which network the wireless adapter is using.
iwlist wlan0 scan: ###Prints a list of the currently available wireless networks.
iwlist wlan0 scan | grep ESSID: ###Use grep along with the name of a field to list only the fields you need (for example to just list the ESSIDs).
nmap: ###Scans your network and lists connected devices, port number, protocol, state (open or closed) operating system, MAC addresses, and other information.
ping: ###Tests connectivity between two devices connected on a network. For example, ping 10.0.0.32 will send a packet to the device at IP 10.0.0.32 and wait for a response. It also works with website addresses.
wget http://www.website.com/example.txt: ###Downloads the file example.txt from the web and saves it to the current directory.
SYSTEM INFORMATION COMMANDS
cat /proc/meminfo: ###Shows details about your memory.
cat /proc/partitions: ###Shows the size and number of partitions on your SD card or hard drive.
cat /proc/version: ###Shows you which version of the Raspberry Pi you are using.
df -h: ###Shows information about the available disk space.
df /: ###Shows how much free disk space is available.
dpkg – –get–selections | grep XXX: ###Shows all of the installed packages that are related to XXX.
dpkg – –get–selections: ###Shows all of your installed packages.
free: ###Shows how much free memory is available.
hostname -I: ###Shows the IP address of your Raspberry Pi.
lsusb: ###Lists USB hardware connected to your Raspberry Pi.
UP key: ###Pressing the UP key will print the last command entered into the command prompt. This is a quick way to repeat previous commands or make corrections to commands.
vcgencmd measure_temp: ###Shows the temperature of the CPU.
vcgencmd get_mem arm && vcgencmd get_mem gpu: ###Shows the memory split between the CPU and GPU.
##############################################################
Web pages:
	1) Raspberry Twitter API
https://projects.raspberrypi.org/en/projects/getting-started-with-the-twitter-api
2) Sensehat Streamer:
https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat
3) Website Hosting 
https://readwrite.com/2014/06/27/raspberry-pi-web-server-website-hosting/

wget -O - http://www.raspberrypi.org/files/astro-pi/astro-pi-install.sh --no-check-certificate | bash
   sudo apt-get update
sudo apt-get dist-upgrade
sudo piwiz
sudo apt-get install realvnc-vnc-server
sudo apt-get install realvnc-vnc-viewer 
sudo apt-get install qpdfview
sudo apt-get purge xpdf
sudo apt-get install rp-prefapps
sudo apt-get install piwiz
sudo apt-get install pi-package
sudo raspi-config

clear
find / -name example.txt
nano example.txt
poweroff
raspi-config

cat example.txt #displays
scp user@10.0.0.32:/some/path/file.txt #downloads file from PC.

ifconfig
iwconfig #check which network
iwlist wlan0 scan #prints list of networks
iwlist wlan0 scan | grep ESSID #grep with name of field to list only field you need
nmap scans your network and lists connected devices, port number, protocol, state, MAC
wget http//www.website.com/example.txt downloads


cat /proc/meminfo #details about memory
cat /proc/partitions
cat /proc/version
df -h diskspace
df / #how much free space
dpkg --get-selections | grep XXX/ #shows all of installed packages that related to XX
dpkg --get-selections
free #free mem available
hostname -I #shows IP address of Pi
lsusb lists usb hardware connected to Pi
vcgencmd measure_temp  #temp of CPU
vcgencmd get_mem arm && vcgencmd get_mem gpu #

#common unix printing system
sudo apt-get install cups 
#stop virtual desktop
vncserver -kill :<display-number> 
#search inside files 
grep "search" *.txt

###############  IOT PIMORONI ############
curl https://get.pimoroni.com/explorerhat | bash  ## !! expands pi filesystem
sudo apt-get install pimoroni  # download examples you'll find them in /home/pi/Pimoroni/explorerhat
sudo apt-get install python3-explorerhat
python -m pip install -U pip setuptools   
sudo date -s "1 MAY 2016 12:00:00" 
sudo iwlist wlan0 scan
#open wpa-supplicant in nano
sudo nano /etc/wpa_supplicant/wpa_supplicant.config
#at bottom of file:
network={
	ssid="testing"
	psk="testingPassword"  }	


#### CAMERA   #########################	
## RaspiCam ###(blue side facing Ether) 

# import cv2
pip install opencv-python
mplt3. 
## mpld3 bring matplotlib to browser

pip install mpld3
import matplotlib.pyplot as plt

fromk mpl_toolkits
scipy.interpolate 

sudo apt-get install gpioquitezero libav-tools
sudo apt-get install python3-gpiozero libav-tools
python3 -c "import gpiozero" # this checks no error
avconv
raspistill -k
raspistill -o image.jpg
#celebritysleuth
sudo nano /boot/config.txt
diable_camera_led=1 # added to the end of the file.
sudo reboot
while True:
	filename = "intruder.h264"
	pir.wait_for_motion()
	camera.start_recording(filename)
	pir.wait_for_no_motion()
		camera.stop_recording()
filename = "intruder.h264"
camera.start_recording(filename)
from datetime import datetime
now = datetime.now()
print('today is the {0:%W} of {0:%A) of {0:%Y}".format(now))
now = datetime.now()
filename = "{0:%Y}={0:%m}-{0:%d}
omxplayer filename
omxplayer test.h264

#SENSEHAT ########## https://trinket.io/sense-hat #######  
	#8x8 LED matrix # Temp and humidity # Barometric 
	# pressure sensor # mini joystick # Gyroscope #
	# Accelerometor # orientation # magnemeter
	 #python exit() control-d
from sense_hat import SenseHat
from time import sleep

########################## SENSE  MARQUEE    ###############

s = SenseHat()
s.low_light = True 
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180) 
def raspi_logo():
    G = green
    R = red
    O = nothing
    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo 
images = [  raspi_logo, raspi_logo,  ]
count = 0 
while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1 

	
API SOURCE :  https://pythonhosted.org/sense-hat/api/
########################  SENSE HUMIDITY TEMPERATURE ############ 
from sense_hat import SenseHat
import time

sense=SenseHat()
humidity = sense.get_humidity()
humidity
	30.211442947387695 --- hour after steam shower ... 33.475124359
sense.clear(0,0,255)  # blue screen
sense.show_message("message")

########################## SENSE  ORIENTATION    ###############
sense.get_orientation()
sense.set_pixel(0,0,255)

	Get more familiar with Raspberry Pi's IoT capabilities: This session will overview the Pi hardware setup, including the sense-hat accessory. Next, we will SSH from a laptop to remotely control temp./humidity sensors and Inertial Measurement Unit chip (gyroscope/accelerometer/magnetometer). Presentation by Abdul Gauba and Tom Maestas.  


########################### ENVIRONMENTAL SENSORS ###############################
#______________HUMIDITY ______________get_humidity()
from sense_hat import SenseHat

sense = SenseHat()
humidity = sense.get_humidity()
print("Humidity: %s %%rH" % humidity) 
print(sense.humidity)

#______________TEMPERATURE______________get_temperature()
from sense_hat import SenseHat
sense = SenseHat()
temp = sense.get_temperature()
print("Temperature: %s C" % temp) 
print(sense.temp)
print(sense.temperature)

#______________BAROMETER PRESSURE 
(TEMP)______________get_temperature_from_pressure()
from sense_hat import SenseHat 
sense = SenseHat()
temp = sense.get_temperature_from_pressure()
print("Temperature: %s C" % temp)

########################### INERTIAL MEASUREMENT UNIT  SENSORS ###############################
The IMU (inertial measurement unit) sensor is a combination of three sensors, each with an x, y and z axis. For this reason it's considered to be a 9 dof (degrees of freedom) sensor.
1) Gyroscope
2) Accelerometer
3) Magnetometer (compass)

#______________IMU CONFIGURATION______________set_imu_config(False, True, False)
#________________________________(compass_enabled, gyro_enabled, accel_enabled)

'''Enables and disables the gyroscope, accelerometer and/or magnetometer contribution to the get orientation functions below.'''

set_imu_config(True, True, True)

from sense_hat import SenseHat
sense = SenseHat()
sense.set_imu_config(False, True, False)  # gyroscope only

#______________GYROSCOPE______________get_gyroscope()
from sense_hat import SenseHat 
sense = SenseHat()
gyro_only = sense.get_gyroscope()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only)) 
print(sense.gyro)
print(sense.gyroscope)

#______________ACCELEROMETER______________get_accelerometer()
from sense_hat import SenseHat
sense = SenseHat()
accel_only = sense.get_accelerometer()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only)) 
print(sense.accel)
print(sense.accelerometer)

#______________MAGNETOMETER ORIENTATION______________get_orientation()
from sense_hat import SenseHat
sense = SenseHat()
orientation = sense.get_orientation()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
print(sense.orientation)

#______________COMPASS______________get_compass()
from sense_hat import SenseHat 
sense = SenseHat()
north = sense.get_compass()
print("North: %s" % north) 
print(sense.compass)

########################### JOYSTICK ###############################
from sense_hat import SenseHat
from time import sleep 
sense = SenseHat()
event = sense.stick.wait_for_event()
print("The joystick was {} {}".format(event.action, event.direction))
sleep(0.1)
event = sense.stick.wait_for_event()
print("The joystick was {} {}".format(event.action, event.direction))



################## PY MATHEMATICS ################################### matplotlib-->holoviews-->datashader-->JS bokeh
matplotlib-->Vaex-->JS bqplot + JS bokeh
matplotlib-->mpld3-->JS d3-->d3po-->Vega-->Vincent +->Vega-Lite-->Altair
matplotlib-->
seaborn
ggpy
scikit-plot
Yellow brick
networkx-->graphviz-->graph-tool
basemap/cartopy
pandas
#
JS-->pythreejs
ipleaflet
ipyvolume
plotly
toyplot
cufflinks
#
PyQTgraph
chaco
Lightning
GlueViz
MayaVi
GR framework
############### Matplotlib ###########3
from matplotlib import rcsetup
rcsetup.all_backends
#
import pandas as pd
iris = pd.read_csv('iris.csv')
iris.head()
color_map = dict(zip(iris.species.unique(),['blue','green','red']))


################# PANDAS-3.5 #####
Pandas - Lofty and Built atop Numpy - 
# https://bootstrap.pypa.io/get-pip.py

conda create -n pandas-3.5 python=3.5
activate pandas-3.5
#source ~/anaconda3/bin/activate pandas-3.5
conda install jupyter
conda install pandas
conda install numpy
#in jupyter
import pandas as pa
import numpy as nu

jupyter notebook
-----------------------pandas library-------
#### data/data.csv -> 'original date', col1, col2
import pandas as pd
newData = pd.read_table('data/data.csv', sep=',') # , header=None
format_cols = ['original date','col1','col2']
newData = pd.read_table('data/data.csv', sep=',', names=format_cols) . # , header=None 
print(type(newData['col2']))  # -> pandas.core.series.Series
print(type(newData)) # pandas.core.frame.DataFrame
print(newData.describe())
print(newData.shape)
print(newData.dtypes)
print(newData.describe(include=['object']))
newData.columns
newData.rename(columns = {'original date':'New_Date','col1':'Col_1','col2':'Col_2'})
newData.rename(columns = {'original date':'New_Date','col1':'Col_1','col2':'Col_2'}, inplace=True)
newData.columns
oCols = ['original date','col1','col2']
newData.columns = oCols
print(newData.head())
#
newData2 = pd.read_table('data/data.csv', sep=',', names=format_cols, header=0) . # , header=None
newData2.columns
newData2.columns = newData2.columns.str.replace(' ', '_')
newData2.columns  # output is:   original date -> original_date 
newData2.shape
newData2.drop('col1',axis=1, inplace =True) 
newData2.drop([0,1] , axis=0, inplace=True)
type(newData2['col2'].sort_values())
newData2.sort_values('col2')
newData2.sort_values(['original_date','col2'])
type(False) # bool
booleans = [] 
    for length in newData2.col2:
        if length >= 400001:
	    booleans.append(True)
	else:
	    booleans.append(False)
print(booleans[0:5])
len(booleans) 
newData2[newData2.col2 >=  10000].original_date
newData2.loc[original_date >= 2010, 'col1']
True or False
True and False
newData2[newData2.col2 >= 400001 and newData2.original_date == '2010'] newData2[(newData2.col2 >= 400001) & (newData2.original_date == '2010')]
newData2[(newData2.col2 >= 400001) | (newData2.original_date == '2010') | (newData2.col1 >= 30)]
newData2[newData2.original_date.isin(['2010','2011'])]

# coding: utf-8.  DRINKS BY COUNTRY 

import pandas as pd
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.dtypes

import numpy as np
drinks.select_dtypes(include=[np.number]).dtypes
drinks.describe()
drinks.describe(include='all')
drinks.describe(include=['object'])
drinks.head()
drinks.drop('continent', axis=1).head()
drinks.drop(2, axis=0).head()
drinks.mean(axis=0)
drinks.mean(axis=1)
drinks.drop(2, axis=0).head()
drinks.mean(axis=1).shape
drinks.mean(axis='columns')
drinks.country.str.upper()
drinks[drinks.country.str.contains('Vietnam')]
drinks[drinks.country.str.startswith('U')]
drinks.country.str.replace(' ', '_').str.replace('\'','')
drinks.dtypes
drinks.beer_servings.astype(float)
drinks_float = pd.read_csv('http://bit.ly/drinksbycountry', dtype={'beer_servings':float})
drinks_float.dtypes
drinks_float.wine_servings.mean()
drinks_float.wine_servings.astype(int).mean()
drinks_float.wine_servings.astype(float).mean()
drinks_float.groupby('continent').wine_servings.mean()
drinks_float[drinks_float.continent=='North America'].wine_servings.mean()
drinks_float[drinks_float.continent=='Europe'].wine_servings.mean()
drinks_float.groupby('continent').wine_servings.max()
drinks_float.groupby('continent').wine_servings.agg(['count','min','max','mean'])
drinks_float.groupby('continent').mean()
get_ipython().magic('matplotlib inline')
drinks.groupby('continent').mean().plot(kind='bar')
drinks.continent.value_counts()
drinks.continent.value_counts(normalize=True)
pd.crosstab(drinks.country,drinks.continent).head()
get_ipython().magic('matplotlib inline')
drinks.continent.value_counts().plot(kind='bar')
drinks.groupby('continent').mean().plot(kind='bar')
drinks.dtypes
drinks.isnull().sum()
drinks[drinks.continent.isnull()]
drinks.shape
drinks.dropna(how='any').shape
drinks.dropna(subset=['country', 'continent'], how='all').shape
drinks['continent'].value_counts(dropna=False)
drinks['continent'].fillna(value='MISCELLANEOUS', inplace=True)
drinks.loc[0,:]
drinks.loc[[0,1,2],:]
drinks.loc[:,'beer_servings':'wine_servings'].head(10)
drinks.head(5).drop('total_litres_of_pure_alcohol', axis=1)
drinks.columns
list(range(0,4))
drinks.iloc[:,0:4].tail(10) 

### APACHE-BEAM ###########
pip install apache-beam
pip install apache-beam[feature1, feature2]
pip install apache-beam[gcp]
pip install apache-beam[test]

conda env export > PiMaterial.yaml # save the packages to YAML file 
conda env create -f PiMaterial.yaml
conda env list 
conda env remove -n py3
conda install jupyter notebook 	 #  or pip install jupyter notebook
jupyter notebook 		##  in your terminal 
	By default, the notebook server runs at http://localhost:8888
conda install nb_conda

--Jupyter # set up matplotlib to work interactively in the notebook with %matplotlib
 (% or %%) for line magics and cell magics
 %%timeit %pdb
jupyter nbconvert --to html notebook.ipynb  # in your terminal use  --to latex
jupyter nbconvert notebook.ipynb --to slides  #   create the slideshow from the notebook file,
jupyter nbconvert notebook.ipynb --to slides --post serve # To convert it and immediately see it,
 
 ####### END MATHEMATICS ###############