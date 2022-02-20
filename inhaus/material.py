#!/usr/binenv python2.7
# -*- coding: utf-8 -*-

__all__ = ['MaterialCommon', 'SheetMaterial']

# - - - - - - - - BUILT-IN IMPORTS

# - - - - - - - - LOCAL IMPORTS

from utility import dotNETBase
import config, document

# - - - - - - - - CLASS LIBRARY

class MaterialCommon(dotNETBase):

    CategoryList = ['PLYWOOD', 'GLASS', 'LAMINATE']
    CustomErrorMessage = '{} input does not have a valid unit.'

    def __init__(self):
        raise NotImplementedError("Abstract class cannot be instantiated.")
    
    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, value, *args):
        self._Length = document.Measurement(value, *args)
        if not self._Length.Category == 'Distance':
            raise TypeError(self.CustomErrorMessage.format('Length'))

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, value, *args):
        self._Width = document.Measurement(value, *args)
        if not self._Width.Category == 'Distance':
            raise TypeError(self.CustomErrorMessage.format('Width'))

    @property
    def Thickness(self):
        return self._Thickness

    @Thickness.setter
    def Thickness(self, value, *args):
        self._Thickness = document.Measurement(value, *args)
        if not self._Thickness.Category == 'Distance':
            raise TypeError(self.CustomErrorMessage.format('Thickness'))

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, value, *args):
        self._Weight = document.Measurement(value, *args)
        if not self._Weight.Category == 'Weight':
            raise TypeError(self.CustomErrorMessage.format('Weight'))

    @property
    def Category(self):
        return self._Category
    
    @Category.setter
    def Category(self, category):
        if category.upper() in config.CATEGORY_LIST:
            self._Category = category.upper()
        else:
            raise ValueError('Invalid Category.')

    @property
    def Cost(self):
        return self._Cost
    
    @Cost.setter
    def Cost(self, value, *args):
        self._Cost = document.Measurement(value, *args)
        if not self._Cost.Category == 'Currency':
            raise TypeError(self.CustomErrorMessage.format('Cost'))

class Sheet(MaterialCommon):
    
    def __init__(self, name, cost, code='XXXX', category='PLYWOOD', length='2400 mm', width='1200 mm', thickness='20 mm', weight='45 Kg', **kwargs):
        self.Name       = name
        self.Category   = category
        self.Code       = code

        self.Cost       = cost
        self.Length     = length
        self.Width      = width
        self.Thickness  = thickness
        self.Weight     = weight

        self.Color      = kwargs.get('color', 'Tan')
        self.Treatment  = kwargs.get('treatment', 'BWR')

    @property
    def IsValid(self):
        return self.Length.Units.Symbol == self.Width.Units.Symbol == self.Thickness.Units.Symbol

    @property
    def Area(self):
        return document.Measurement(self.Length.Value*self.Width.Value, 'mm2')
    
    @property
    def Size(self):
        return '{} x {} x {}'.format(self.Length, self.Width, self.Thickness)
    
    def __str__(self):        
        outString = "Material : {0}\n  "
        outString += "Weight : {4}\n    "
        outString += "Type : SHEET\n    "
        outString += "Name : {1}\n    "
        outString += "Size : {2}\n    "
        outString += "Cost : {3}"

        return outString.format(self.Category, self.Name, self.Size, self.Cost, self.Weight)
    
    def ToDictionary(self):

        return  {   'Name'      : self.Name    ,
                    'Category'  : self.Category ,
                    'Code'      : self.Code     ,
                    'Color'     : self.Color    ,
                    'Cost'      : self.Cost     ,
                    'Treatment' : self.Treatment,
                    'Length'    : self.Length   ,
                    'Width'     : self.Width    ,
                    'Thickness' : self.Thickness,
                    'Weight'    : self.Weight   }