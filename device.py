"""ShuXinFeng Device API wrapper."""
import logging

_LOGGER = logging.getLogger(__name__)

import requests

import json
import time
import hashlib

class AirPurifier:
    def __init__(self, data=None):
        # Initialize all properties with default values
        self.sensor_onoff = False
        self.anion_timestamp = 0
        self.temp_indoor = 0
        self.sensor_onoff_timestamp = 0
        self.smart_mode_switch = False
        self.screen_set_timestamp = 0
        self.humidity_timestamp = 0
        self.mode = 0
        self.child_lock_timestamp = 0
        self.filter_life = 0
        self.runtime_total = 0
        self.wifi_info_timestamp = 0
        self.filter_warn = 0
        self.humidity = 0
        self.mode_timestamp = 0
        self.uv = False
        self.time_plan_timestamp = 0
        self.screen_set = 0
        self.smart_hcho_off = 0
        self.child_lock = False
        self.smart_mode_switch_timestamp = 0
        self.smart_hcho = 0
        self.anion = False
        self.filter_days_timestamp = 0
        self.online_state = 0
        self.pm25 = 0
        self.light = False
        self.filter_reset_timestamp = 0
        self.pm25_timestamp = 0
        self.switch_timestamp = 0
        self.online_state_timestamp = 0
        self.fan_speed_enum = 0
        self.timestamp_timestamp = 0
        self.filter_reset = False
        self.aal = 0
        self.switch = False
        self.smart_hcho_timestamp = 0
        self.filter_days = 0
        self.filter_warn_reset_timestamp = 0
        self.smart_fan_speed_timestamp = 0
        self.smart_pm25_off = 0
        self.runtime_total_timestamp = 0
        self.smart_pm25_timestamp = 0
        self.uv_timestamp = 0
        self.aal_timestamp = 0
        self.timestamp = "0"
        self.ch2o_value = 0
        self.filter_warn_timestamp = 0
        self.smart_hcho_off_timestamp = 0
        self.temp_indoor_timestamp = 0
        self.filter_life_timestamp = 0
        self.ch2o_value_timestamp = 0
        self.wifi_info = ""
        self.filter_warn_reset = 0
        self.smart_pm25 = 0
        self.smart_fan_speed = 0
        self.time_plan = []
        self.speaker_onoff = False
        self.speaker_onoff_timestamp = 0
        self.smart_pm25_off_timestamp = 0
        self.light_timestamp = 0
        self.fan_speed_enum_timestamp = 0

        if data:
            self.from_json(data)

    def from_json(self, json_data):
        # Handle both JSON string and dict input
        if isinstance(json_data, str):
            data = json.loads(json_data)
        else:
            data = json_data

        if "Air_Purifier" in data:
            air_purifier_data = data["Air_Purifier"]

            # Map JSON properties to class attributes
            self.sensor_onoff = air_purifier_data.get("sensor_onoff", False)
            self.anion_timestamp = air_purifier_data.get("anion&timestamp", 0)
            self.temp_indoor = air_purifier_data.get("temp_indoor", 0)
            self.sensor_onoff_timestamp = air_purifier_data.get("sensor_onoff&timestamp", 0)
            self.smart_mode_switch = air_purifier_data.get("smart_mode_switch", False)
            self.screen_set_timestamp = air_purifier_data.get("screen_set&timestamp", 0)
            self.humidity_timestamp = air_purifier_data.get("humidity&timestamp", 0)
            self.mode = air_purifier_data.get("mode", 0)
            self.child_lock_timestamp = air_purifier_data.get("child_lock&timestamp", 0)
            self.filter_life = air_purifier_data.get("filter_life", 0)
            self.runtime_total = air_purifier_data.get("runtime_total", 0)
            self.wifi_info_timestamp = air_purifier_data.get("wifi_info&timestamp", 0)
            self.filter_warn = air_purifier_data.get("filter_warn", 0)
            self.humidity = air_purifier_data.get("humidity", 0)
            self.mode_timestamp = air_purifier_data.get("mode&timestamp", 0)
            self.uv = air_purifier_data.get("uv", False)
            self.time_plan_timestamp = air_purifier_data.get("time_plan&timestamp", 0)
            self.screen_set = air_purifier_data.get("screen_set", 0)
            self.smart_hcho_off = air_purifier_data.get("smart_hcho_off", 0)
            self.child_lock = air_purifier_data.get("child_lock", False)
            self.smart_mode_switch_timestamp = air_purifier_data.get("smart_mode_switch&timestamp", 0)
            self.smart_hcho = air_purifier_data.get("smart_hcho", 0)
            self.anion = air_purifier_data.get("anion", False)
            self.filter_days_timestamp = air_purifier_data.get("filter_days&timestamp", 0)
            self.online_state = air_purifier_data.get("online_state", 0)
            self.pm25 = air_purifier_data.get("pm25", 0)
            self.light = air_purifier_data.get("light", False)
            self.filter_reset_timestamp = air_purifier_data.get("filter_reset&timestamp", 0)
            self.pm25_timestamp = air_purifier_data.get("pm25&timestamp", 0)
            self.switch_timestamp = air_purifier_data.get("switch&timestamp", 0)
            self.online_state_timestamp = air_purifier_data.get("online_state&timestamp", 0)
            self.fan_speed_enum = air_purifier_data.get("fan_speed_enum", 0)
            self.timestamp_timestamp = air_purifier_data.get("timestamp&timestamp", 0)
            self.filter_reset = air_purifier_data.get("filter_reset", False)
            self.aal = air_purifier_data.get("aal", 0)
            self.switch = air_purifier_data.get("switch", False)
            self.smart_hcho_timestamp = air_purifier_data.get("smart_hcho&timestamp", 0)
            self.filter_days = air_purifier_data.get("filter_days", 0)
            self.filter_warn_reset_timestamp = air_purifier_data.get("filter_warn_reset&timestamp", 0)
            self.smart_fan_speed_timestamp = air_purifier_data.get("smart_fan_speed&timestamp", 0)
            self.smart_pm25_off = air_purifier_data.get("smart_pm25_off", 0)
            self.runtime_total_timestamp = air_purifier_data.get("runtime_total&timestamp", 0)
            self.smart_pm25_timestamp = air_purifier_data.get("smart_pm25&timestamp", 0)
            self.uv_timestamp = air_purifier_data.get("uv&timestamp", 0)
            self.aal_timestamp = air_purifier_data.get("aal&timestamp", 0)
            self.timestamp = air_purifier_data.get("timestamp", "0")
            self.ch2o_value = air_purifier_data.get("ch2o_value", 0)
            self.filter_warn_timestamp = air_purifier_data.get("filter_warn&timestamp", 0)
            self.smart_hcho_off_timestamp = air_purifier_data.get("smart_hcho_off&timestamp", 0)
            self.temp_indoor_timestamp = air_purifier_data.get("temp_indoor&timestamp", 0)
            self.filter_life_timestamp = air_purifier_data.get("filter_life&timestamp", 0)
            self.ch2o_value_timestamp = air_purifier_data.get("ch2o_value&timestamp", 0)
            self.wifi_info = air_purifier_data.get("wifi_info", "")
            self.filter_warn_reset = air_purifier_data.get("filter_warn_reset", 0)
            self.smart_pm25 = air_purifier_data.get("smart_pm25", 0)
            self.smart_fan_speed = air_purifier_data.get("smart_fan_speed", 0)
            self.time_plan = air_purifier_data.get("time_plan", [])
            self.speaker_onoff = air_purifier_data.get("speaker_onoff", False)
            self.speaker_onoff_timestamp = air_purifier_data.get("speaker_onoff&timestamp", 0)
            self.smart_pm25_off_timestamp = air_purifier_data.get("smart_pm25_off&timestamp", 0)
            self.light_timestamp = air_purifier_data.get("light&timestamp", 0)
            self.fan_speed_enum_timestamp = air_purifier_data.get("fan_speed_enum&timestamp", 0)

    def to_json(self):
        """Convert the object back to a JSON string"""
        data = {
            "Air_Purifier": {
                "sensor_onoff": self.sensor_onoff,
                "anion&timestamp": self.anion_timestamp,
                "temp_indoor": self.temp_indoor,
                "sensor_onoff&timestamp": self.sensor_onoff_timestamp,
                "smart_mode_switch": self.smart_mode_switch,
                "screen_set&timestamp": self.screen_set_timestamp,
                "humidity&timestamp": self.humidity_timestamp,
                "mode": self.mode,
                "child_lock&timestamp": self.child_lock_timestamp,
                "filter_life": self.filter_life,
                "runtime_total": self.runtime_total,
                "wifi_info&timestamp": self.wifi_info_timestamp,
                "filter_warn": self.filter_warn,
                "humidity": self.humidity,
                "mode&timestamp": self.mode_timestamp,
                "uv": self.uv,
                "time_plan&timestamp": self.time_plan_timestamp,
                "screen_set": self.screen_set,
                "smart_hcho_off": self.smart_hcho_off,
                "child_lock": self.child_lock,
                "smart_mode_switch&timestamp": self.smart_mode_switch_timestamp,
                "smart_hcho": self.smart_hcho,
                "anion": self.anion,
                "filter_days&timestamp": self.filter_days_timestamp,
                "online_state": self.online_state,
                "pm25": self.pm25,
                "light": self.light,
                "filter_reset&timestamp": self.filter_reset_timestamp,
                "pm25&timestamp": self.pm25_timestamp,
                "switch&timestamp": self.switch_timestamp,
                "online_state&timestamp": self.online_state_timestamp,
                "fan_speed_enum": self.fan_speed_enum,
                "timestamp&timestamp": self.timestamp_timestamp,
                "filter_reset": self.filter_reset,
                "aal": self.aal,
                "switch": self.switch,
                "smart_hcho&timestamp": self.smart_hcho_timestamp,
                "filter_days": self.filter_days,
                "filter_warn_reset&timestamp": self.filter_warn_reset_timestamp,
                "smart_fan_speed&timestamp": self.smart_fan_speed_timestamp,
                "smart_pm25_off": self.smart_pm25_off,
                "runtime_total&timestamp": self.runtime_total_timestamp,
                "smart_pm25&timestamp": self.smart_pm25_timestamp,
                "uv&timestamp": self.uv_timestamp,
                "aal&timestamp": self.aal_timestamp,
                "timestamp": self.timestamp,
                "ch2o_value": self.ch2o_value,
                "filter_warn&timestamp": self.filter_warn_timestamp,
                "smart_hcho_off&timestamp": self.smart_hcho_off_timestamp,
                "temp_indoor&timestamp": self.temp_indoor_timestamp,
                "filter_life&timestamp": self.filter_life_timestamp,
                "ch2o_value&timestamp": self.ch2o_value_timestamp,
                "wifi_info": self.wifi_info,
                "filter_warn_reset": self.filter_warn_reset,
                "smart_pm25": self.smart_pm25,
                "smart_fan_speed": self.smart_fan_speed,
                "time_plan": self.time_plan,
                "speaker_onoff": self.speaker_onoff,
                "speaker_onoff&timestamp": self.speaker_onoff_timestamp,
                "smart_pm25_off&timestamp": self.smart_pm25_off_timestamp,
                "light&timestamp": self.light_timestamp,
                "fan_speed_enum&timestamp": self.fan_speed_enum_timestamp
            }
        }
        return json.dumps(data, indent=2)

    def __str__(self):
        return f"AirPurifier: mode={self.mode}, pm25={self.pm25}, temp={self.temp_indoor}°C, humidity={self.humidity}%"

