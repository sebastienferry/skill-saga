def add_objective(objectives, objective):
    objectives.append(objective)
    objectives.sort(key=lambda x: x['position'])

def delete_objective(objectives, objectif_id):
    objectives[:] = [obj for obj in objectives if obj['id'] != objectif_id]

def trier_objectifs(objectives):
    return sorted(objectives, key=lambda x: x['position'])