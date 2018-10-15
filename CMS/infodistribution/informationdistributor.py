from utilities.incidentstatus import IncidentStatus
from .statusreportgenerator import StatusReportGenerator
from .socialmediaalerter import SocialMediaAlerter
from .dispatcher import Dispatcher



class InformationDistributor:
    """
    Distributes messages to the appropriate component of the subsystem
    for information distribution.
    """

    def __init__(self):
        """
        Only incidents with the status NEW shall be dispatched to a department
        and needs to be notified to the status report generator.
        """
        self.new_incident_observers = [Dispatcher(),
                                       StatusReportGenerator(1800.0)]

        """
        All incident status updates shall be included in social medias alerts.
        """
        self.incident_status_observers = [SocialMediaAlerter()]


    def distribute(self, message):
        """
        Distributes the given message to all observers of that Incident Status.
        """
        if message.incident_status == IncidentStatus.NEW:
            for observer in self.new_incident_observers:
                observer.notify(message)

        for observer in self.incident_status_observers:
            observer.notify(message)
