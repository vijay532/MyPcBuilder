from flask import Flask, render_template
import subprocess
import requests
import xml.etree.ElementTree as ET
from lxml import etree
import json
import xmltodict
import time
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['CACHE_TYPE'] = "null"
app.config['SECRET_KEY'] = "nirvana"
socketio = SocketIO(app)

config = {
    'access_key': 'AKIAIYXQISLBGBBINRXA',
    'secret_key': '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',
    'associate_tag': 'buildmypc03-20',
    'locale': 'us'
}
# api = amazonproduct.API(cfg=config)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/choose-monitor')
def chooseMonitor():
    
    
    global budget_total
    budget_total = 100000*100
    global budget_monitor
    budget_monitor = 0.2*budget_total
    global budget_cpu
    budget_cpu = 0.65*budget_total
    global budget_mouse
    budget_mouse = 0.05*budget_total
    global budget_keyboard
    budget_keyboard = 0.1*budget_total
    print("Break the walls")
    print(budget_monitor,budget_cpu,budget_mouse,budget_keyboard)


    '''Monitors'''

    proc = subprocess.Popen("php url.php "+str(budget_monitor)+" Gaming Monitors", shell=True, stdout=subprocess.PIPE)
    script_response = proc.stdout.read()
    print(script_response)

    r = requests.get(script_response)
    while r.status_code != 200:
        time.sleep(10)
        r = requests.get(script_response)
    print(r.status_code)
    with open('content.xml', 'wb') as f:
        f.write(r.content)

    
    jsonString = json.dumps(xmltodict.parse(r.content), indent=4)
    with open("output.json", 'w') as f:
        f.write(jsonString)
    j = json.loads(jsonString)
    r = j["ItemSearchResponse"]["Items"]["Item"]
    # print(j["ItemSearchResponse"]["Items"]["Item"][0]["ASIN"])

    # for item in r:
    #     print(item["ASIN"])    

    return render_template("choose-monitor.html",items=r)


@app.route('/choose-cpu')
def chooseCPU():
    proc = subprocess.Popen("php url.php "+str(budget_cpu)+" Gaming CPU", shell=True, stdout=subprocess.PIPE)
    script_response = proc.stdout.read()
    print(script_response)

    r = requests.get(script_response)
    while r.status_code != 200:
        time.sleep(10)
        r = requests.get(script_response)
    print(r.status_code)
    with open('content.xml', 'wb') as f:
        f.write(r.content)

    
    jsonString = json.dumps(xmltodict.parse(r.content), indent=4)
    with open("output.json", 'w') as f:
        f.write(jsonString)
    j = json.loads(jsonString)
    r = j["ItemSearchResponse"]["Items"]["Item"]
    # print(j["ItemSearchResponse"]["Items"]["Item"][0]["ASIN"])

    # for item in r:
    #     print(item["ASIN"])    

    return render_template("choose-cpu.html",items=r)


@app.route('/choose-mouse')
def chooseMouse():
    proc = subprocess.Popen("php url.php "+str(budget_mouse)+" Gaming Mouse", shell=True, stdout=subprocess.PIPE)
    script_response = proc.stdout.read()
    print(script_response)

    r = requests.get(script_response)
    while r.status_code != 200:
        time.sleep(10)
        r = requests.get(script_response)
    print(r.status_code)
    with open('content.xml', 'wb') as f:
        f.write(r.content)

    
    jsonString = json.dumps(xmltodict.parse(r.content), indent=4)
    with open("output.json", 'w') as f:
        f.write(jsonString)
    j = json.loads(jsonString)
    r = j["ItemSearchResponse"]["Items"]["Item"]
    # print(j["ItemSearchResponse"]["Items"]["Item"][0]["ASIN"])

    # for item in r:
    #     print(item["ASIN"])    

    return render_template("choose-mouse.html",items=r)


@app.route('/choose-keyboard')
def chooseKeyboard():
    proc = subprocess.Popen("php url.php "+str(budget_keyboard)+" Gaming Keyboard", shell=True, stdout=subprocess.PIPE)
    script_response = proc.stdout.read()
    print(script_response)

    r = requests.get(script_response)
    while r.status_code != 200:
        time.sleep(10)
        r = requests.get(script_response)
    print(r.status_code)
    with open('content.xml', 'wb') as f:
        f.write(r.content)

    
    jsonString = json.dumps(xmltodict.parse(r.content), indent=4)
    with open("output.json", 'w') as f:
        f.write(jsonString)
    j = json.loads(jsonString)
    r = j["ItemSearchResponse"]["Items"]["Item"]
    # print(j["ItemSearchResponse"]["Items"]["Item"][0]["ASIN"])

    # for item in r:
    #     print(item["ASIN"])    

    return render_template("choose-keyboard.html",items=r)

