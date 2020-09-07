import semgrepl.main as sm

def test_python_classes_simple():
    config = sm.init("tests/testcases/python/classes/simple.py")
    classes = sm.classes(config)
    assert len(classes) == 1
    assert classes[0].name == "Handler"
