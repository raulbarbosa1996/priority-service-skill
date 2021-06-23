from mycroft import MycroftSkill, intent_file_handler


class PriorityService(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('service.priority.intent')
    def handle_service_priority(self, message):
        self.speak_dialog('service.priority')


def create_skill():
    return PriorityService()

