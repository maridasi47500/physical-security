# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Gossip(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists gossip(
        id integer primary key autoincrement,
        person_id text,
            place_id text,
            text text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select gossip.*, person.name as personne_name, person.pic as pic_personne,lieu.pic as pic_lieu from gossip left join person on gossip.person_id = person.id left join place lieu on lieu.id = gossip.place_id")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from gossip where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from gossip where id = ?",(myid,))
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
        try:
          self.cur.execute("insert into gossip (person_id,place_id,text) values (:person_id,:place_id,:text)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["gossip_id"]=myid
        azerty["notice"]="votre gossip a été ajouté"
        return azerty




