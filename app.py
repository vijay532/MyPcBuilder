from flask import Flask, render_template
import subprocess
import requests
import xml.etree.ElementTree as ET
from lxml import etree
import json
import xmltodict
#import jsonify

app = Flask(__name__)

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

@app.route('/choose-pc')
def choosePc():
    
    
    proc = subprocess.Popen("php url.php", shell=True, stdout=subprocess.PIPE)
    script_response = proc.stdout.read()
    print(script_response)

    r = requests.get(script_response)

    with open('content.xml', 'wb') as f:
        f.write(r.content)

    # tree = ET.parse("content.xml")
    # print("before loop")
    # print(tree.getroot())
    # root = tree.getroot()
    # for child in root.findall('../Items/Item'):
    #     print("test")
    #     print(child.tag, child.attrib)
    #     asin = child.find('ItemLink')

    jsonString = json.dumps(xmltodict.parse(r.content), indent=4)
    with open("output.json", 'w') as f:
        f.write(jsonString)
    j = json.loads(jsonString)
    r = j["ItemSearchResponse"]["Items"]["Item"]
    print(j["ItemSearchResponse"]["Items"]["Item"][0]["ASIN"])

    for item in r:
        print(item["ASIN"])    

    return render_template("choose-pc.html",items=r)

if __name__ == "__main__":
    app.run(debug=True)