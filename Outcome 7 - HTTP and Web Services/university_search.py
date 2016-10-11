
import sys
from util.lib import Util


class Main(object):
    """class the Util class to get and diplay the university data from the API"""

    __util = Util()

    def find_university(self, univeristy_name="", country_name="Kenya"):
        """"
            given either, name and/or country, it calls the lib class and 
            print the response
        """

        if not isinstance(university_name, str):
            raise TypeError("Expected university_name to be a string")
        if not isinstance(country_name, str):
            raise TypeError("Expected country_name to be a string")

        data = self.__util.get_universties_list(univeristy_name, country_name)
        self.__util.padded_print(data)


if __name__ == '__main__':

    university_name = ""
    country_name = "Kenya"


    if len(sys.argv) > 3:
        university_name = sys.argv[1]
        country_name = sys.argv[2]

    if len(sys.argv) == 2:
        university_name = sys.argv[1]

    if len(sys.argv) == 1:
        print "usage:"
        print "     ", sys.argv[0], " university_name [country]"
        print "         the country is optional"
        print ""
        print "default output using Country Kenya shown below: \n\n"

    Main().find_university(university_name, country_name)



