import os
import sys


def list_files(startpath):
    output = []
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        output.append('{}- {}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            size_in_gb = os.path.getsize(os.path.join(root, f)) / (10 ** 9)  # convert size to GB
            output.append('{}+ {} ({:.2f} GB)'.format(subindent, f, size_in_gb))
    return output


def write_to_file(lines, output_file):
    with open(output_file, 'w') as f:
        for line in lines:
            f.write(f'{line}\n')


directory_path = os.path.dirname(os.path.abspath(sys.executable))
output_file_path = os.path.join(directory_path, 'output.txt')
file_lines = list_files(directory_path)
write_to_file(file_lines, output_file_path)
