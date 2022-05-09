# -*- coding: utf-8 -*-
import logging
import asyncio
import random
import re
import random
from aiohttp import web
from cbpi.api import *

import requests
from requests.auth import HTTPBasicAuth
import time

logger = logging.getLogger(__name__)


@parameters([

    Property.Text(label="IP ILC", configurable=True, description="IP Adress of ILC SPS (example: 192.168.1.150)", default_value="192.168.1.152"),
    Property.Text(label="Sensor Variable", configurable=True, description="Sensor Variable in SPS (example: SENSORS.SENSOR1", default_value="ANALOG_KG.WP_DS"),
    Property.Number(label="Continuous Interval", configurable=True, description="Refresh interval in seconds used in continuous mode")


])
class CustomSensor(CBPiSensor):
    
    def __init__(self, cbpi, id, props):
        super(CustomSensor, self).__init__(cbpi, id, props)
        self.value = 0

    @action(key="Test", parameters=[])
    async def action1(self, **kwargs):
        print("ACTION!", kwargs)

    async def run(self):
        while self.running is True:
            
            ip_ilc = self.props.get("IP ILC")
            variable_ilc = self.props.get("Sensor Variable")            
            url = "http://" + ip_ilc + "/cgi-bin/readVal.exe?" + variable_ilc
            r = requests.get(url)
            
            #self.value = random.randint(0,50)
            self.value = r.text
            self.push_update(self.value)
            await asyncio.sleep(5)
    
    def get_state(self):
        return dict(value=self.value)


def setup(cbpi):
    cbpi.plugin.register("ILC Sensor", CustomSensor)
    pass
