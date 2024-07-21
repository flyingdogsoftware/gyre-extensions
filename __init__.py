import os


from .nodes import (
    JSONPointsSAMParameters,
    JSONBoxesToSEGS,
)



NODE_CLASS_MAPPINGS = {
    "Gyre_JSONBoxes To SEGS": JSONBoxesToSEGS,
    "Gyre_JSONPoints SAM Parameters": JSONPointsSAMParameters,
}
