# semgrepl

[Semgrep](https://github.com/returntocorp/semgrep) is a powerful, lightweight
static analysis tool that makes it easy to bugs or potential code of interest
across many languages.

The default Semgrep workflow is to write patterns that find what you're looking for, and then review the results.

`semgrepl` (a combination of "Semgrep" and "REPL"), on the other hand, aims to
enable you to *iteratively*, *interactively* search code. For example:
* Find all of a web app's routes. Then, filter them down based to the routes not
  requiring a certain annotation (e.g. `@requires_authentication`) or routes
  that lead to potentially dangerous code like an unparameterized SQL query.
* Find all methods that call potentially sketchy APIs like `eval()`, `exec()` or
  running shell commands. Then, recursively find methods calling those methods
  until you reach an entry point, like a `main()` method or HTTP endpoint.

In short, `semgrepl` allows you run Semgrep patterns programmatically via a
Python REPL and load the results back and interact with them as Python objects.
The results of prior queries can then be used to customize future ones.

## How It Works

* `main.py` wraps running the Semgrep binary and has a number of helper
  functions that do common tasks like extracting imports, finding function
  definitions, etc.
* `rules/` contains a number of Semgrep patterns that are used by `main.py` and
  other parts of `semgrepl`. Note that some of these patterns are templatized
  using [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) to allow
  programmatically running slightly different but similar Semgrep patterns; for
  example, find all methods named `<user input>`.
* `notebooks/` contains example Python Jupyter notebooks that illustrate usage
  of `semgrepl`.



## Getting Set Up

### Using Docker

Build the docker image using:
`docker build -t semgrepl .`

Run the docker container using:
`docker run --rm -p 8888:8888 semgrepl`

This will start a Jupyter Notebook where you can use `semgrepl`.

Try setting the target to `..` to run it on itself.


### Manual

Python package dependencies can be installed using
`pip3 install -r requirements.txt`.

Also install [tokei](https://github.com/XAMPPRocky/tokei) for getting
code/languages used.

## Hacking on semgrepl in ipython

When developing semgrepl it is convenient to have ipython autoreload modules.
That way you can keep ipython open and it reloads the module when you save a
file. Type the following magic commands when ipython is first loaded:

```
%load_ext autoreload
%autoreload 2
```

Note: You can autorun the above commands on IPython startup using a config file
[docs](https://ipython.readthedocs.io/en/stable/config/intro.html). This can be
a global config file or via `ipython_config.py` in your current working
directory. You can see all locations in which IPython is looking for configuration files by starting ipython in debug mode:

~~~bash
$ ipython --debug -c 'exit()'
~~~

The main entrypoint into semgrepl is `utils.py` which can be loaded in ipython
with:


For example, to find all function definitions in the file `semgrepl/main.py`.
```
import semgrepl.main as sm
config = sm.init("semgrepl/main.py")
sm.all_function_defs(config)
```

### `semgrepl_init`

Oftentimes you have a specific target repo(s) in mind.

Use `semgrepl_init` to set your "working directory" of rules and target repo dirs, so you don't have pass them in to every semgrepl function.

~~~python
import semgrepl.main as sm
# Add 1 dir as a target
config = sm.init(path_to_repo)

# Or, Add every dir in a directory as a target, uses glob.glob()
config = sm.init_dir("Users/me/target_repos/*")

# Examine the config that's been set up
config

# See the various tech stacks used
config.print_languages_used()
~~~

### Running tests

From root of repo, type `pytest`.
