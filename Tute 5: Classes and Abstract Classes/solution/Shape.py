from abc import ABC, abstractmethod

# use ABC to define a class as Abstract
class Shape(ABC):

    # if the class has common attributes
    # then you can define a constructor like normal
    # but we only have one method

    # use abstractmethod decorator to say that
    # any class that 'realises' Shape must implement get_area()
    @abstractmethod
    def get_area(self):
        pass
