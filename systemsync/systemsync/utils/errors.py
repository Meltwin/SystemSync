class PathDontExist(RuntimeError):
    def __init__(self, file: str):
        super().__init__(f"Error: File {file} does not exist!")
