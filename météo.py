from datetime import datetime
from telnetlib import NAOL
from time import time
from turtle import clear
from unicodedata import name
from PyQt5 import QtCore, QtGui, QtWidgets
from interfacee import Ui_Dialog
import requests
from PyQt5.QtCore import QTime, QTimer



    
    



   




import sys
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

api_key = "b792d12459899e636fef072d79bed0e8"



def afi():

   

   name = ui.lineEdit_4.text()
   url = f'https://api.openweathermap.org/data/2.5/weather?q={name}&appid={api_key}'
   

   req = requests.get(url).json()

   if req["cod"] != "404":
    main = req["main"]
    temperature = round(main["temp"] - 273.15,2 )
    humidity = main["humidity"]
    weather = req["weather"]
    weather_descrption = weather[0]["description"]
    ui.lineEdit.setText(f'{weather_descrption}')
    ui.lineEdit.text()

    ui.lineEdit_2.setText(f'{temperature}')
    ui.lineEdit_2.text()

    ui.lineEdit_3.setText(f'{humidity}')
    ui.lineEdit_3.text()
   else :
    ui.lineEdit_4.clear()
    ui.lineEdit_4.setPlaceholderText('cite note fond')



#timer = QTimer()
#ui.timer.timeout.connect(ui.lcdNumber)

ui.lcdNumber.startTimer(1000)

time = datetime.now()
formatted_time = time.strftime("%H:%M:%S %p")
ui.lcdNumber.setDigitCount(12)
ui.lcdNumber.display(formatted_time)





tex = ui.pushButton.clicked.connect(afi)

#url = f'https://api.openweathermap.org/data/2.5/weather?q={ag}&appid={api_key}'
#req = requests.get(url).json()



#text = ui.lineEdit_4.text()


#if req["cod"] != "404":
    #main = req["main"]
    #temperature = round(main["temp"] - 273.15,2 )
    #humidity = main["humidity"]
    #weather = req["weather"]
    #weather_descrption = weather[0]["description"]




sys.exit(app.exec_())
