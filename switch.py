"""Support for ShuXinFeng Device switches."""
import logging
from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from datetime import timedelta


from .const import *
from .device import ShuXinFengDevice

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the switch platform."""

    device = hass.data[DOMAIN][entry.entry_id]
    # Add switch entity
    async_add_entities([ShuXinFengSwitch(device, entry)])

class ShuXinFengSwitch(SwitchEntity):
    """Representation of a ShuXinFeng Device switch."""

    SCAN_INTERVAL = timedelta(seconds=1)  # 改为每分钟更新一次

    
    def __init__(self, device: ShuXinFengDevice, entry: ConfigEntry):
        """Initialize the switch."""
        self._device = device
        self._entry = entry
        self._attr_name = self._device.get_name()
        self._attr_unique_id = entry.entry_id
        self._state = self._device.is_open()

    @property
    def is_on(self) -> bool:
        """Return true if device is on."""
        self._state = self._device.is_open()
        return self._state

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the device on."""
        if await self.hass.async_add_executor_job(self._device.open):
            self._state = True
            self.async_write_ha_state()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the device off."""
        if await self.hass.async_add_executor_job(self._device.close):
            self._state = False
            self.async_write_ha_state()

    async def async_update(self):
        """从设备同步开关状态"""
        try:
            if await self.hass.async_add_executor_job(self._device.update_props):
                self._state = self._device.is_open()
                self.async_write_ha_state()
        except Exception as e:
            _LOGGER.error("Failed to update switch state: %s", e)


    @property
    def device_info(self) -> DeviceInfo:
        """Return device info."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._entry.entry_id)},
            name=self._device.get_name(),
            manufacturer="ShuXinFeng"
        )