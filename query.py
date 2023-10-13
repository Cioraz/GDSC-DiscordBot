import utils


def display_SIG_info(signame):
    if (utils.isValidSigname(signame)):
        return f"{signame}"
    else:
        return "INVALID SIG NAME!"
# Head - {utils.display_head(collection_siginfo,signame)}
# Members - {utils.display_members(GDSC_collection_sigInfo)}


def display_Upcoming_events():
    pass


def display_Events_past():
    pass


def display_Events_Non_Tech():
    pass


def Member_Info(username):
    pass
