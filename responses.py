import utils

# Handling non admin responses available to NEP and intruders in the group


def handle_response(message, db_GDSC):
    # Splitting the message
    string = message.split(' ')

    if (len(string) == 1):
        string = string[0]
        if (string.lower() == 'hello'):
            return '''Hello! I am the WEC bot. I can help you with the following commands:\n1. upcoming_events (This gets a list of the 3 upcoming events of WEC)\n2. sig_info <sig_name> (This gives information about the SIG)\n3. member_info <discord_username> (This gives information about the member)\n4. event_info <event_name> (This gives information about the event)'''
        if (string.lower() == 'help'):
            return "Welcome to WEC command help page\n1. upcoming_events (This gets a list of the 3 upcoming events of WEC)\n2. sig_info <sig_name> (This gives information about the SIG)\n3. member_info <discord_username> (This gives information about the member)\n4. event_info <event_name> (This gives information about the event)"
        if (string.lower() == 'upcoming_events'):

            L = utils.upcomingEvents(db_GDSC)
            print(L)

            # only top 3 events displayed
            if (len(L) == 0):
                return "No upcoming events"
            else:
                if (len(L) == 1):
                    return "Upcoming event is " + L[0]
                elif (len(L) == 2):
                    return f'''Upcoming events are:\n1. {L[0]}\n2. {L[1]}\n\nType event_info <event_name> to learn more about the event!'''

                else:
                    return f'''Upcoming events are:\n1. {L[0]}\n2. {L[1]}\n3. {L[2]}\n\nType event_info <event_name> to learn more about the event!'''

        if (string.lower() == 'non_technical_events'):
            k = 0
            msg = ''
            for i in utils.displayNonTechnicalEvents(db_GDSC):
                msg = msg + f'{k+1}. {i}'
                msg = msg+'\n'
                k += 1
            return msg

        # code for past events
        if (string.lower() == 'past_events'):
            k = 0
            msg = ''
            for i in utils.displayPastEvents(db_GDSC):
                msg = msg + f'{k+1}. {i}'
                msg = msg+'\n'
                k += 1
            return msg

        if (string.lower() == 'technical_events'):
            k = 0
            msg = ''
            for i in utils.displayTechnicalEvents(db_GDSC):
                msg = msg + f'{k+1}. {i}'
                msg = msg+'\n'
                k += 1
            return msg

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
                return "INVALID DISCORD USERNAME! User not found on WEC database!"

            # have to code for event_info
        if (x == 'event_info'):
            # Making the sig name to suit all cases
            event_name = string[1].lower()
            if (utils.isValidEventName(db_GDSC, event_name)):
                return utils.eventInfo(db_GDSC, event_name)
            else:
                return "INVALID EVENT NAME"
