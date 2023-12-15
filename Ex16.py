data = [
    {"Name": "Pip", "Age": 26, "Hair": "None", "Python-Score": 0.69, "Active": True},
    {"Name": "Leia", "Age": 25, "Hair": "Purple", "Python-Score": 0.78, "Active": True},
    {"Name": "Prof. Turtle", "Age": 134, "Hair": "Gray", "Python-Score": 0.99, "Active": False}
]


def write_to_file(data, txt=False, csv=False, json=False, csv_character=";"):
    if csv:
        f = open("data.csv", "w")

        key_list = [k for k in data[0].keys()]

        for i in range(len(key_list)):
            f.write(key_list[i])

            if i < len(key_list) - 1:
                f.write(csv_character)

        for data_line in data:
            f.write("\n")

            for i in range(len(key_list)):

                e = data_line[key_list[i]]

                if type(e) != str:
                    f.write(str(e))
                else:
                    f.write("\"" + e + "\"")

                if i < len(key_list) - 1:
                    f.write(csv_character)

        f.close()

    if json:
        f = open("data.json", "w")
        f.write("{\n\"data\": [")

        for i in range(len(data)):
            l = len(data[i])
            c = 0

            f.write("\n{\n")

            for key, e in data[i].items():

                f.write("\"" + key + "\": ")

                if type(e) == bool:
                    f.write(str(e).lower())
                elif type(e) != str:
                    f.write(str(e))
                else:
                    f.write("\"" + e + "\"")

                c += 1
                if c != l:
                    f.write(",")
                f.write("\n")

            f.write("}")
            if i < len(data) - 1:
                f.write(",")

        f.write("\n]\n}")
        f.close()

    if txt:
        f = open("data.txt", "w")
        for set in data:
            for key, ele in set.items():
                f.write(key + ":" + str(ele) + "\n")
            f.write("\n")
        f.close()


def read_from_file(txt=False, csv=False, json=False):
    data = []

    s = txt + csv + json
    if s == 0:
        print("Enter the data you want to read.")
        return data
    elif s > 1:
        print("You can use only one type.")
        return data

    def value_conversion(value):
        # Bool
        if value.lower() == "true":
            value = True
        elif value.lower() == "false":
            value = False
        # Int
        elif value.isdecimal():
            value = int(value)
        else:
            # Float
            try:
                value = float(value)
            except ValueError:

                # Strings
                # Remove " at beginning and end of the csv-string
                if value.startswith("\"") and value.endswith("\""):
                    value = value[1:-1]

        return value

    if txt:
        f = open("data.txt", "r")
        t = [[k.split(":") for k in z] for z in [x.split("\n") for x in f.read().split("\n\n")]]
        t.pop()  # Remove empty element

        for a in t:
            d = {}
            for b in a:
                d[b[0]] = value_conversion(b[1])
            data.append(d)

    if csv:
        f = open("data.csv", "r")
        t = [x.split(";") for x in f.read().split("\n")]

        keys = t[0]
        t.pop(0) # Remove head/keys

        for a in t:
            d = {}
            for i in range(len(a)):
                d[keys[i]] = value_conversion(a[i])
            data.append(d)

    if json:
        f = open("data.json", "r")
        t = f.read()
        t = t[t.index("[") + 1 :t.index("]")]
        t = [x.split("\n") for x in t.replace("},\n", "").replace("{", "").replace("}", "").split("\n\n")]
        t.pop()
        t.pop(0)

        for a in t:
            d = {}
            for b in a:
                e = b
                if b.endswith(","):
                    e = b[:-1]

                l = e.split(": ")
                d[value_conversion(l[0])] = value_conversion(l[1])
            data.append(d)
    return data


write_to_file(data, csv=True, json=True, txt=True)
txt_data = read_from_file(txt=True)
if str(data) == str(txt_data):
    print("TXT is equal")
else:
    print("TXT is NOT equal")

csv_data = read_from_file(csv=True)
if str(data) == str(csv_data):
    print("CSV is equal")
else:
    print("CSV is NOT equal")

json_data = read_from_file(json=True)
if str(data) == str(json_data):
    print("JSON is equal")
else:
    print("JSON is NOT equal")

