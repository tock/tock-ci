# ![Tock CI](http://www.tockos.org/assets/img/tockci.svg#a "Tock CI Logo")

Tool for testing Tock on actual hardware.

Goals
-----

The grand vision is to run this as a continuous integration (CI) test on every
pull request to the Tock repository. This would mean that code is tested on
actual hardware, rather than just compiled (as it is now).

So, a computer would sit somewhere with a bunch of Tock-supporting-boards
plugged into it, and this tool would download the correct Tock kernel commit,
compile it for each board, flash it on each board, and then run a series of
tests to determine if the code still works.

The next step would be to make this CI tool work in a distributed fashion, so
maintainers of various boards could run this tool on a local computer and have
the CI tool test PRs on their hardware.

Status
------

This description is unlikely to get updated along the way, but this project is
somewhat ambitious and won't materialize very quickly.

The first steps are:

1. To have some format to describe test cases, and what success looks like.

1. To be able to run those tests on actual hardware and detect success.

Specific Todos
--------------

- Determine a hardware platform we intend to run this on. It's probably not worth
trying to support multiple platforms if we have some small Linux platform that
isn't too expensive.


Internal Notes
--------------

### Test Locally

To test the code locally without installing as a package, from the top-level
directory:

    python3 -m tockloader.main <COMMANDS>


### Upload to PyPI

    python3 setup.py sdist bdist_wheel
    twine upload dist/*

