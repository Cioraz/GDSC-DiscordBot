import query


def handle_response(message):
    p_message = message.lower()
    if p_message == "hello":
        return "Hello, Welcome to Web Ethusiasts Club"

    # info about sig
    if p_message == 'sig_info':
        query.display_SIG_info()

    # help
    if p_message == 'help':
        query.display_help()

    # Upcoming Events
    if p_message == 'upcoming_events':
        query.display_SIG_info()

    # Non technical events
    if p_message == 'non_t_events':
        query.display_SIG_info()

    # Member Info
    if p_message == 'member_info':
        query.display_SIG_info()

    # SIG INFO
    if p_message == 'IASIG':
        query.display_SIG_info()

    # SIG INFO
    if p_message == 'IASIG':
        query.display_SIG_info()
