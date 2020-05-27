from mycroft import MycroftSkill, intent_file_handler


class AhTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('Scream.intent')
    def handle_test_ah(self, message):
        self.speak_dialog('Scream')


def create_skill():
    return AhTest()

