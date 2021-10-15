import requests,sys,re
from bs4 import BeautifulSoup as bs

option = sys.argv[1]
inputt = sys.argv[2]

def check():
  ses = requests.Session()
  link = inputt
  raww = ses.get(link,headers={"User-Agent":"Chrome"}).text
  soup = bs(raww, "html.parser")
  down = re.search('href="https://sfile.mobi/download(.*?)"',raww).group(1)
  load = "https://sfile.mobi/download"+down
  judul_link = re.search('class="img" alt="(.*?)"', raww).group(1)
  oleh = re.search('rel="nofollow">(.*?)<', raww).group(1)
  pada = re.search('i> - Uploaded: (.*?)<', raww).group(1)
  tot_down = re.search('i> - Downloads: (.*?)<', raww).group(1)
  tag = re.search("i> - (.*?)<", raww).group(1)
  penis = re.search('.html">(.*?)<',raww).group(1)
  ukuran = re.search("Download File (.*?)<",raww).group(1)
  print(f"**================================")
  print(f"[*] Title         : "+judul_link)
  print(f"[#] Tags          : "+tag)
  print(f"[] File Type     : "+penis)
  print(f"[-] Bio File      : ")
  print(f"[-] File Size     : "+ukuran)
  print(f"[=] Uploaded By   : "+oleh)
  print(f"[?] Upload Date   : "+pada)
  print(f"[*] Total Download: "+tot_down)
  print(f"================================**")

if option == "-check":
 check()
