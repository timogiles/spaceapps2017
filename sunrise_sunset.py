import ephem

lat = '27.9621333'
long = '-82.4448439'


o=ephem.Observer()
o.lat = lat
o.long = long
s=ephem.Sun()
s.compute()

print ephem.localtime(o.previous_rising(s))

print ephem.localtime(o.next_rising(s))
print ephem.localtime(o.previous_setting(s))
print ephem.localtime(o.next_setting(s))