def change_password(data: dict) -> str:
    username = data.get("username")
    return f"Password changed successfully for user: {username}"
 
def reset_password(data: dict) -> str:
    username = data.get("username")
    return f"Password reset successfully for user: {username}"
 
def lock_account(data: dict) -> str:
    username = data.get("username")
    return f"Account locked successfully for user: {username}"
 
def unlock_account(data: dict) -> str:
    username = data.get("username")
    return f"Account unlocked successfully for user: {username}"
