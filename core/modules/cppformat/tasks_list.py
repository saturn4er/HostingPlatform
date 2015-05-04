import os

from config import directories
from core.default_structures import cleanup_extensions


sources_dir = "sources"
build_directory = os.path.join(directories['buildDir'], 'cppformat')
lib_directory = os.path.join(build_directory, 'lib')
headers_dir = os.path.join(build_directory, 'headers')
vcxproj_file = os.path.join(sources_dir, 'format.vcxproj')

build_tasks = [
    {"task": "check_dependencies", "params": ("version", 'rebuild')},
    {"task": "git_clone", "repository": "https://github.com/cppformat/cppformat.git", "sources_dir": sources_dir,
     'description': 'Downloading'},
    {"task": "git_checkout", "sources_dir": sources_dir, "branch": "{version}",
     'description': 'Checkout...'},

    {"task": "run_cmake_and_build", "sources_dir": sources_dir, "architecture": "x32",
     "user_task": True, 'description': 'Running cmake for Win32...'},
    {"task": "set_vcxproj_runtime_library", "vcxproj_file": vcxproj_file, 'description': 'Setting runtime library...'},
    {"task": "make", "vcxproj_file": vcxproj_file, 'output_dir': lib_directory,
     'description': 'Build project for win32'},

    {"task": "run_cmake_and_build", "sources_dir": sources_dir, "architecture": "x64",
     "user_task": True, 'description': 'Running cmake for Win64...'},
    {"task": "set_vcxproj_runtime_library", "vcxproj_file": vcxproj_file, 'description': 'Setting runtime library...'},
    {"task": "make", "vcxproj_file": vcxproj_file, 'output_dir': lib_directory,
     'description': 'Build project for win64'},


    {"task": "move_files_to_dir_by_mask", 'overwrite': True, 'destination': headers_dir,
     'mask': os.path.join(sources_dir, '*.h'), 'description': "Copy includes..."},
    {"task": "rdfff", "directory": sources_dir, "extensions": cleanup_extensions["c++"],
     'description': 'Cleaning up trash..'}

]
integration_tasks = [

    {'task': 'add_library', 'config': ('windows', 'x86', 'release'), 'library_location':
        os.path.join(build_directory + '/Release/Win32/format.lib')},
    {'task': 'add_library', 'config': ('windows', 'x86', 'debug'), 'library_location':
        os.path.join(build_directory + '/Debug/Win32/format.lib')},
    # x32
    {'task': 'add_library', 'config': ('windows', 'x64', 'release'), 'library_location':
        os.path.join(build_directory + '/Release/x64/format.lib')},
    {'task': 'add_library', 'config': ('windows', 'x64', 'debug'), 'library_location':
        os.path.join(build_directory + '/Debug/x64/format.lib')},

    {'task': 'add_location', 'location': headers_dir},
]