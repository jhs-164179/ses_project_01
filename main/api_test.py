import requests

url = 'http://apis.data.go.kr/B553881/prfomncChckInfoService/prfomncChckInfoService'
params ={'serviceKey' : 'UH+Mc8jhYyRLsrSA7MppqKWOudoTtmD/ylIRBx6kF88i0zvh2u415PmhmYcegUMVcrTmclI4vRNRii//CcKC/g==', 'registYy' : '2020', 'registMt' : '1', 'vhctyAsortCode' : '1', 'registGrcCode' : '1', 'prye' : '2010' }

response = requests.get(url, params=params)
print(response.content)