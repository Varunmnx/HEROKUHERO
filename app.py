# from crypt import methods
# from importlib import import_module
import os
from flask import Flask,render_template
# import flask
import pulumi.automation as auto


def ensure_plugins():
    ws = auto.LocalWorkspace()
    ws.install_plugin("aws","v4.0.0") #aws provider plugin

def create_app():
    ensure_plugins() 
    app = Flask(__name__,instance_relative_config=True)
    #change while deploying
    app.config.from_mapping(    
        SECRET_KEY ="secret",
        PROJECT_NAME ="HEROCOOL",
        PULUMI_ORG =os.environ.get("PULUMI_ORG"),
    )    

    @app.route("/",methods =["GET"])
    def index():
        return render_template("index.html")

    import sites
    app.register_blueprint(sites.bp) #for additional routes from additional files    
    import virtual_machines
    app.register_blueprint(virtual_machines.bp)  
    return app  