from setuptools import setup, find_packages
import appserv_fake_app

version = appserv_fake_app.__version__

if __name__ == '__main__':
    setup(name='appserv_fake_app',
          version=appserv_fake_app.__version__,
          description="appserv_fake_app",
          long_description="""\
              """,
          classifiers=[],
          keywords='',
          author='',
          author_email='',
          url='',
          license='',
          zip_safe=False,
          include_package_data=True,
          packages=find_packages(exclude=["tests"]),
          install_requires=[
              "pyspacewar==0.9.7"
          ]
    )