final_list = []

@socketio.on('chose')
def cart(asin):
    print("And the answer is ------------------------------>>>"+str(asin))
    final_list.append(asin)
    print(final_list)


@app.route('/checkout')
def checkout():
    print(final_list)

    
    '''Individual request for all the components and get their json'''
    proc = subprocess.Popen("php ItemLookup.php "+str(final_list[0]), shell=True, stdout=subprocess.PIPE)
    script_response = proc.stdout.read()
    print(script_response)
    
    r = requests.get(script_response)
    while r.status_code != 200:
        time.sleep(10)
        r = requests.get(script_response)
    print(r.status_code)
    with open('content.xml', 'wb') as f:
        f.write(r.content)

    
    jsonString = json.dumps(xmltodict.parse(r.content), indent=4)
    with open("item.json", 'w') as f:
        f.write(jsonString)

    # Combine all the 4 jsons and send it
    jsonString = json.dumps(xmltodict.parse(r.content), indent=4)
    with open("item.json", 'w') as f:
        f.write(jsonString)
    j = json.loads(jsonString)
    monitor = j["ItemLookupResponse"]["Items"]["Item"]


    '''Individual request for all the components and get their json'''
    proc = subprocess.Popen("php ItemLookup.php "+str(final_list[1]), shell=True, stdout=subprocess.PIPE)
    script_response = proc.stdout.read()
    print(script_response)
    
    r = requests.get(script_response)
    while r.status_code != 200:
        time.sleep(10)
        r = requests.get(script_response)
    print(r.status_code)
    with open('content.xml', 'wb') as f:
        f.write(r.content)

    
    jsonString = json.dumps(xmltodict.parse(r.content), indent=4)
    with open("item.json", 'w') as f:
        f.write(jsonString)

    # Combine all the 4 jsons and send it
    jsonString = json.dumps(xmltodict.parse(r.content), indent=4)
    with open("item.json", 'w') as f:
        f.write(jsonString)
    j = json.loads(jsonString)
    cpu = j["ItemLookupResponse"]["Items"]["Item"]



    '''Individual request for all the components and get their json'''
    proc = subprocess.Popen("php ItemLookup.php "+str(final_list[2]), shell=True, stdout=subprocess.PIPE)
    script_response = proc.stdout.read()
    print(script_response)
    
    r = requests.get(script_response)
    while r.status_code != 200:
        time.sleep(10)
        r = requests.get(script_response)
    print(r.status_code)
    with open('content.xml', 'wb') as f:
        f.write(r.content)

    
    jsonString = json.dumps(xmltodict.parse(r.content), indent=4)
    with open("item.json", 'w') as f:
        f.write(jsonString)

    # Combine all the 4 jsons and send it
    jsonString = json.dumps(xmltodict.parse(r.content), indent=4)
    with open("item.json", 'w') as f:
        f.write(jsonString)
    j = json.loads(jsonString)
    mouse = j["ItemLookupResponse"]["Items"]["Item"]


    '''Individual request for all the components and get their json'''
    proc = subprocess.Popen("php ItemLookup.php "+str(final_list[3]), shell=True, stdout=subprocess.PIPE)
    script_response = proc.stdout.read()
    print(script_response)
    
    r = requests.get(script_response)
    while r.status_code != 200:
        time.sleep(10)
        r = requests.get(script_response)
    print(r.status_code)
    with open('content.xml', 'wb') as f:
        f.write(r.content)

    
    jsonString = json.dumps(xmltodict.parse(r.content), indent=4)
    with open("item.json", 'w') as f:
        f.write(jsonString)

    # Combine all the 4 jsons and send it
    jsonString = json.dumps(xmltodict.parse(r.content), indent=4)
    with open("item.json", 'w') as f:
        f.write(jsonString)
    j = json.loads(jsonString)
    keyboard = j["ItemLookupResponse"]["Items"]["Item"]

    return render_template("checkout.html",monitor=monitor, cpu=cpu, mouse=mouse, keyboard=keyboard)


if __name__ == "__main__":
    socketio.run(app, debug=True)