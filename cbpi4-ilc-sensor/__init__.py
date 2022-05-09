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


@parameters([Property.Text(label="IP_ILC", configurable=True, default_value="192.168.1.152"), 
             Property.Text(label="Variable_ILC", configurable=True, default_value="ANALOG_KG.WP_DS")
            ])


   class CustomSensor(CBPiSensor):
    
    def __init__(self, cbpi, id, props):
    
        super(CustomSensor, self).__init__(cbpi, id, props)
        self.value = 0

    
    @action(key="Test", parameters=[])
    async def action1(self, **kwargs):
     
    self.ip_ilc = self.props.get("IP_ILC")
    self.variable_ilc = self.props.get("Variable_ILC") 
      
      print("ACTION!", kwargs)

    async def run(self):

        while self.running is True:
            self.value = random.randint(0,50)
            self.push_update(self.value)
            await asyncio.sleep(1)
    
    def get_state(self):
        # return the current state of the sensor
        return dict(value=self.value)


def setup(cbpi):
    cbpi.plugin.register("ILC Sensor", CustomSensor)
    pass
