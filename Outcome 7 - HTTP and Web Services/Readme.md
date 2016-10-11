# Day 2 : Outcome 7 - HTTP and Web Services

This program is submitted as the solution to the Day 2 Github assignment . 
This assignment  is designed to impact knowledge on HTTP and API use to a developer

## The Solution
the breakdown of the solution is as follows:
```
    lib
      +
      +--+lib.py
      +--+__init__.py
      +
    university_search.py
```
```lib``` folder containing the file ```lib.py```, ```__init__.py```

```lib.py``` contains the code to connect to the API and print the response to the console

```university_search.py``` - entry point of the program. It initilialisess an instance of ```lib.py``` and  
access the methods to get and display the information


## THE API 
The API selected provides information on University Domains and Names Data List & API. It allows 
the data to be filtered based on partial ```name``` and/or ```country``` . 
It provides one URL endpoint [```/search```](http://universities.hipolabs.com/search) for accessing the resource . 
The parameters are sent as HTTP GET  queries to the endpoint. The response from the API is a JSON file containing
a list of a university data . Homepage at [http://universities.hipolabs.com](http://universities.hipolabs.com/).


#### sample query
* [http://universities.hipolabs.com/search?name=middle&country=Turkey](http://universities.hipolabs.com/search?name=middle&country=Turkey)
  : get universities with ```middle``` in the name  and located in ```Turkey```
  
* [http://universities.hipolabs.com/search?country=Kenya](http://universities.hipolabs.com/search?country=Kenya)
  : get all universities  and located in ```Kenya```

#### sample response
```
[
    ...
    {
        "alpha_two_code": "TR",
        "country": "Turkey",
        "domain": "sabanciuniv.edu.tr",
        "name": "Sabanci University",
        "web_page": "http://www.sabanciuniv.edu.tr/"
    },
    ...
]
```

## Usage
requires the ```requests``` package 
  
      ```python university_search.py university_name [country] ```

The script expects a full/partial name and an optional country name to obtain the data
Note: Running the script without any arguments defaults to hardcoded parameters: Country = Kenya and an empty University Name 

## sample output

```
usage:
      university_search.py  university_name [country]
         the country is optional

default output using Country Kenya shown below: 


 ||============================================================================================================|| 
 ||                             Name                              |   Country   |            Domain            || 
 ||============================================================================================================|| 
 ||  Africa International University                               |  Kenya      |  aiu.ac.ke                  || 
 ||------------------------------------------------------------------------------------------------------------|| 
 ||  Aga Khan University                                           |  Kenya      |  aku.edu                    || 
 ||------------------------------------------------------------------------------------------------------------|| 
 ||  Africa Nazarene University                                    |  Kenya      |  anu.ac.ke                  || 
 ||------------------------------------------------------------------------------------------------------------|| 
 ||  Adventist University of Africa                                |  Kenya      |  aua.ac.ke                  || 
 ||------------------------------------------------------------------------------------------------------------|| 
 ||  Chuka University                                              |  Kenya      |  chuka.ac.ke                || 
 ||------------------------------------------------------------------------------------------------------------|| 
 ||  Catholic University of Eastern Africa                         |  Kenya      |  cuea.edu                   || 
 ||------------------------------------------------------------------------------------------------------------|| 


```



