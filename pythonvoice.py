import pyttsx3
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from translate import Translator





engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("WELCOME to audisankara college of engineering in gudur",)
engine.say("enter a student name:")
engine.runAndWait()

user = input("enter a student name:")
gm = (user," enter a year of studying")
engine.say(gm)
engine.runAndWait()
year = int(input("enter a year of studying:"))
present = 0


def options():
    engine.say("please select top of  the list")
    engine.runAndWait()
    print(user,"welcome to hp college")
    print("enter 'cls' (class) 'tp'(topic) 'a'(adentance) 'data'(details) 'internet'(browser) 'trans'(translator) or 'q'(quit)")

def select():
    transaction = str(input("what you like to do? :"))
    return transaction

options()
command = str(select())

while command != 'q':
    if command == 'cls':
        engine.say("hey you select class")
        engine.runAndWait()
        if year == 2:
            print(year,'top of building in our college')
            command = str(select())
        elif year == 3:
            print(year,"middle of the building")
            command = str(select())
        elif year == 4 :
            print(year,"ground floor")
            command = str(select())
        else:

            engine.say(" invalid selected year")
            engine.runAndWait()
        command = str(select())

    elif command == 'tp':
        engine.say("hey you select topics")
        engine.runAndWait()
        if year == 2:
            print("1.co,2.se,3.java,4.database")
        elif year == 3:
            print("python,data analysis")
        elif year == 4:
            print("projects")
        else:

            engine.say(" there no topics selected year")
            engine.runAndWait()
        command = str(select())
    elif command == 'a':
        engine.say("hey you select attendence")
        engine.runAndWait()
        month = 31
        at = int(input(" how many days absentance in this month:"))
        present = month - at
        if at <= 31:
            present = month - at
            print(user, "your attented class", present, "days")
            command = str(select())
        else:
            print("enter valid days")
            print(at)
    elif command == 'data':
        engine.say("hey you select details")
        engine.runAndWait()

        print("STUDENT NAME:",user)
        print("YEAR",year)
        if present == 0:
            print("attendance in this month:""data not  entered")
        else:
             print("attendance in this month",present,"days")
        command = str(select())

    elif command == 'internet':
        engine.say("hello you are entered into internet")
        engine.runAndWait()



        class MainWindow(QMainWindow):
            def __init__(self):
                super(MainWindow, self).__init__()
                self.browser = QWebEngineView()
                self.browser.setUrl(QUrl('http://google.com'))
                self.setCentralWidget(self.browser)


                self.showMaximized()

                # navbar

                navbar = QToolBar()
                self.addToolBar(navbar)

                back_btn = QAction('Back', self)
                back_btn.triggered.connect(self.browser.back)
                navbar.addAction(back_btn)

                forward_btn = QAction('Forward', self)
                forward_btn.triggered.connect(self.browser.forward)
                navbar.addAction(forward_btn)

                reload_btn = QAction('reload', self)
                reload_btn.triggered.connect(self.browser.reload)
                navbar.addAction(reload_btn)

                home_btn = QAction('Home', self)
                home_btn.triggered.connect(self.navigate_home)
                navbar.addAction(home_btn)

                face_btn = QAction('facebook', self)
                face_btn.triggered.connect(self.face_book)
                navbar.addAction(face_btn)

                self.url_bar = QLineEdit()
                self.url_bar.returnPressed.connect(self.navigate_to_url)
                navbar.addWidget(self.url_bar)

            def face_book(self):
                self.browser.setUrl(QUrl('http://facebook.com'))


            def navigate_home(self):
                self.browser.setUrl(QUrl('http://duckduckgoharish.com'))

            def navigate_to_url(self):
                url = self.url_bar.text()
                self.browser.setUrl(QUrl(url))


        app = QApplication(sys.argv)

        QApplication.setApplicationName('harish browser')

        window = MainWindow()
        app.exec_()
        command = str(select())

    elif command == 'trans':
        engine.say("you are entered into translation")
        engine.runAndWait()

        translate = Translator(from_lang=str(input("enter a language from translate:")), to_lang=str(input("enter a language to translate")))
        translate = translate.translate(input("enter a word:"))
        engine.say(translate)
        engine.runAndWait()
        print(translate)
        command = str(select())


    else:

        engine.say(" enter valid option")
        engine.runAndWait()
        command = str(select())




else:

    engine.say("thanks for using our application")
    engine.say("see you again")
    engine.runAndWait()
