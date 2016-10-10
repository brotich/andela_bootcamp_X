#Outcome 4 - Object-Oriented Programming

Real World Problem modeled using OOP principles:

#Inheritance
The classes CommercialBuilding, ResidentialBuilding and UtilityBuilding are subclass of the BaseBuilding class

#abstraction
The building have different formula for calculatining the land rate to pay to the municipal i.e
  CommercialBuilding = 30 units per floorspace
  ResidentialBuilding = 10 units per unit
  UtilityBuilding = 0 (buildings owned by the municipality don't pay rates)

#polymorphism
The classes CommercialBuilding, ResidentialBuilding and UtilityBuilding are subclass of the BaseBuilding class 
However each class defines unique attributes and behaviors to the particular building class i.e
  CommercialBuilding have floorspace
  ResidentialBuilding have units
  UtilityBuilding define the utility it provides

#encapsulation 
the calculation of rate is dependent on the class of the building. It is not important to display the formula
used to calculate the rate hence the calculated rate is expose via get_land_rate method in the subclasses. It also
allows for the use of different formula based on the type of the building

#events
this allows for the communication between the instances of related classes. This wasn't implemented in this 
model however
