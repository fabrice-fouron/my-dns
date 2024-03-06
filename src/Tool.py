class Tool:
    id = 0
    def __init__(self, name: str, link: str) -> None:
        id += 1
        self.name = name
        self.link = link

    def modify(self, name, link) -> None:
        self.name = name
        self.link = link

    def check_integrity(self) -> None:
        # check the integrity of the tool
        pass
