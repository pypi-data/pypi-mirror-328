""" Versatile collection of routines & tools for common development tasks """

__author__ = 'Dr. Marcus Zeller (dsp4444@gmail.com)'
__version__ = '0.1.2'
__all__ = []

# def main(verbose=False):
#     import zdev.base as zb
#     if (verbose):
#          print("Welcome to the 'zdev' package!")
#          print("Initialising Python...")
#     zb.init_session(zb._BASE, zb._ENVIRONMENT, verbose)
#     if (verbose): print("...done - have phun! ;)")
#     return

# main(True) # call 'init_session' with internal defaults if only 'import zdev'!

def demo():
    from zdev.plot import qplot
    print("Welcome to the zdev package!")
    tmp = input("Please enter some numbers (separated by ','): ") 
    x = str(tmp).split(',')
    qplot(x, info='what-u-just-entered')
    print("See how quickly things can be plotted?")
    print("Therefore... have phun! ;)")
    return

