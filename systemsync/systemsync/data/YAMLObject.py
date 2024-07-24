from ..utils.errors import UnImplementedMethod


def YAMLObject(_cls=None, *, tag: str = None, auto_implement: bool = True):
    """
    Decorator that take care of all YAML Tag automatic parsing.

    Args:
        _cls (_type_, optional): the class that represent the data structure of the tag
        tag (str, optional): the tag name (e.g. if the tag is "foo", then it will automatically parse !foo blocks in the file)
        auto_implement (bool, optional): should the decorator implement an automatic parsing function (that simply redirect all values into the class constructor)

    Raises:
        UnImplementedMethod: if auto_implement is False and the class doesn't have a written static yaml_constructor method,
                            then raise an error since it won't be possible to load the YAML Tag.
    """
    from yaml import SafeLoader

    def decorator(cls):
        if auto_implement:

            def yaml_constructor(loader, node):
                return cls(**loader.construct_mapping(node))

            setattr(cls, "yaml_constructor", yaml_constructor)
        if not hasattr(cls, "yaml_constructor"):
            raise UnImplementedMethod("yaml_constructor", str(cls))
        SafeLoader.add_constructor(
            f"!{tag if tag is not None else str(cls)}", cls.yaml_constructor
        )
        return cls

    if _cls is None:
        return decorator
    else:
        return decorator(_cls)
