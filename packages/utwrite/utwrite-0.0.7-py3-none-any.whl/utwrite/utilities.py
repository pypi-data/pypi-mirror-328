r"""Utilities for python unittest generator """
import os

def leading_whitespace(s):
    r"""Get amount of leading whitespace.

    Returns:
        `int`: Number of whitespaces

    Examples::

        from utwrite import utilities

        s = '    foo bar'
        utilities.leading_whitespace(s)
        # Result: 4 #
        utilities.leading_whitespace('no whitespace')
        # Result: 0 #
        utilities.leading_whitespace(' one  two   three')
        # Result: 1 #
    """
    return len(s) - len(s.lstrip(' '))
# [end] leading_whitespace

def get_files_from_dir(path, ext=[], ignore=[], sort_key=None):
    r"""Get files inside given path.

    Args:
        - path `str`: Path to get files in directory from.
        - ext `list`: Default []. Wanted extension filter (i.e. `.py`)
        - ignore `list`: Default []. Files wanted to ignore (i.e. `__init__.py`)
        - sortKey `str`: Default None. Key to use to sort in `files` list

    Returns:
        `list`: Files inside given `path` param matching criteria from params.

    Examples::

        from utwrite import utilities

        p = utilities.__file__
        files = utilities.get_files_from_dir(p)
        files = [os.path.basename(f) for f in files]
        expected_files = ['auto_generate_test.py', 'headers.py', 'unittest_cases.py', 'utilities.py']

        all (e in files for e in expected_files)
        # Result: True #

        '__init__.py' in files
        # Result: True #

        files = utilities.get_files_from_dir(p, ext=['.py'], ignore=['__init__.py'])
        files = [os.path.basename(f) for f in files]
        '__init__.py' in files
        # Result: False #

        'utilities.py' in files
        # Result: True #
    """
    if os.path.isfile(path):
        path = os.path.dirname(path)

    if not os.path.isdir(path):
        raise IOError('%s: Path does not exist'%path)

    if ext:
        ext = ['.%s'%e if e[0]!='.' else e for e in ext]

    files = [f for f in os.listdir(path) if f not in ignore]
    if ext:
        files = [f for f in files if os.path.splitext(f)[-1] in ext]

    files = [os.path.join(path,f) for f in files]
    if sort_key:
        files.sort(key=sort_key)
    return files
# [end] get_files_from_dir

def write_to_file(contents, fp, verbose=True):
    r"""Write contents to a file.

    Args:
        - contents `types`: Contents wanted to write to a file
        - fp `str`: File path to write contents on.
        - verbose `bool`: Default True, prints file writting messages.

    Returns:
        `bool`: True if file successfully written, False otherwise.

    Examples::

        from utwrite import utilities

        import os, tempfile, shutil

        temp_dir = os.path.join(tempfile.gettempdir(), 'utwrite_utilities_unittest_DELETE')
        f = os.path.join(temp_dir, 'f.txt')
        if os.path.isfile(f):
           shutil.rmtree(temp_dir)

        os.path.isfile(f)
        # Result: False #

        utilities.write_to_file('utwrite.utilities.write_to_file() unittest', f, verbose=False)

        os.path.isfile(f)
        # Result: True #

        # Delete temp dir
        if os.path.isdir(temp_dir):
            shutil.rmtree(temp_dir)
    """
    try:
        ensure_path_to_file(fp)
        populate_init_files(fp, verbose=verbose)
        with open(fp, 'w') as f:
            f.write(contents)
            if verbose:
                print('%s: File written!'%fp)
        return True
    except Exception as e:
        os.remove(fp)
        print('%s: Failed to write to file!\n%s'%(fp, e))
        return False
# [end] write_to_file

def populate_init_files(fp, root='', verbose=True):
    r"""Add `__init__.py` files along given filepath.

    Expects project root in PYTHONPATH.

    Args:
        - fp `str`: File to
        - root `str`: Root directory for head cut off.

    Returns:
        `None`: Creates `__init__.py` files and and print info

    Examples::

        from utwrite import utilities
        import os, tempfile, shutil

        root_dir = os.path.join(tempfile.gettempdir(), 'utwrite_utilities_unittest_DELETE')
        if os.path.isdir(root_dir):
            shutil.rmtree(root_dir)

        os.path.isdir(root_dir)
        # Result: False #

        f = os.path.join(root_dir, 'd1', 'd2', 'ut_file.py')

        # Ensure path to file is created
        utilities.ensure_path_to_file(f)

        # Populate init files along the way
        utilities.populate_init_files(f, root=root_dir, verbose=False)

        os.path.isfile(os.path.join(root_dir, '__init__.py'))
        # Result: False #
        os.path.isfile(os.path.join(root_dir, 'd1', '__init__.py'))
        # Result: True #
        os.path.isfile(os.path.join(root_dir, 'd1', 'd2', '__init__.py'))
        # Result: True #

        # Delete temp dir
        if os.path.isdir(root_dir):
            shutil.rmtree(root_dir)
    """
    fp_dir = os.path.dirname(fp)
    if not root:
        root = get_git_dir(fp) or fp_dir

    rel_path = os.path.relpath(fp_dir, root)
    populate_path = root
    for d in rel_path.split(os.sep):
        populate_path = os.path.join(populate_path, d)
        init_file = os.path.join(populate_path, '__init__.py')
        if not os.path.isfile(init_file):
            open(init_file, 'w').close()
            if verbose:
                print('%s: File created!'%init_file)
# [end] populate_init_files

