def print_depth(data: dict, depth: int=1 ):
    """
    print out depth of the key using recursive function
    """
    for key in data:
        print(f"{key} {depth}")
        if isinstance(data[key], dict):
            print_depth(data[key], depth+1)