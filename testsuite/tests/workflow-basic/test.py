"""
Test a basic get-build-run workflow.

TODO: this test relies on external resources (GitHub repositories for the
hello/libhello crates sources). This makes this test slower than needed and
potentially unstable. We should refactor it to rely only on testsuite files
instead.
"""

from glob import glob
import os

from drivers.alr import run_alr
from drivers.asserts import assert_eq


# Get the "hello" project and enter its directory
run_alr('get', '-q', 'hello')
os.chdir(glob('hello*')[0])

# Build it
run_alr('build', '-q')

# Run it
p = run_alr('run', '-q')
assert_eq('Hello, world!\n' , p.out)

print('SUCCESS')
