import json
import numpy as np




class Segment:
    def __init__(self, bbox):
        self.bbox = bbox    
class JSONBoxesToSEGS:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_string": ("STRING", {"forceInput": True}),
            } 
        }

    RETURN_TYPES = ("SEGS",)
    FUNCTION = "get_boxes"
    CATEGORY = "Gyre"
    """
    JSON string like {"boxes": [x,y,w,h] } to define the bounding boxes for detection, usually it is just one
    """
    def get_boxes(self, json_string=''):
        data = json.loads(json_string)        
        boxes = data['boxes']  
        segs = []
        for box in boxes:
            x = box['x']
            y = box['y']
            w = box['w']
            h = box['h']
            x1 = x
            y1 = y
            x2 = x + w
            y2 = y + h
            segs.append({'bbox': [x1, y1, x2, y2]})

        # Convert each dictionary to an instance of Segment
        segments = [Segment(seg['bbox']) for seg in segs]
        segs_result = [None, segments]
        
        return (segs_result,)
    

class JSONPointsSAMParameters:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_string": ("STRING", {"forceInput": True}),
            } 
        }

    RETURN_TYPES = ("SAM_PARAMETERS",)
    FUNCTION = "get_points"
    CATEGORY = "Gyre"
    """
    JSON string like {"points": [x,y,label] } to define the points for detection, label: 1 indicates a foreground point and 0 indicates a  background point
    """
    def get_points(self, json_string=''):
        data = json.loads(json_string)        
        points = data['points']          
        # Separate the coordinates and labels
        coords = [[point['x'], point['y']] for point in points]
        labels = [point['label'] for point in points]
        
        # Convert to tensors
        parameters = {
            "points": np.asarray(np.matrix(coords)),
            "labels": np.array(np.matrix(labels))[0]
        }
        return (parameters,)


