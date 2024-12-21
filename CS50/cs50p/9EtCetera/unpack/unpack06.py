# *args, **kwargs
def f(*args, **kwargs):
    print("Named: ", kwargs)


f(galleons=100, sickles=50, knuts=25)
# python unpack06.py
# Named: ('galleons': 100, 'sickles': 50,'knuts': 25)