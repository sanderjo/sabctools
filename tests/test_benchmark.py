from tests.testsupport import *

def test_sabctools_decode(benchmark):
    data_plain = read_plain_yenc_file("test_regular.yenc")
    benchmark(sabctools_yenc_wrapper, data_plain)

def test_python_decode(benchmark):
    data_plain = read_plain_yenc_file("test_regular.yenc")
    benchmark(python_yenc, data_plain)
    
