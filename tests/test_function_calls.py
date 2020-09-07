import semgrepl.main as sm

def test_python_function_calls_simple():
    config = sm.init("tests/testcases/python/function_calls/simple.py")
    calls = sm.function_calls(config)
    assert len(calls) == 1
    assert calls[0].name == "bar"

def test_python_function_calls_instance():
    config = sm.init("tests/testcases/python/function_calls/instance.py")
    calls = sm.function_calls(config)
    assert len(calls) == 3
    for call in calls:
        if call.name == "write":
            assert(call.instance == "tf")
