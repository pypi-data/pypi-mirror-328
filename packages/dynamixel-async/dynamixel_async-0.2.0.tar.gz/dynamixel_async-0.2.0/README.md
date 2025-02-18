# Dynamixel Async

A high-level Python library for controlling Dynamixel servos with async support and comprehensive control table definitions.

## Features

- Asynchronous API for better performance and control
- Complete control table definitions for XM430 series servos
- High-level abstractions for common operations
- Type hints for better IDE support
- Comprehensive error handling
- Auto port detection

## Installation

```bash
pip install dynamixel-async
```

## Quick Start

```python
import asyncio
from dynamixel_async import DynamixelController

async def main():
    # Create controller instance (auto-detects port)
    controller = DynamixelController(baudrate=57600)
    
    try:
        # Connect and scan for servos
        await controller.connect()
        print(f"Connected servos: {controller.get_connected_ids()}")
        
        # Get first servo
        servo = controller.get_servo(1)
        if not servo:
            print("No servo found with ID 1")
            return
            
        # Enable torque
        servo.enable_torque()
        
        # Move to different positions
        positions = [0, 90, 180, 90, 0]
        for pos in positions:
            print(f"Moving to {pos} degrees...")
            servo.set_position(pos)
            await controller.wait_for_servos()
            
            # Read current position
            current_pos = servo.get_position()
            print(f"Current position: {current_pos:.1f} degrees")
            await asyncio.sleep(1.0)
            
    finally:
        # Clean up
        if controller:
            await controller.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
```

## Supported Models

Currently supports:
- XM430-W210
- XM430-W350

More models can be easily added by defining their control tables.

## Control Modes

Supports all XM430 control modes:
- Position Control
- Velocity Control
- Current Control
- Extended Position Control
- PWM Control

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 