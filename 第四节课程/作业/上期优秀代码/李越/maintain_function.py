import codecs
import json


def maintainColumn(inputType, inputStr):
    file = open("resource.txt", "r", encoding='UTF-8')
    resource = file.read()
    res_dict = json.loads(resource)
    file.close()
    if inputType == '1':
        times = res_dict.get("time")
        times.append(inputStr)
        res_dict["time"] = times
    elif inputType == '2':
        persons = res_dict.get("person")
        persons.append(inputStr)
        res_dict["person"] = persons
    elif inputType == '3':
        situses = res_dict.get("situs")
        situses.append(inputStr)
        res_dict["situs"] = situses
    elif inputType == '4':
        events = res_dict.get("event")
        events.append(inputStr)
        res_dict["event"] = events
    newFile = codecs.open("resource.txt", "w", "utf-8")
    newFile.write(json.dumps(res_dict, ensure_ascii=False))
    newFile.close()