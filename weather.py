from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk


root = tk.Tk()
root.geometry("890x470+320+150")

def getWeather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="geiapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()

    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    #weather
    api="https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=49ae2e9c5214489d95f13b5e43087667"
    json_data=requests.get(api).json()

    #current
    temp=json_data['current']['temp']
    humidity=json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']
    
    t.config(text = (temp, "°C"))
    h.config(text = (humidity, "%"))
    p.config(text = (pressure, "hPa"))
    w.config(text = (wind, "m/s"))
    d.config(text = description)

    #fisrt cell
    
    firstdayimage = json_data['daily'][0]['weather'][0]['icon']
    
    photo1 = ImageTk.PhotoImage(file=f"weather\icon\{firstdayimage}.png")
    firstimage.config(image = photo1)
    firstimage.image = photo1
  
    tempday1 = json_data['daily'][0]['temp']['day']
    tempnight1 = json_data['daily'][0]['temp']['night']

    day1temp.config(text=f"Day:{tempday1}\n Night:{tempnight1}")

    #second cell
    seconddayimage = json_data['daily'][1]['weather'][0]['icon']
    
    img = (Image.open(f"weather\icon\{seconddayimage}.png"))
    resized_image = img.resize((50, 50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image = photo2

    tempday2 = json_data['daily'][1]['temp']['day']
    tempnight2 = json_data['daily'][1]['temp']['night']

    day2temp.config(text=f"Day:{tempday2}\n Night:{tempnight2}")


    #third cell
    thirddayimage = json_data['daily'][2]['weather'][0]['icon']
    
    img = (Image.open(f"weather\icon\{thirddayimage}.png"))
    resized_image = img.resize((50, 50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image = photo3

    tempday3 = json_data['daily'][2]['temp']['day']
    tempnight3 = json_data['daily'][2]['temp']['night']

    day3temp.config(text=f"Day:{tempday3}\n Night:{tempnight3}")

    #fourth cell
    fourthdayimage = json_data['daily'][3]['weather'][0]['icon']
    
    img = (Image.open(f"weather\icon\{fourthdayimage}.png"))
    resized_image = img.resize((50, 50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image = photo4

    tempday4 = json_data['daily'][3]['temp']['day']
    tempnight4 = json_data['daily'][3]['temp']['night']

    day4temp.config(text=f"Day:{tempday4}\n Night:{tempnight4}")

    #fifth cell
    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']
   
    img = (Image.open(f"weather\icon\{fifthdayimage}.png"))
    resized_image = img.resize((50, 50))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image = photo5

    tempday5 = json_data['daily'][4]['temp']['day']
    tempnight5 = json_data['daily'][4]['temp']['night']

    day5temp.config(text=f"Day:{tempday5}\n Night:{tempnight5}")

    # sixth cell
    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']

    img = (Image.open(f"weather\icon\{sixthdayimage}.png"))
    resized_image = img.resize((50, 50))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image = photo6

    tempday6 = json_data['daily'][5]['temp']['day']
    tempnight6 = json_data['daily'][5]['temp']['night']

    day6temp.config(text=f"Day:{tempday6}\n Night:{tempnight6}")

    #seventh cell
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']

    img = (Image.open(f"weather\icon\{seventhdayimage}.png"))
    resized_image = img.resize((50, 50))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image = photo7
    
    tempday7 = json_data['daily'][6]['temp']['day']
    tempnight7 = json_data['daily'][6]['temp']['night']

    day7temp.config(text=f"Day:{tempday7}\n Night:{tempnight7}")

    #days 

    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first + timedelta(days = 1)
    day2.config(text=second.strftime("%A"))

    third = first + timedelta(days = 2)
    day3.config(text=third.strftime("%A"))

    fourth = first + timedelta(days = 3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first + timedelta(days = 4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first + timedelta(days = 5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first + timedelta(days = 6)
    day7.config(text=seventh.strftime("%A"))




#backgr
bgimg= tk.PhotoImage(file = "weather\image\gr3.png")
limg= Label(root, i=bgimg)
limg.pack()
root.resizable(False,FALSE)

#icon
image_icon = PhotoImage(file="weather\image\logo.png")
root.iconphoto(False, image_icon)

Round_box=PhotoImage(file="weather\image\gr6.png")
Label(root,image=Round_box).place(x=70,y=86)
#label
label1=Label(root,text="Temperature",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=90,y=100)

label2=Label(root,text="Humidity",font=('Helvetica',11),fg="white",bg="#203243")
label2.place(x=90,y=138)

label3=Label(root,text="Pressure",font=('Helvetica',11),fg="white",bg="#203243")
label3.place(x=90,y=176)

label4=Label(root,text="Wind Speed",font=('Helvetica',11),fg="white",bg="#203243")
label4.place(x=90,y=214)

label5=Label(root,text="Description",font=('Helvetica',11),fg="white",bg="#203243")
label5.place(x=90,y=252)

# Search
Search_img=PhotoImage(file="weather\image\gr10.png")
Label(root,image=Search_img).place(x=330,y=180)

textfield=tk.Entry(root,justify='center',width=20,font=('poppins',25,'bold'),bg="#131c24",border=0,fg="white")
textfield.place(x=360,y=193)
textfield.focus()

Search_icon=PhotoImage(file="weather\image\srch.png")
myimg_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#131c24",command=getWeather)
myimg_icon.place(x=735,y=190)
#bottombox
frame=Frame(root,width=900,height=180,bg="#0d0e0f")
frame.place(x=0,y=320)
#bottom boxers
firstbox=PhotoImage(file="weather\image\c12.png")
secondbox=PhotoImage(file="weather\image\c13.png")

Label(frame,image=firstbox).place(x=30,y=20)
Label(frame,image=secondbox).place(x=320,y=9)
Label(frame,image=secondbox).place(x=416,y=9)
Label(frame,image=secondbox).place(x=512,y=9)
Label(frame,image=secondbox).place(x=608,y=9)
Label(frame,image=secondbox).place(x=704,y=9)
Label(frame,image=secondbox).place(x=800,y=9)

#clock
clock=Label(root,font=("Helvetica",30,'bold'),fg="white",bg="#406385")
clock.place(x=80,y=20)
#timezone
timezone=Label(root,font=("Helvetica",20,'bold'),fg="white",bg="#406385")
timezone.place(x=690,y=50)

long_lat=Label(root,font=("Helvetica",10,'bold'),fg="white",bg="#406385")
long_lat.place(x=710,y=80)

#thpwd
t = Label(root, font = ("Helvetica", 11), fg = "white", bg = "#203243")
t.place(x = 190,y = 100)
h = Label(root, font = ("Helvetica", 11), fg = "white", bg = "#203243")
h.place(x = 190,y = 138)
p = Label(root, font = ("Helvetica", 11), fg = "white", bg = "#203243")
p.place(x = 190,y = 176)
w = Label(root, font = ("Helvetica", 11), fg = "white", bg = "#203243")
w.place(x = 190,y = 214)
d = Label(root, font = ("Helvetica", 11), fg = "white", bg = "#203243")
d.place(x = 190,y = 252)

#fisrt cell
firstframe = Frame(root, width = 265, heigh = 110, bg = "#282829")
firstframe.place(x = 32, y = 342)

day1 = Label(firstframe, font = "arial 20", bg = "#282829", fg = "#fff")
day1.place(x = 115, y = 5)

firstimage = Label(firstframe, bg = "#282829")
firstimage.place(x = 1, y = 15)

day1temp = Label(firstframe, bg = "#282829", fg = "#57adff", font = "arial 15 bold")
day1temp.place(x = 100, y = 50)

#second cell
secondframe = Frame(root, width = 80, heigh = 132, bg = "#282829")
secondframe.place(x = 322, y = 331) 

day2 = Label(secondframe, bg = "#282829", fg = "#fff")
day2.place(x = 10, y = 5)

secondimage = Label(secondframe, bg = "#282829")
secondimage.place(x = 7, y = 20)  

day2temp = Label(secondframe, bg = "#282829", fg = "#fff")
day2temp.place(x = 2, y = 70)

#third cell
thirdframe = Frame(root, width = 80, heigh = 132, bg = "#282829")
thirdframe.place(x = 418, y = 331)

day3 = Label(thirdframe, bg = "#282829", fg = "#fff")
day3.place(x = 10, y = 5)

thirdimage = Label(thirdframe, bg = "#282829")
thirdimage.place(x = 7, y = 20)  

day3temp = Label(thirdframe, bg = "#282829", fg = "#fff")
day3temp.place(x = 2, y = 70)

#fourth cell
fourthframe = Frame(root, width = 80, heigh = 132, bg = "#282829")
fourthframe.place(x = 514, y = 331)

day4 = Label(fourthframe, bg = "#282829", fg = "#fff")
day4.place(x = 10, y = 5)

fourthimage = Label(fourthframe, bg = "#282829")
fourthimage.place(x = 7, y = 20)  

day4temp = Label(fourthframe, bg = "#282829", fg = "#fff")
day4temp.place(x = 2, y = 70)

#fifth cell
fifthframe = Frame(root, width = 80, heigh = 132, bg = "#282829")
fifthframe.place(x = 610, y = 331)

day5 = Label(fifthframe, bg = "#282829", fg = "#fff")
day5.place(x = 10, y = 5)

fifthimage = Label(fifthframe, bg = "#282829")
fifthimage.place(x = 7, y = 20)  

day5temp = Label(fifthframe, bg = "#282829", fg = "#fff")
day5temp.place(x = 2, y = 70)


#sixth cell
sixthframe = Frame(root, width = 80, heigh = 132, bg = "#282829")
sixthframe.place(x = 706, y = 331)

day6 = Label(sixthframe, bg = "#282829", fg = "#fff")
day6.place(x = 10, y = 5)

sixthimage = Label(sixthframe, bg = "#282829")
sixthimage.place(x = 7, y = 20)  

day6temp = Label(sixthframe, bg = "#282829", fg = "#fff")
day6temp.place(x = 2, y = 70)

#seventh cell
seventhframe = Frame(root, width = 80, heigh = 132, bg = "#282829")
seventhframe.place(x = 802, y = 331)

day7 = Label(seventhframe, bg = "#282829", fg = "#fff")
day7.place(x = 10, y = 5)

seventhimage = Label(seventhframe, bg = "#282829")
seventhimage.place(x = 7, y = 20)  

day7temp = Label(seventhframe, bg = "#282829", fg = "#fff")
day7temp.place(x = 2, y = 70)

#label
Round_box2=PhotoImage(file="weather\image\gr12.png")
Label(root,image=Round_box2).place(x=720,y=10)
root.mainloop()