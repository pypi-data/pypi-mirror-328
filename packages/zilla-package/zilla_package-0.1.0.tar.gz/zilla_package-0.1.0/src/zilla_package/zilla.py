class Zilla:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def create(name: str) -> str:
        assert name is not None, "name of the zilla cannot be None"
        return f"{name}-zilla "
