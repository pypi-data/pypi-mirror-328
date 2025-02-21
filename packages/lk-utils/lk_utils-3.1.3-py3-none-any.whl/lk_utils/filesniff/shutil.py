import os
import shutil
import typing as t
from os.path import exists
from textwrap import dedent
from zipfile import ZIP_DEFLATED
from zipfile import ZipFile

from .finder import findall_dirs
from .finder import findall_files
from .main import IS_WINDOWS  # noqa
from .main import basename
from .main import dirname
from .main import isdir
from .main import relpath
from .main import xpath
from ..subproc import run_cmd_args

__all__ = [
    'clone_tree',
    'copy_file',
    'copy_tree',
    'make_dir',
    'make_dirs',
    'make_file',
    'make_link',
    'make_links',
    'make_shortcut',
    'move',
    'move_file',
    'move_tree',
    'remove',
    'remove_file',
    'remove_tree',
    'unzip',
    'unzip_file',
    'zip',
    'zip_dir',
]


class T:
    OverwriteScheme = t.Optional[bool]


def clone_tree(src: str, dst: str, overwrite: T.OverwriteScheme = None) -> None:
    if exists(dst):
        if _overwrite(dst, overwrite) is False:
            return
    if not exists(dst):
        os.mkdir(dst)
    for d in findall_dirs(src):
        dp_o = f'{dst}/{d.relpath}'
        if not exists(dp_o):
            os.mkdir(dp_o)


def copy_file(src: str, dst: str, overwrite: T.OverwriteScheme = None) -> None:
    if exists(dst):
        if _overwrite(dst, overwrite) is False:
            return
    shutil.copyfile(src, dst)


def copy_tree(
    src: str,
    dst: str,
    overwrite: T.OverwriteScheme = None,
    symlinks: bool = False
) -> None:
    if exists(dst):
        if _overwrite(dst, overwrite) is False:
            return
    shutil.copytree(src, dst, symlinks=symlinks)


def make_dir(dst: str) -> None:
    if not exists(dst):
        os.mkdir(dst)


def make_dirs(dst: str) -> None:
    os.makedirs(dst, exist_ok=True)


def make_file(dst: str) -> None:
    open(dst, 'w').close()


def make_link(src: str, dst: str, overwrite: T.OverwriteScheme = None) -> str:
    """
    args:
        overwrite:
            True: if exists, overwrite
            False: if exists, raise an error
            None: if exists, skip it
    
    ref: https://blog.walterlv.com/post/ntfs-link-comparisons.html
    """
    from .main import normpath
    
    src = normpath(src, force_abspath=True)
    dst = normpath(dst, force_abspath=True)
    
    assert exists(src), src
    if exists(dst):
        if _overwrite(dst, overwrite) is False:
            return dst
    
    if IS_WINDOWS:
        os.symlink(src, dst, target_is_directory=os.path.isdir(src))
    else:
        os.symlink(src, dst)
    
    return dst


def make_links(
    src: str,
    dst: str,
    names: t.List[str] = None,
    overwrite: T.OverwriteScheme = None
) -> t.List[str]:
    out = []
    for n in names or os.listdir(src):
        out.append(make_link(f'{src}/{n}', f'{dst}/{n}', overwrite))
    return out


def make_shortcut(
    src: str,
    dst: str = None,
    overwrite: T.OverwriteScheme = None
) -> None:
    """
    use batch script to create shortcut, no pywin32 required.
    
    params:
        dst:
            if not given, will create a shortcut in the same folder as `src`, -
            with the same base name.
            trick: use "<desktop>" to create a shortcut on the desktop.
    
    refs:
        https://superuser.com/questions/455364/how-to-create-a-shortcut
        -using-a-batch-script
        https://www.blog.pythonlibrary.org/2010/01/23/using-python-to-create
        -shortcuts/
    """
    if exists(dst):
        if _overwrite(dst, overwrite) is False:
            return
    if not IS_WINDOWS:
        raise NotImplementedError
    
    assert exists(src) and not src.endswith('.lnk')
    if not dst:
        dst = os.path.splitext(os.path.basename(src))[0] + '.lnk'
    else:
        assert dst.endswith('.lnk')
        if '<desktop>' in dst:
            dst = dst.replace('<desktop>', os.path.expanduser('~/Desktop'))
    
    vbs = xpath('./_temp_shortcut_generator.vbs')
    with open(vbs, 'w') as f:
        f.write(dedent('''
            Set objWS = WScript.CreateObject("WScript.Shell")
            lnkFile = "{file_o}"
            Set objLink = objWS.CreateShortcut(lnkFile)
            objLink.TargetPath = "{file_i}"
            objLink.Save
        ''').format(
            file_i=src.replace('/', '\\'),
            file_o=dst.replace('/', '\\'),
        ))
    run_cmd_args('cscript', '/nologo', vbs)
    os.remove(vbs)


