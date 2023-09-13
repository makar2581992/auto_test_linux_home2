import subprocess
import hashlib


def test_list_files():
    result = subprocess.run(['./project', 'l'], capture_output=True, text=True)
    output = result.stdout.strip()

    expected_files = ['file1.txt']

    assert output == '\n'.join(expected_files)


def test_extract_files():

    # Извлечение файлов
    result = subprocess.run(['./project', 'x'], capture_output=True, text=True)
    output = result.stdout.strip()

    # Определение пути к файлу
    expected_files = [" cd /home/user/file1.txt"]

    assert output == '\n'.join(expected_files)


def test_calculate_hash():
    # Запуск вычисления хеша
    result = subprocess.run(['./project', 'h'], capture_output=True, text=True)
    output = result.stdout.strip()


    md5_hash = hashlib.md5()
    md5_hash.update(open('file1.txt', 'rb').read())
    expected_hash = md5_hash.hexdigest()

    assert output == expected_hash


# Запуск тестов
test_list_files()
test_extract_files()
test_calculate_hash()
