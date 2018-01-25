from django.views.generic import TemplateView
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from utils.bluetooth_interface import BluetoothController

class ControlIndex(TemplateView):
    template_name = 'index.html'


@method_decorator(csrf_exempt, name='dispatch')
class ControlActions(View):
    def post(self, request, *args, **kwargs):
        action_control = request.POST['action']
        mac_address = request.POST['mac']
        bt = BluetoothController(mac_address, 1)
        if action_control == 'on':
            bt.on()
        else:
            bt.off()
        return HttpResponse('')
