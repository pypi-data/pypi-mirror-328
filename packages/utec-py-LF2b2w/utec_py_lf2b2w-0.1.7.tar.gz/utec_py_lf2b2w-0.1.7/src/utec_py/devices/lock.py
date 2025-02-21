"""Abstraction layer for device interaction - Lock."""

from .device import BaseDevice
from .device_const import DeviceCapability, DeviceCategory, DeviceCommand, LockState


class Lock(BaseDevice):
    """Represents a Switch device in the U-Home API.

    Maps to Home Assistant's switch platform.
    """

    @property
    def has_door_sensor(self) -> bool:
        """Check if the lock has a door sensor capability."""
        return self.has_capability(DeviceCapability.DOOR_SENSOR)

    @property
    def door_state(self) -> str | None:
        """Get the door state if door sensor is present."""
        if not self.has_door_sensor:
            return None
        return self._get_state_value(DeviceCapability.DOOR_SENSOR, "sensorState")

    @property
    def category(self) -> DeviceCategory:
        """Get the device category."""
        return DeviceCategory.LOCK

    @property
    def lock_state(self) -> LockState:
        """Get the current lock state."""
        state = self._get_state_value(DeviceCapability.LOCK, "lockState")
        return LockState(state) if state else LockState.UNKNOWN

    @property
    def battery_level(self) -> int | None:
        """Get the current battery level (0-100)."""
        return self._get_state_value(DeviceCapability.BATTERY_LEVEL, "level")

    @property
    def is_locked(self) -> bool:
        """Check if the lock is in locked state."""
        return self.lock_state == LockState.LOCKED

    @property
    def is_door_closed(self) -> bool | None:
        """Check if the door is closed (binary sensor)."""
        if not self.has_door_sensor:
            return None
        return self.door_state == "closed"

    async def lock(self) -> None:
        """Lock the device."""
        command = DeviceCommand(capability=DeviceCapability.LOCK, name="lock")
        await self.send_command(command)

    async def unlock(self) -> None:
        """Unlock the device."""
        command = DeviceCommand(capability=DeviceCapability.LOCK, name="unlock")
        await self.send_command(command)

    async def update(self) -> None:
        """Update device state."""
        await super().update()
