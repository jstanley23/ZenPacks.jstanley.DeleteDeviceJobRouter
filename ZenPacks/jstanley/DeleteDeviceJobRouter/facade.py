from zope.interface import implements

from Products.Jobber.facade import FacadeMethodJob

from Products.Zuul.facades import ZuulFacade
from Products.Zuul.interfaces import IFacade

from Products.Zuul.decorators import info

from ZenPacks.jstanley.DeleteDeviceJobRouter.jobs import DeleteDeviceJob

class IDeleteDevicesFacade(IFacade):
    '''
    New JobsRouter API interface
    '''
    def deleteDevices(self, uids, deleteEvents):
        '''
        Delete a batch of devices using Uids
        '''


class DeleteDevicesFacade(ZuulFacade):
    '''
    DeleteDevice API implementation
    '''
    implements(IDeleteDevicesFacade)

    @info
    def deleteDevices(self, uids, deleteEvents=True):
        jobIds = []
        for uid in uids:
            jobId = self._dmd.JobManager.addJob(
                DeleteDeviceJob, description="Deleting %s" % (uid),
                kwargs=dict(
                    uid=uid,
                    deleteEvents=deleteEvents,
            ))
            jobIds.append(jobId)

        return (True, jobIds)
