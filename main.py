# eg 1, only node names: `python3 main.py input.json name,reach`
# eg 2, disambiguated node paths: `python3 main.py input.json boxers.name,reach`
# eg 3, full node paths: `python3 main.py input.json boxers.name,boxers.stats.reach`
import json, sys

def walk_json_recursively(json_obj, target_keys, current_path):
    if type(json_obj) is dict:
        for key in json_obj:
            new_path = f"{key}" if current_path == "" else f"{current_path}.{key}"
            for tk in target_keys:
                if tk == key:
                    print_node(new_path, json_obj[key])
                elif new_path.endswith(tk):
                    print_node(new_path, json_obj[key])
            walk_json_recursively(json_obj[key], target_keys, new_path)
    elif type(json_obj) is list:
        for item in json_obj:
            walk_json_recursively(item, target_keys, current_path)

def print_node(path, v):
    if type(v) is str:
        print(f'{path}: "{v}"')
    else:
        print(f"{path}: {v}")

def err(msg):
    print(msg)
    exit(1)

def main():
    if len(sys.argv) < 3:
        err("Not enough args.")
    try:
        f = open(sys.argv[1])
    except:
        err("File couldn't be opened.")
    try:
        json_obj = json.load(f)
    except:
        err("Invalid JSON.")
    f.close()
    target_keys = sys.argv[2].split(",")
    if "" in target_keys:
        target_keys.remove("")
    walk_json_recursively(json_obj, target_keys, "")

if __name__ == "__main__":
    main()