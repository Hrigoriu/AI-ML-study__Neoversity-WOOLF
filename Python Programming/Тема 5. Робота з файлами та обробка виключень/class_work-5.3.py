import shutil

# Створення ZIP-архіву з вмістом директорії 'my_folder'
shutil.make_archive('example', 'zip', root_dir='my_folder')

#------------------------------
import shutil

# Створення TAR.GZ архіву
shutil.make_archive('example', 'gztar', root_dir='my_folder')

#------------------------------
import shutil

# Створення TAR.GZ архіву
shutil.make_archive('example', 'gztar', root_dir='my_folder')

#------------------------------
import shutil

# Копіюємо файл
source_file = '/path/to/source/file.txt'
destination_dir = '/path/to/destination'
shutil.copy(source_file, destination_dir)

# Копіюємо всю директорію
source_dir = '/path/to/source/directory'
destination_dir = '/path/to/destination/directory'
shutil.copytree(source_dir, destination_dir)

#------------------------------
