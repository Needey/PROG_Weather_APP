import tkinter
from tkinter.constants import *
from tkinter import  PhotoImage, StringVar, IntVar, Tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import urllib3
from io import BytesIO
from model.weather import Weather


class View(tkinter.Tk):

    def __init__(self, controller):
        self.weather = Weather()
        super().__init__()
        self.geometry("1000x600")

        self.controller = controller
        self.bind('<Return>', self.controller.handleButtonSearch)

        #---- Variables ----
        self.varSearch = StringVar()
        self.varTemp = StringVar()
        self.varLocation = StringVar()
        self.varCondition = StringVar()
        self.varFeelsLike = StringVar()
        self.varWindSpeed = StringVar()
        self.varWindDir = StringVar()
        self.varUnits = IntVar()
        self.varIcon = StringVar()

        pre_url=self.weather.getWeather().weather_icon_path
        self.varIcon 
        URL= 'http:'+ pre_url
        self.http = urllib3.PoolManager()
        self.r = self.http.request('GET',URL) 
        self.htmlSource = self.r.data

        self.im = Image.open(BytesIO(self.htmlSource))
        self.url_meteo = ImageTk.PhotoImage(self.im)

        #---- Frames ----
        self.mainframe = Frame(self)
        self.mainframe.pack()
        self._createFrameSearchBar()
        self._createFrameInfo()
        self._createFrameDetails()
        self._createFrameControls()

    
    def _createFrameSearchBar(self):
        self.frameSearchBar = Frame(self.mainframe)

        self.comboSearch = Combobox(self.frameSearchBar, textvariable=self.varSearch)
        buttonSearch = Button(self.frameSearchBar, text="Search", command=self.controller.handleButtonSearch)

        self.comboSearch.pack(padx=10, side=LEFT)
        buttonSearch.pack(side=RIGHT)
        self.frameSearchBar.pack()


    def _createFrameInfo(self):
        self.frameInfo = Frame(self.mainframe)

        labelTemp = Label(self.frameInfo, textvariable = self.varTemp)
        labelLocation = Label(self.frameInfo, textvariable = self.varLocation)
        labelIcon = Label(self.frameInfo, image = self.url_meteo)
        

        labelTemp.pack(pady=5)
        labelLocation.pack(pady=5)
        labelIcon.pack(pady=5)
        self.frameInfo.pack()

    def _createFrameDetails(self):
        self.frameDetails = Frame(self.mainframe)

        labelConditionLeft = Label(self.frameDetails, text='condition:')
        labelFeelsLikeLeft = Label(self.frameDetails, text='Temp ressentie:')
        labelWindSpeedLeft = Label(self.frameDetails, text='Vent:')
        labelWindDirLeft = Label(self.frameDetails, text='direction du vent:')

        labelConditionRight = Label(self.frameDetails, textvariable=self.varCondition)
        labelFeelsLikeRight = Label(self.frameDetails, textvariable=self.varFeelsLike)
        labelWindSpeedRight = Label(self.frameDetails, textvariable=self.varWindSpeed)
        labelWindDirRight = Label(self.frameDetails, textvariable=self.varWindDir)

        labelConditionLeft.grid(row=0, column=0, pady=5, sticky=W)
        labelConditionRight.grid(row=0, column=1, pady=5, sticky=E)
        labelFeelsLikeLeft.grid(row=1, column=0, pady=5, sticky=W)
        labelFeelsLikeRight.grid(row=1, column=1, pady=5, sticky=E)
        labelWindSpeedLeft.grid(row=2, column=0, pady=5, sticky=W)
        labelWindSpeedRight.grid(row=2, column=1, pady=5, sticky=E)
        labelWindDirLeft.grid(row=3, column=0, pady=5, sticky=W)
        labelWindDirRight.grid(row=3, column=1, pady=5, sticky=E)
        self.frameDetails.pack()


    def _createFrameControls(self):
        self.frameControls = Frame(self.mainframe)

        radioC = Radiobutton(self.frameControls, text='Celcius', variable=self.varUnits, value=2, command=self.controller.update)
        radioF = Radiobutton(self.frameControls, text='Fahrenheit', variable=self.varUnits, value=1, command=self.controller.update)
        

        radioC.invoke()

        radioF.pack(side=RIGHT, padx=7.5, pady=5)
        radioC.pack(side=LEFT, padx=7.5, pady=5)
        self.frameControls.pack()


    def main(self):
        self.mainloop()


      