# def merge_tree(src: str, dst: str, overwrite: bool = False) -> None:
#     if overwrite:  # TODO
#         raise NotImplementedError
#     src_dirs = frozenset(x.relpath for x in findall_dirs(src))
#     src_files = frozenset(x.relpath for x in findall_files(src))
#     dst_dirs = frozenset(x.relpath for x in findall_dirs(dst))
#     dst_files = frozenset(x.relpath for x in findall_files(dst))
#     # TODO


def move(src: str, dst: str, overwrite: T.OverwriteScheme = None) -> None:
    if exists(dst):
        if _overwrite(dst, overwrite) is False:
            return
    shutil.move(src, dst)


move_file = move
move_tree = move


def remove(dst: str) -> None:
    if exists(dst):
        if os.path.isfile(dst):
            os.remove(dst)
        elif os.path.islink(dst):
            os.unlink(dst)
        else:
            shutil.rmtree(dst)


def remove_file(dst: str) -> None:
    if exists(dst):
        os.remove(dst)


def remove_tree(dst: str) -> None:
    if exists(dst):
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        elif os.path.islink(dst):
            os.unlink(dst)
        else:
            raise Exception('Unknown file type', dst)


def zip_dir(
    src: str,
    dst: str = None,
    overwrite: T.OverwriteScheme = None,
    compress_level: int = 7,
) -> str:
    """
    ref: https://likianta.blog.csdn.net/article/details/126710855
    """
    if dst is None:
        dst = src + '.zip'
    else:
        assert dst.endswith('.zip')
    if exists(dst):
        if _overwrite(dst, overwrite) is False:
            return dst
    top_name = basename(dst[:-4])
    with ZipFile(
        dst, 'w', compression=ZIP_DEFLATED, compresslevel=compress_level
    ) as z:
        z.write(src, arcname=top_name)
        for f in tuple(findall_files(src)):
            z.write(f.path, arcname='{}/{}'.format(
                top_name, relpath(f.path, src)
            ))
    return dst


def unzip_file(
    src: str,
    dst: str = None,
    overwrite: T.OverwriteScheme = None,
    compress_level: int = 7,
) -> str:
    assert src.endswith('.zip')
    if dst is None:
        dst = src[:-4]
    # print(src, dst, overwrite, exists(path_o), ':lvp')
    if exists(dst):
        if _overwrite(dst, overwrite) is False:
            return dst
    
    dirname_o = dirname(dst)
    with ZipFile(
        src, 'r', compression=ZIP_DEFLATED, compresslevel=compress_level
    ) as z:
        if IS_WINDOWS:
            # avoid path limit error in windows.
            # ref: docs/devnote/issues-summary-202401.zh.md
            z.extractall('\\\\?\\' + dst.replace('/', '\\'))
        else:
            z.extractall(dst)
    
    dlist = tuple(
        x for x in os.listdir(dst)
        if x not in ('.DS_Store', '__MACOSX')
    )
    if len(dlist) == 1:
        x = dlist[0]
        if isdir(f'{dst}/{x}'):
            if x == dirname_o:
                print(
                    f'move up sub folder [cyan]({x})[/] to be parent', ':vspr'
                )
                dir_m = f'{dst}_tmp'
                assert not exists(dir_m)
                os.rename(dst, dir_m)
                shutil.move(f'{dir_m}/{x}', dst)
                shutil.rmtree(dir_m)
            else:
                print(
                    f'notice there is only one folder [magenta]({x})[/] in '
                    f'this folder: [yellow]{dst}[/]. '
                    '[dim](we don\'t move up it because its name is not same '
                    'with its parent.)[/]',
                    ':pr',
                )
    return dst


zip = zip_dir
unzip = unzip_file


def _overwrite(path: str, scheme: T.OverwriteScheme) -> bool:
    """
    args:
        scheme:
            True: overwrite
            False: no overwrite, and raise an FileExistsError
            None: no overwrite, no error (skip)
    returns: bool
        the return value reflects what "overwrite" results in, literally.
        i.e. True means "we DID overwrite", False means "we DID NOT overwrite".
        the caller should take care of the return value and do the leftovers. \
        usually, if caller receives True, it can continue its work; if False, \
        should return at once.
    """
    if scheme is None:
        return False
    elif scheme is True:
        remove(path)
        return True
    else:  # raise error
        raise FileExistsError(path)
