import sys
sys.path.append('../openFoamLib')

import logTools as ot

log_file_name = 'log.out'

lf = ot.LogFile(log_file_name)


lf.parseRunTime()
