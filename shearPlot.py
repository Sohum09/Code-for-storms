import requests
from PIL import Image
from io import BytesIO

basin = input("Enter Basin: ")
url = ""
if basin == "westpac":
    url += "https://tropic.ssec.wisc.edu/real-time/westpac/winds/wgmsshr.GIF"
elif basin == "eastpac":
    url += "https://tropic.ssec.wisc.edu/real-time/eastpac/winds/wg9shr.GIF"
elif basin == "seastpac":
    url += "https://tropic.ssec.wisc.edu/real-time/seastpac/winds/wg10sshr.GIF"
elif basin == "atlantic":
    url += "https://tropic.ssec.wisc.edu/real-time/atlantic/winds/wg8shr.GIF"
elif basin == "europe":
    url += "https://tropic.ssec.wisc.edu/real-time/europe/winds/wm7shr.GIF"
elif basin == "indian":
    url += "https://tropic.ssec.wisc.edu/real-time/indian/winds/wm5shr.GIF"
elif basin == "austwest":
    url += "https://tropic.ssec.wisc.edu/real-time/austwest/winds/wgmsshr.GIF"
elif basin == "austeast":
    url += "https://tropic.ssec.wisc.edu/real-time/austeast/winds/wgmsshr.GIF"
else:
    print("The given basin is not valid! Valid basins are [westpac, eastpac, seastpac, atlantic, europe, indian, austwest, austeast]")


response = requests.get(url)

if(response.status_code == 200): #If image exists...
        #Display Image:
        image = Image.open(BytesIO(response.content))
        image.show()
else:
    print("Error 404: The image either does not exist or is yet to be created.")