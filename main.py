import io
import re
import gzip
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

# Chinese EPG
china_epg = requests.get("https://raw.githubusercontent.com/BurningC4/Chinese-IPTV/refs/heads/master/guide.xml").text
china_epg = china_epg.splitlines()[:-1]
china_epg = '\n'.join(china_epg)

# Indonesia EPG
indonesia = requests.get('https://s.urfan.web.id/epg', stream=True)
with gzip.open(io.BytesIO(indonesia.content), 'rb') as f_in:
    with open('guide.xml', 'wb') as f_out:
        f_out.write(f_in.read())

with open("guide.xml", "r") as f:
	indonesia = f.read()
	indonesia = indonesia.splitlines()[2:]
	indonesia = '\n'.join(indonesia)

with open("guide.xml", "w") as f:
	f.write(china_epg + indonesia)
