"""Climate object """

from typing import Union, cast

from pyhilo import API
from pyhilo.const import LOG
from pyhilo.device import HiloDevice


class Climate(HiloDevice):
    def __init__(self, api: API, **kwargs: dict[str, Union[str, int]]):
        super().__init__(api, **kwargs)  # type: ignore
        LOG.debug(f"Setting up Climate device: {self.name}")

    @property
    def current_temperature(self) -> float:
        return cast(float, self.get_value("current_temperature", 0))

    @property
    def target_temperature(self) -> float:
        return cast(float, self.get_value("target_temperature", 0))

    @property
    def max_temp(self) -> float:
        value = self.get_value("max_temp_setpoint", 0)

        if value is None or value == 0:
            return 36.0
        return float(value)

    @property
    def min_temp(self) -> float:
        value = self.get_value("min_temp_setpoint", 0)

        if value is None or value == 0:
            return 5.0
        return float(value)

    @property
    def hvac_action(self) -> str:
        attr = self.get_value("heating", 0)
        return "heating" if attr > 0 else "idle"

    async def async_set_temperature(self, **kwargs: dict[str, int]) -> None:
        temperature = kwargs.get("temperature", 0)
        if temperature:
            LOG.info(f"{self._tag} Setting temperature to {temperature}")
            await self.set_attribute("target_temperature", temperature)  # type: ignore
