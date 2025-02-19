import json
import requests
from enum import Enum, IntFlag
import time
import threading
from typing import Callable
import inspect
from dataclasses import dataclass


class VehicleType(IntFlag):
    ALL                  = 0
    NORMAL_BUS           = 1 << 0
    RAIL                 = 1 << 1
    MAX_TYPE_1           = 1 << 2
    MAX_TYPE_2           = 1 << 3
    MAX_TYPE_3           = 1 << 4
    MAX_TYPE_4           = 1 << 5
    MAX_TYPE_5           = 1 << 6
    MAX_TYPE_6           = 1 << 7
    MAX_GREEN            = 1 << 8
    MAX_BLUE             = 1 << 9
    MAX_ORANGE           = 1 << 10
    MAX_RED              = 1 << 11
    MAX_YELLOW           = 1 << 12
    UNKNOWN_VEHICLE_TYPE = 1 << 13
    FX_BUS               = 1 << 14
    OTHER_BUS            = 1 << 15

class Garage(Enum):
    UNKNOWN = 0
    RUBY    = 1
    POWELL  = 2
    MERLO   = 3
    CENTER  = 4
    ELMO    = 5

@dataclass
class Position:
    lat: float
    lon: float

@dataclass
class Route:
    id: int
    desc: str

@dataclass
class ServiceAlert:
    routeAffected: Route
    location: Position

class Vehicle:
    type: VehicleType
    pos: Position
    line: int
    signMessage: str
    garage: Garage
    vehicleID: int
    hexColor: str
    
    def __eq__(self, other):
        return (isinstance(other, Vehicle) and self.vehicleID == other.vehicleID)

    def __init__(self, type: str, pos: Position, color: str, signMessage: str, garage: str, vehicleID: int, line: int):
        self.type = 0
        if type == "rail":
            self.type = self.type | VehicleType.RAIL
            match color:
                case "008342": # Green Line
                    self.type = self.type | VehicleType.MAX_GREEN
                case "114C96": # Blue Line
                    self.type = self.type | VehicleType.MAX_BLUE
                case "FFC52F": # Yellow Line
                    self.type = self.type | VehicleType.MAX_YELLOW
                case "D05F27": # Orange Line
                    self.type = self.type | VehicleType.MAX_ORANGE
                case "C41F3E": # Red Line
                    self.type = self.type | VehicleType.MAX_RED
            match int(vehicleID / 100):
                case 1:
                    self.type = self.type | VehicleType.MAX_TYPE_1
                case 2:
                    self.type = self.type | VehicleType.MAX_TYPE_2
                case 3:
                    self.type = self.type | VehicleType.MAX_TYPE_3
                case 4:
                    self.type = self.type | VehicleType.MAX_TYPE_4
                case 5:
                    self.type = self.type | VehicleType.MAX_TYPE_5
                case 6:
                    self.type = self.type | VehicleType.MAX_TYPE_6
                case _:
                    self.type = self.type | VehicleType.UNKNOWN_VEHICLE_TYPE
        elif type == "bus":
            self.type = (self.type | VehicleType.NORMAL_BUS if color == "084C8D" else (self.type | VehicleType.FX_BUS if color == "61A744" else self.type | VehicleType.OTHER_BUS))
        else:
            print("Found vehicle with unknown type:", type)
            self.type = self.type | VehicleType.UNKNOWN_VEHICLE_TYPE
        match garage:
            case "RUBY":
                self.garage = Garage.RUBY
            case "POWELL":
                self.garage = Garage.POWELL
            case "MERLO":
                self.garage = Garage.MERLO
            case "CENTER":
                self.garage = Garage.CENTER
            case "ELMO":
                self.garage = Garage.ELMO
            case _:
                self.garage = Garage.UNKNOWN
        self.signMessage = signMessage
        self.pos = pos
        self.vehicleID = vehicleID
        self.line = line
        self.hexColor = color

class StreetcarRoute(Enum):
    A = 0
    B = 1
    NS = 2
    UNKNOWN = 3

class StreetcarType(Enum):
    united_10T3        = 0 # Car  015
    united_100         = 1 # Cars 021-026
    brookville_liberty = 2 # Cars 031-033
    inekon_12T         = 3 # Cars 008-010
    skoda_10T          = 4 # Cars 001-007
    unknown            = 5