def ensure_path_to_file(fp, create=True):
    r"""Create any missing directories to `fp`.

    Args:
        - fp `str`: File path to check for existence
        - created `bool`: Default True, if given `fp` does not exist, create
          it. Otherwise only create leading directories.

    Returns:
        `None`: Create directories. Create file, if `create` is True.

    :Tags:
        notest, already-tested

    Examples::

        from utwrite import utilities
        import os, tempfile, shutil

        root_dir = os.path.join(tempfile.gettempdir(), 'utwrite_utilities_unittest_DELETE')
        if os.path.isdir(root_dir):
            shutil.rmtree(root_dir)

        f = os.path.join(root_dir, 'd1', 'd2', 'ut_file.py')

        os.path.isfile(f)
        # Result: False #

        # Ensure path to file is created
        utilities.ensure_path_to_file(f)

        os.path.isfile(f)
        # Result: True #

        # Delete temp dir
        if os.path.isdir(root_dir):
            shutil.rmtree(root_dir)
    """

    dir_name = os.path.dirname(fp)
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    if create:
        open(fp, 'w').close()
# [end] ensure_path_to_file

def get_test_dir(module_path):
    r"""Get a tests directory.

    Args:
        - module_path `str`: Path to a python module file to get the `tests`
          directory from.

    Returns:
        `str`: Location path for `tests` directory

    Examples::

        from utwrite import utilities
        import os, tempfile, shutil

        root_dir = os.path.join(tempfile.gettempdir(), 'utwrite_utilities_unittest_DELETE')
        if os.path.isdir(root_dir):
            shutil.rmtree(root_dir)

        git_dir = os.path.join(root_dir, '.git')
        os.makedirs(git_dir)
        f = os.path.join(root_dir, 'd1', 'd2', 'ut_file.py')

        utilities.ensure_path_to_file(f)
        test_dir = utilities.get_test_dir(f)
        os.path.realpath(test_dir) == os.path.realpath(os.path.join(root_dir, 'tests', 'd1', 'd2'))
        # Result: True #

        # Delete temp dir
        if os.path.isdir(root_dir):
            shutil.rmtree(root_dir)

    """
    if not os.path.isfile(module_path):
        print('"%s": module path not a file'%module_path)
        return ''

    mod_dir = os.path.realpath(os.path.dirname(module_path))
    project_root = mod_dir

    # - Try to get git project root
    git_dir = get_git_dir(module_path)
    if git_dir:
        project_root = os.path.realpath(git_dir)

    rel_path = os.path.relpath(mod_dir, project_root)
    tst_dir = os.path.join(project_root, 'tests', rel_path)
    return tst_dir
# [end] get_test_dir

def get_git_dir(module_path):
    r"""Go up directories until find a .git dir.

    Args:
        - module_path `str`: Path to a python module file to get the root git
          directory from.

    Returns:
        `str`: Location path for Git repo root.

    :Tags:
        notest, already-tested

    Examples::

        from utwrite import utilities
        import os, tempfile, shutil

        root_dir = os.path.join(tempfile.gettempdir(), 'utwrite_utilities_unittest_DELETE')
        if os.path.isdir(root_dir):
            shutil.rmtree(root_dir)

        git_dir = os.path.join(root_dir, '.git')
        os.makedirs(git_dir)
        f = os.path.join(root_dir, 'd1', 'd2', 'ut_file.py')

        utilities.ensure_path_to_file(f)
        r = utilities.get_git_dir(f)

        os.path.isdir(os.path.join(r, '.git'))
        # Result: True #

        # Delete temp dir
        if os.path.isdir(root_dir):
            shutil.rmtree(root_dir)

    """

    if not os.path.isfile(module_path):
        raise RuntimeError('"%s": file given does not exist'%module_path)
    # walk up directories and look for a .git folder
    module_dir = os.path.realpath(os.path.dirname(module_path))
    directories = module_dir.split(os.path.sep)
    max_loops =100
    while directories:
        max_loops -=1
        if not max_loops:
            break
        p = os.path.sep.join(directories)
        gdir = os.path.join(p, '.git')
        if os.path.isdir(gdir):
            return p
        directories.pop()

    return ''
# [end] get_git_dir

def number_increase(st, increase_by=1):
    r"""Increase trailing number is `st` by `increase_by`.

    Args:
        - st `str`: String to increase trailing number
        - increase_by `int`: Number to increase the string by

    Returns:
        `str`: Resulting string with number increase

    Examples::

        from utwrite import utilities

        utilities.number_increase('some string')
        # Result: 'some string1' #
        utilities.number_increase('1_some_string_2')
        # Result:  '1_some_string_3'#
        utilities.number_increase('my_string_005', increase_by=10)
        # Result:  'my_string_015'#
    """
    last_char = st[-1]
    try:
        float(last_char)
        max_loops = 999
        counter=0
        idx=0
        charLen = len(st)
        for i in range(charLen):
            max_loops -=1
            if max_loops <0:
                break
            idx-=1
            if not st[idx].isnumeric():
                break
            counter+=1

        # shift idx back to last number
        idx+=1
        # increment number
        nextNum = int(st[idx:])+increase_by
        res = st[:idx]+str(nextNum).zfill(counter)
        return res
    except:
        # - does not end with a number, just add increase_by
        return st+str(increase_by)#'1'
# [end] number_increase

def flatten_list(l):
    r"""Flatten list given recursivelly

    Args:
        - l `list`: List to be flattened

    Returns:
        `list`: Flattened list

    Examples::

        from utwrite import utilities

        l = [0,1,[2],3,[4,[5,6,7,[8]]]]
        utilities.flatten_list(l)
        # Result:  [0, 1, 2, 3, 4, 5, 6, 7, 8] #
    """
    return_list = []
    for i in l:
        if isinstance(i, (list,tuple)):
            return_list.extend(flatten_list(i))
        else:
            return_list.append(i)

    return return_list
# [end] flatten_list
