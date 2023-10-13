import query
import utils


def handle_response(message, db_GDSC):
    p_message = message.lower()
    string = p_message.split(' ')
    if (len(string) == 1):
        if (string[0] == 'hello'):
            return "Welcome Msg"
        elif (string[0] == 'add_sig'):
            return utils.addSIG()
        else:
            return "INVALID"
    elif (len(string) == 2):
        if (string[0] == 'sig_info'):
            sig_name = string[1]
            if (utils.isValidSigName(db_GDSC, sig_name)):
                return utils.findSigInfo(db_GDSC, sig_name)
            else:
                return "INVALID SIG NAME"
        else:
            return "INVALID"

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
