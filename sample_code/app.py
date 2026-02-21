def validate_user(data):
    if "name" not in data:
        return False
    return True

def create_user(data):
    if validate_user(data):
        return {"status": "created"}
    return {"status": "failed"}

def notify_user(user):
    print("Notification sent")

def register(data):
    user = create_user(data)
    notify_user(user)
    return user