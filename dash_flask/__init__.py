"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment
from .dash_code import dashboard
from flask_login import LoginManager, login_required
from . import auth
from . import User
from . import extension


def create_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    app.secret_key = 's3cr3t'
    login_manager = LoginManager()
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    db = extension.db
    db.init_app(app)

    migrate = extension.migrate
    migrate.init_app(app, db)

    assets = Environment()
    assets.init_app(app)

    dash_plot = dashboard.init_dashboard()
    dash_plot.init_app(app)

    for view_func in app.view_functions:
        if view_func.startswith("/dashapp/"):
            app.view_functions[view_func] = login_required(app.view_functions[view_func])

    @login_manager.user_loader
    def load_user(id):
        return User.User.query.get(int(id))

    app.register_blueprint(auth.auth)
    #app.register_blueprint(routes.server_bp)


    with app.app_context():
    #
          from . import routes
          from .assets import compile_static_assets
    #
    # #     # Compile static assets
          compile_static_assets(assets)

    return app
