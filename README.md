# Trivia OCR Search

This is a Python script that googles the question as it appears on a trivia game. It uses tesseract OCR to convert a picture of the question to text and then perform a google search.

<b>Note</b>: 
This program is not a web crawler, it does not suggest a right answer for the question. Rather it just googles the question, it's up to the user to find the answer from the search result.


![Demo](https://i.imgur.com/5Z1HjlK.gif)


## Setup

Make sure to have completed all the following steps before running the program.

### Downloading the Program

Download the program by either clicking the 'Clone or download' button or by running the following command in a command line interpreter:

```
git clone https://github.com/R3l3ntl3ss/Trivia_OCR_Search.git
```

Before proceeding make sure to be within the Trivia\_OCR\_Search directory.

### Installing Packages

This script was written completely in Python 3.6, so make sure to have installed the latest version of python to avoid any errors.

The packages and libraries used in the program include:
```
pyscreenshot
pillow
pytesseract
```
Install all the above libraries individually or run the following command to install them:

```
pip install -r requirements.txt
```

### Mirroring Phone Screen

In order for the script to get the question, you will have to mirror your phone screen unto your computer. 

Use any software of your choice to do the same. Some options include:

- Vysor
- Reflector 
- AirPlay

After mirroring keep the window on one side of your desktop.


### Getting Question Coordinates

In this step you need to specify where exactly the question will appear on your computer screen so that the script can take a screenshot of the question. Depending on your screen resolution the coordinates will vary. 

![Question-Coordinates](https://i.imgur.com/bnA0HXW.png)

Find the X and Y coordinates of the red points around the question.

For Windows, download and use [Mofiki's Coordinate Finder](https://www.softpedia.com/get/Desktop-Enhancements/Other-Desktop-Enhancements/Mofiki-s-Coordinate-Finder.shtml).

For Mac, press Command-Shift-4 to view your mouse coordinates. Move the mouse to the points around the question and record the coordinates. Press esc to exit.

Once you have recorded the coordinates, open `main.py` in a text editor and change the coordinates in `im = imagegrab.grab(bbox=(X1, Y1, X2, Y2))` for the specific game.

There is a separate function for each game in the script, be sure to make changes in the appropriate function.

`screen_grab_loco_ques()` is for Loco and so on.


### Running the Program

Execute and run the program by simply opening `main.py` or by using the command `python main.py` on your command line interpreter.
