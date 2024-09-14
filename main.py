import re
import requests

new_data = []
# Chinese Channel
china = requests.get('https://raw.githubusercontent.com/Qst236/TV/main/IPV4.m3u').text
china = china.split('\n\n')[:62]

new_data.extend(china)

# Indonesia Channel
data = requests.get('https://iptv.urfan.web.id').text
data = data.split('\n\n')[5:][:-3]
for x in data:
    if not re.search("info.png", x):
        new_data.append(x)

new_data.append(china[0])

f = open("IPV4.m3u", "w")
f.write("\n\n".join(new_data))