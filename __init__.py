"""
@author: Shir Ofir
@title: comfy loop utilities
@nickname: loop utilities
@description: This extension adds helper nodes for looping over prompts and other data types
"""
import logging
from .nodes import *

logging.info(f"### Loading: comfy loop utilities : START")

#  Map all your custom nodes classes with the names that will be displayed in the UI.
NODE_CLASS_MAPPINGS = {
    "ForeachPrompt" : ForeachPromptClass
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ForeachPrompt": "Foreach Prompt",
}

__all__ = ['NODE_CLASS_MAPPINGS']


import cm_global
cm_global.register_extension('ComfyUI-Inspire-Pack',
                                {'version': "1.0.0",
                                'name': 'comfy loop utilities',
                                'nodes': set(NODE_CLASS_MAPPINGS.keys()),
                                'description': 'This extension adds helper nodes for looping over prompts and other data types.', })

logging.info(f"### Loading: comfy loop utilities :  DONE") 