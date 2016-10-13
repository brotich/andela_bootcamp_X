## Day 1: Outcome 4 - Object-Oriented Programming

Real World Problem modeled using OOP principles. The model is based on the various formulae of calculation land rates in a sample municipality.

The formulae for calculating land-rate  are:

```
+===========================================================+
||  Type Of Building      |         Land Rate              ||
|===========================================================|
| Commercial              | KES 30 per floor+space unit     |
+-----------------------------------------------------------+
| Residential             | KES 10  per housing unit        |
+-----------------------------------------------------------+
| Utility                 | 0(Municipal owned are rate free)|
+-----------------------------------------------------------+
| Uncategorized           | KES 500(Flat Rate)              |
+-------------------------+---------------------------------+
                                    created on asciiflow.com
```

  
The [`tests`](./tests) folder contains the tests used in the development of the classes using TDD format
##Applied Basic OOP principles

#### Inheritance ###
* The classes ```CommercialBuilding```, `ResidentialBuilding` and ```UtilityBuilding``` are subclasses of the ```BaseBuilding``` class.

#### abstraction
* Each class of buildings has a different formula for calculating the land rate to pay to the municipal as per the table above. The exact implementation is hidden behind the ```get_land_rate``` function of the subclass.

#### polymorphism
* The classes  ```CommercialBuilding```, ```ResidentialBuilding``` and ```UtilityBuilding```  inherit the attributes and behaviour of the super class ```BaseBuilding``` . However, each individual class define some  unique attributes and behaviors to that  particular building class i.e:
  :  - CommercialBuilding has floorspace
  :  - ResidentialBuilding has living units
  :  - UtilityBuilding defines the utility it provides

#### encapsulation 
* Some of the attributes in the `BaseBuilding` class and its sub-classes are private to that particular instance. These attributes are therefore manipulated using getter and setter functions. i.e `set_location` and [`get_location`](types_buildings.py#L34) functions are used to manipulate the value of `self.__location` attribute in an instance of the classes.

#### events
* This allows for the communication between the instances of classes. This was, however,  not implemented in this model 
