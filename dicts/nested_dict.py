'''
    Given a nested dictionary DICT
        Write a function to get list of topic
'''

DICT = {
    "groups": [
        {
            "name": "Event",
            "groups": [
                {
                    "name": "Service",
                    "subscriptions": [
                        {"topic": "SERVICE_STATUS_PRESETS"},
                        {"topic": "AIRCRAFT_ACTIVATION"},
                        {"topic": "OUT_OF_SERVICE"},
                    ]
                }
            ]
        },
        {
            "name": "Enquiries",
            "groups": [
                {
                    "name": "Service-related",
                    "subscriptions": [
                        {"topic": "PROMO_CODES_REQUESTS"},
                    ]
                }
            ]
        }
    ],
    "subscriptions": [
        {"topic": "BANNERS"},
        {"topic": "DOCUMENTS"},
        {"topic": "USER"},
    ]
}

def get_topics(dictdata):
    '''
        Recursive function to get list of topic
    '''
    topics = []
    if 'groups' in dictdata:
        for groups_dict in dictdata['groups']:
            topics += get_topics(groups_dict)
    if 'subscriptions' in dictdata:
        for t in dictdata['subscriptions']:
            topics.append(t['topic'])
    return topics


if __name__ == '__main__':
    print(get_topics(DICT))
