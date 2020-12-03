from cal_ui import *

t1315 = new_time(new_hour(13), new_minute(15))
print(t1315)

t1500 = new_time(new_hour(15), new_minute(00))
print(t1500)

ts1315 = new_time_span(t1315, t1500)
print(ts1315)

create('Anton')
cd15 = new_calendar_day(new_day(15))
print(cd15)
t815 = new_time(new_hour(8), new_minute(15))
t930 = new_time(new_hour(9), new_minute(30))
ts815 = new_time_span(t815, t930)
sub815 = new_subject('Redovisning av uppgift')
ap815 = new_appointment(ts815, sub815)
cd15cp = cd_plus_appointment(cd15, ap815)
print(cd15cp)
