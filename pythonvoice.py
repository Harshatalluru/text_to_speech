import pyttsx3
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from translate import Translator


def talk(talk):
    engine.say(talk)
    return talk
def run():
    run = engine.runAndWait()
    return  run  


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
talk("WELCOME to audisankara college of engineering in gudur")
talk("enter a student name:")
run()

user = input("enter a student name:")
gm = (user," enter a year of studying")
talk(gm)
run()
year = int(input("enter a year of studying:"))
present = 0


def options():
    talk("please select top of  the list")
    run()
    print(user,"welcome to hp college")
    print("enter 'cls' (class) 'tp'(topic) 'a'(adentance) 'data'(details) 'internet'(browser) 'trans'(translator) or 'q'(quit)")

def select():
    transaction = str(input("what you like to do? :"))
    return transaction

options()
command = str(select())

while command != 'q':
    if command == 'cls':
        talk("hey you select class")
        run()
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

            talk(" invalid selected year")
            run()
        command = str(select())

    elif command == 'tp':
        talk("hey you select topics")
        run()
        if year == 2:
            print("1.co,2.se,3.java,4.database")
        elif year == 3:
            print("python,data analysis")
        elif year == 4:
            print("projects")
        else:

            talk(" there no topics selected year")
            run()
        command = str(select())
    elif command == 'a':
        talk("hey you select attendence")
        run()
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
        talk("hey you select details")
        run()

        print("STUDENT NAME:",user)
        print("YEAR",year)
        if present == 0:
            print("attendance in this month:""data not  entered")
        else:
             print("attendance in this month",present,"days")
        command = str(select())

    elif command == 'internet':
        talk("hello you are entered into internet")
        run()



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
        talk("you are entered into translation")
        run()

        translate = Translator(from_lang=str(input("enter a language from translate:")), to_lang=str(input("enter a language to translate")))
        translate = translate.translate(input("enter a word:"))
        talk(translate)
        run()
        print(translate)
        command = str(select())


    else:

        talk(" enter valid option")
        run()
        command = str(select())




else:

    talk("thanks for using our application")
    talk("see you again")
    run()
