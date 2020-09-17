# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from translate import Translator


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
try:
    with open('test.txt', mode='r') as my_file:
        content_list = my_file.readlines()
except FileNotFoundError:
    print("Check with your file")

translator = Translator(to_lang='ja')
item = ''
with open('JapText.txt',mode='w') as output_file:
    for item in content_list:
        textLine = translator.translate(item)
        print(textLine)
        output_file.write(textLine)
        output_file.write('\n')
