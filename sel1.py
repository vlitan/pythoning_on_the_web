#fooling around
import serial
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def	hide_window():
	display = Display(visible=0, size=(800, 600))
	display.start()

def login(email, passw):
	browser.find_element_by_id('email').send_keys(email)
	browser.find_element_by_id('pass').send_keys(passw)
	browser.find_element_by_id('loginbutton').click()
	time.sleep(3);

#hide_window()

#init browser
browser = webdriver.Firefox();
browser.get('http://www.facebook.com/messages/virgil.zappa');
browser.maximize_window();

login('clapavlad@yahoo.com', 'Rock7metal');

ser = serial.Serial('/dev/ttyACM0', 9600);

last_msg = 'a';
msg = 'b'

while (1):
	last_msg = msg;
	
	text_p = browser.find_element_by_xpath('.//li[@class=\'webMessengerMessageGroup clearfix\'][last()]/descendant::p[last()]');
	name_a =  browser.find_element_by_xpath('.//li[@class=\'webMessengerMessageGroup clearfix\'][last()]/descendant::strong/descendant::a');
	name_a.send_keys(Keys.NULL);
	text_p.send_keys(Keys.NULL);
	msg = text_p.text;
	name = name_a.text;
	if ((msg != last_msg) and (name == 'Virgil Litan')):
		print ("@@" + name + "=>" + msg + "##");
		if (msg == 'on'):
			ser.write('b')
		elif (msg == 'off'):
			ser.write('a')
	time.sleep(0.2);

#browser.quit();
#::strong/descendant::a
