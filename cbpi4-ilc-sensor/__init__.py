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
    #Property.Number(label="Continuous Interval", configurable=True, description="Refresh interval in seconds used in continuous mode")


])
class ILCSensor(CBPiSensor):
    
    def __init__(self, cbpi, id, props):
        super(ILCSensor, self).__init__(cbpi, id, props)
        self.value = 0
        self.ip_ilc = self.props.get("IP ILC")
        self.variable_ilc = self.props.get("Sensor Variable")
        self.log_data(self.value)
        self.request_session = requests.Session()
        self.url = ""
        self.url_read = "http://" + self.ip_ilc + "/cgi-bin/readVal.exe?"
        
        #http://192.168.1.152/cgi-bin/readVal.exe?variable_ilc

    @action(key="Test", parameters=[])
    async def action1(self, **kwargs):
        print("ACTION!", kwargs)

#Funktion starte Request---------------------------------------------------------------------------------------
    
    async def start_request(self, variableilc):

        url = self.url_read + variableilc

        logger.info("ILCReadData type=request_start url=\"%s\"" % (url))

        response = self.request_session.get(url)
        
        logger.info("ILCReadData type=request_done url=\"%s\" http_statuscode=%s response_text=\"%s\"" % (url, response.status_code, response.text.replace('"', '\\"')))
    
    
    
    async def run(self):
        while self.running is True:
            try:
                url = self.url_read + self.variable_ilc
                #await self.start_request(str(variable_ilc)) 
                response = self.request_session.get(url)
                self.value = float(response.text)
                self.push_update(self.value)
            except Exception as e:
                pass
            await asyncio.sleep(2)
    
    def get_state(self):
        return dict(value=self.value)


def setup(cbpi):
    cbpi.plugin.register("ILC Sensor", ILCSensor)
    pass