class ShuXinFengDevice:
    """Wrapper for ShuXinFeng device API."""
    
    def __init__(self, username, passwd):
        """Initialize the device."""
        self.username = username
        self.passwd = passwd.encode()
        self.authorization = "N/A"
        self.device_serial = "N/A"
        self.last_login_time = 0
        self._available = True
        self.props = AirPurifier()
        self.on_off_datetime = "N/A"
        self.version = "N/A"

        _LOGGER.warning("init dev {} {}", username, passwd)


    def modify_device_switch(self, v):
        url = "https://eziotes.treeow.com.cn/api/resource/v3/device/otap/prop"
        headers = {
            "Accept-Encoding": "gzip",
            "Authorization": self.authorization,
            "Connection": "Keep-Alive",
            "Content-Type": "application/json; charset=utf-8",
            "Host": "eziotes.treeow.com.cn",
            "User-Agent": "okhttp/3.14.9",
            "clientType": "3",
            "deviceSerial": self.device_serial,
            "domainIdentifier": "Air_Purifier",
            "localIndex": "0",
            "propIdentifier": "switch",
            "resourceCategory": "default"
        }
        data = {"value": v}

        response = requests.put(url, headers=headers, json=data)
        return response.json()

    def query_device_infomation(self):
        url = "https://eziotes.treeow.com.cn/api/resource/device/info"
        headers = {
            "Accept-Encoding": "gzip",
            "Authorization": self.authorization,
            "Connection": "Keep-Alive",
            "Content-Type": "application/json; charset=utf-8",
            "Host": "eziotes.treeow.com.cn",
            "User-Agent": "okhttp/3.14.9",
            "clientType": "3",
        }
        payload = {"deviceSerial": self.device_serial}  # 请求体数据

        response = requests.post(url, headers=headers, json=payload)
        return response.json()


    def get_default_group_id(self):
        url = "https://eziotes.treeow.com.cn/api/resource/home/list"
        headers = {
            "Accept-Encoding": "gzip",
            "Authorization": self.authorization,
            "Connection": "Keep-Alive",
            "Content-Type": "application/json; charset=utf-8",
            "Host": "eziotes.treeow.com.cn",
            "User-Agent": "okhttp/3.14.9",
            "clientType": "3",
        }

        response = requests.post(url, headers=headers)
        home_info = response.json()
        home_groups = home_info['data'][0]['homeGroups']
        for g in home_groups:
            if g['defaultGroup'] == 1:
                return g['id']
        return 0

    def get_device_in_group(self, gid):
        url = "https://eziotes.treeow.com.cn/api/resource/v3/device/list/page"
        headers = {
            "Accept-Encoding": "gzip",
            "Authorization": self.authorization,
            "Connection": "Keep-Alive",
            "Content-Type": "application/json; charset=utf-8",
            "Host": "eziotes.treeow.com.cn",
            "User-Agent": "okhttp/3.14.9",
            "clientType": "3",
        }
        json = {"pageNo": 1, "pageSize": 50, "groupId": "{}".format(gid)}
        response = requests.post(url, headers=headers, json=json)
        device = response.json()['data'][0]
        return device

    def init_device_info(self):
        try:
            self.refresh_token()
            dev = self.get_device_in_group(self.get_default_group_id())
            self.device_serial = dev['deviceSerial']
            self.on_off_datetime = dev['onOfflineDateTime']
            self.version = dev['version']
            self.device_name = dev['deviceName']
        except Exception as e:
            _LOGGER.warning("init device infomation failed {}".format(str(e)))

    def get_name(self):
        return self.device_name
 
    def open(self) -> bool:
        """Open the device."""
        return self.modify_device_switch(True)
        
    def close(self) -> bool:
        """Close the device."""
        return self.modify_device_switch(False)

    def update_props(self):

        self.refresh_token()
        info = self.query_device_infomation()
        props = info['data']['props'][0]['value']
        self.props.from_json(props)

        self.init_device_info()

    def refresh_token(self):
        ct = int(time.time())
        if ct - self.last_login_time > 60 * 30:
            self.login()

        
    def login(self):

        try:
            url = "https://eziotes.treeow.com.cn/api/user/account/login"

            headers = {
                "Accept-Encoding": "gzip",
                "Connection": "Keep-Alive",
                "Content-Type": "application/json; charset=utf-8",
                "Host": "eziotes.treeow.com.cn",
                "User-Agent": "okhttp/3.14.9",
                "clientType": "3"
            }

            md5hash = hashlib.md5(self.passwd)
            md5 = md5hash.hexdigest()

            data = {
                "account": self.username,
                "password": md5,
                "terminalIdentifier": "0de26605de863fb984666682c8169c23",
                "terminalName": "SM-G977N"
            }

            response = requests.post(url, headers=headers, json=data)
            res = response.json()
            data = res['data']
            token = data['accessToken']
            self.authorization = "Bearer " + token

            self.last_login_time = int(time.time())
        except Exception as e:
            _LOGGER.warning("login error: " + str(e))

    def is_open(self) -> bool:
        """Check if device is open.
        
        Note: You'll need to implement actual status checking
        """
        return self.props.switch
    
    def get_temp(self):
        return self.props.temp_indoor
    
    def get_fan(self):
        return self.props.fan_speed_enum
    
    def get_timestamp(self):
        """Check if device is open.
        
        Note: You'll need to implement actual status checking
        """
        return self.props.ch2o_value_timestamp
    
    def get_ch2o(self):
        return self.props.ch2o_value
        
    @property
    def available(self) -> bool:
        """Return if device is available."""
        return self._available