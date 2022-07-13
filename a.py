from simplegmail import Gmail
import xml.etree.ElementTree as ET
import sqlite3
import re
import openai

def gpt3(texts):
    openai.api_key =

    response = openai.Completion.create(
      engine="davinci",
      prompt= texts,
          temperature=0.7,
          max_tokens=60,
          top_p=1,
          frequency_penalty=0.0,
          presence_penalty=0.0,
    )
    content= response.choices[0].text.split(".")
    print(content)
    return response.choices[0].text

def remove_urls (vTEXT):
    vTEXT = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", vTEXT)

    return(vTEXT)

conn = sqlite3.connect('gmaildb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Rawtext;
DROP TABLE IF EXISTS Sender;
DROP TABLE IF EXISTS GPTsum;
DROP TABLE IF EXISTS Date;


CREATE TABLE Date (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Sender (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Rawtext (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    sender_id  INTEGER,
    name    TEXT UNIQUE
);

CREATE TABLE GPTsum (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    summary TEXT  UNIQUE,
    rawtext_id  INTEGER,
    date_id  INTEGER,
    sender_id  INTEGER,
    len INTEGER,  count INTEGER
);
''')

gmail = Gmail()

messages = gmail.get_starred_messages()

count= 0
for message in messages[::-1]:
    count=count+1


    try:
        length = len(message.plain)
    except:
        continue
    if length < 5 or length > 3000:
        continue
    print("end234")
    print("To: " + message.recipient)
    print("From: " + message.sender)
    print("Subject: " + message.subject)
    print("Date: " + message.date)
    print("Preview: " + message.snippet)

    print("Message Body: " + message.plain)




    if message.recipient is None or message.sender is None or message.subject is None or message.date is None or message.snippet is None or message.plain is None:
        continue
    body= str(message.plain)
    remove_urls(body)

    print("summary:")
    summary=gpt3(body+".\n\ntl;dr:")

    cur.execute('''INSERT OR IGNORE INTO Sender (name)
        VALUES ( ? )''', ( message.sender, ) )
    cur.execute('SELECT id FROM Sender WHERE name = ? ', (message.sender, ))
    sender_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Rawtext (name, sender_id)
        VALUES ( ?, ? )''', ( message.plain, sender_id ) )
    cur.execute('SELECT id FROM Rawtext WHERE name = ? ', (message.plain, ))
    rawtext_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Date (name)
        VALUES ( ? )''', ( message.date, ) )
    cur.execute('SELECT id FROM Date WHERE name = ? ', (message.date, ))
    date_id = cur.fetchone()[0]


    cur.execute('''INSERT OR REPLACE INTO GPTsum
        (summary, rawtext_id, sender_id, len, count, date_id)
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        ( summary, rawtext_id, sender_id, length, count, date_id ) )

    conn.commit()
