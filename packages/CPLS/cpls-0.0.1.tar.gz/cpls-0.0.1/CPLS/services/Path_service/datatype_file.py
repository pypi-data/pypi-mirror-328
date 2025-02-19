from pydantic import BaseModel, Field, model_validator, field_validator,  ConfigDict
from typing import Optional, Dict, Union, List
from .base_path_obj import PathFile
import ast
import os
