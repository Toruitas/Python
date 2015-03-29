__author__ = 'Stuart'


from threading import Thread


def async(f):
    """
    Indirectly creates framework for asynchronous tasks.
    :param f: function
    :return:
    """
    def wrapper(*args,**kwargs):
        """
        Creates threat object, with target being the function f.
        args/kwargs change depending on function.
        For send_async_email: [app,msg] are args. And there are no kwargs.
        :param args:
        :param kwargs:
        :return:
        """
        thr = Thread(target=f,args=args,kwargs=kwargs)
        thr.start()
    return wrapper

"""
As an exercise, how would this look using processes instead of threads?
We don't want a new process started for each email that we need to send, so we instead an use
Pool class from multiprocessing module.
Class creates a specified number of processes (which are forks of the main process) and all those wait to recieve
jobs to run, given to the pool via the 'apply_async' method.
Could be very useful and interesting for a busy site.
"""