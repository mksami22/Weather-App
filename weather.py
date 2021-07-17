import tkinter as tk
import requests 
import time

# Function to get information from API
def getWeather(canvas):
    city = textField.get()
    url = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=b9072ab31cf8ca0c9e84dc03c0ff7d68"
    jsonData = requests.get(url).json()
    condition = jsonData['weather'][0]['main']
    # Convert temprature to Celcius
    temprature = int(jsonData['main']['temp'] - 273.15)
    minTemprature = int(jsonData['main']['temp_min'] - 273.15)
    maxTemprature = int(jsonData['main']['temp_max'] - 273.15)
    pressure = jsonData['main']['pressure']
    humidity = jsonData['main']['humidity']
    windSpeed = jsonData['wind']['speed']
    # Time provided by API is in seconds
    sunrise = time.strftime("%H:%M:%S", time.gmtime(jsonData['sys']['sunrise'] - 21600))
    sunset = time.strftime("%H:%M:%S", time.gmtime(jsonData['sys']['sunset'] - 2100))
    finalInfo = condition + "\n" + str(temprature) + "ºC"
    finalData = "\n" + "Max Temprature: " + str(maxTemprature) + "ºC" + "\n" + "Min Temprature: " + str(minTemprature) + "ºC" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "/n" + "Windspeed: " + str(windSpeed) + "\n" + "Sunrise: " + str(sunrise) + "Sunset: " + str(sunset)
    label1.config(text = finalInfo)
    label2.config(text = finalData)
canvas = tk.Tk()
canvas.geometry("500x600")
canvas.title("Weather App")

font1 = ("poppins", 15, "bold")
font2 = ("poppins", 35, "bold")

# Take single line entry from  users
textField = tk.Entry(canvas, justify = 'center', font = font2)
textField.pack(pady = 20)
# Focussing the text field so that user can type in without moving the cursor after opening the application
textField.focus()
textField.bind('<Return>', getWeather)

# Create labels to show the data
# Labels are boxes where you can place text or images
label1 = tk.Label(canvas, font = font2)
label1.pack()
label2 = tk.Label(canvas, font = font1)
label2.pack()

canvas .mainloop()
