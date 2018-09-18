import pyscreenshot as imagegrab
import pytesseract
from PIL import Image
import PIL.ImageOps
import webbrowser


def screen_grab_loco_ques(to_save):

    # Screen cap the left side of the desktop for loco
    im = imagegrab.grab(bbox=(37, 306, 359, 389))
    im.save(to_save)
    return


def screen_grab_hq_ques(to_save):

    # Screen cap the left side of the desktop for HQ Trivia
    im = imagegrab.grab(bbox=(42, 209, 354, 325))
    im.save(to_save)
    return


def screen_grab_cashshow(to_save):

    # Screen cap the left side of the desktop for The Cash Show
    im = imagegrab.grab(bbox=(28, 203, 346, 284))
    im.save(to_save)
    return


def screen_grab_brainbazzi(to_save):

    # Screen cap the left side of the desktop for Brain Bazzi
    im = imagegrab.grab(bbox=(26, 273, 367, 367))
    im.save(to_save)
    return


def screen_grab_theq(to_save):
    # Screen cap the left side of the desktop for The Q
    im = imagegrab.grab(bbox=(11, 440, 379, 534))
    im.save(to_save)
    return


def screen_grab_qureka(to_save):
    # Screen cap the left side of the desktop for Quereka
    im = imagegrab.grab(bbox=(47, 284, 346, 355))
    im.save(to_save)
    return


# Since loco has a dark background and light text the performance of OCR
# isn't great. So by inverting the color of the screen cap OCR performs
# better


def invert_ques_loco(filename):
    image = Image.open(filename)
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image_loc = "Screens/Inverted_images/invert.png"
    inverted_image.save(inverted_image_loc)
    return inverted_image_loc


def read_screen(filename):
    # Call pytesseract image to string function
    text = pytesseract.image_to_string(Image.open(filename))
    return text


def perform_search(query):
    # Do Google search of the question
    url = "https://www.google.co.in/search?q=" + query
    webbrowser.open_new(url)


def perform_search_wolframalpha(query):
    # Search the question on Wolframalpha
    # Wolframalpha is much slower than google so it's not prefered
    url = "http://www.wolframalpha.com/input/?i=" + query
    webbrowser.open_new(url)


def parse_question(filename):
    text = read_screen(filename)
    # Take the raw output from tesseract and make it more search friendly

    lines = text.splitlines()
    question = ""
    options = list()
    flag = False

    for line in lines:
        if not flag:
            question = question+" "+line

        if '?' in line:
            flag = True
            continue

        if flag:
            if line != '':
                options.append(line)

    new_question = question.replace('"', '')

    return new_question


if __name__ == '__main__':

    screenshot_file = "Screens/to_ocr.png"
    prompt = '> '

    print("Select An Option:\n1-Loco    2-HQ Trivia    3-The Cash Show    4-Brain Bazzi    5-The Q    6-Qureka")
    op = int(input(prompt))

    print("Press s to Screenshot and q to quit")
    res = ''

    while res != 'q':
        res = input(prompt)
        question = ''

        if res == 's':

            if op == 1:
                screen_grab_loco_ques(screenshot_file)
                inverted_loc = invert_ques_loco(screenshot_file)

                question = parse_question(inverted_loc)

            if op == 2:
                screen_grab_hq_ques(screenshot_file)

                question = parse_question(screenshot_file)

            if op == 3:
                screen_grab_cashshow(screenshot_file)

                question = parse_question(screenshot_file)

            if op == 4:
                screen_grab_brainbazzi(screenshot_file)

                question = parse_question(screenshot_file)

            if op == 5:
                screen_grab_theq(screenshot_file)
                inverted_loc = invert_ques_loco(screenshot_file)

                question = parse_question(inverted_loc)

            if op == 6:
                screen_grab_qureka(screenshot_file)
                inverted_loc = invert_ques_loco(screenshot_file)

                question = parse_question(inverted_loc)

            print("Question : ")
            print(question)

            print()

            perform_search(question)

        elif res == 'q':
            break

        else:
            print("Wrong option try again")
