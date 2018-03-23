import requests
import datetime
import collections
import urllib.parse
import hmac, hashlib
import base64
    
access_key = 'AKIAIYXQISLBGBBINRXA'
secret_key = '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'
associate_tag = 'buildmypc03-20'
    
endpoint = "webservices.amazon.in"
  
uri = "/onca/xml"
    
params = {
    "Service" : "AWSECommerceService",
    "Operation" : "ItemSearch",
    "AWSAccessKeyId" : "AKIAIYXQISLBGBBINRXA",
    "AssociateTag" : "buildmypc03-20",
    "SearchIndex" : "All",
    "ResponseGroup" : "Images,ItemAttributes,Offers",
    "Keywords" : "Gaming PCs"
}
# Y-m-d\TH:i:s\Zx
d = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")

params["Timestamp"] = d[:-3]+"Z"

orderedParams = collections.OrderedDict(sorted(params.items()))

# params.sort()

# print(urllib.parse.quote(orderedParams,safe=''))

pairs=[]

for key, value in orderedParams.items():
    # print(key,value)
    # print(urllib.parse.quote(key,safe='') + "=" + urllib.parse.quote(value,safe=''))
    pairs.append(urllib.parse.quote(key,safe='') + "=" + urllib.parse.quote(value,safe=''))

canonical_query_string = "&".join(pairs)

# print(canonical_query_string)

string_to_sign = "GET\n"+endpoint+"\n"+uri+"\n"+canonical_query_string

signature = (hmac.new(secret_key.encode('utf-8'), string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest())
signature = signature.encode('utf-8')
signature = base64.b64encode(signature)
# print(signature)

request_url = 'http://'+endpoint+uri+'?'+canonical_query_string+'&Signature='+urllib.parse.quote(signature,safe='')
print(request_url)