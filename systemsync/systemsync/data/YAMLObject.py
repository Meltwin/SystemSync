from ..utils.errors import UnImplementedMethod


def YAMLObject(_cls=None, *, tag: str = None, auto_implement: bool = True):
    from yaml import SafeLoader

    def decorator(cls):
        if auto_implement:
            def yaml_constructor(loader, node):
                return cls(**loader.construct_mapping(node))
            setattr(cls, "yaml_constructor", yaml_constructor)
        if not hasattr(cls, "yaml_constructor"):
            raise UnImplementedMethod("yaml_constructor", str(cls))
        SafeLoader.add_constructor(f"!{tag if tag is not None else str(cls)}", cls.yaml_constructor)
        return cls

    if _cls is None:
        return decorator
    else:
        return decorator(_cls)
