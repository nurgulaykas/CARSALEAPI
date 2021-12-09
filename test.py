import requests


data = requests.get('http://127.0.0.1:5000/api/search',json={
    "renk" : "",
    "marka" : "",
    "vites" : "",
    "yil_max" : 2022,
    "yil_min" : 2021
}
)
print(data)