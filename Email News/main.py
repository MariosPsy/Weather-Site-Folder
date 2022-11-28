import requests

api = "b2c2b8a40ae144a28bf4a74f4390bdfc"
url = "https://www.xtypos.gr/%CE%BA%CE%B1%CF%84%CE%B7%CE%B3%CE%BF%CF%81%CE%AF%CE%B1/%ce%b4%ce%ae%ce%bc%ce%bf%ce%b9-%ce%b1%cf%84%cf%84%ce%b9%ce%ba%ce%ae%cf%82/%ce%b4%ce%ae%ce%bc%ce%bf%cf%82-%ce%b7%cf%81%ce%b1%ce%ba%ce%bb%ce%b5%ce%af%ce%bf%cf%85-%ce%b1%cf%84%cf%84%ce%b9%ce%ba%ce%ae%cf%82/"

requests = requests.get(url)
content = requests.text
print(content)




