from service.database import Database

class DbMiddleware:
    def __init__(self) -> None:
        self.database = Database() 
    

    def create_user(self, ksuid, email, pswrd, created_at):
        return self.database.create_user(ksuid, email, pswrd, created_at)

    def delete_user(self, ksuid):
        self.database._execute_(ksuid)

    def create_task(self):
        self.database._execute_(f"")

    def delete_task(self):
        self.database._execute_