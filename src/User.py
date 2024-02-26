class User:
    def __init__(self, username:str, first_name:str, last_name:str, email:str) -> None:
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def get_username(self) -> str:
        return self.username
    
    def get_fullname(self) -> str:
        return self.first_name + " " + self.last_name
