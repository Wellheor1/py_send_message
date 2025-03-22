import sys
sys.path.append('../py_send_message')
from settings import MODULES

modules = {module for module in MODULES if MODULES[module]}
print(modules)
# settings_dir = os.path.join(root_dir, 'settings')
# local_settings_dir = os.path.join(root_dir, 'settings', 'local_settings')
# ignore_files = {'__init__.py', '__pycache__', 'local_settings'}
# print(f'Копирование файлов\nиз: {settings_dir}\nв {local_settings_dir}')
#
# settings_files = set(os.listdir(settings_dir)) - ignore_files
# local_settings_files = set(os.listdir(local_settings_dir)) - ignore_files
#
# local_settings_files = {file_name.split('_')[1] for file_name in local_settings_files}
#
# files_to_copy = settings_files - local_settings_files
# print('Следующие файлы будут скопированы:', files_to_copy)
# for file_name in files_to_copy:
#     shutil.copy(os.path.join(settings_dir, file_name), f"{local_settings_dir}/local_{file_name}")
# print('Файлы успешно скопированы')
