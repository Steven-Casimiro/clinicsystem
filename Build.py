import PyInstaller.__main__

PyInstaller.__main__.run([
    '-y',
    '-w',
    '-n Dentist'
    '--hidden-import=babel.numbers',
    '--add-binary= clinic.db',
    'main.py'
])

