from typing import List


def find_special_rows(rows: List[str]) -> List[str]:
    rows_with_duplicates = []

    for row in rows:
        unique_numbers = []

        for number in row.split(' '):
            if number not in unique_numbers:
                unique_numbers.append(number)
            else:
                rows_with_duplicates.append(row)
                break

    return rows_with_duplicates


def write_file(data: List[str]) -> None:
    file = open('files/output.txt', 'w')
    file.write('\n'.join(data))


def read_file() -> str:
    file = open("files/file.txt", 'r', encoding='utf-8')

    return file.read()


def main():
    data = read_file()
    result = find_special_rows(data.split("\n"))
    write_file(result)

    print("Check your output file at /files!")


if __name__ == '__main__':
    main()