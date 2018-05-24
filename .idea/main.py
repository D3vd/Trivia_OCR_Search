import pyscreenshot as Imagegrab
import pytesseract
from PIL import Image
import PIL.ImageOps
import cv2
import argparse
import os
import webbrowser


def Screen_grab_loco(to_save):

    #Screen cap the left side of the desktop for loco
    im=Imagegrab.grab(bbox=(44,304,349,616))
    im.save(to_save)
    return

def Screen_grab_loco_ques(to_save):

    #Screen cap the left side of the desktop for loco
    im=Imagegrab.grab(bbox=(37,306,359,389))
    im.save(to_save)
    return

#Since loco has a dark background and light text the performance of OCR 
#isn't great. So by inverting the color of the screen cap OCR performes 
#better
def Invert_ques_loco(filename):
    image = Image.open(filename)
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image_loc = "Screens/Inverted_images/invert.png"
    inverted_image.save(inverted_image_loc)
    return inverted_image_loc

def Screen_grab_HQ(to_save):

    #Screen cap the left side of the desktop for HQ Trivia
    im=Imagegrab.grab(bbox=(42,209,368,560))
    im.save(to_save)
    return

def Screen_grab_HQ_ques(to_save):

    #Screen cap the left side of the desktop for HQ Trivia
    im=Imagegrab.grab(bbox=(42,209,354,325))
    im.save(to_save)
    return

def Read_screen(filename):

    #Convert the screen cap to grayscale so that OCR performamce is better
    '''
    ap = argparse.ArgumentParser(description='HQ_Bot')
    ap.add_argument("-i", "--image", required=False,default=screenshot_file,help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if args["preprocess"] == "thresh":
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif args["preprocess"] == "blur":
        gray = cv2.medianBlur(gray, 3)

    filename = "Screens/{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    '''

    #Call pytesseract image to string function
    text = pytesseract.image_to_string(Image.open(filename))
    return text

def Perform_search(query):
	#Do Google search of the question
    url = "https://www.google.co.in/search?q=" +(query)
    webbrowser.open_new(url)

def Perform_search_wolframalpha(query):
	#Search the question on Wolframalpha 
	#Wolframalpha is much slower than google so it's not prefered
    url = "http://www.wolframalpha.com/input/?i=" +(query)
    webbrowser.open_new(url)

def Parse_question(filename):
    text = Read_screen(filename)
	
	#Take the raw output from tesseract and make it more search friendly
    lines = text.splitlines()
    question = ""
    options = list()
    flag=False

    for line in lines :
        if not flag :
            question=question+" "+line

        if '?' in line :
            flag=True
            continue

        if flag :
            if line != '' :
                options.append(line)


    new_question = question.replace('"','')

    return new_question

if __name__ == '__main__':

    screenshot_file = "Screens/to_ocr.png"
    prompt = '> '

    print("Select An Option:\n1-Loco    2-HQ Trivia")
    op = int(input(prompt))

    print("Press s to Screenshot and q to quit")
    res = ''

    while(res != 'q'):
        res = input(prompt)

        if(res == 's'):

            if(op == 1):
                Screen_grab_loco_ques(screenshot_file)
                inverted_loc = Invert_ques_loco(screenshot_file)

                question = Parse_question(inverted_loc)

            if(op == 2):
                Screen_grab_HQ_ques(screenshot_file)

                question = Parse_question(screenshot_file)

            print("Question : ")
            print(question)
            print()

            Perform_search(question)

        elif(res == 'q'):
            break;

        else:
            print("Wrong option try again")
