# coding=utf-8
import sqlite3
import sys
import re
from model import Model
from chien import Chien
from garde import Garde
from cle import Cle
from serrure import Serrure
class Hack(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.dbChien=Chien()
        self.dbGarde=Garde()
        self.dbCle=Cle()
        self.dbSerrure=Serrure()
        self.cur.execute("""create table if not exists hack(
        id integer primary key autoincrement,
        user_id text,
        security_id text,
            metier_id text,
            details text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select hack.*,security.name as security1, metier.name as metier1 from hack left join security on security.id = hack.security_id left join metier on metier.id = hack.metier_id")
        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from hack where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select hack.*,security.name as security1, metier.name as metier1  from hack left join security on security.id = hack.security_id left join metier on metier.id = hack.metier_id where hack.id = ?",(myid,))
        row=dict(self.cur.fetchone())
        row["chien"]=self.dbChien.getallbyid(myid)
        row["garde"]=self.dbGarde.getallbyid(myid)
        row["cle"]=self.dbCle.getallbyid(myid)
        row["serrure"]=self.dbSerrure.getallbyid(myid)
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if x in ["chien","garde","serrure","cle"]:
                try:
                  myhash[x.replace("[","").replace("]","")]=params[x]
                except:
                  print("eerreur")
            elif '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myhash1={}
        for x in ["security_id","user_id","metier_id","details"]:
            myhash1[x]=myhash[x]
        myid=None
        z={}
        try:
            self.cur.execute("insert into hack (user_id,security_id,metier_id,details) values (:user_id,:security_id,:metier_id,:details)",myhash1)
            self.con.commit()
            myid=str(self.cur.lastrowid)
            try:
                for y in myhash["chien"]:
                    z=myhash["chien"][y]
                    z["hack_id"]=myid
                    self.dbChien.create(z)
            except:
                print("hey")
            try:
                for y in myhash["garde"]:
                    z=myhash["garde"][y]
                    z["hack_id"]=myid
                    self.dbGarde.create(z)
            except:
                print("hey")
            try:
                for y in myhash["cle"]:
                    z=myhash["cle"][y]
                    z["hack_id"]=myid
                    self.dbCle.create(z)
            except:
                print("hey")
            try:
                for y in myhash["serrure"]:
                    z=myhash["serrure"][y]
                    z["hack_id"]=myid
                    self.dbSerrure.create(z)
            except:
                print("hey")
        except Exception as e:
            print("my error"+str(e))
        azerty={}
        azerty["hack_id"]=myid
        azerty["notice"]="votre hack a été ajouté"
        return azerty
