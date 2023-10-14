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


def addUser(db_GDSC, role, username, email, github, sig, year, branch, phone, discord_username, head):
    user_collection = db_GDSC["users"]
    data = {
        "role": role,
        "username": username,
        "email": email,
        "github": github,
        "sig": sig,
        "year": year,
        "branch": branch,
        "phone": phone,
        "discord_username": discord_username,
        "head": head
    }
    user_collection.insert_one(data)


def addUserToSig(db_GDSC, sig, discord_username):
    sig_collection = db_GDSC["sig"]
    x = sig_collection.find_one({"sig": sig})
    if x == None:
        return 0
    else:
        sig_collection.update_one(
            {"sig": sig}, {"$push": {"members": discord_username}})
        return 1
