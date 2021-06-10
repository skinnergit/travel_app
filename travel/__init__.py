from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

#create a function that creates a web application
# a web server will run this web application
def create_app():
  
    app=Flask(__name__)  # this is the name of the module/package that is calling this app
    app.debug=True
    app.secret_key='anythingilike'

    #set the app configuration data 
    app.config['UPLOAD_FOLDER'] = '/static/image'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///appdatabase.sqlite'
    
    #initialize db with flask app
    db.init_app(app)

    bootstrap = Bootstrap(app)

    from . import views, destinations, auth
    app.register_blueprint(views.mainbp)
    app.register_blueprint(destinations.bp)
    app.register_blueprint(auth.bp)

    return app

    if __name__ == '__main__':
        n_app=create_app()
        n_app.run()