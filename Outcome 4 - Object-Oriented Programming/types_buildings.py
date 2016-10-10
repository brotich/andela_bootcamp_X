
class BaseBuilding(object):
    """
        boilder-plate class used to initiale the various building in
        municipality
    """

    def __init__(self, location=None, land_rate=500):

        if not isinstance(location, str) and location is not None:
            raise TypeError("Location should be of type str")

        if not isinstance(land_rate, (float, int, long)):
            raise TypeError("Land rate should be of type numeric")

        self.__location = location
        self.__land_rate = land_rate

    def set_location(self, location):

        if not isinstance(location, str):
            raise TypeError("Location should be of type str")
        self.__location = location

    def set_land_rate(self, land_rate):
        if not isinstance(land_rate, (float, int, long)):
            raise TypeError("Land rate should be of type numeric")

        self.__land_rate = land_rate

    def get_location(self):
        return self.__location

    def get_land_rate(self):
        return self.__land_rate


class CommercialBuilding(BaseBuilding):
    """
        This building provides space for offices and warehouses
        Land rate is based on the available floor space
    """
    def __init__(self, location=None, floor_space=0):

        if not isinstance(floor_space, (float, int, long)):
            raise TypeError("Floor Space should be of type numeric")

        super(self.__class__, self).__init__(location)
        self.__floor_space = floor_space

    def set_floor_space(self, floor_space):
        self.__floor_space = floor_space

    def get_floor_space(self):
        return self.__floor_space

    def get_land_rate(self):
        return self.__floor_space * 30


class ResidentialBuilding(BaseBuilding):
    """
        This building that provide space for housing
        Land rate depends on the numver of availabe units
    """
    def __init__(self, location=None, num_units=0):

        if not isinstance(num_units, (float, int, long)):
            raise TypeError("Land rate should be of type numeric")
        super(self.__class__, self).__init__(location)
        self.__num_units = num_units

    def set_num_units(self, num_units):
        self.__num_units == num_units

    def get_num_units(self):
        return self.__num_units

    def get_land_rate(self):
        """land rate = num_unit * 20"""
        return self.__num_units * 20


class Utilities(BaseBuilding):
    """
        This building are owned by the municipality hence pay
        no land rate
    """
    def __init__(self, location=None, utility_name=None):

        if not isinstance(utility_name, str) and utility_name is not None:
            raise TypeError("Utlity hould be of type str")
        super(self.__class__, self).__init__(location)
        self.__utility_name = utility_name

    def set_land_rate(self, land_rate):
        raise NotImplementedError("Utility Building owned pay no land rate")

    def set_utility(self, utility_name):
        self.__utility_name = utility_name

    def get_utility(self):
        return self.__utility_name

    def get_land_rate(self):
        return 0
