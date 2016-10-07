from distutils.core import setup, Extension

setup(name='babeltrace',
      version='1.4.0',
      description='Babeltrace',
      author='EfficiOS',
      author_email='a@a.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['babeltrace'],
      ext_modules=[Extension(
          '_nativebt',
          ['nativebt.i', 'python-complements.c'],
          include_dirs=['../babeltrace', '../babeltrace/include', 'C:/msys64/mingw64/include/glib-2.0', 'C:/msys64/mingw64/lib/glib-2.0/include/'],
          extra_objects=['../babeltrace/formats/ctf/.libs/libbabeltrace-ctf.a', '../babeltrace/compat/.libs/libcompat.a', '../babeltrace/lib/.libs/libbabeltrace.a'],
#          library_dirs=[''],
          libraries=['glib-2.0', 'rpcrt4'],
#          define_macros=[('BABELTRACE_HAVE_LIBUUID', '1')],
          )],
     )
