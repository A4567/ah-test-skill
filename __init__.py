from mycroft import MycroftSkill, intent_file_handler

import requests

API_URL = 'https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=cycle-shops-and-repairs&q='

def count_bikes(region):
    """Search openData for number of bike shops in region."""
    r = requests.get(API_URL, params={'refine.region':region})
    
    if(r.json()['nhits'] == 0):
        return None
    else:
        return r.json()['nhits']

def shop_address(index,region):
    re = requests.get(API_URL, params={'refine.region':region})
    if(re.json()['nhits'] == 0):
        return None
    else:
        return re.json()['records'][index]['fields']['address']
        
class AhTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('bike.intent')
    def get_number_bikes(self, message):
        number = count_bikes(message.data['region'])
        if number:
            self.speak_dialog('bike',{'count' : count_bikes(message.data['region'])})
        else:
            self.speak_dialog('error')

    @intent_file_handler('address.intent')
    def get_shop_address(self, message):
        location = shop_address(int(message.data['index']),message.data['region'])
        if location:
            self.speak_dialog('address',{'address' : location})
        else:
            self.speak_dialog('error')

    

def create_skill():
    return AhTest()

