"""Constants for ShuXinFeng Device integration."""
DOMAIN = "shuxinfeng_device"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

DEFAULT_NAME = "ShuXinFeng Device"

# Sensor types
SENSOR_TYPES = {
    "power_state": ["Power State", None, "mdi:power", "state"],
    "wind_speed": ["Wind Speed", "m/s", "mdi:weather-windy", "measurement"],
    "temperature": ["Temperature", "°C", "mdi:thermometer", "measurement"],
    "hcho": ["Formaldehyde", "mg/m³", "mdi:chemical-weapon", "measurement"],
    "last_update": ["Last Update", None, "mdi:clock", "timestamp"],
}




GLOBAL_CONF = {"token": "", "last_update_time": 0}