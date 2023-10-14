import query
import utils

# Handling non admin responses available to NEP and intruders in the group


def handle_response(message, db_GDSC):
    # Splitting the message
    string = message.split(' ')

    if (len(string) == 1):
        string = string[0]
        if (string.lower() == 'hello'):
            return "Randomm Welcome"
    elif (len(string) == 2):
        # To ensure first word is in all word cases
        x = string[0]
        x = x.lower()
        if (x == 'sig_info'):
            # Making the sig name to suit all cases
            sig_name = string[1].lower()
            if (utils.isValidSigName(db_GDSC, sig_name)):
                return utils.findSigInfo(db_GDSC, sig_name)
            else:
                return "INVALID SIG NAME"
        if (x.lower() == 'member_info'):
            # No lower case as discord_username can include caps
            discord_username = string[1]
            if (utils.isValidDiscordUsername(db_GDSC, discord_username)):
                return utils.findUserInfo(db_GDSC, discord_username)
            else:
                return "INVALID DISCORD USERNAME!"

#     # help
# p_message == 'help':
#         query.display_help()

#     # Upcoming Events
# p_message == 'upcoming_events':
#         query.display_SIG_info()

#     # Non technical events
#     if p_message == 'non_t_events':
#         query.display_SIG_info()

#     # Member Info
#     if p_message == 'member_info':
#         query.display_SIG_info()

#     # SIG INFO
#     if p_message == 'IASIG':
#         query.display_SIG_info()

#     # SIG INFO
#     if p_message == 'IASIG':
#         query.display_SIG_info()
