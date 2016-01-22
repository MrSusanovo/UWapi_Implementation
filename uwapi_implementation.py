from uwaterlooapi import UWaterlooAPI
class Subject(object):
    def __init__(self,name,catalog,section,starts,ends,days,prof):
        self.name=name
        self.catalog=catalog
        self.section=section
        self.starts=starts
        self.ends=ends
        self.days=dyas
        self.prof=prof
    def display(self):
        print '%s:%s:%s:%s:%s:%s:%s' %(self.name,self.catalog,self.section,self.starts,self.ends,self.days,self.prof)
    def numeric_time(self):
        return (int(self.starts),int(self.ends))
uw=UWaterlooAPI(api_key=raw_input("Please Enter Your APIkey"))
courses=raw_input("Please enter your desired courses, e.g. 'CS 136, MATH 230'")

# acquiring course information

courses=courses.split(',')
course=[]
for i in range(0,len(courses)):
    a=courses[i].split()
    course.append((a[0],a[1]))
datalist=[]

#downloading data via the api

for k,v in course:
    datalist.append(uw.course_schedule(k,v))
time=raw_input('please enter the time period you would like to take course, e.g. "9:30,14:20" means courses starts from 9:30 ends before 14:20 everyday')
print  map(lambda x: filter(lambda a: a!=[], map(lambda y: y.__getitem__('classes')[0].__getitem__('instructors') , x)), datalist)
professor=raw_input('please select your preferred profs from the list above ,e.g. "Tompkins,Dave", you do not need to include u quote')

