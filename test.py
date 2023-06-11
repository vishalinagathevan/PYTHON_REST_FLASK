from flask import Flask, request
#from flask_restful import Resource, Api
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api=Api(app)

Data=[]

@app.route('/')
def index():
    return "Welcome To The Python Flask REST API"

class People(Resource):
    def get(self, name):
        for x in Data:
            if x['Data'] == name:
                return {'Data':name}
            else:
                 return {'Data':None}
        return {'Data':name}  
    
    def post(self, name):
        Tem = {'Data':name}
        Data.append(Tem)
        return Tem
    
    def delete(self,name):
        for ind,x in enumerate(Data):
            if x['Data'] == name:
                Tem = Data.pop(ind)
                return {'Note':"Deleted"}    
    
api.add_resource(People,'/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
