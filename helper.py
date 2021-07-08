import json

def authToTable(ses):
    if("auth" in ses):
        if(ses["auth"]=="SOC"):
            return "Society"
        elif(ses["auth"]=="ADMIN"):
            return "Administrator"
        elif(ses["auth"]=="USER"):
            return "User"
        elif(ses["auth"]=="ADVISOR"):
            return "Advisor"
    else:
        return ""


def litowin(result):
    flag = False
    refactored_result = ''
    if(len(result.split('\\'))==1):
        result = result.split('/')
    else:
        result = result.split('\\')
    for i in result:
        if flag==True or i == 'static':
            flag = True
            if i == 'static':
                continue
            refactored_result += i+'/'
    return refactored_result[:-1]

def dbJSON_create(host, user, password, db):
    jsonData = {
        "host": host,
        "user": user,
        "password": password,
        "db": db
    }
    with open('dbconfig.json', 'w') as outfile:
        json.dump(jsonData, outfile, indent=4)