#!/usr/binenv python2.7
# -*- coding: utf-8 -*-

# - - - - - - - - BUILT-IN IMPORTS

import json, datetime, os

# - - - - - - - - LOCAL IMPORTS

import config
from utility import dotNETBase

# - - - - - - - - CLASS LIBRARY

#region UNITS AND MEASUREMENT
class Units(dotNETBase):

    @staticmethod
    def Validate(unit):
        if isinstance(unit, Units):
            return True
        
        elif isinstance(unit, str):
            for standard_unit in config.UNITS.values():
                for key, val in standard_unit.items():
                    if unit.lower() in [key.lower(), val.lower()]:
                        return True
        return False

    def __init__(self, unit):

        IsValid = False

        if isinstance(unit, str):
            for category, standard_unit in config.UNITS.items():
                for key, val in standard_unit.items():
                    if unit.lower() in [key.lower(), val.lower()]:
                        self.Name = key
                        self._symbol = val
                        self._category = category
                        IsValid = True       
                        break

        elif isinstance(unit, Units):
            self.Name = unit.Name
            self._symbol = unit.Symbol
            self._category = unit.Category
            IsValid = True
        
        if not IsValid:
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

    def __init__(self, amount, *args):

        if isinstance(amount, str):
            newMeasurementUnit = Measurement.FromString(amount)
            self.Value = newMeasurementUnit.Value
            self.Units = newMeasurementUnit.Units

        elif isinstance(amount, (int, float)) and isinstance(args[0], (str, Units)):
            self.Value = float(amount)
            self.Units = Units(args[0])
        
        elif isinstance(amount, Measurement):
            self.Value = amount.Value
            self.Units = amount.Units
    
    @property
    def Category(self):
        return self.Units.Category

    @classmethod
    def FromString(cls, unit, seperator=' '):
        
        if not isinstance(unit, str):
            raise TypeError('Input is not a string')
        
        if not seperator in unit:
            raise ValueError('Seperator mismatch. There is no "{}" in "{}"'.format(seperator, unit))
        
        value, unit = unit.split(seperator)
        if value.isdigit:
            return cls(float(value), Units(unit))
        else:
            raise ValueError('Value part of input is not a valid number.')
    
    def __str__(self):
        return '{} {}'.format(self.Value, self.Units.Symbol)
#endregion
