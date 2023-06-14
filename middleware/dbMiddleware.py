from service.database import Database

class DbMiddleware:
    def __init__(self):
        self.db = Database() 

    def create_user(self, ksuid: int, email: str, pswrd: str, created_at):
        return self.db.create_user(ksuid, email, pswrd, created_at)

    def delete_user(self, ksuid: int):
        self.db.delete_user(ksuid)

    def create_task(self, id: int, description: str, priority: int):
        return self.db.create_task(id, description, priority)

    def delete_task(self, id: int):
        self.db.delete_task(id)