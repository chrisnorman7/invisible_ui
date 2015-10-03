from setuptools import setup

setup(
 name = 'invisible_ui',
 version = '1.4',
 description = 'Accessible UI elements for pygame.',
 url = 'http://github.com/chrisnorman7/invisible_ui.git',
 author = 'Chris Norman',
 author_email = 'chris.norman2@googlemail.com',
 license = 'GPL',
 packages = ['invisible_ui', 'invisible_ui.elements', 'invisible_ui.xtras'],
 zip_safe = True,
 keywords = ['ui', 'pygame', 'accessible', 'a11y', 'accessible', 'spoken', 'menu', 'element'],
 install_requires = [
  'pygame'
 ],
 dependency_links = [
  'hg+http://hg.q-continuum.net/accessible_output2#egg=accessible_output2'
 ]
)
