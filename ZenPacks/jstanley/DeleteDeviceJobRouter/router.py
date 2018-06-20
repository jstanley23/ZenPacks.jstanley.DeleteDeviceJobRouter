from Products import Zuul
from Products.ZenUtils.Ext import DirectRouter, DirectResponse


class DeleteDevicesRouter(DirectRouter):
    """
    Router for deleting devices using jobs
    """
    def __init__(self, context, request):
        self.facade = Zuul.getFacade('deletedevices', context.dmd)
        self.context = context
        self.request = request
        super(DirectRouter, self).__init__(context, request)


    def deleteDevices(self, uids, deleteEvents=True):
        """
        Delete devices using a job
        """
        success, data = self.facade.deleteDevices(uids, deleteEvents)
        if success:
            return DirectResponse.succeed(data=Zuul.marshal(data))
        else:
            return DirectResponse.fail(msg=data)
