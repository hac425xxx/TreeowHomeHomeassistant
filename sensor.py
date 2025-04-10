"""Support for ShuXinFeng Device sensors."""
from __future__ import annotations

import logging
from datetime import datetime
from typing import Any
from datetime import timedelta

from homeassistant.components.sensor import (
    SensorEntity,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import *
from .device import ShuXinFengDevice

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    device = hass.data[DOMAIN][entry.entry_id] 
    
    sensors = [
        ShuXinFengSensor(device, entry, sensor_type)
        for sensor_type in SENSOR_TYPES
    ]

    sensors.append(DeviceInfoSensor(device))
    
    async_add_entities(sensors)

class ShuXinFengSensor(SensorEntity):
    """Representation of a ShuXinFeng Device sensor."""

    SCAN_INTERVAL = timedelta(seconds=1)  # 改为每分钟更新一次

    
    def __init__(
        self,
        device: ShuXinFengDevice,
        entry: ConfigEntry,
        sensor_type: str,
    ) -> None:
        """Initialize the sensor."""
        self._device = device
        self._entry = entry
        self._sensor_type = sensor_type
        self._attr_name = f"{self._device.get_name()} {SENSOR_TYPES[sensor_type][0]}"
        self._attr_unique_id = f"{entry.entry_id}_{sensor_type}"
        self._attr_icon = SENSOR_TYPES[sensor_type][2]
        self._attr_state_class = SENSOR_TYPES[sensor_type][3]
        self._attr_native_unit_of_measurement = SENSOR_TYPES[sensor_type][1]
        self._state = None
        
        # Set device class for specific sensors
        if sensor_type == "temperature":
            self._attr_device_class = SensorDeviceClass.TEMPERATURE
        elif sensor_type == "hcho":
            self._attr_device_class = SensorDeviceClass.VOLATILE_ORGANIC_COMPOUNDS
        
    @property
    def device_info(self) -> DeviceInfo:
        """Return device info."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._entry.entry_id)},
            name=self._device.get_name(),
            manufacturer="ShuXinFeng",
        )
    
    @property
    def native_value(self):
        return self._state
        
    async def async_update(self) -> None:
        """Fetch new state data for the sensor."""
        try:
            # In a real implementation, you would fetch these values from the device
            # For demonstration, we're using mock values
            device_data = {
                "power_state": 1 if self._device.is_open() else 0,
                "wind_speed": self._device.get_fan(),  # m/s
                "temperature": self._device.get_temp(),  # °C
                "hcho": self._device.get_ch2o() / 1000,  # mg/m³
                "last_update": self._device.get_timestamp(),
            }

            _LOGGER.warning("info {} {}".format(self._entry.entry_id, self._sensor_type))
            
            self._state = device_data.get(self._sensor_type)
            self.async_write_ha_state()
            
        except Exception as e:
            _LOGGER.error(f"Error updating sensor {self._sensor_type}: {e}")
            self._state = None




class DeviceInfoSensor(SensorEntity):
    """自定义文本传感器示例"""
    
    def __init__(self, device):
        self._device = device
        self._attr_unique_id = f"{self._device.get_name()} Name"
        self._attr_native_value = f"{self._device.get_name()} {self._device.device_serial}  {self._device.on_off_datetime}"
        self._attr_device_class = None  # 文本传感器通常不需要device_class
        self._attr_icon = "mdi:form-textbox"

    async def async_update(self):
        """示例更新逻辑"""
        self._attr_native_value = f"{self._device.get_name()} {self._device.device_serial}  {self._device.on_off_datetime}"
        self.async_write_ha_state()