def isValidSigName(db_GDSC, sig_name):
    sig_collection = db_GDSC["sig"]
    x = sig_collection.find_one({"sig": sig_name})
    if x == None:
        return 0
    else:
        return 1


def findSigInfo(db_GDSC, sig_name):
    sig_collection = db_GDSC["sig"]
    x = sig_collection.find_one({"sig": sig_name})
    print(x)
    return f'''
        SIG Name: {sig_name}\nSIG Head: {x["head"]}
    '''


def isHead(db_GDSC, discord_username):
    user_collection = db_GDSC['users']
    x = user_collection.find_one({'discord_username': discord_username})
    if x['head'] == True:
        return 1
    else:
        return 0


def addSIG(db_GDSC, sig_name, sig_head):
    sig_collection = db_GDSC["sig"]
    sig_collection.insert_one({"sig": sig_name, "head": sig_head})
