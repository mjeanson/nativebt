from distutils.core import setup, Extension

setup(name='babeltrace',
      version='2.0.0',
      description='Babeltrace',
      author='EfficiOS',
      author_email='a@a.com',
      url='https://efficios.com/',
      packages=['babeltrace'],
      ext_modules=[Extension(
          '_nativebt',
          ['nativebt.i', 'python-complements.c'],
          include_dirs=['../babeltrace', '../babeltrace/include', 'C:/msys64/mingw64/include/glib-2.0', 'C:/msys64/mingw64/lib/glib-2.0/include/'],
          extra_objects=['../babeltrace/formats/ctf/.libs/libbabeltrace-ctf.a', '../babeltrace/compat/.libs/libcompat.a', '../babeltrace/lib/.libs/libbabeltrace.a'],
          extra_link_args=['-Wl,-Bstatic', '-lglib-2.0', '-lintl', '-lrpcrt4', '-lws2_32', '-lwinmm', '-liconv', '-lole32', '-Wl,-Bdynamic', '-static-libgcc'],
          )],
     )
