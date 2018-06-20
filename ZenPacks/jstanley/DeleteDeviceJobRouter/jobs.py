from ZODB.transact import transact
from Products.Jobber.jobs import Job

from Products.Zuul import getFacade

class DeleteDeviceJob(Job):
    """
    """

    @classmethod
    def getJobType(cls):
        return "Delete Device"

    @classmethod
    def getJobDescription(cls, *args, **kwargs):
        return "Delete device: {uid}".format(**kwargs)

    def _run(self, uid, **kwargs):
        deleteEvents = kwargs.get('deleteEvents', True)
        result = self._deleteDevice(uid, deleteEvents)
        self.log.info(result)

    @transact
    def _deleteDevice(self, uid, deleteEvents=True):
        facade = getFacade('device')
        try:
            result = facade.deleteDevices([uid], deleteEvents=deleteEvents)
        except Exception as e:
            result = "Unable to device device {0}. {1}".format(uid, e.message)

        return result
