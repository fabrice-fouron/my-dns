class Task:

    def __init__(self, name) -> None:
        self.id = id
        self.start_time = 0
        self.end_time = 0
        self.description = ""
        self.tools = []

    def set_start_time(self, time: int) -> None:
        self.start_time = time

    def set_description(self, description: str) -> None:
        self.description = description

    def set_tools(self, *args) -> None:
        for i in args:
            self.tools.append(i)