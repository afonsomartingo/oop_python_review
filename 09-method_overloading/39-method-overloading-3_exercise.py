'''Exercise: Advanced Vehicle Class with Method Overloading

Objective: Extend the Vehicle hierarchy to demonstrate method overloading by implementing multiple versions of methods with different parameters.

Instructions:

1. Create a new class ElectricCar that inherits from the Car class with the following requirements:

    - Override the start_engine method to accept an optional parameter 'mode' (str):
        * If mode is "normal", return "Electric motor started in normal mode"
        * If mode is "sport", return "Electric motor started in sport mode"
        * If no mode is specified, default to "normal" mode
    
    - Override the drive method to accept optional parameters:
        * speed (int): The driving speed in km/h
        * autopilot (bool): Whether autopilot is engaged
        * The method should return different messages based on the parameters:
            - If only speed is provided: "Driving at {speed} km/h"
            - If autopilot is True: "Autopilot engaged, cruising at {speed} km/h"
            - If no parameters: "Driving in manual mode"

    - Add a charge_battery method that can accept either:
        * percentage (int): Charge to specific percentage
        * hours (float): Charge for specified hours
        * If both are provided, use percentage and ignore hours

2. Implement error handling:
    - Speed must be between 0 and 200 km/h
    - Percentage must be between 0 and 100
    - Hours must be positive
    - Mode must be either "normal" or "sport"

Example usage:
    tesla = ElectricCar("Model 3", "Tesla")
    print(tesla.start_engine())  # "Electric motor started in normal mode"
    print(tesla.start_engine("sport"))  # "Electric motor started in sport mode"
    print(tesla.drive(speed=120))  # "Driving at 120 km/h"
    print(tesla.drive(speed=80, autopilot=True))  # "Autopilot engaged, cruising at 80 km/h"
    tesla.charge_battery(percentage=90)  # "Charging battery to 90%"
    tesla.charge_battery(hours=2.5)  # "Charging battery for 2.5 hours"

Bonus Challenge:
    Add a battery_status property that returns the current battery percentage
    and estimated range based on the last charging method used.
'''

class ElectricCar(Car):
    def start_engine(self, mode: str = "normal") -> str:
        if mode not in ["normal", "sport"]:
            raise ValueError("Mode must be either 'normal' or 'sport'")
        return f"Electric motor started in {mode} mode"
        
    def drive(self, speed: int = None, autopilot: bool = False) -> str:
        if speed is not None:
            if not isinstance(speed, int) or speed < 0 or speed > 200:
                raise ValueError("Speed must be between 0 and 200 km/h")
            if autopilot:
                return f"Autopilot engaged, cruising at {speed} km/h"
            return f"Driving at {speed} km/h"
        return "Driving in manual mode"
    
    def charge_battery(self, percentage: int = None, hours: float = None) -> str:
        if percentage is not None:
            if not isinstance(percentage, int) or percentage < 0 or percentage > 100:
                raise ValueError("Percentage must be between 0 and 100")
            return f"Charging battery to {percentage}%"
        elif hours is not None:
            if not isinstance(hours, (int, float)) or hours <= 0:
                raise ValueError("Hours must be positive")
            return f"Charging battery for {hours} hours"
        raise ValueError("Either percentage or hours must be provided")