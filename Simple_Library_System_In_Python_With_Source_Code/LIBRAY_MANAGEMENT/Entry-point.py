from dbm.ndbm import library

import db
import sys
import os

from LIBRAY_MANAGEMENT import Reg

py=sys.executable


# Entry point for application
if __name__ == '__main__':
    if not db.checkSetup():
        db.setup()
        os.system('%s %s' % (py, 'Reg.py'))
    else:
        os.system('%s %s' % (py, 'main.py'))
