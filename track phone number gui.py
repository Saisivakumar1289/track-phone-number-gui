from tkinter import *
import phonenumbers
from phonenumbers import carrier,geocoder,timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root=Tk()
root.title("Phone Number Tracker")
root.geometry("365x784+400+100")
root.resizable(False,False)

def track():
    try:

        enter_number=entry.get()
        number=phonenumbers.parse(enter_number)

        #country
        locate=geocoder.description_for_number(number,"en")
        country.config(text=locate)

        #operator
        operator=carrier.name_for_number(number,"en")
        sim.config(text=operator)

        #phone timezone
        time=timezone.time_zones_for_number(number)
        zone.config(text=time)

        #longitude and latitude
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(locate)
        lng=location.longitude
        lat=location.latitude
        longitude.config(text=lng)
        latitude.config(text=lat)

        #time showing in phone
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M:%p")
        clock.config(text=current_time)
    except:
        print("Some error occured while running the program...once,check internet connection")
    finally:
        print("Successfully executed")        

#logo
logo = PhotoImage(file="tracklogo.png")
Label(root,image=logo).place(x=240,y=70)
Heading=Label(root,text="Track Number",font=("arial",15,"bold"))
Heading.place(x=70,y=110)

#entry
Entry_back=PhotoImage(file="search.png")
Label(root,image=Entry_back).place(x=20,y=220)

entry=StringVar()
enter_number=Entry(root,textvariable=entry,width=17,bd=0,font=("arial",20),justify="center")
enter_number.place(x=70,y=250)

#button
search_image=PhotoImage(file="search button.png")
search=Button(image=search_image,borderwidth=0,cursor="hand2",bd=0,font=("arial",16),justify="center",command=track)
search.place(x=35,y=330)

#bottom box
Box=PhotoImage(file="bottom.png")
Label(root,image=Box).place(x=5,y=390)

#country name

country=Label(root,text="country:",bg="#57adff",font=("arial",10,"bold"))
country.place(x=70,y=450)

#sim or Operator name

sim=Label(root,text="sim:",bg="#57adff",font=("arial",10,"bold"))
sim.place(x=200,y=450)

#timeZone

zone=Label(root,text="zone:",bg="#57adff",font=("arial",10,"bold"))
zone.place(x=70,y=500)

#clock

clock=Label(root,text="clock:",bg="#57adff",font=("arial",10,"bold"))
clock.place(x=200,y=500)

#longitude 

longitude=Label(root,text="longitude:",bg="#57adff",font=("arial",10,"bold"))
longitude.place(x=70,y=550)

#latitude

latitude=Label(root,text="latitude:",bg="#57adff",font=("arial",10,"bold"))
latitude.place(x=200,y=550)


root.mainloop()