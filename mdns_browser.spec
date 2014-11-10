# -*- mode: python -*-
a = Analysis(['src\\mdns_browser.py'],
             pathex=['mdns_browser'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
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
          console=False , icon='favicon.ico')
