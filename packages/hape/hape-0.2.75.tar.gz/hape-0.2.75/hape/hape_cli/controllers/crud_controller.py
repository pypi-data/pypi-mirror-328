import json
import yaml
import os

from hape.logging import Logging
from hape.hape_cli.models.crud_model import Crud

class CrudController:

    def __init__(self, name, schema_json, schema_yaml):
        self.logger = Logging.get_logger('hape.hape_cli.controllers.crud_controller')
        schema = None
        schema_and_name = None
        
        if schema_json:
            try:
                schema_and_name = json.loads(schema_json)
            except json.JSONDecodeError as e:
                self.logger.error(f"Invalid JSON schema: {schema_json}")
                exit(1)
        elif schema_yaml:
            try:
                schema_and_name = yaml.safe_load(schema_yaml)
            except yaml.YAMLError as e:
                self.logger.error(f"Invalid YAML schema: {schema_yaml}")
        
        if schema_and_name:
            name = schema_and_name["name"]
            schema = schema_and_name["schema"]
        
        self.crud = Crud(os.path.basename(os.getcwd()), name, schema)
        self.crud.validate()
    
    def generate(self):
        self.crud.validate_schema()
        self.crud.generate()
        
    def delete(self):
        self.crud.delete()
