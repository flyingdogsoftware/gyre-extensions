import json
import supervision as sv
import numpy as np
import torch
from segment_anything import  SamPredictor



class JSONBoxes:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_string": ("STRING", {"forceInput": True}),
            } 
        }

    RETURN_TYPES = ("DINO_BOXES",)
    FUNCTION = "get_boxes"
    CATEGORY = "Matte Anything"
    """
    JSON string like {"boxes": [x,y,w,h] } to define the bounding boxes for detection, usually it is just one
    """
    def get_boxes(self, json_string=''):
        data = json.loads(json_string)        
        boxes = data['boxes']  
        xyxy = []
        for box in boxes:
            x = box['x']
            y = box['y']
            w = box['w']
            h = box['h']
            x1 = x
            y1 = y
            x2 = x + w
            y2 = y + h
            xyxy.append([x1, y1, x2, y2])
        
        xyxy = np.array(xyxy, dtype=np.float32)
        # Create an sv.Detections object
        detections = sv.Detections(
            xyxy=xyxy,
        )
        return (detections,)
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
    CATEGORY = "Matte Anything"
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
        print(segments)
        segs_result = [None, segments]
        
        return (segs_result,)
    
class JSONPoints:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_string": ("STRING", {"forceInput": True}),
            } 
        }

    RETURN_TYPES = ("POINT_COORDS","POINT_LABELS")
    FUNCTION = "get_points"
    CATEGORY = "Matte Anything"
    """
    JSON string like {"points": [x,y,label] } to define the points for detection, label: 1 indicates a foreground point and 0 indicates a  background point
    """
    def get_points(self, json_string=''):
        data = json.loads(json_string)        
        points = data['points']          
        print(points)
        # Separate the coordinates and labels
        coords = [[point['x'], point['y']] for point in points]
        labels = [point['label'] for point in points]
        
        # Convert to tensors
        point_coords = torch.tensor([coords], dtype=torch.float)
        point_labels = torch.tensor([labels], dtype=torch.float)
        print(point_coords,point_labels)
        return (point_coords,point_labels)
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
    CATEGORY = "Matte Anything"
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



class SAMMaskFromPoints:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "sam_predictor": ("SAM_PREDICTOR", {}),
                "point_coords": ("POINT_COORDS", {}),
                "point_labels": ("POINT_LABELS", {}),
            }
        }

    RETURN_TYPES = ("MASK",)
    FUNCTION = "get_mask"

    CATEGORY = "Matte Anything"

    def get_mask(self, sam_predictor: SamPredictor, point_coords,point_labels ):
        masks, scores, logits = sam_predictor.predict_torch(
            point_coords=point_coords,
            point_labels=point_labels,
            boxes=None,
            multimask_output=False
        )

        return (torch.squeeze(masks),)    
    
    