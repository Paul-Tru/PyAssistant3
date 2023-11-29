import json
from datetime import datetime

now = datetime.now()
date = now.strftime("%Y-%m-%d")
current = now.strftime("%H:%M")

x = r"../../data/data.json"


def read_json(sec, var):
    with open(x, 'r') as f:
        data = json.load(f)
    if var in data.get(sec, {}):
        return data[sec][var]
    else:
        return None


def write_json(sec, var, text, src_date):
    if src_date == "0":
        src_date = date
    try:
        with open(x, "r") as file:
            try:
                info_data = json.load(file)
            except json.JSONDecodeError:
                info_data = {}

        new_entry = {"text": text, "date": src_date}
        info_data[sec][var] = new_entry

        with open(x, "w") as file:
            file.write(json.dumps(info_data, indent=4))
        return True

    except Exception as e:
        return e
