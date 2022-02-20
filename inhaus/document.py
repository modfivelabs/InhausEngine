#!/usr/binenv python2.7
# -*- coding: utf-8 -*-

__all__ = ['Units', 'Measurement']

# - - - - - - - - BUILT-IN IMPORTS

# - - - - - - - - LOCAL IMPORTS

from utility import dotNETBase
import config

# - - - - - - - - CLASS LIBRARY

#region UNITS and MEASUREMENT
class Units(dotNETBase):

    @staticmethod
    def validate(unit):

        if isinstance(unit, Units):
            return True, (unit.Category, unit.Name, unit.Symbol)

        elif isinstance(unit, str):
            for category, standard_unit in config.UNITS.items():
                for name, symbol in standard_unit.items():
                    if unit.lower() in [name.lower(), symbol.lower()]:
                        return True, (category, name, symbol)
        
        else:
            return False, ()
    
    def __init__(self, unit):

        result, values = Units.validate(unit)
        if result:
            self._category, self.Name, self._symbol = values
        else:
            raise ValueError('Invalid Unit')
    
    @property
    def Symbol(self):
        return self._symbol
    
    @property
    def Category(self):
        return self._category
    
    def __str__(self):
        return self.Name
    

class Measurement(dotNETBase):

    @classmethod
    def FromString(cls, unit, seperator = ' '):

        if not isinstance(unit, str):
            raise TypeError('Input is not a string')

        if not seperator in unit:
            raise ValueError('Seperator mismatch. There is no "{}" in "{}"'.format(seperator, unit))
        
        value, unit = unit.split(seperator)
        if value.isdigit:
            return cls(float(value), Units(unit))
        else:
            raise ValueError('Invalid numeric input.')
    
    def __init__(self, amount, *args):

        if isinstance(amount, str):
            new_measurement = Measurement.FromString(amount)
            self.Value = new_measurement.Value
            self.Units = new_measurement.Units

        elif isinstance(amount, (int, float)) and isinstance(args[0], (str, Units)):
            self.Value = float(amount)
            self.Units = Units(args[0])
    
    @property
    def Category(self):
        return self.Units.Category
    
    def __str__(self):
        return '{} {}'.format(self.Value, self.Units.Symbol)

    