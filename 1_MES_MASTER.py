# -*- coding: utf-8 -*-
"""
OSE MES
Copyright 2019 Jonathan D. Takacs


Description:
    Breif of purpose: On orders that are not yet shipped and fufilled, see what needs done next and kick off child processes to do that work. 
        
    Bried operation mode: Connect to Order table in MES SQL DB. Check any orders not shipped. Evaulate next step based on not shipped's production tags.
    Kick off processes to finish work as needed in their own threads. Collect KPI and Process information from child processes. Store in this applications DB; make this information
    avaiable to GUI modules by writing this to SQL.
    Wiki:
    
"""


"""

"""
Workplan:
    
"""