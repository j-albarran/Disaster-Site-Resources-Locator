from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'JAY'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

resources = []

class Resource_Type(Resource):
    @jwt_required()
    def get(self, name):
        for resource in resources:
            if resource['name'] == name:
                return resource
        return {'resource': None}, 404

    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, resources), None):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = request.get_json(silent=True)
        resource = {'name': name, 'items': data['items']}
        resources.append(resource)
        return resource, 201

    @jwt_required()
    def delete(self, name):
        global resources
        resources = list(filter(lambda x: x['name'] != name, resources))
        return {'message', 'Resource deleted'}

    @jwt_required()
    def put(self, name):
        data = request.get_json(silent=True)
        resource = next(filter(lambda x: x['name'] == name, resources), None)
        if resource is None:
            resource = {'name': name, 'items': data['items']}
            resource.append(resource)
        else:
            resource.update(data)
        return resource


class ResourceList(Resource):
    def get(self):
        return {'resources': resources}

api.add_resource(Resource_Type, '/resource/<string:name>')
api.add_resource(ResourceList, '/resources')

app.run(port=5000, debug=True)
