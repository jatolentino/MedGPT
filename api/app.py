from flask import Flask
from routes.chat import chat_blueprint
from routes.data import data_blueprint
from routes.patients import patients_blueprint

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(chat_blueprint, url_prefix='/chat')
    app.register_blueprint(data_blueprint, url_prefix='/data')
    app.register_blueprint(patients_blueprint, url_prefix='/patients')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
