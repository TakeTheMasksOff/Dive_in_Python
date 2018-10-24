import os 
import argparse
import json
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("--key", required=True, help = "Required key option of the stored object. Only 1 parameter must be defined.")
parser.add_argument("--value", help = "Value of the key parameter to be stored. If omitted results of the key parameter in the storage will be returned" )
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), "storage.data")
with open(storage_path, "a+") as f:
    f.seek(0)
    file_content = f.read()
    json_obj = dict(json.loads(file_content)) if file_content != "" else None
    if args.value != None:
        if json_obj == None: 
            json_obj = {}
        if args.key in json_obj:
            value_list = json_obj[args.key]
            if not args.value in value_list:
                value_list.append(args.value)
                print(f"value '{args.value}' was appended to the key '{args.key}' in the storage")
            else:
                print(f"value '{args.value}' of the key '{args.key}' is already in the storage")
        else:
            json_obj[args.key] = [args.value]
            print(f"value '{args.value}' was added to the key '{args.key}' in the storage")
        f.truncate(0)
        json.dump(json_obj,f)
    else:
        if json_obj == None:
            print ("None")
        else:
            value_list = json_obj.get(args.key)
            print(*value_list, sep=", ") if value_list != None else print(value_list)