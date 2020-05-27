from mycroft import MycroftSkill, intent_file_handler

import requests

API_URL = 'https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=cycle-shops-and-repairs&q='

def search_bike(region):
    """Search openData for number of bike shops in region."""
    r = requests.get(API_URL, params={'refine.region':region})
    print('Searching in: ' + region)
    
    if(r.json()['nhits'] == 0):
        return None
    else:
        return r.json()['nhits']



class AhTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('bike.intent')
    def get_number_bikes(self, message):
        number = search_bike(message.data['region'])
        if number:
            self.speak_dialog('bike',{'count' : search_bike(message.data['region'])})
        else:
            self.speak_dialog('error')
        


def create_skill():
    return AhTest()

