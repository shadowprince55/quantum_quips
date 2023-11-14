# !pip3 install pyqpanda
# https://github.com/OriginQ/QPanda-2

from pyqpanda import *

qvm = CPUQVM()
qvm.init_qvm()
prog = QProg()
q = qvm.qAlloc_many(4)
c = qvm.cAlloc_many(4)
prog<< H(q[0])\
    << CNOT(q[0:-1], q[1:])\
    << measure_all(q,c)
result = qvm.run_with_configuration(prog, c, 1000)
print(result)
qvm.finalize()

