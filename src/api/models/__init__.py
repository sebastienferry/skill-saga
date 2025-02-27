import json

class Objective:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __repr__(self):
        return f"Objective(name={self.name}, position={self.position})"
    
class ObjectiveJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Objective):
            return {
                'name': obj.name,
                'position': obj.position
            }
        return super().default(obj)