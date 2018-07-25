from datetime import datetime, timedelta

BASETIME = datetime.now()

def in_time(time_x, time_y):
    '''
    Decorator to judge if a function called during specific period
    :param datatime time_x: start_time or end_time of the period
    :param datatime time_y: end_time or start_time of the period
    '''
    def func_decorator(func):
        def wrapper(*args, **kwargs):
            time_now = datetime.now() # get closest execution time
            result = func(*args, **kwargs) # execute target function
            if time_x < time_y:
                if time_now >= time_x and time_now <= time_y:
                    print('in time !')
            else:
                if time_now >= time_y and time_now <= time_x:
                    print('in time !')
            return result
        return wrapper
    return func_decorator

@in_time(BASETIME-timedelta(seconds=10),
		 BASETIME+timedelta(seconds=10))
def foo():
	print('execute foo()')

@in_time(BASETIME+timedelta(seconds=10),
		 BASETIME+timedelta(seconds=20))
def foo2():
	print('execute foo2()')

@in_time(BASETIME-timedelta(seconds=10),
         BASETIME-timedelta(seconds=20))
def foo3():
    print('execute foo3()')

@in_time(BASETIME+timedelta(seconds=10),
         BASETIME-timedelta(seconds=10))
def foo4():
    print('execute foo4()')


foo()
foo2()
foo3()
foo4()