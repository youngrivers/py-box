import urllib.request

url='http://ip.chinaz.com/getip.aspx'

proxy_support=urllib.request.ProxyHandler({'http':'114.228.74.107'})

opener=urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)

response=urllib.request.urlopen(url)
html=response.read().decode('utf-8')

print(html)
