import requests
from PIL import Image
from io import BytesIO

def displayCRW(year, month, day):
    #For cases where single digit numbers exist for month and day:
    month_f = str(month).zfill(2)
    day_f = str(day).zfill(2)

    #Opening the URL:
    url = f"https://coralreefwatch.noaa.gov/data/5km/v3.1/image/daily/ssta/gif/{year}/coraltemp5km_ssta_{year}{month_f}{day_f}_large.gif"
    response = requests.get(url)

    if(response.status_code == 200): #If image exists...
        #Display Image:
        image = Image.open(BytesIO(response.content))
        image.show()
    else:
        print("Error 404: The image either does not exist or is yet to be created.")

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

displayCRW(year, month, day)