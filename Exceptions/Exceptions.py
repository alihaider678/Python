try:
    f = open('CurruptFile.txt')
    # if f.name == 'currupt_file.txt':
    #     raise Exception
except IOError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

print('End of program')