"""The ShuXinFeng Device integration."""
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .device import ShuXinFengDevice

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the component from YAML configuration."""
    # This allows YAML configuration but doesn't actually do anything with it
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    # Create device instance
    device = ShuXinFengDevice(entry.data["username"], entry.data["password"])
    await hass.async_add_executor_job(device.login)
    await hass.async_add_executor_job(device.init_device_info)

    hass.data[DOMAIN][entry.entry_id] = device


    # Forward to switch platform
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "switch")
    )
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    await hass.config_entries.async_forward_entry_unload(entry, "switch")
    await hass.config_entries.async_forward_entry_unload(entry, "sensor")

    hass.data[DOMAIN].pop(entry.entry_id)
    return True