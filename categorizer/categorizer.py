import utils

category_action = ["chat", "hyperlink", "money", "reply"]

def categorize_action(test_message):
    msg_terms = utils.get_words(test_message)
    flags = dict()

    for category in category_action:
        flags[category] = False

    for term in msg_terms:
        flags[__judge_action(term)] = True

    return flags

def __judge_action(term):
    if term == "talk" or term == "chat" or term == "LINE":
        return category_action[0]
    elif term == "link" or term == "http" or term == "https":
        return category_action[1]
    elif term == "money" or term == "coin":
        return category_action[2]
    elif term == "reply":
        return category_action[3]
    else:
        return None
