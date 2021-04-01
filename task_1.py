def print_depth(data: dict, depth=1):
    for key in data:
        print(f"{key} {depth}")
        if isinstance(data[key], dict):
            print_depth(data[key], depth + 1)

