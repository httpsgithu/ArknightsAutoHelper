# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import sys

if not hasattr(sys, '_using_makepackage'):
    print('NOTE: use packaging/makepackage.py to build package.')
    input('press Enter to continue anyway')

sys.modules['FixTk'] = None

extra_path = ['vendor/penguin_client']
hiddenimports = ['imgreco.ocr.baidu', 'imgreco.ocr.tesseract', 'imgreco.ocr.windows_media_ocr', 'automator.connector.enumerator.bluestacks_hyperv', 'automator.connector.enumerator.append']
excludes = ['FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter', 'resources', 'packaging', 'matplotlib']

a = Analysis(['akhelper.py'],
             pathex=extra_path,
             binaries=[],
             datas=[
                ('resources.zip', '.'),
                ('config/config-template.yaml', 'config'),
                ('config/device-config.schema.json', 'config'),
                ('config/logging.yaml', 'config'),
                ('LICENSE', '.'),
                ('README.md', '.'),
                ('tessdata', 'tessdata'),
                ('vendor/platform-tools', 'vendor/platform-tools'),
                ('vendor/tesseract', 'vendor/tesseract'),
                ('webgui2/dist', 'web'),
                ('extra_items/README.txt', 'extra_items'),
            ],
             hiddenimports=hiddenimports,
             hookspath=[],
             runtime_hooks=[],
             excludes=excludes,
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

agui = Analysis(['akhelper-gui.pyw'],
             pathex=extra_path,
             binaries=[],
             hiddenimports=hiddenimports,
             hookspath=[],
             runtime_hooks=[],
             excludes=excludes,
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

MERGE((a, 'akhelper', 'akhelper'), (agui, 'akhelper-gui', 'akhelper-gui'))

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
pyzgui = PYZ(agui.pure, agui.zipped_data, cipher=block_cipher)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True, name='akhelper', debug=False, icon='packaging/carrot.ico',
          bootloader_ignore_signals=False, strip=False, upx=True, console=True)
exegui = EXE(pyzgui, agui.scripts, [], exclude_binaries=True, name='akhelper-gui', debug=False, icon='packaging/carrot.ico',
          bootloader_ignore_signals=False, strip=False, upx=True, console=False)

def is_crt_binary(name):
    name = name.lower()
    prefixes = [
        'api-ms',
        'vcruntime',
        'msvcr',
        'msvcp',
        'vcomp',
        'concrt',
        'vccorlib',
        'ucrtbase',
    ]
    for prefix in prefixes:
        if name.startswith(prefix):
            return True
    return False

a.binaries[:] = (x for x in a.binaries if not is_crt_binary(x[0]) and 'opencv_videoio' not in x[0])
agui.binaries[:] = (x for x in agui.binaries if not is_crt_binary(x[0]) and 'opencv_videoio' not in x[0])

coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas, exegui, agui.binaries, agui.zipfiles, agui.datas, strip=False, upx=False, upx_exclude=[], name='akhelper')

import os
os.mkdir(os.path.join(DISTPATH, 'akhelper', 'screenshot'))
