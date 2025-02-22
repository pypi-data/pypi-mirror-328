"""
Trossen SLATE Python Bindings
"""
from __future__ import annotations
import pybind11_stubgen.typing_ext
import typing
import typing_extensions
__all__ = ['BLUE', 'BLUE_FLASH', 'CYAN', 'CYAN_FLASH', 'ChassisData', 'GREEN', 'GREEN_FLASH', 'LightState', 'OFF', 'PURPLE', 'PURPLE_FLASH', 'RED', 'RED_FLASH', 'TrossenSlate', 'WHITE', 'WHITE_FLASH', 'YELLOW', 'YELLOW_FLASH']
class ChassisData:
    charge: int
    cmd: int
    cmd_vel_x: float
    cmd_vel_y: float
    cmd_vel_z: float
    current: float
    err: int
    io: int
    light_state: int
    odom_x: float
    odom_y: float
    odom_z: float
    system_state: int
    vel_x: float
    vel_y: float
    vel_z: float
    voltage: float
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
class LightState:
    """
    Members:
    
      OFF
    
      RED
    
      GREEN
    
      YELLOW
    
      BLUE
    
      PURPLE
    
      CYAN
    
      WHITE
    
      RED_FLASH
    
      GREEN_FLASH
    
      YELLOW_FLASH
    
      BLUE_FLASH
    
      PURPLE_FLASH
    
      CYAN_FLASH
    
      WHITE_FLASH
    """
    BLUE: typing.ClassVar[LightState]  # value = <LightState.BLUE: 4>
    BLUE_FLASH: typing.ClassVar[LightState]  # value = <LightState.BLUE_FLASH: 12>
    CYAN: typing.ClassVar[LightState]  # value = <LightState.CYAN: 6>
    CYAN_FLASH: typing.ClassVar[LightState]  # value = <LightState.CYAN_FLASH: 14>
    GREEN: typing.ClassVar[LightState]  # value = <LightState.GREEN: 2>
    GREEN_FLASH: typing.ClassVar[LightState]  # value = <LightState.GREEN_FLASH: 10>
    OFF: typing.ClassVar[LightState]  # value = <LightState.OFF: 0>
    PURPLE: typing.ClassVar[LightState]  # value = <LightState.PURPLE: 5>
    PURPLE_FLASH: typing.ClassVar[LightState]  # value = <LightState.PURPLE_FLASH: 13>
    RED: typing.ClassVar[LightState]  # value = <LightState.RED: 1>
    RED_FLASH: typing.ClassVar[LightState]  # value = <LightState.RED_FLASH: 9>
    WHITE: typing.ClassVar[LightState]  # value = <LightState.WHITE: 7>
    WHITE_FLASH: typing.ClassVar[LightState]  # value = <LightState.WHITE_FLASH: 15>
    YELLOW: typing.ClassVar[LightState]  # value = <LightState.YELLOW: 3>
    YELLOW_FLASH: typing.ClassVar[LightState]  # value = <LightState.YELLOW_FLASH: 11>
    __members__: typing.ClassVar[dict[str, LightState]]  # value = {'OFF': <LightState.OFF: 0>, 'RED': <LightState.RED: 1>, 'GREEN': <LightState.GREEN: 2>, 'YELLOW': <LightState.YELLOW: 3>, 'BLUE': <LightState.BLUE: 4>, 'PURPLE': <LightState.PURPLE: 5>, 'CYAN': <LightState.CYAN: 6>, 'WHITE': <LightState.WHITE: 7>, 'RED_FLASH': <LightState.RED_FLASH: 9>, 'GREEN_FLASH': <LightState.GREEN_FLASH: 10>, 'YELLOW_FLASH': <LightState.YELLOW_FLASH: 11>, 'BLUE_FLASH': <LightState.BLUE_FLASH: 12>, 'PURPLE_FLASH': <LightState.PURPLE_FLASH: 13>, 'CYAN_FLASH': <LightState.CYAN_FLASH: 14>, 'WHITE_FLASH': <LightState.WHITE_FLASH: 15>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class TrossenSlate:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def enable_charging(self, enable: bool) -> tuple[bool, str]:
        """
              @brief Enable/disable charging
        
              @param enable Whether to enable charging or not
              @return A pair (bool, string) indicating success and the resulting output string
        """
    def enable_motor_torque(self, enable: bool) -> tuple[bool, str]:
        """
              @brief Enable/disable motor torque
        
              @param enable Whether to enable motor torque or not
              @return A pair (bool, string) indicating success and the resulting output string
        """
    def get_charge(self) -> int:
        """
              @brief Get the current charge percentage
        
              @return The current charge
        """
    def get_current(self) -> float:
        """
              @brief Get the current motor current in amps
        
              @return The current motor current
        """
    def get_pose(self) -> typing_extensions.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
        """
              @brief Get the current pose in meters (x,y) and radians (theta)
        
              @return The current pose [x, y, theta]
        """
    def get_vel(self) -> typing_extensions.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(2)]:
        """
              @brief Get the current velocity in meters per seconds (linear) and radians per seconds (angular)
        
              @return The current velocity [linear velocity, angular velocity]
        """
    def get_voltage(self) -> float:
        """
              @brief Get the current voltage in volts
        
              @return The current voltage
        """
    def init_base(self) -> tuple[bool, str]:
        """
              @brief Initializes the SLATE base
        
              @param result The resulting output string
              @return true if succeeded, false otherwise
        """
    def read(self, data: ChassisData) -> None:
        """
              @brief Read data from the SLATE base
        
              @param data The desired data reference to update with current data
              @return true if succeeded, false otherwise
        """
    def set_cmd_vel(self, linear: float, angular: float) -> bool:
        """
              @brief Set velocity commands in meters per seconds (linear) and radians per seconds (angular)
        
              @param linear The desired linear velocity
              @param angular The desired angular velocity
              @return true if succeeded, false otherwise
        """
    def set_light_state(self, light_state: LightState) -> bool:
        """
              @brief Set light state
        
              @param light_state The desired light state
              @return true if succeeded, false otherwise
        """
    def set_text(self, text: str) -> bool:
        """
              @brief Set text on screen
        
              @param text The desired text
              @return true if succeeded, false otherwise
        """
    def update_state(self) -> bool:
        """
              @brief Update the state of the SLATE base
        
              @return true if succeeded, false otherwise
        """
    def write(self, data: ChassisData) -> bool:
        """
              @brief Write data to the SLATE base
        
              @param data The desired data to write
              @return true if succeeded, false otherwise
        """
BLUE: LightState  # value = <LightState.BLUE: 4>
BLUE_FLASH: LightState  # value = <LightState.BLUE_FLASH: 12>
CYAN: LightState  # value = <LightState.CYAN: 6>
CYAN_FLASH: LightState  # value = <LightState.CYAN_FLASH: 14>
GREEN: LightState  # value = <LightState.GREEN: 2>
GREEN_FLASH: LightState  # value = <LightState.GREEN_FLASH: 10>
OFF: LightState  # value = <LightState.OFF: 0>
PURPLE: LightState  # value = <LightState.PURPLE: 5>
PURPLE_FLASH: LightState  # value = <LightState.PURPLE_FLASH: 13>
RED: LightState  # value = <LightState.RED: 1>
RED_FLASH: LightState  # value = <LightState.RED_FLASH: 9>
WHITE: LightState  # value = <LightState.WHITE: 7>
WHITE_FLASH: LightState  # value = <LightState.WHITE_FLASH: 15>
YELLOW: LightState  # value = <LightState.YELLOW: 3>
YELLOW_FLASH: LightState  # value = <LightState.YELLOW_FLASH: 11>
