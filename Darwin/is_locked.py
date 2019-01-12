import Quartz
d = Quartz.CGSessionCopyCurrentDictionary()
print('CGSSessionScreenIsLocked' in d.keys())
