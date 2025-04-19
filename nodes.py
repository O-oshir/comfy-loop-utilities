import logging

class ForeachPromptClass:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompts_string": ("STRING", {"default":""}),
            },
            #  Specify the parameters with type and default value.
            "optional": {
                "delimiter": ("STRING", {"default": "---"}),
            }
        }

    #  Define these constants inside the node.
    #  `RETURN_TYPES` is important, as it limits the parameter types that can be passed to the next node, in `INPUT_TYPES()` above.
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    OUTPUT_IS_LIST = (True,)
    #  `FUNCTION` is the function name that will be called in the node.
    FUNCTION = "loopEachPrompt"
    #  `CATEGORY` is the category name that will be used when user searches the node.
    CATEGORY = "LoopUtilities"
    DESCRIPTION = "Splitting the prompt by the delimiter and run the following flow once for each prompt"
    INPUT_IS_LIST = False

    def loopEachPrompt(self, prompts_string, delimiter):
        splittedPrompts =  prompts_string.split(delimiter)
        return (splittedPrompts,)
        