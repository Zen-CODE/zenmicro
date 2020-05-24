from flask import Flask
from json import load
from core.loader import Loader


class ZenService():
    """
    This class  acts as a generic base for Zen Miroservice instances.
    """
    @staticmethod
    def add_routes(app, path, service):
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

    @staticmethod
    def get_service(service_config):
        """ Build and return the service object given it's configuration """
        return Loader.get_class(
            service_config["module"],
            service_config["class"])(service_config)

    def build(self):
        """ Configure, build and return the Flask application """
        app = Flask(__name__)
        config = self.load_config()
        service = self.get_service(config)

        self.add_routes(app, config["url_path"], service)

        return app


app = ZenService().build()
