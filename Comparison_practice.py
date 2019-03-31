fname1 = raw_input("Enter the first filename: ")
fname2 = raw_input("Enter the second filename: ")
def main():
    with open(fname1, 'r') as file1:
        with open(fname2, 'r') as file2:
            same = set(file1).difference(file2)

    same.discard('\n')
    line_no = 0
    with open('outputfile.txt', 'w') as file_out:
        for line in same:
                line_no += 1
                file_out.write(line)
                file_out.write(str(line_no))


if __name__ == '__main__':
    main()
