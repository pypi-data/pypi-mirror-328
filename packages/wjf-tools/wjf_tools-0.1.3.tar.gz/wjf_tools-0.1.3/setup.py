from distutils.core import setup
setup(
  name = 'wjf_tools',         # How you named your package folder (MyLib)
  packages = ['wjf_tools'],   # Chose the same as "name"
  version = '0.1.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'all kinds of API',   # Give a short description about your library
  author = 'Jinfang Wei',                   # Type in your name
  author_email = '2295542405@qq.com',      # Type in your E-Mail
  url = '',   # Provide either the link to your github or to your website
  download_url = '',    # I explain this later on
  keywords = ['API', 'tools', 'Python'],   # Keywords that define your package best
  install_requires=[  # I get to this in a second
    'requests',  # 可以加上版本号，如validators=1.5.1
    'datetime',
    'urllib3==1.26.6',
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.7',
  ]
)
