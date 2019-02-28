from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

from html.entities import codepoint2name
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# db = create_engine("postgres://rohan@localhost/postgres")
# table = Table('rv', MetaData(db),
#               Column('id', Integer),
#               Column('sect', Integer),
#               Column('page', Integer),
#               Column('dev', String),
#               Column('rom', String),
#               Column('eng', String),
#               Column('rec', String)
#               )
# add verse int


def sanScrape(num):
    url = "http://www.sacred-texts.com/hin/rvsan/rv" + num + ".htm"

    uClient = uReq(url)  # opens stream and grabs webpage
    page_html = uClient.read()  # stores into variable
    uClient.close()  # closes stream

    page = soup(page_html, "html.parser")  # parses HTML file
    body = page.find("h3")  # finds first <div> with this id

    # fullverses = {"verse num": ["dev", "rom", "eng"]}
    dev = []
    rom = []

    arr = dev
    i = 0
    while i != -1:
        body = body.next_element.next_element
        if body.next_element.name == "p":
            body = body.next_element.next_element
            arr = rom
        if body.name == "hr":
            break
        arr.append(body)
        i += 1

    # print(dev)
    # print(rom)
    return dev, rom

def engScrape(num):
    url = "http://www.sacred-texts.com/hin/rigveda/rv" + num + ".htm"

    uClient = uReq(url)  # opens stream and grabs webpage
    page_html = uClient.read()  # stores into variable
    uClient.close()  # closes stream

    page = soup(page_html, "html.parser")  # parses HTML file
    body = page.find("h3")  # finds first <div> with this id

    eng = []
    i = 0
    while i != -1:
        body = body.next_element.next_element
        if body.next_element.name == "p":
            body = body.next_element.next_element
        if body.name == "p":
            break
        eng.append(body)
        i += 1

    # print(eng)
    return eng

dev, rom = sanScrape("01001")
eng = engScrape("01001")

verses = {}
for i in range(0, len(dev), 2):
  j = int(i/2)
  verses[j] = [dev[i] + dev[i+1], rom[i] + rom[i+1], eng[i] + eng[i+1]]

print(verses)
'''
{
  0: ['\nअग्निमीळे पुरोहितं यज्ञस्य देवं रत्वीजम | \nहोतारं रत्नधातमम || ', '\naghnimīḷe purohitaṃ yajñasya devaṃ ṛtvījam | \nhotāraṃ ratnadhātamam || ', '1 I Laud Agni, the chosen Priest, God, minister of sacrifice, The hotar, lavishest of wealth.'],
  1: ['\nअग्निः पूर्वेभिर्र्षिभिरीड्यो नूतनैरुत | \nस देवानेह वक्षति || ', '\naghniḥ pūrvebhirṛṣibhirīḍyo nūtanairuta | \nsa devāneha vakṣati || ', ' 2 Worthy is Agni to be praised by living as by ancient seers. He shall bring hitherward the Gods.'],
  2: ['\nअग्निना रयिमश्नवत पोषमेव दिवे-दिवे | \nयशसं वीरवत्तमम || ', '\naghninā rayimaśnavat poṣameva dive-dive | \nyaśasaṃ vīravattamam || ', ' 3 Through Agni man obtaineth wealth, yea, plenty waxing day by day, Most rich in heroes, glorious.'],
  3: ['\nअग्ने यं यज्ञमध्वरं विश्वतः परिभूरसि | \nस इद्देवेषु गछति || ', '\naghne yaṃ yajñamadhvaraṃ viśvataḥ paribhūrasi | \nsa iddeveṣu ghachati || ', ' 4 Agni, the perfect sacrifice which thou encompassest about Verily goeth to the Gods.'],
  4: ['\nअग्निर्होता कविक्रतुः सत्यश्चित्रश्रवस्तमः | \nदेवो देवेभिरा गमत || ', '\naghnirhotā kavikratuḥ satyaścitraśravastamaḥ | \ndevo devebhirā ghamat || ', ' 5 May Agni, sapient-minded Priest, truthful, most gloriously great, The God, come hither with the Gods.'],
  5: ['\nयदङग दाशुषे तवमग्ने भद्रं करिष्यसि | \nतवेत तत सत्यमङगिरः || ', '\nyadaṅgha dāśuṣe tvamaghne bhadraṃ kariṣyasi | \ntavet tat satyamaṅghiraḥ || ', ' 6 Whatever blessing, Agni, thou wilt grant unto thy worshipper, That, Aṅgiras, is indeed thy truth.'],
  6: ['\nउप तवाग्ने दिवे-दिवे दोषावस्तर्धिया वयम | \nनमो भरन्त एमसि || ', '\nupa tvāghne dive-dive doṣāvastardhiyā vayam | \nnamo bharanta emasi || ', ' 7 To thee, dispeller of the night, O Agni, day by day with prayer Bringing thee reverence, we come'],
  7: ['\nराजन्तमध्वराणां गोपां रतस्य दीदिविम | \nवर्धमानंस्वे दमे || ', '\nrājantamadhvarāṇāṃ ghopāṃ ṛtasya dīdivim | \nvardhamānaṃsve dame || ', ' 8 Ruler of sacrifices, guard of Law eternal, radiant One, Increasing in thine own abode.'],
  8: ['\nस नः पितेव सूनवे.अग्ने सूपायनो भव | \nसचस्वा नः सवस्तये ||', '\nsa naḥ piteva sūnave.aghne sūpāyano bhava | \nsacasvā naḥ svastaye ||', ' 9 Be to us easy of approach, even as a father to his son: Agni, be with us for our weal.']
}
'''

# def insertDb(id, sect, page, dev, rom, eng):
#     insert = table.insert().values(id=id, sect=sect, page=page, dev=dev,
#                                    rom=rom, eng=eng)
#     conn.execute(insert)

#     select = table.select()
#     result = conn.execute(select)
#     for r in result:
#         print(r)


# with db.connect() as conn:
#     insertDb()
