#coding:utf-8
import redis
import json
import tornado.web
import tornado.httpserver
from tornado.options import define,options

define('port',default=8888,type=int)

class DealHandler(tornado.web.RequestHandler):
  def initialize(self):
    self.host='localhost'
    self.port=6379
  def get(self):
    city=self.get_argument('city',None)
    src=self.get_argument('src',None)
    year=self.get_argument('year',None)
    month=self.get_argument('month',None)
    
    keyset=[]
    for i in range(1,30):
      key='_'.join(src,city,str(year),str(month),str(i))
      keyset.apped(key)
    r=redis.StrictRedis(host=self.hostm,port=self.port)
    self.write(json.dumps(r.mget(keyset)))
    
  def post(self):
    pass

class ExampleHandler(tornado.web.RequestHandler):
  def get(self):
    who=self.get_argument("who",None)
    if who:
      self.write("hello"+who)
    else:
      self.write("hello world")
  def post(self):
    pass

class Application(tornado.web.Application):
  def __init(self):
    handlers=[
      (r"/",ExampleHandler),
      (r"/deal",DealHandler)
    ]
    settings=dict()
    tornado.web.Application.__init__(self,handlers,settins)
  
def create_server():
  tornado.options.parse_command_line()
  http_server=tornado.httpserver.HTTPServer(Application)
  http_server.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()
  
if __name__=='__main__':
  create_server()
