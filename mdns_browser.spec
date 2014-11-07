# -*- mode: python -*-
a = Analysis(['mdns_browser.py'],
             pathex=['I:\\mdns_browser'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)

a.datas += [ ('mobacon.ico', './mobacon.ico', 'DATA')]

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mdns_browser.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False)
