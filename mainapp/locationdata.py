from . import indianNewsPuller
from . import weatherr
import datetime

location = weatherr.city

title = indianNewsPuller.news_title
author = indianNewsPuller.news_author
desc = indianNewsPuller.news_desc
link = indianNewsPuller.news_link

main_weather = weatherr.weather_main
tempc = weatherr.tempC
tempf = weatherr.tempF
humidity_ = weatherr.humidity
visibility_ = weatherr.visibilty

title_ = weatherr.title
hours_ = datetime.datetime.now().hour
mins = datetime.datetime.now().minute

main = {
"title": title[0],
"author": author[0],
"desc": desc[0],
"link": link[0],

"title2": title[1],
"author2": author[1],
"desc2": desc[1],
"link2": link[1],

"title3": title[2],
"author3": author[2],
"desc3": desc[2],
"link3": link[2],

"title4": title[3],
"author4": author[3],
"desc4": desc[3],
"link4": link[3],

"title5": title[4],
"author5": author[4],
"desc5": desc[4],
"link5": link[4],

"title6": title[5],
"author6": author[5],
"desc6": desc[5],
"link6": link[5],

"title7": title[6],
"author7": author[6],
"desc7": desc[6],
"link7": link[6],

"title8": title[7],
"author8": author[7],
"desc8": desc[7],
"link8": link[7],

"title9": title[8],
"author9": author[8],
"desc9": desc[8],
"link9": link[8],

"title10": title[9],
"author10": author[9],
"desc10": desc[9],
"link10": link[9],

"title11": title[10],
"author11": author[10],
"desc11": desc[10],
"link11": link[10],

"title12": title[11],
"author12": author[11],
"desc12": desc[11],
"link12": link[11],

"title13": title[12],
"author13": author[12],
"desc13": desc[12],
"link13": link[12],

"title14": title[13],
"author14": author[13],
"desc14": desc[13],
"link14": link[13],

"title15": title[14],
"author15": author[14],
"desc15": desc[14],
"link15": link[14],

"title16": title[15],
"author16": author[15],
"desc16": desc[15],
"link16": link[15],

"title17": title[16],
"author17": author[16],
"desc17": desc[16],
"link17": link[16],

"title18": title[17],
"author18": author[17],
"desc18": desc[17],
"link18": link[17],

"title19": title[18],
"author19": author[18],
"desc19": desc[18],
"link19": link[18],

"title20": title[19],
"author20": author[19],
"desc20": desc[19],
"link20": link[19],

'main_weather': main_weather,
'tempC': tempc,
'tempf': tempf,
'humidity': humidity_,
'visibility':  visibility_,

'title_': title_,
'time': f'{hours_}:{mins}',
'locationofuser': {location}
}