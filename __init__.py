import os


from .nodes import (

    JSONBoxes,
    JSONPoints,
    SAMMaskFromPoints,
    JSONPointsSAMParameters,
    JSONBoxesToSEGS,
)



NODE_CLASS_MAPPINGS = {
    "MatteAnything_JSONDinoBoxes": JSONBoxes,
    "MatteAnything_JSONBoxes To SEGS": JSONBoxesToSEGS,
    "MatteAnything_JSONPoints": JSONPoints,
    "MatteAnything_JSONPoints SAM Parameters": JSONPointsSAMParameters,
    "MatteAnything_SAMMaskFromPoints": SAMMaskFromPoints,
}
