# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['maze_car.py'],
             pathex=["C:\\Users\\user\\Desktop\\PAIA-MLGame-Bots\\launcher"],
             binaries=[],
             datas=[
                 ("images\\car_01.png", "images"),
                 ("images\\car_02.png", "images"),
                 ("images\\car_03.png", "images"),
                 ("images\\car_04.png", "images"),
                 ("images\\car_05.png", "images"),
                 ("images\\car_06.png", "images"),
             ],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas, [],
          name='maze_car',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None)
