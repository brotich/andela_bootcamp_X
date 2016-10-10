import unittest


from types_buildings import CommercialBuilding
from types_buildings import BaseBuilding
from types_buildings import Utilities
from types_buildings import ResidentialBuilding


class TypeOfBuildingTest(unittest.TestCase):

    def test_building_is_instance_of_object(self):
        bld = BaseBuilding()
        self.assertIsInstance(bld, object,
                msg='BaseBuilding should be an instance of object')

    def test_commercial_instance_of_building(self):
        bld = CommercialBuilding()
        self.assertIsInstance(bld, BaseBuilding,
                msg='Commercial BaseBuilding should be an instance of BaseBuilding')

    def test_residential_instance_of_building(self):
        bld = ResidentialBuilding()
        self.assertIsInstance(bld, BaseBuilding,
                msg='Residential BaseBuilding should be an instance of BaseBuilding')

    def test_utility_instance_of_building(self):
        bld = Utilities()
        self.assertIsInstance(bld, BaseBuilding,
                msg='Utilities BaseBuilding should be an instance of BaseBuilding')

    def test_default_building_values(self):
        bld = BaseBuilding()
        land_rate = bld.get_land_rate()
        location = bld.get_location()
        self.assertListEqual([land_rate, location], [500, None],
                msg="Default Values for the BaseBuilding should be Landrate:500 and Location None")

    def test_default_residential_values(self):
        bld = BaseBuilding()
        land_rate = bld.get_land_rate()
        location = bld.get_location()
        self.assertListEqual([land_rate, location], [500, None],
                msg="Default Values for the Residential BaseBuilding should be Landrate:500 and Location None")

    def test_commercial_building_initialization_with_location_and_rate(self):
        bld = CommercialBuilding("Kilimani Drive", 1000)
        land_rate = bld.get_land_rate()
        location = bld.get_location()
        self.assertListEqual([location, land_rate], ["Kilimani Drive", 30000], 
                msg="Commercial Building Location should be Kilimani Drive and land rate 1000")

    def test_commercial_buildling_land_rate(self):
        bld = CommercialBuilding()
        bld.set_floor_space(1000)
        land_rate = bld.get_land_rate()
        self.assertEqual(land_rate, 30000, msg="The land rate for floorspace 1000 should be 30000")

    def test_setting_location_to_commercial_building(self):
        bld = CommercialBuilding()
        bld.set_location("Kilimani Drive")
        location = bld.get_location()
        self.assertEqual(location, "Kilimani Drive", msg="The building should be located at Kilimani Drive")
