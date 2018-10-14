from app.core.tasks import BaseTaskHandler


class AfricasTalkingSendMessageTaskHandler(BaseTaskHandler):
    """
    Africa's Talking send sms message task handler
    """
    name = 'africas-talking.sms.send_message'
    state_transition = True
    support_recon = True
    event_name = 'send_africastalking_message'

    def execute(self, params):
        self.logger.info(event='{}_start'.format(self.event_name))
        return dict()
