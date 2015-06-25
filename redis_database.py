#coding:utf-8
import redis
import datetime

class Database:
  def __init__(self):
    self.host='localhost'
    self.port=6379
    self.write_pool={}
  
  def write(self,website,city,year,month,day,deal_number):
    try:
      key='_'.join(website,city,str(year),str(month),str(day))
      val=deal_number
      r=redis.StrictRedis(host=self.host,port=self.port)
      r.set(key,val)
    except Exception as e:
      print e
  def read(self,websit,city,year,month,day):
    try:
      key='_'.join(website,city,str(year),str(month),str(day))
      r=redis.StrictRedis(host=self.host,port=self.port)
      value=r.get(key)
      return value
    except Exception as e:
      print e
  
  def add_write(self,website,city,year,month,day,deal_number):
    key='_'.join(website,city,str(year),str(month),str(day))
    val=deal_number
    self.write_pool[key]=val
  def batch_write(self):
    try:
      r=redis.StrictRedis(host=self.host,port=self.port)
      r.mset(self.write_pool)
    except Exception as e:
      print e
      
  def add_read(self,website,city,year,month,day):
    key='_'.join(website,city,str(year),str(month),str(day))
    self.write_pool.append(key)
  def batch_read(self):
    try:
      r=redis.StrictRedis(host=self.host,port=self.port)
      val=r.mget(self.write_pool)
      return val
    except Exception as e:
      print e
      
def single_write():
  beg=datetime.datetime.now()
  db=Database()
  for i in range(1,10000):
    db.write('meituan','beijing',i,9,1,i)
  end=datetime.datetime.now()
  print end-beg

def batch_write():
  beg=datetime.datetime.now()
  db=Database()
  for i in range(1,10000)
    db.add_write('meituan','beijing',i,9,1,i)
  db.batch_write()
  end=datetime.datetime.now()
  print end-beg
  
def single_read():
  beg=datetime.datetime.now()
  db=Database()
  for i in range(1,10000):
    db.read('meituan','beijing',i,9,1)
  end=datetime.datetime.now()
  print end-beg
  
def batch_read():
  beg=datetime.datetime.now()
  db=Database()
  for i in range(1,10000):
    db.add_read('meituan','beijing',i,9,1)
  db.batch_read()
  end=datetime.datetime.now()
  print end-beg
  
if __name__=='__main__':
  single_write()
  batch_write()
  single_read()
  batch_read()
