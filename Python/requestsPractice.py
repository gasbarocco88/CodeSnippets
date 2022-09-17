import requests

url = "https://httpbin.org/post"
payload = {
    "name": "Rocco",
    "age": 34,
    "hobbies&interests": ["videogames", "computers", "football", "animals"],
    "abc": True,
}
r = requests.post(url, data=payload)
print("STATUS CODE: ", r.status_code)
print("HEADERS: ", r.headers)
print("URL: ", r.url)

print("")

url2 = "https://httpbin.org/get"
r2 = requests.get(url2, params=payload)
print("STATUS CODE: ", r2.status_code)
print("HEADERS: ", r2.headers)
print("URL: ", r2.url)
print("TEXT: ", r2.text)
