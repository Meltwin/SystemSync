YAML_OBJECTS = {}


def YAMLObject(_cls=None, *, tag: str = None):
    from yaml import SafeLoader

    def decorator(cls):
        def yaml_constructor(loader, node):
            return cls(**loader.construct_mapping(node))

        setattr(cls, "yaml_constructor", yaml_constructor)
        SafeLoader.add_constructor(f"!{tag if tag is not None else str(cls)}", cls.yaml_constructor)
        return cls

    if _cls is None:
        return decorator
    else:
        return decorator(_cls)
