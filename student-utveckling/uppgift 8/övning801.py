from cal_ui import *

create('Anton')
book('Anton', 23, 'apr', '15:00', '17:00', 'Kalas')
show('Anton', 23, 'apr')

create('Axel')
book('Axel', 3, 'jan', '12:00', '13:00', 'Simma')
show('Axel', 3, 'jan')

show_calendars()
for months in cy_iter_months():
    print(months)

save('testdata')
