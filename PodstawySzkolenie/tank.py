import pprint
from datetime import datetime
from typing import Dict


class Tank:

    def __init__(self, name, capacity, water_lvl):
        self.name = name
        self.capacity = capacity
        self.water_lvl = water_lvl
        self.operations_history = []

    def __str__(self):
        # użycie pprint.pformat rozwiązało problem
        return pprint.pformat(self.__dict__)

    def __repr__(self):
        return pprint.pformat(self.__dict__)


class Operation:
    def __init__(self):
        self.tanks_dict: Dict[str, Tank] = {}

    def add_tank_to_list(self, tank):
        """Metoda sprawdzająca, czy zbiornik jest na liście, jeśli nie to go dodaje"""
        if tank.name not in self.tanks_dict:
            self.tanks_dict[tank.name] = tank

        return self.tanks_dict

    def _update_tank_list(self, tank):
        """Metoda dodająca zmiany do listy"""
        self.tanks_dict[tank.name] = tank
        # print(f"Tank list po update: ", self.tanks_dict)

    @staticmethod
    def _operation_history(operation_name, tank_name, volume, success):
        """Metoda zwracająca słownik historii operacji"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "timestamp": timestamp,
            "name": operation_name,
            "tank": tank_name,
            "volume": volume,
            "success": success,
        }

    def pour_water(self, tank, volume):
        """Metoda dolewająca wody do zbiornika"""
        if tank.name not in self.tanks_dict:
            self.add_tank_to_list(tank)
        water_lvl = self.tanks_dict[tank.name].water_lvl
        # print("Water lvl: ", water_lvl)
        capacity = self.tanks_dict[tank.name].capacity
        # print("Capacity: ", capacity)
        if water_lvl + volume <= capacity:
            tank.water_lvl = water_lvl + volume
            tank.operations_history.append(
                self._operation_history("pour water", tank.name, volume, True)
            )
            self._update_tank_list(tank)
        else:
            tank.operations_history.append(
                self._operation_history("pour water", tank.name, volume, False)
            )
            self._update_tank_list(tank)

    def pour_out_water(self, tank, volume):
        """Metoda odlewająca wode ze zbiornika"""
        if tank.name not in self.tanks_dict:
            self.add_tank_to_list(tank)
        water_lvl = self.tanks_dict[tank.name].water_lvl
        # print("Water lvl: ", water_lvl)
        if water_lvl - volume >= 0:
            tank.water_lvl = water_lvl - volume
            tank.operations_history.append(
                self._operation_history("pour out water", tank.name, volume, True)
            )
            self._update_tank_list(tank)
        else:
            tank.operations_history.append(
                self._operation_history("pour out water", tank.name, volume, False)
            )
            self._update_tank_list(tank)

    def transfer_water(self, tank1, tank2, volume):
        """Metoda przelewająca wodę z tank1 do tank2 o volume"""
        if tank1.name not in self.tanks_dict:
            self.add_tank_to_list(tank1)
        if tank2.name not in self.tanks_dict:
            self.add_tank_to_list(tank2)
        water_lvl1 = self.tanks_dict[tank1.name].water_lvl
        water_lvl2 = self.tanks_dict[tank2.name].water_lvl
        capacity2 = self.tanks_dict[tank2.name].capacity
        if water_lvl1 >= water_lvl1 - volume and capacity2 >= water_lvl2 + volume:
            tank2.water_lvl = water_lvl2 - volume
            tank1.water_lvl = water_lvl1 + volume
            tank2.operations_history.append(
                self._operation_history("transfer", tank2.name, -volume, True)
            )
            tank1.operations_history.append(
                self._operation_history("transfer", tank1.name, volume, True)
            )
            self._update_tank_list(tank1)
            self._update_tank_list(tank2)
        else:
            tank2.operations_history.append(
                self._operation_history("transfer", tank2.name, -volume, False)
            )
            tank1.operations_history.append(
                self._operation_history("transfer", tank1.name, volume, False)
            )
            self._update_tank_list(tank1)
            self._update_tank_list(tank2)

    def find_tank_with_most_water(self):
        """Metoda znajdująca zbiorniki z największą ilością wody"""
        max_water_lvl = None
        tanks_with_max_water_lvl = []

        for tank_name, tank_data in self.tanks_dict.items():
            water_lvl = tank_data.water_lvl
            if max_water_lvl is None or water_lvl > max_water_lvl:
                # Nowa największa wartość, zresetuj listę i dodaj aktualny zbiornik
                max_water_lvl = water_lvl
                tanks_with_max_water_lvl = [tank_name]
            elif water_lvl == max_water_lvl:
                # Równa największa wartość, dodaj aktualny zbiornik do listy
                tanks_with_max_water_lvl.append(tank_name)

        return tanks_with_max_water_lvl

    def find_tank_with_the_highest_water_lvl(self):
        """Metoda znajdująca najbardziej wypełniony zbiornik"""
        max_capacity_filling = None
        tanks_with_highest_water_lvl = []

        for tank_name, tank_data in self.tanks_dict.items():
            if tank_data.water_lvl != 0:
                capacity_filling = tank_data.capacity / tank_data.water_lvl
                if (
                    max_capacity_filling is None
                    or capacity_filling < max_capacity_filling
                ):
                    max_capacity_filling = capacity_filling
                    tanks_with_highest_water_lvl = [tank_name]
                elif capacity_filling == max_capacity_filling:
                    tanks_with_highest_water_lvl.append(tank_name)
        return tanks_with_highest_water_lvl

    def find_empty_tank(self):
        """Metoda znajdująca puste zbiorniki"""
        empty_tank = []

        for tank_name, tank_data in self.tanks_dict.items():
            water_lvl = tank_data.water_lvl
            if water_lvl == 0:
                empty_tank.append(tank_name)
        return empty_tank

    def find_tank_with_the_most_failed_operation(self):
        """Metoda znajdująca zbiorniki z największą ilością nieudanych operacji"""
        tank_with_failed_operation = []
        frequency_dict = {}

        for tank_name, tank_data in self.tanks_dict.items():
            operation_history = tank_data.operations_history
            for element in operation_history:
                if not element["success"]:
                    # print(element)
                    tank_with_failed_operation.append(tank_name)
                    # print(tank_with_failed_operation)
        for element in tank_with_failed_operation:
            if element in frequency_dict:
                frequency_dict[element] += 1
            else:
                frequency_dict[element] = 1
        return max(frequency_dict, key=frequency_dict.get)

    def find_tank_with_the_most_operation_of_type(self, operation_type):
        """Metoda znajdująca zbiornik z największą liczbą operacji danego typu"""
        tank_operation = {}
        most_operation = {}

        for tank_name, tank_data in self.tanks_dict.items():
            operation_history = tank_data.operations_history
            tank_operation[tank_name] = {}
            for element in operation_history:
                for key, value in element.items():
                    if key == "name":
                        tank_operation[tank_name][value] = (
                            tank_operation[tank_name].get(value, 0) + 1
                        )
                        # print(tank_operation)

        for tank_name, tank_data in tank_operation.items():
            operation = tank_data.get(operation_type)
            # print(operation)
            if operation:
                most_operation[tank_name] = operation
                # print(most_operation)

        max_value = max(most_operation.values())
        keys_with_max_values = [
            key for key, value in most_operation.items() if value == max_value
        ]
        # print(keys_with_max_values)
        return keys_with_max_values

    def check_state(self, tank_name: str, start_value):
        """Metoda sprawdzająca spójność stanu wody z historią operacji"""
        water_level_from_history = 0
        for operation in self.tanks_dict[tank_name].operations_history:
            if operation["success"]:
                if operation["name"] == "pour water":
                    water_level_from_history += operation["volume"]
                elif operation["name"] == "transfer":
                    water_level_from_history += operation["volume"]
                elif operation["name"] == "pour out water":
                    water_level_from_history -= operation["volume"]
        return (
            self.tanks_dict[tank_name].water_lvl - start_value
        ) == water_level_from_history


def main():
    operation = Operation()

    tank1 = Tank("Tank1", 100, 50)
    tank2 = Tank("Tank2", 100, 40)
    tank3 = Tank("Tank3", 200, 50)
    tank4 = Tank("Tank4", 100, 50)
    tank5 = Tank("Tank5", 200, 50)
    tank6 = Tank("Tank6", 100, 0)
    tank7 = Tank("Tank7", 100, 0)

    operation.add_tank_to_list(tank1)
    operation.add_tank_to_list(tank2)
    operation.add_tank_to_list(tank3)
    operation.add_tank_to_list(tank4)
    operation.add_tank_to_list(tank5)
    operation.add_tank_to_list(tank6)
    operation.add_tank_to_list(tank7)

    """print("Tank1:")
        operation.pour_water(tank1, 20)
        print(f"Instancja klasy po dodaniu wody: ", tank1.water_lvl)
        print(f"Instancja klasy po dodaniu wody (historia): ", tank1.operations_history)
        print("Tank2:")
        operation.pour_water(tank2, 300)
        print(f"Instancja klasy po dodaniu wody: ", tank2.water_lvl)
        print(f"Instancja klasy po dodaniu wody (historia): ", tank2.operations_history)"""

    """print("Tank1:")
        operation.pour_out_water(tank1, 20)
        print(f"Instancja klasy po dodaniu wody: ", tank1.water_lvl)
        print(f"Instancja klasy po dodaniu wody (historia): ", tank1.operations_history)
        print("Tank2:")
        operation.pour_out_water(tank2, 300)
        print(f"Instancja klasy po dodaniu wody: ", tank2.water_lvl)
        print(f"Instancja klasy po dodaniu wody (historia): ", tank2.operations_history)"""

    """print("Tank1:")
        operation.transfer_water(tank1, tank2, 300)
        print(f"Instancja klasy po dodaniu wody: ", tank1.water_lvl)
        print(f"Instancja klasy po dodaniu wody (historia): ", tank1.operations_history)
        print("Tank2:")
        print(f"Instancja klasy po dodaniu wody: ", tank2.water_lvl)
        print(f"Instancja klasy po dodaniu wody (historia): ", tank2.operations_history)"""

    operation.pour_water(tank1, 20)
    operation.pour_water(tank1, 20)
    operation.pour_water(tank1, 20)
    operation.pour_water(tank4, 20)
    operation.pour_water(tank2, 300)
    operation.pour_water(tank2, 300)
    operation.pour_water(tank2, 300)
    operation.pour_out_water(tank1, 20)
    operation.pour_out_water(tank2, 300)
    operation.transfer_water(tank1, tank2, 300)
    operation.transfer_water(tank2, tank1, 20)
    operation.transfer_water(tank1, tank2, 20)
    print("Most water tank:", operation.find_tank_with_most_water())
    print("Highest water lvl tank:", operation.find_tank_with_the_highest_water_lvl())
    print("Empty tank:", operation.find_empty_tank())
    print(
        "The most failed operation:",
        operation.find_tank_with_the_most_failed_operation(),
    )
    print(
        "Tank with teh most operation of specified type",
        operation.find_tank_with_the_most_operation_of_type("pour water"),
    )
    print("Check state tank1: ", operation.check_state("Tank1", 50))
    print("Check state tank2: ", operation.check_state(tank2.name, 40))
    """for tank_name, tank_data in operation.tanks_dict.items():
        print(tank_name)
        print(tank_data)"""
    # TODO
    # dlaczego drukuje w kolejnośc capacity': 200, 'name': 'Tank5', 'operations_history': [], 'water_lvl': 50
    # jak to zmienić
    pprint.pprint(operation.tanks_dict)


if __name__ == "__main__":
    main()
