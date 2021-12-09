from flask import Flask, request, jsonify
app = Flask(__name__)
import requests
from bs4 import BeautifulSoup

@app.route('/api/search', methods=['GET'])
def search():
    params = request.json
    weblink="https://www.cars.com/shopping/results/?page_size=51"\
    "&exterior_color_slugs[]="+params['renk']\
    +"&makes[]="+params['marka']\
    +"&transmission_slugs[]="+params['vites']\
    +"&year_max="+str(params['yil_max'])+"&year_min="+str(params['yil_min'])

    response= requests.get(weblink)
    soup= BeautifulSoup(response.content,"html.parser")


    data= soup.find_all("div",{"class":"vehicle-card"})
    #cars=(data[1].contents)[len(data[0].contents)-4]
    cars=soup.find_all("a",{"class":"vehicle-card-visited-tracking-link"})
    item = {}
    list= []
    for car in cars:
        #print(car.get('href'))
        carlink ="https://www.cars.com"+(car.get('href'))
        response = requests.get(carlink)
        soup = BeautifulSoup(response.content, "html.parser")

        ilanbaslik = soup.find("h1", {"class": "listing-title"}).text
        fiyat = soup.find("span", {"class": "primary-price"}).text
        resmiurl = carlink
        marka = ilanbaslik[5:]
        modelyili=ilanbaslik[0:5]
        disrenkVites = soup.find_all("dd")
        disrenk=(disrenkVites[0].contents)[len(disrenkVites[0].contents)-1]
        vites=(disrenkVites[5].contents)[len(disrenkVites[5].contents)-1]
        #print(modelyili)
        #print(len(cars))

        # item['ilanbaslik'] = ilanbaslik
        # item['fiyat'] = fiyat
        # item['aracresmiurl'] = resmiurl
        # item['marka'] = marka
        # item['modelyili'] = modelyili
        # item['disrenk'] = disrenk
        # item['vites'] = vites
        list.append({'ilanbaslik' : ilanbaslik, 'fiyat' : fiyat, 'aracresmiurl' : resmiurl,'marka' : marka,'modelyili' : modelyili ,'disrenk' : disrenk, 'vites' : vites })
    return jsonify(list)

if __name__ == '_main_':
    app.run(host= 'localhost',debug=True)