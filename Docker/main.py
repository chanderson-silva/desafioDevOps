from flask import Flask
import redis
app = Flask(__name__)
#Use dns for acces any service
rs  = redis.StrictRedis(host='redis-service.default.svc.cluster.local',port=6379,db=0,password='1nUMbNBIqI8b', decode_responses=True)
@app.route('/healthcheck')
def healthy():
    return {
        'API': {
            'api': '1.0',
            'dep': {
            'fila': healthcheck(),
            }
        }
    }
def healthcheck():
   try:
       rs.ping()
       return 'Ok'
   except:
     return 'Nok'
if __name__ == '__main__':
    app.run(host='0.0.0.0')
