from flask import Flask

def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)

    from .public import public_bp
    app.register_blueprint(public_bp)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .admin import admin_bp
    app.register_blueprint(admin_bp)


    return app