import requests


class Util(object):
    """
        Class to download hata from the hipolabs.com api, parse respose as json 
        print to console
    """

    __base_url = "http://universities.hipolabs.com/search"

    def get_universties_list(self, name="", country=""):
        """
            opens connection to the url endpoint, retrievs the data
            and parse it into an list.
            returns: list containing universioty name, country and domain
        """

        if not isinstance(name, str):
            raise TypeError("Expected name to be a string")
        if not isinstance(country, str):
            raise TypeError("Expected country to be a string")

        json = None
        try:
            params = {}
            params['name'] = name
            params['country'] = country

            response = requests.get(self.__base_url, params=params, timeout=6)

            if response.status_code != requests.codes.ok:
                raise response.raise_for_status()

            json = response.json()
        except Exception:
            print "An error occured connectin to the API, try again later"
            return []

        university_list = []

        max_country = 8
        max_domain = 0
        max_name = 4

        for university in json:
            name = university['name']
            country = university['country']
            domain = university['domain']

            if len(name) > max_name:
                max_name = len(name)
            if len(domain) > max_domain:
                max_domain = len(domain)
            if len(country) > max_country:
                max_country = len(country)

            university_list.append({"name": name, "country": country,
                                    "domain": domain})

        field_length = {"name": max_name, "country": max_country,
                        "domain": max_domain}

        return (university_list, field_length)

    def print_table_header(self, max_name, max_country, max_domain):

        """
            create the header for the data to print to the console
            the heading are padded to form a consistent look
        """

        header = " ||" + "=" * (max_name + max_domain + max_country + 17) + "|| "

        print header
        print " ||", " " * (max_name / 2 - 2), "Name", " " * (max_name / 2 - 2), " | ",
        print " " * (max_country / 2 - 4), "Country", " " * (max_country / 2 - 4), " | ",
        print " " * (max_domain / 2 - 3), "Domain", " " * (max_domain / 2 - 3), " || "
        print header

    def print_table_item(self, university, max_name, max_country, max_domain):

        """
            print the list item to the console, padding  the data to align
            with the table headers
        """

        sep = " ||" + "-" * (max_name + max_domain + max_country + 17) + "|| "

        name = university['name']
        country = university['country']
        domain = university['domain']

        print " || ",
        print name, " " * (max_name - len(name)), " | ",  # padded name
        print country, " " * (max_country - len(country)), " | ",  # country
        print domain, " " * (max_domain - len(domain)),  # domain
        print " || "
        print sep

    def padded_print(self, university_data):
        """
            iniates the call to print the downloaded data
        """
        if university_data is []:
            print "No Data receved from the API"
        else:
            university_list = university_data[0]
            field_length = university_data[1]

            max_name = field_length['name']
            max_country = field_length['country']
            max_domain = field_length['domain']

            self.print_table_header(max_name, max_country, max_domain)

            for university in university_list:
                self.print_table_item(university, max_name, max_country, max_domain)
