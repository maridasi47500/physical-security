# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Security(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists security(
        id integer primary key autoincrement,
        name text
                    );""")
        self.con.commit()
        self.create1("asseyez-vous dans la salle de contrôle et surveillez chaque zone grâce aux ré seaux de camé ras installé es à  des endroits straté giques")
        self.create1("faire semblant d'aider un employé  lé gitime à  transporter un plateau de nourriture dans un centre de donné es")
        self.create1("traîner dans la zone fumeurs et suivre un employé  dans le bâtiment")
        self.create1("faire semblant de parler au té lé phone ou d'ê tre avec des bé quilles, ce qui incite l'employé  à  vous aider à  franchir la porte")
        self.create1("obtenez un camion de service et du maté riel pour vous aider à  ressembler à  la vraie affaire")
        self.create1("pirater le flux de la camé ra et manipuler ce que voit le personnel de sé curité")
        self.create1("brouiller les signaux d'une camé ra sans fil")

        #self.con.close()
    def getall(self):
        self.cur.execute("select * from security")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from security where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from security where id = ?",(myid,))
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
          self.cur.execute("insert into security (name) values (:name)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["security_id"]=myid
        azerty["notice"]="votre security a été ajouté"
        return azerty
    def create1(self,param):
        self.cur.execute("""insert or ignore into security(name) values (?)""", (param,))
        self.con.commit()




