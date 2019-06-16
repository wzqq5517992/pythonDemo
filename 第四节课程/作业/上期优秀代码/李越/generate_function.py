import json


def getStory(inputStr):
    # get every position number
    timeNum = int(inputStr[0])
    personNum = int(inputStr[1])
    situsNum = int(inputStr[2])
    eventNum = int(inputStr[3])

    # get lists from resource file
    file = open("resource.txt", "r", encoding='UTF-8')
    resource = file.read()
    res_dict = json.loads(resource)
    times = res_dict.get("time")
    persons = res_dict.get("person")
    situses = res_dict.get("situs")
    events = res_dict.get("event")
    file.close()

    # get index for every list
    timeIndex = getIndex(timeNum, len(times))
    personIndex = getIndex(personNum, len(persons))
    situsIndex = getIndex(situsNum, len(situses))
    eventIndex = getIndex(eventNum, len(events))

    # generate time person situs event
    generTime = times[timeIndex]
    generPerson = persons[personIndex]
    generSitus = situses[situsIndex]
    generEvent = events[eventIndex]

    # generate story
    story = generTime + generPerson + generSitus + generEvent

    # persistence story
    stories = open('generate_stories.txt', 'a', encoding='UTF-8')
    stories.write(story+'\n')
    stories.close()

    return story


def getIndex(inputNum,arrayLen):
    while inputNum >= arrayLen-1:
        inputNum = inputNum % arrayLen
        if inputNum <= arrayLen-1:
            break
    return inputNum
