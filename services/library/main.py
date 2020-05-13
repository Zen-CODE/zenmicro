from flask import Flask
from json import load
from core.loader import Loader


class ZenService():
    """
    This class  acts as a generic base for Zen Miroservice instances.
    """
    def add_routes(self, app, path, service):
        """
        Add the exposed functions of the *obj* object to the *base_url* route.
        """
        route = f"/{path}/"
        for mth in Loader.get_public_methods(service):
            app.add_url_rule(route + mth, route + mth,
                             getattr(service, mth), methods=['GET'])

    @staticmethod
    def load_config():
        """
        Load the configuration from the specified file file.
        """
        with open("service/config.json") as f:
            return load(f)

    def run(self):

        app = Flask(__name__)
        config = self.load_config()
        service = Loader.get_class(config["service"]["module"],
                                   config["service"]["class"])()

        self.add_routes(app, config["service"]["path"], service)

        app.run(**config["flask"])
        return app


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


# @app.route('/list')
# def list_folder():
#     contents = str(listdir("/app/Music"))
#     return f'Hello Music! {contents}'
app = ZenService().run()