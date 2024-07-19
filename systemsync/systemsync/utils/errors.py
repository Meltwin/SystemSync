class PathDontExist(RuntimeError):
    def __init__(self, file: str):
        super().__init__(f"Error: File {file} does not exist!")


class UnImplementedMethod(RuntimeError):
    def __init__(self, method: str, class_name: str):
        super().__init__(f"Method {method} is unimplemented for class {class_name}")
