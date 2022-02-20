#!/usr/binenv python2.7
# -*- coding: utf-8 -*-

__all__ = ['dotNETBase']

# - - - - - - - - CLASS LIBRARY

class dotNETBase(object):

    def __init__(self):
        raise NotImplementedError('Abstract base class cannot be instantiated.')
    
    def __str__(self):
        pass
    
    def __repr__(self):
        return self.__str__()
    
    def ToString(self):
        return self.__str__()
    
    def ToDictionary(self):
        pass

    def GetType(self):
        return self.__class__.__name__
    
    