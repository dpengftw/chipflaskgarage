# chipflaskgarage
Python Flask application running on CHIP

## Quick Start
You will need a:
- CHIP computer or [Raspberry Pi](https://www.amazon.com/s/ref=nb_sb_ss_c_1_3?url=search-alias%3Daps&field-keywords=raspberry+pi+3+b%2B&sprefix=ras%2Caps%2C240&crid=3BEW56TSTPD0Z&rh=i%3Aaps%2Ck%3Araspberry+pi+3+b%2B)
- [MicroSD card](https://www.amazon.com/Samsung-MicroSD-Adapter-MB-ME32GA-AM/dp/B06XWN9Q99/ref=pd_bxgy_147_2?_encoding=UTF8&pd_rd_i=B06XWN9Q99&pd_rd_r=2672257b-f5c4-11e8-a5eb-e38e346fe626&pd_rd_w=9RIWf&pd_rd_wg=yk3H5&pf_rd_i=desktop-dp-sims&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=6725dbd6-9917-451d-beba-16af7874e407&pf_rd_r=5ZNT0XJN51547EK82NFY&pf_rd_s=desktop-dp-sims&pf_rd_t=40701&psc=1&refRID=5ZNT0XJN51547EK82NFY)
- (optional) [Case](https://www.amazon.com/Miuzei-Raspberry-Heatsinks-Supply-Compatible/dp/B07BTHNW9W/ref=pd_bxgy_147_img_3?_encoding=UTF8&pd_rd_i=B07BTHNW9W&pd_rd_r=2672257b-f5c4-11e8-a5eb-e38e346fe626&pd_rd_w=9RIWf&pd_rd_wg=yk3H5&pf_rd_i=desktop-dp-sims&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=6725dbd6-9917-451d-beba-16af7874e407&pf_rd_r=5ZNT0XJN51547EK82NFY&pf_rd_s=desktop-dp-sims&pf_rd_t=40701&psc=1&refRID=5ZNT0XJN51547EK82NFY) for Pi
- 1 channel [relay](https://www.amazon.com/s/ref=nb_sb_ss_i_1_18?url=search-alias%3Daps&field-keywords=3v+1+channel+relay&sprefix=1+channel+relay+3v%2Caps%2C222&crid=AK2JH814BN0C&rh=i%3Aaps%2Ck%3A3v+1+channel+relay)
- USB power adapter

1. Flash your CHIP computer or [Raspberry Pi](https://www.raspberrypi.org/downloads/raspbian/)
2. Install the necessary binaries
```
sudo apt-get install nginx pip

pip install CHIP-IO uWSGI supervisor
```
3. Clone the base code
```
git clone https://github.com/jedioncrk/chipflaskgarage.git
```
4. Connect the GPIO PINs of the computer to relay
<img src="https://github.com/jedioncrk/chipflaskgarage/blob/master/pinout.PNG" />


## Simple Flask web application that verifies the user via a passcode.  Upon verification, the garage control page is available to the user.

<img src="https://github.com/jedioncrk/chipflaskgarage/blob/master/prompt.PNG" /><br />
<img src="https://github.com/jedioncrk/chipflaskgarage/blob/master/inside.PNG" />

## What is CHIP?

The world's first $9 computer, made to make making things more of a thing!  With WiFi, Bluetooth, power management, and onboard storage with mainline Linux pre-installed, C.H.I.P. is ready to pop into your projects! 

https://chip.hackster.io/products/c-h-i-p

## How about Raspberry Pi?

Yes, as long as you have GPIO pins, and run Python, any computer with these two requirements will work.

