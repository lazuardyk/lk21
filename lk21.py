import requests
from bs4 import BeautifulSoup
import re
Message1 = "LK21 / Dunia21 Download Link Grabber"
Message2 = "https://github.com/lazuardyk"
print('{:^80}'.format(Message1))
print('{:^80}'.format(Message2))

a = input("Masukkan judul film:\n")
payload = {"s":a}
req = requests.get("https://dunia21.net/", params=payload).text
soup = BeautifulSoup(req, "html.parser")
linknya = soup.find_all('h2')
link = linknya[2]
try:
    idfilm = re.search(r'<a href="https://dunia21.net/(.*)/" rel="bookmark"', str(link)).group(1)
    linkdl = "https://dl.layarkaca21.vip/get/" + idfilm
    linkby = "https://dl.layarkaca21.vip/verifying.php"
    data = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Accept":"*/*",
            "X-Requested-With":"XMLHttpRequest"}
    payload2 = {"slug":idfilm}
    req2 = requests.post(linkby, headers=data, params=payload2).text
    soup2 = BeautifulSoup(req2, "html.parser")
    linkdownload = soup2.find_all('a')
    reso360 = re.findall(r'btn-360" href="(.*)" rel=', str(linkdownload))
    if len(reso360) > 0:
        for laz1 in reso360:
            print("Link Download",idfilm,"360P:",laz1)
    reso480 = re.findall(r'btn-480" href="(.*)" rel=', str(linkdownload))
    if len(reso480) > 0:
        for laz2 in reso480:
            print("Link Download",idfilm,"480p:",laz2)
    reso720 = re.findall(r'btn-720" href="(.*)" rel=', str(linkdownload))
    if len(reso720) > 0:
        for laz3 in reso720:
            print("Link Download",idfilm,"720P:",laz3)
    reso1080 = re.findall(r'btn-1080" href="(.*)" rel=', str(linkdownload))
    if len(reso1080) > 0:
        for laz4 in reso1080:
            print("Link Download",idfilm,"1080P:",laz4)
except:
    print("Film tidak ditemukan. Masukkan judul yang lebih spesifik.")
