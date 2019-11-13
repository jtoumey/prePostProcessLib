import sys
sys.path.append('../openFoamLib')

import foamDictTools as fdt


test_file_handle = 'testDict'
test_file = fdt.OfDict(test_file_handle)


buffer = '\n Sample file written via the OfDict class.\n'

test_file.clearLine()
test_file.writeBuffer(buffer)
test_file.clearLine()
