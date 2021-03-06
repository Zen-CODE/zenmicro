"""
The is module houses the Swagger documentation helper
"""

from flasgger import Swagger
from json import loads
from os.path import join


class ZenSwagger:
    """
    Manager the swagger API documentation backend.
    """
    @staticmethod
    def get_swagger_config():
        return {
            "headers": [],
            "specs": [{
                    "endpoint": 'apispec_v1',
                    "route": '/apispec_v1.json',
                    "rule_filter": lambda rule: True,
                    "model_filter": lambda tag: True}],
            "static_url_path": "/flasgger_static",
            # "static_folder": "static",  # must be set by user
            "swagger_ui": True,
            "specs_route": "/swagger/"
        }

    @staticmethod
    def init_swagger(app, instance):
        """
        Initialize the Swagger UI application and configuration exposing the
        API documentation. Once running, go to http://localhost:5000/swagger/

        Args:
            app: An instance of the Flask application
            class_data: a list of dicts with "name" and "instance" keys from
                        which to build the tags
        """
        with open(join("swagger", "swagger.template.json"), "rb") as f:
            template = loads(f.read())

        # Extract the description for the objects doc string
        template["tags"] = [{"name": instance.__class__.__name__,
                             "description": instance.__doc__}]
        swagger_app = Swagger(app,
                              template=template,
                              config=ZenSwagger.get_swagger_config())
        return swagger_app
