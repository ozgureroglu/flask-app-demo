import os

from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, current_app


# Bu application factory kullanilarak olusturuluyor
def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     # a default secret that should be overridden by instance config
    #     SECRET_KEY="dev",
    #     # store the database in the instance folder
    #     DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    # )
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        
        app.config.from_object('flaskr.settings')
        # Join the instance path and the database file name    
        print(app.config)
        db_path = os.path.join(app.instance_path, app.config['DATABASE'])
        app.config['DATABASE'] = db_path
    
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    


    @app.route("/hello")
    def hello():
        return "Hello, World!"

    # register the database commands
    from . import db

    db.init_app(app)

    # ----- BLUEPRINTS -----
    # apply the blueprints to the app
    from . import auth
    from . import blog
    from . import api
    
    from .api import initialize_routes
    
    
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    # app.register_blueprint(api.bp)

    api = Api(app)
    initialize_routes(api)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app
