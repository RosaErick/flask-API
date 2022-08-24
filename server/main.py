from flask import Flask
from flask_cors import CORS
from flask_restx import Api, Namespace, Resource
from structlog import get_logger
from werkzeug.middleware.proxy_fix import ProxyFix


 
logger = get_logger(__name__)


# instantiate the app
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)
app.config.from_object("server.config.DevelopmentConfig")

#instantiate cors

cors = CORS()
cors.init_app(app, resources={r"*": {"origins": "*"}})



#instantiate the api

api = Api(version="1.0", title="Flask API", doc="/api/v1/docs")
api.init_app(app)
api_namespace = Namespace("api")



class Ping(Resource):
    def get(self):
        """health check"""
    
        logger.debug("Ping.GET")
        return {"message": "pong"}, 200
    
    
    
    

api_namespace.add_resource(Ping, "/ping")
api.add_namespace(api_namespace, path="/api/v1")