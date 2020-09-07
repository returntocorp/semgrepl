import semgrepl.main as sm

def _find_import(import_name, imports):
    for i in imports:
        if i.import_path == import_name:
            return True
    return False

def test_go_imports_simple():
    config = sm.init("tests/testcases/go/imports/simple.go")
    imports = sm.imports(config)
    # Would be nice to strip quotes here.
    assert _find_import('"fmt"', imports)

def test_java_imports_simple():
    config = sm.init("tests/testcases/java/imports/simple.java")
    imports = sm.imports(config)
    # Do we want / can we get the full path java.util.ArrayList?
    assert _find_import("ArrayList", imports)

def test_javascripts_import_simple():
    config = sm.init("tests/testcases/javascript/imports/simple.js")
    imports = sm.imports(config)
    assert _find_import('"d3".d3', imports)

def test_python_imports_simple():
    config = sm.init("tests/testcases/python/imports/simple.py")
    imports = sm.imports(config)
    assert _find_import("logging", imports)

