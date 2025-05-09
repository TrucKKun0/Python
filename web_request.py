import requests

playload = {
    'foo1':"bar1",
    'foo2':"bar2",
}
# r = requests.get("https://imgs.xkcd.com/s/temperature.png")
# with open("temperature.png", "wb") as f:
#     f.write(r.content)
# r= requests.get("https://postman-echo.com/get", params=playload)
# res= requests.get("https://postman-echo.com/post", data=playload)
# r_dict = r.json()
# print(r_dict)
# #print(r.text)
# print(res.url)
# print(res.text)

#Basic Authentication
# r = requests.get("https://postman-echo.com/basic-auth", auth=('postman', 'password'))
# print(r.status_code)
# print(r.text)

#Delay response
r = requests.get("https://postman-echo.com/delay/3",timeout=5)
print(r.status_code)