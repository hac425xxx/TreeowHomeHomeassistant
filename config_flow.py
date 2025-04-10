"""Config flow for ShuXinFeng Device."""
from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult

from .const import (
    CONF_USERNAME,
    CONF_PASSWORD,
    DEFAULT_NAME,
    DOMAIN,
)

class ShuXinFengConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for ShuXinFeng Device."""
    
    VERSION = 1
    
    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors = {}
        
        if user_input is not None:
            # Validate input
            if len(user_input[CONF_USERNAME]) > 0 and len(user_input[CONF_PASSWORD]) > 0:
                # Check if device is already configured
                await self.async_set_unique_id(user_input[CONF_PASSWORD])
                self._abort_if_unique_id_configured()
                
                return self.async_create_entry(
                    title=DEFAULT_NAME,
                    data=user_input,
                )
            errors["base"] = "invalid_auth"
            
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_USERNAME): str,
                vol.Required(CONF_PASSWORD): str,
            }),
            errors=errors,
        )