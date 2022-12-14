

from flask import Flask
from flask_login import LoginManager



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'itsasecret'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

    from views import views
    from auth import auth
    from  models import User, Food, db
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=False)
    

