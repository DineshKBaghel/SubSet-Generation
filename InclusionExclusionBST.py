# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:35:36 2020

@author: Dinesh
"""
import copy

class subsetGeneration(object):
    def __init__(self):
        self.possibility = [[]] #denotes all possible combinations. Initially empty
        
    def subsets(self,agt_dmd):
        """
        Test Cases:
        ===========
            
        >>> agt_dmd = [1,2,3]
        >>> o = subsetGeneration()
        >>> subsets = o.subsets(agt_dmd)
        >>> subsets.sort(key=sum)
        >>> subsets.sort(key=len)
        >>> subsets
        [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        
        >>> agt_dmd = []
        >>> o = subsetGeneration()
        >>> subsets = o.subsets(agt_dmd)
        >>> subsets.sort(key=sum)
        >>> subsets.sort(key=len)
        >>> subsets
        [[]]
        
        >>> agt_dmd = [1]
        >>> o = subsetGeneration()
        >>> subsets = o.subsets(agt_dmd)
        >>> subsets.sort(key=sum)
        >>> subsets.sort(key=len)
        >>> subsets
        [[], [1]]
        
        >>> agt_dmd = [1,2]
        >>> o = subsetGeneration()
        >>> subsets = o.subsets(agt_dmd)
        >>> subsets.sort(key=sum)
        >>> subsets.sort(key=len)
        >>> subsets
        [[], [1], [2], [1, 2]]
        """
        for e in agt_dmd:
            self.exclude(e)
            self.include(e)
        return self.possibility

    def include(self,e):
        l = int(len(self.possibility)/2)
        for i in range(l):
            self.possibility[i].append(e)
    
    def exclude(self,e):
        l = len(self.possibility)
        for i in range(l):
            self.possibility.append(copy.deepcopy(self.possibility[i]))
    
if __name__ == "__main__":
    import doctest
    (failures,tests) = doctest.testmod(report=True, verbose=True)
    print ("{} failures, {} tests".format(failures,tests))  