from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

from html.entities import codepoint2name
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from re import sub

db = create_engine("postgres://rohan@localhost/postgres")
table = Table('rv', MetaData(db),
              Column('id', Integer),
              Column('sect', Integer),
              Column('page', Integer),
              Column('verse', Integer),
              Column('dev', String),
              Column('rom', String),
              Column('eng', String),
              Column('rec', String)
              )


def insertDb(id, sect, page, verse, dev, rom, eng):
    insert = table.insert().values(id=id, sect=sect, page=page, verse=verse, dev=dev,
                                   rom=rom, eng=eng)
    conn.execute(insert)

    # select = table.select()
    # result = conn.execute(select)
    # for r in result:
    #     print(r)


def sanScrape(num):
    url = "http://www.sacred-texts.com/hin/rvsan/rv" + num + ".htm"

    uClient = uReq(url)  # opens stream and grabs webpage
    page_html = uClient.read()  # stores into variable
    uClient.close()  # closes stream

    page = soup(page_html, "html.parser")  # parses HTML file
    k = page.__str__().splitlines()

    dev, rom = [], []
    read = 0
    for i in k:
        if '<hr' in i and read == 2:
            break
        if read == 1 and '<p' not in i:
            dev.append(i.replace('<br/>', '').strip())
        if read == 2:
            rom.append(i.replace('<br/>', '').strip())
        if '<p' in i and read == 1:
            read = 2
        if 'h3' in i:
            read = 1

    devComb, romComb = [], []
    for i in range(0, len(dev), 2):
        if i+1 < len(dev):
            if '||' in dev[i+1] and '||' in rom[i+1]:
                devComb.append(dev[i] + " " + dev[i+1])
                romComb.append(rom[i] + " " + rom[i+1])
            else:
                devComb[-1] = devComb[-1] + " " + dev[i]
                romComb[-1] = romComb[-1] + " " + rom[i]
                del dev[i]
                del rom[i]
        elif i+1 == len(dev):
            devComb.append(dev[i])
            romComb.append(rom[i])

    dev, rom = devComb, romComb
    return dev, rom


def engScrape(num):
    url = "http://www.sacred-texts.com/hin/rigveda/rv" + num + ".htm"

    uClient = uReq(url)  # opens stream and grabs webpage
    page_html = uClient.read()  # stores into variable
    uClient.close()  # closes stream

    page = soup(page_html, "html.parser")  # parses HTML file
    k = page.__str__().splitlines()

    eng = []
    read = False
    for i in k:
        if '<hr' in i and read:
            break
        if read:
            eng = i.__str__().split('<br/>')
        if '<h3' in i:
            read = True

    comb = []
    for i in range(0, len(eng), 2):
        if i+1 < len(eng) and 'loquitur' not in eng[i]:
            comb.append(sub("\d" or "\d\d", "", eng[i].replace("<p>", "")).strip(
            ) + " " + eng[i+1].replace("</p>", "").strip())
        else:
            comb.append(
                sub("\d" or "\d\d", "", eng[i].replace("<p>", "")).strip())
            if 'loquitur' in eng[i]:
                comb.append(
                    sub("\d" or "\d\d", "", eng[i+1].replace("</p>", "")).strip())

    eng = comb
    return eng


with db.connect() as conn:
    id = 9315 # change to row count
    sect = 10 # change to mandala
    hymnCount = 192 # change to mandala length + 1
    sectStr = str(sect).zfill(2)
    problemPages = []
    for j in range(1, hymnCount):
        try:
            num = str(j).zfill(3)
            dev, rom = sanScrape(sectStr+num)
            eng = engScrape(sectStr+num)
            for i in range(0, len(dev)):
                print([id, sect, j, i+1, dev[i], rom[i], eng[i]])
                insertDb(id, sect, j, i+1, dev[i], rom[i], eng[i])
                id += 1
        except:
            problemPages.append(j)

print(problemPages)
# copypaste these manually

# 1 Verse misalignment | | || [138, 139, 179, 187, 191]
# 2 [38, 39, 40, 43]
# 3 [62]
# 4 [58]
# 5 [24, 87]
# 6 [16, 40, 41, 75]
# 7 English translations wrong? [34, 36, 37, 46, 52, 60, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103]
# 8 [34, 36, 37, 46, 52, 60, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103]
# 9 [114] 
# 10 [20, 86, 106, 191]