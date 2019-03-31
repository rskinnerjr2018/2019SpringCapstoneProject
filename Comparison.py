import difflib
file1 = raw_input("Enter text file 1:")
file2 = raw_input('Enter text file 2:')

def main():
    with open('filename.txt', 'w') as file_out:

        line_no = 0
        for line in difflib.unified_diff(file1,file2):
                line_no += 1
                file_out.write(line)
                file_out.write(str(line_no))

if __name__ == '__main__':
    main()