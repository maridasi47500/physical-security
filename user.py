# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class User(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists user(
        id integer primary key autoincrement,
        email text,
            password text,
            nomcomplet text,
            image text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from user")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from user where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyemailpwsecurity(self,myid):
        self.cur.execute("select * from user where email = ? and password = ?",(myid["email"],myid["password"],))
        row=dict(self.cur.fetchone())
        hey={}
        try:
            hey["user_id"]=row["id"]
            hey["email"]=row["email"]
            hey["name"]=row["nomcomplet"]
            hey["notice"]="user trouvé"
        except:
            hey["email"]=None
            hey["user_id"]=""
            hey["name"]=None
            hey["notice"]="user non trouvé"
        return hey
    def getbyid(self,myid):
        self.cur.execute("select * from user where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
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
        azerty={}
        try:
            if myhash["password"] == myhash["passwordconfirmation"]:
                 del myhash["passwordconfirmation"]
                 self.cur.execute("insert into user (email,password,nomcomplet,image) values (:email,:password,:nomcomplet,:image)",myhash)
                 self.con.commit()
                 myid=str(self.cur.lastrowid)

                 azerty["notice"]="votre user a été ajouté"
            else:
                 myid=None
                 azerty["notice"]="votre user n'a pas été ajouté les mots de passe ne sont pas identiques"
            azerty["user_id"]=myid

        except Exception as e:
            print("my error"+str(e))
            azerty["user_id"]=None
            azerty["notice"]="votre user n'a pas été ajouté les mots de passe ne sont pas identiques"+str(e)


        return azerty




