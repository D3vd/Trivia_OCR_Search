import pyscreenshot as Imagegrab
import pytesseract
from PIL import Image
import PIL.ImageOps
import cv2
import argparse
import os
import webbrowser


remove_words = ["who","what","where","when","of","and","that","have","for","the","why","the","on","with","as","this","by","from","they","a","an",
    "and","my","are","in","to","these","is","does","which","his","her","also","have","it","not","we","means","you","comes","came","come",
    "about","if","by","from","go","?",",","!","'","has","\""]
negative_words= ["not","isn\"t","except","don\"t","doesn\"t","wasn\"t","wouldn\"t","can\"t"]

def simplify_ques(question):
    neg = False
    qwords = question.lower().split()
    if [i for i in qwords if i in negative_words]:
        neg = True
    cleanwords = [word for word in qwords if word.lower() not in remove_words]
    temp = ' '.join(cleanwords)
    clean_question=""
    for ch in temp: 
        if ch!="?" or ch!="\"" or ch!="\'":
            clean_question=clean_question+ch

    return clean_question.lower(),neg


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

def Screen_grab_CashShow(to_save):

    #Screen cap the left side of the desktop for The Cash Show
    im = Imagegrab.grab(bbox=(28,203,346,284))
    im.save(to_save)
    return

def Screen_grab_BrainBazzi(to_save):

    #Screen cap the left side of the desktop for Brain Bazzi
    im = Imagegrab.grab(bbox=(26,273,367,367))
    im.save(to_save)
    return

def Screen_grab_TheQ(to_save):

    #Screen cap the left side of the desktop for The Q
    im = Imagegrab.grab(bbox=(11,440,379,534))
    im.save(to_save)
    return

def Screen_grab_Quereka(to_save):

    #Screen cap the left side of the desktop for Quereka
    im = Imagegrab.grab(bbox=(47,284,346,355))
    im.save(to_save)
    return


def Read_screen(filename):

    #Convert the scren cap to grayscale so that OCR performamce is better
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
    url = "https://www.google.co.in/search?q=" +(query)
    webbrowser.open_new(url)

def Perform_search_wolframalpha(query):
    url = "http://www.wolframalpha.com/input/?i=" +(query)
    webbrowser.open_new(url)

def Parse_question(filename):
    text = Read_screen(filename)
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

    print("Select An Option:\n1-Loco    2-HQ Trivia    3-The Cash Show    4-Brain Bazzi    5-The Q    6-Quereka")
    op = int(input(prompt))

    print("Press s to Screenshot and q to quit")
    res = ''

    text_file = open("Question_archive.txt","a")

    if(op == 1):
        text_file.write("Loco\n\n")
    elif(op == 2):
        text_file.write("HQ Trivia\n\n")
    elif(op == 3):
        text_file.write("The Cash Show\n\n")
    elif(op == 4):
        text_file.write("Brain Bazzi\n\n")
    elif(op == 5):
        text_file.write("The Q\n\n")
    elif(op == 6):
        text_file.write("Quereka\n\n")

    cnt = 1

    while(res != 'q'):
        res = input(prompt)

        if(res == 's'):

            if(op == 1):
                Screen_grab_loco_ques(screenshot_file)
                inverted_loc = Invert_ques_loco(screenshot_file)

                question = Parse_question(inverted_loc)

            elif(op == 2):
                Screen_grab_HQ_ques(screenshot_file)

                question = Parse_question(screenshot_file)

            elif(op == 3):
                Screen_grab_CashShow(screenshot_file)

                question = Parse_question(screenshot_file)

            elif(op == 4):
                Screen_grab_BrainBazzi(screenshot_file)

                question = Parse_question(screenshot_file)

            elif(op == 5):
                Screen_grab_TheQ(screenshot_file)
                inverted_loc = Invert_ques_loco(screenshot_file)

                question = Parse_question(inverted_loc)

            elif(op == 6):
                Screen_grab_Quereka(screenshot_file)
                inverted_loc = Invert_ques_loco(screenshot_file)

                question = Parse_question(inverted_loc)


            
            print("Question : ")
            print(question)
            simp_ques, neg = simplify_ques(question)
            text_file.write(str(cnt)+". ")
            text_file.write(question)
            text_file.write("\n")
            cnt = cnt + 1

            if neg:
                print("-- Question is NEGATIVE!")

            print()

            Perform_search(simp_ques)

        elif(res == 'q'):
            text_file.write("\n\n\n")
            break;

        else:
            print("Wrong option try again")

    text_file.seek(0)
    text_file.close()
