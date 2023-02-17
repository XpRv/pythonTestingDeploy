data = {
    "incidents": [
      {
        "id": 1234,
        "title": 'here is title',
        "team name": 'here is team name'
      },
      {
        "id": 5678,
        "title": 'here is title2',
        "team name": 'here is team name2'
      }
    ]
}

def get_incidents():
    return data['incidents']

# def add_todo(task):
#     task["id"] = len(data['todos']) + 1
#     data['todos'].append(task)
#     return {
#       "message": "task added",
#       "number of tasks": len(data['todos'])
#     }

# def edit_todo(task):
#     for i,todo in enumerate(data["todos"]):
#         if todo["id"] == task["id"]:
#            data["todos"][i] = task
    
#     return {
#       "message": "task edited",
#       "number of tasks": len(data['todos'])
#     }

# def delete_todo(task_id):
#     item_to_remove = '';
#     for todo in data["todos"]:
#         if int(task_id) == todo["id"]:
#             item_to_remove = todo
#     if item_to_remove:
#         data["todos"].remove(item_to_remove)
    
#     return {
#       "message": "task deleted",
#       "number of tasks": len(data['todos'])
#     }