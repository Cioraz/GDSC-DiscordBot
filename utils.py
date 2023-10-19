# All validator functions

'''
    Handling all is validators
'''


def isValidSigName(db_GDSC, sig_name):
    sig_collection = db_GDSC["sig"]
    x = sig_collection.find_one({"sig": sig_name})
    if x == None:
        return 0  # Dint find such a SIG
    else:
        return 1  # Found the SIG


def isValidDiscordUsername(db_GDSC, discord_username):
    user_collection = db_GDSC["users"]
    x = user_collection.find_one({"discord_username": discord_username})
    if x == None:
        return 0  # Dint find such a discord_username
    else:
        return 1  # Found the discord_username


def isHead(db_GDSC, discord_username):
    user_collection = db_GDSC['users']
    x = user_collection.find_one({'discord_username': discord_username})
    if x['head'] == True:
        return 1  # If user is head
    else:
        return 0  # User not head


def isDiscordUsernameOnDatabase(db_GDSC, discord_username):
    user_collection = db_GDSC['users']
    x = user_collection.find_one({'discord_username': discord_username})
    if x == None:
        # not in WEC
        return 0
    else:
        # in WEC
        return 1


def isExecutive(db_GDSC, discord_username):
    user_collection = db_GDSC['users']
    x = user_collection.find_one({'discord_username': discord_username})
    # EM-Executive Member
    if x['role'] == "EM":
        return 1  # If executive Member
    else:
        return 0  # Not an executive Member


'''
    Handling all finder functions
'''


def findUserInfo(db_GDSC, discord_username):
    user_collection = db_GDSC["users"]
    x = user_collection.find_one({"discord_username": discord_username})
    return f'''
        Name: {x["username"]}\nRole: {x["role"]}\nEmail: {x["email"]}\nGithub: {x["github"]}\nSIG: {x["sig"]}\nYear: {x["year"]}\nBranch: {x["branch"]}\nPhone: {x["phone"]}\nDiscord Username: {x["discord_username"]}
    '''


def findSigInfo(db_GDSC, sig_name):
    sig_collection = db_GDSC["sig"]
    data = {
        "sig": sig_name,
    }
    x = sig_collection.find_one(data)
    print(x)
    return f'''
        SIG Name: {sig_name}\nSIG Head: {x["head"]}\nMembers: {x["members"]}
    '''


'''
Handling all adding stuff
'''


def addSIG(db_GDSC, sig_name, sig_head):
    sig_collection = db_GDSC["sig"]
    data = {
        "sig": sig_name,
        "head": sig_head
    }
    sig_collection.insert_one(data)


def addEvent(db_GDSC, date, event_Name, venue, time, about, tech_or_tech):
    event_collection = db_GDSC["events"]
    data = {
        "date": date,
        "event_Name": event_Name,
        "venue": venue,
        "time": time,
        "about": about,
        "tech_or_tech": tech_or_tech,
    }
    event_collection.insert_one(data)


async def addUser(db_GDSC, role, username, email, github, sig, year, branch, phone, discord_username, head, app):
    user_collection = db_GDSC["users"]
    app.run(debug=True)
    # data = {
    #     "role": role,
    #     "username": username,
    #     "email": email,
    #     "github": github,
    #     "sig": sig,
    #     "year": year,
    #     "branch": branch,
    #     "phone": phone,
    #     "discord_username": discord_username,
    #     "head": head
    # }
    # user_collection.insert_one(data)


def addUserToSig(db_GDSC, sig, discord_username):
    sig_collection = db_GDSC["sig"]
    x = sig_collection.find_one({"sig": sig})
    if x == None:
        return 0
    else:
        sig_collection.update_one(
            {"sig": sig}, {"$push": {"members": discord_username}})
        return 1


def upcomingEvents(db_GDSC):
    events_collection = db_GDSC["events"]
    # sort by the date of events

    x = events_collection.find({})
    L = []

    # sorted_events = sorted(x, key=lambda k: k['event_date'])
    sorted_events = sorted(x, key=lambda k: k['event_date'])
    for i in sorted_events:
        L.append(i['event_name'])
    return L


def eventInfo(db_GDSC, event_name):
    events_collection = db_GDSC["events"]
    x = events_collection.find_one({"event_name": event_name})
    if x == None:
        return 0
    else:
        return f'''
            Event Name: {x["event_name"]}\nDate: {x["event_date"]}\nTime: {x["event_time"]}\nVenue: {x["event_venue"]}\nAbout: {x["event_description"]}\nTechical Event: {x["event_T"]}
        '''


def displayNonTechnicalEvents(db_GDSC):
    events_collection = db_GDSC["events"]
    x = events_collection.find({"event_T": False})
    L = []
    for i in x:
        L.append(i["event_name"])
    return L


def displayTechnicalEvents(db_GDSC):
    events_collection = db_GDSC["events"]
    x = events_collection.find({"event_T": True})
    L = []
    for i in x:
        L.append(i["event_name"])
    return L


def isValidEventName(db_GDSC, event_name):
    event_collection = db_GDSC["events"]
    x = event_collection.find_one({"event_name": event_name})
    if x == None:
        return 0  # Dint find such a Event
    else:
        return 1  # Found the Event
