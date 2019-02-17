import datetime

from lib.GedObjects import Individual, Family, Tree

_individuals = [
    Individual(id='@I1@', name='Kristen /Tan/', sex='F', birthday=datetime.datetime(1998, 9, 29, 0, 0), death=None, child='@F1@', spouse=None),
    Individual(id='@I2@', name='Reynaldo /Tan/', sex='M', birthday=datetime.datetime(1963, 5, 10, 0, 0), death=None, child='@F2@', spouse='@F1@'),
    Individual(id='@I3@', name='Laura /Hotaling/', sex='F', birthday=datetime.datetime(1962, 8, 21, 0, 0), death=None, child='@F3@', spouse='@F1@'),
    Individual(id='@I4@', name='Charles /Hotaling/', sex='M', birthday=datetime.datetime(1916, 12, 12, 0, 0), death=datetime.datetime(1983, 12, 25, 0, 0), child='@F4@',
               spouse='@F3@'),
    Individual(id='@I5@', name='Marjorie /Johnson/', sex='F', birthday=datetime.datetime(1926, 11, 21, 0, 0), death=None, child='@F5@', spouse='@F3@'),
    Individual(id='@I6@', name='Cho Kiat /Tan/', sex='M', birthday=datetime.datetime(1935, 4, 4, 0, 0), death=datetime.datetime(2003, 2, 4, 0, 0), child='@F6@', spouse='@F2@'),
    Individual(id='@I7@', name='Go Siok Lian /Xiao/', sex='F', birthday=datetime.datetime(1934, 12, 14, 0, 0), death=None, child='@F7@', spouse='@F2@'),
    Individual(id='@I8@', name='Kevin /Tan/', sex='M', birthday=datetime.datetime(1997, 3, 6, 0, 0), death=None, child='@F1@', spouse=None),
    Individual(id='@I9@', name='Daniel /Tan/', sex='M', birthday=datetime.datetime(1994, 7, 8, 0, 0), death=None, child='@F1@', spouse=None),
    Individual(id='@I10@', name='Patricia /Hotaling/', sex='F', birthday=datetime.datetime(1958, 8, 12, 0, 0), death=None, child='@F3@', spouse='@F10@'),
    Individual(id='@I11@', name='Jason /Hotaling/', sex='M', birthday=datetime.datetime(1968, 1, 8, 0, 0), death=None, child='@F3@', spouse=None),
    Individual(id='@I12@', name='Andrew /Allens/', sex='M', birthday=datetime.datetime(1957, 6, 1, 0, 0), death=datetime.datetime(1994, 3, 3, 0, 0), child=None, spouse='@F10@'),
    Individual(id='@I13@', name='James /Marron/', sex='M', birthday=datetime.datetime(1955, 10, 18, 0, 0), death=None, child=None, spouse='@F8@'),
    Individual(id='@I14@', name='Max /Allens/', sex='M', birthday=datetime.datetime(1986, 11, 27, 0, 0), death=None, child='@F10@', spouse=None),
    Individual(id='@I15@', name='Richard /Johnson/', sex='M', birthday=datetime.datetime(1900, 7, 8, 0, 0), death=datetime.datetime(1942, 2, 18, 0, 0), child=None, spouse='@F5@'),
    Individual(id='@I16@', name='Grace /Whitten/', sex='F', birthday=datetime.datetime(1899, 1, 8, 0, 0), death=datetime.datetime(1935, 12, 4, 0, 0), child=None, spouse='@F5@'),
    Individual(id='@I17@', name='Nathan /Johnson/', sex='M', birthday=datetime.datetime(1922, 9, 26, 0, 0), death=datetime.datetime(1952, 5, 9, 0, 0), child='@F5@',
               spouse='@F11@'),
    Individual(id='@I18@', name='Marie /Gannon/', sex='F', birthday=datetime.datetime(1925, 5, 12, 0, 0), death=datetime.datetime(1982, 9, 22, 0, 0), child=None, spouse='@F12@'),
    Individual(id='@I19@', name='William /Harrington/', sex='M', birthday=datetime.datetime(1921, 11, 5, 0, 0), death=datetime.datetime(1996, 5, 1, 0, 0), child=None,
               spouse='@F12@'),
    Individual(id='@I20@', name='Elizabeth /Johnson/', sex='F', birthday=datetime.datetime(1944, 3, 19, 0, 0), death=None, child='@F11@', spouse=None),
    Individual(id='@I21@', name='Erin /Harrington/', sex='F', birthday=datetime.datetime(1959, 11, 12, 0, 0), death=None, child='@F12@', spouse=None),
    Individual(id='@I22@', name='Jane /Tan/', sex='F', birthday=datetime.datetime(1974, 8, 4, 0, 0), death=None, child='@F2@', spouse='@F14@'),
    Individual(id='@I23@', name='Peter /Zhu/', sex='M', birthday=datetime.datetime(1972, 2, 20, 0, 0), death=None, child=None, spouse='@F14@'),
    Individual(id='@I24@', name='Tai Wei /Xiao/', sex='M', birthday=datetime.datetime(1900, 11, 2, 0, 0), death=datetime.datetime(1967, 6, 24, 0, 0), child=None, spouse='@F7@'),
    Individual(id='@I25@', name='Li Fan /Ming/', sex='F', birthday=datetime.datetime(1902, 8, 4, 0, 0), death=datetime.datetime(1978, 6, 11, 0, 0), child=None, spouse='@F7@'),
    Individual(id='@I26@', name='Raymond /Liang/', sex='M', birthday=datetime.datetime(1970, 10, 21, 0, 0), death=None, child=None, spouse='@F13@'),
    Individual(id='@I27@', name='Jacob /Hotaling/', sex='M', birthday=datetime.datetime(1893, 5, 11, 0, 0), death=datetime.datetime(1962, 4, 4, 0, 0), child=None, spouse='@F4@'),
    Individual(id='@I28@', name='Eileen /Maxwell/', sex='F', birthday=datetime.datetime(1894, 5, 3, 0, 0), death=datetime.datetime(1951, 8, 5, 0, 0), child=None, spouse='@F4@'),
    Individual(id='@I29@', name='Cai Wen /Tan/', sex='M', birthday=datetime.datetime(1895, 1, 3, 0, 0), death=datetime.datetime(1979, 11, 15, 0, 0), child=None, spouse='@F6@'),
    Individual(id='@I30@', name='Mei Li /Liu/', sex='F', birthday=datetime.datetime(1901, 12, 3, 0, 0), death=datetime.datetime(1982, 2, 26, 0, 0), child=None, spouse='@F6@'),
]

