from tkinter import *
import pyowm

def destroy():
    screen1.destroy()

def weather():
    global screen1
    getcity=city.get()
    screen1=Toplevel(screen)
    screen1.title("Realtime Weather")
    screen1.geometry("250x150")

    get = pyowm.OWM('be9adf1beea879e4a05ec1aa8966aef4')
    weather = get.weather_at_place(getcity)
    getweather = weather.get_weather()
    wind = getweather.get_wind('miles_hour')['speed']
    status = getweather.get_status()
    getstring = str(wind)


    Label(screen1,text="This is The Realtime Forecast from "+getcity+" City").pack()
    Label(screen1, text="The Weather Now is "+status).pack()
    Label(screen1, text="The Wind Speed is "+getstring+" MPH").pack()
    Button(screen1, text="OK", command=destroy).pack()
    #print(f'The wind speed is {wind} MPH')
    #print(f'The weather now in {city} City is {status}')



def MainScreen():
    global screen
    screen = Tk()
    screen.geometry("250x200")
    screen.title("Realtime Weather Forecast")
    global city
    city = StringVar()
    Label(text="Please input city", bg="yellow", font="Arial").pack()
    city_entry = Entry(screen, textvariable=city)
    city_entry.pack()

    Button(screen, text="OK", width="10", height="1", command=weather).pack()
    screen.mainloop()

MainScreen()