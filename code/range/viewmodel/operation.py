class Operation:
    NONE = 'NONE'
    CONTAINS = 'CONTAINS'
    OVERLAP = 'OVERLAP'
    EQUALS = 'EQUALS'
    ALL_POINTS = 'ALL POINTS'
    END_POINTS = 'END POINTS'
    ALL = [CONTAINS, OVERLAP, EQUALS, ALL_POINTS, END_POINTS]