class StreetcarVehicle:
    # Example: {"id":"SC010","lat":45.5103043,"lon":-122.6797828,"route_name":"NS Line","dir_name":"NS Line to NW 23rd Ave","route_id":193}
    route_id: int
    dir_name: str
    route: StreetcarRoute
    pos: Position
    id: int
    type: StreetcarType
    def __init__(self, id: str, lat: float, lon: float, route_name: str, dir_name: str, route_id: int):
        self.pos = Position(lat, lon)
        self.id = int(id.removeprefix("SC"))
        self.route = StreetcarRoute.A if route_name == "A Loop" else (StreetcarRoute.B if route_name == "B Loop" else (StreetcarRoute.NS if route_name == "NS Line" else StreetcarRoute.UNKNOWN))
        self.type = StreetcarType.united_10T3 if self.id == 15 else (StreetcarType.united_100 if 21 <= self.id <= 26 else (StreetcarType.brookville_liberty if 31 <= self.id <= 33 else (StreetcarType.inekon_12T if 8 <= self.id <= 10 else (StreetcarType.skoda_10T if 1 <= self.id <= 7 else StreetcarType.unknown))))
        self.dir_name = dir_name
        self.route_id = route_id
    def to_vehicle(self) -> Vehicle:
        return Vehicle("rail", self.pos, ("362783" if self.route == StreetcarRoute.B else ("DB0962" if self.route == StreetcarRoute.A else ("95C11F" if self.route == StreetcarRoute.NS else "000000"))), self.dir_name, "streetcar", self.id, self.route_id)

def fetch_streetcars() -> list[StreetcarVehicle]:
    response = requests.get("https://portlandstreetcar.org/cust/streetcar_lines/public/view/live_train_data.php")
    result = []
    if response.status_code != 200:
        print("Couldn't fetch streetcars.")
        return result
    if (data := json.loads(response.content)) and isinstance(data, list):
        for vehicle in data:
            result.append(StreetcarVehicle(vehicle["id"], vehicle["lat"], vehicle["lon"], vehicle["route_name"], vehicle["dir_name"], vehicle["route_id"]))
    else:
        print("Received invalid or empty data: " + response.content)
    return result

def count_args(func: Callable) -> int:
    sig = inspect.signature(func)
    count: int = 0
    for _ in sig.parameters.values():
        count += 1
    return count

class TriMet:
    filter: VehicleType
    appId: str
    allVehicles: list[Vehicle] = []
    lastAllVehicles: list[Vehicle] = []
    registered_callbacks: dict[int, list[Callable]] = {}
    refreshInterval: float
    registered_update_callbacks: list[Callable] = []

    def on_update(self, func: Callable):
        if not func in self.registered_update_callbacks:
            self.registered_update_callbacks.append(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    def track_vehicle(self, id):
        def decorator(func):
            if self.registered_callbacks.get(id, []):
                self.registered_callbacks[id].append(func)
            else:
                self.registered_callbacks[id] = [func]
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator
    def fetch_vehicles(self) -> list[Vehicle]:
        response = requests.get(f"https://developer.trimet.org/ws/v2/vehicles?appID={self.appId}")
        if response.status_code != 200:
            print(f"Failed to fetch. Code: {response.status_code}. Response: {response.content}")
            return []
        data = json.loads(response.content)
        if not data:
            print("Invalid JSON response received.")
            return []
        if not data["resultSet"]:
            print("Invalid JSON response received.")
            return []
        if not data["resultSet"]["vehicle"]:
            print("Invalid JSON response received.")
            return []
        result = []
        for vehicle in data["resultSet"]["vehicle"]:
            result.append(Vehicle(vehicle["type"], Position(vehicle["latitude"], vehicle["longitude"]), vehicle["routeColor"], vehicle["signMessage"], vehicle["garage"], vehicle["vehicleID"], vehicle["routeNumber"]))
        return result + [s_vehicle.to_vehicle() for s_vehicle in fetch_streetcars()]
    def filterList(self, vehicles: list[Vehicle]):
        if self.filter == VehicleType.ALL:
            return vehicles
        result = []
        for vehicle in vehicles:
            if (vehicle.type & self.filter):
                result.append(vehicle)
        return result

            
    def __init__(self, filter: VehicleType, appId: str, refreshInterval: float = 10, keep_main_thread_alive: bool = False):
        response = requests.get(f"https://developer.trimet.org/ws/v2/vehicles?appID={appId}")
        if response.status_code != 200:
            print(f"Failed to initialize. Status code: {response.status_code}. Response: {str(response.content)}")
            return
        self.filter = filter
        self.appId = appId
        self.refreshInterval = refreshInterval
        self.allVehicles = self.filterList(self.fetch_vehicles())
        threading.Thread(target=self.start_tracking, daemon=True).start()
        if keep_main_thread_alive:
            while True:
                continue
    def start_tracking(self):
        while True:
            self.lastAllVehicles = self.allVehicles
            self.allVehicles = self.filterList(self.fetch_vehicles())
            for vehicle in self.allVehicles:
                for lastVehicle in self.lastAllVehicles:
                    if vehicle == lastVehicle and vehicle.pos != lastVehicle.pos:
                        # Same vehicle, different position, it most likely moved since the last update
                        if self.registered_callbacks.get(vehicle.vehicleID, []):
                            for func in self.registered_callbacks[vehicle.vehicleID]:
                                if count_args(func) != 1:
                                    print("Not calling back function with more or less than 1 argument.")
                                    continue
                                func(vehicle.pos)
            time.sleep(self.refreshInterval)
            for func in self.registered_update_callbacks:
                func()