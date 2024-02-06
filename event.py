# coding=utf-8
import sqlite3
import sys
import re
from model import Model
from texttospeech import Texttospeech
from speaker import Speaker
class Event(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.dbSpeaker=Speaker()
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists event(
        id integer primary key autoincrement,
        date text,
            heure text,
            organization_id text,
            subtitle text,
            place_id text,
            privpubl text,
            mytext text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from event")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from event where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from event where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        hey=Texttospeech(myhash["recording"])
        hey.script1()
        temps=0
        duration=60

        try:
          myhash["mytext"]=""
          self.cur.execute("insert into event (date,heure,organization_id,subtitle,place_id,privpubl,mytext) values (:date,:heure,:organization_id,:subtitle,:place_id,:privpubl,:mytext)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        try:
          while True:
            tempsdebut=temps
            if temps == 0:
              sometext=hey.get_text_hey(duration)
            else:
              sometext=hey.get_text_hey(duration,temps)
            temps+=60
            tempsfin=temps
            speaker=self.dbSpeaker.create({"name":"Speaker","text":sometext,"timedebut":tempsdebut,"timefin":tempsfin,"event_id":myid})

        except Exception as e:
          print("Hey",e)
        azerty={}
        azerty["event_id"]=myid
        azerty["notice"]="votre event a été ajouté"
        return azerty