_families = [
    Family(id='@F1@', husband_id='@I2@', wife_id='@I3@', children=['@I1@', '@I8@', '@I9@'], married=datetime.datetime(1994, 6, 4, 0, 0), divorced=None),
    Family(id='@F2@', husband_id='@I6@', wife_id='@I7@', children=['@I2@', '@I22@'], married=datetime.datetime(1961, 1, 13, 0, 0), divorced=None),
    Family(id='@F3@', husband_id='@I4@', wife_id='@I5@', children=['@I3@', '@I10@', '@I11@'], married=datetime.datetime(1948, 5, 6, 0, 0), divorced=None),
    Family(id='@F4@', husband_id='@I27@', wife_id='@I28@', children=['@I4@'], married=datetime.datetime(1915, 6, 1, 0, 0), divorced=None),
    Family(id='@F5@', husband_id='@I15@', wife_id='@I16@', children=['@I5@', '@I17@'], married=datetime.datetime(1923, 4, 2, 0, 0), divorced=None),
    Family(id='@F6@', husband_id='@I29@', wife_id='@I30@', children=['@I6@'], married=datetime.datetime(1933, 8, 14, 0, 0), divorced=None),
    Family(id='@F7@', husband_id='@I24@', wife_id='@I25@', children=['@I7@'], married=datetime.datetime(1930, 4, 20, 0, 0), divorced=None),
    Family(id='@F8@', husband_id='@I13@', wife_id='@I10@', children=[], married=datetime.datetime(2009, 2, 10, 0, 0), divorced=None),
    Family(id='@F9@', husband_id=None, wife_id='@I10@', children=[], married=None, divorced=None),
    Family(id='@F10@', husband_id='@I12@', wife_id='@I10@', children=['@I14@'], married=datetime.datetime(1984, 5, 8, 0, 0), divorced=None),
    Family(id='@F11@', husband_id='@I17@', wife_id='@I18@', children=['@I20@'], married=datetime.datetime(1943, 3, 4, 0, 0), divorced=None),
    Family(id='@F12@', husband_id='@I19@', wife_id='@I18@', children=['@I21@'], married=datetime.datetime(1957, 2, 14, 0, 0), divorced=None),
    Family(id='@F13@', husband_id='@I26@', wife_id='@I22@', children=[], married=datetime.datetime(2007, 4, 29, 0, 0), divorced=None),
    Family(id='@F14@', husband_id='@I23@', wife_id='@I22@', children=[], married=datetime.datetime(2002, 9, 25, 0, 0), divorced=datetime.datetime(2003, 5, 23, 0, 0))
]

kristen_tree = Tree()

[kristen_tree.add_individual(i) for i in _individuals]
[kristen_tree.add_family(f) for f in _families]
