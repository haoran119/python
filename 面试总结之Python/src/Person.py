"""
Complete the program
"""


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

# >>> TODO
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def add_mobile_number(self, mobile_number):
        self.mobile_number = mobile_number.replace(" ", "")
# <<<


class Developer(Person):

    def __init__(self, programming_language, first_name, last_name):
        super().__init__(first_name, last_name)
        self.programming_language = programming_language

# >>> TODO
    def update_programming_language(self, programming_language):
        self.programming_language = programming_language
# <<<


if __name__ == '__main__':

    dev_1_first_name = 'John'
    dev_1_last_name = 'Smith'
    dev1_programming_language = 'Python'

    # -- TODO: Start here ---> Implement functions in the Developer and Person objects so that these commands work
    dev_1 = Developer(programming_language=dev1_programming_language,
                      first_name=dev_1_first_name,
                      last_name=dev_1_last_name)

    dev_1.add_mobile_number(mobile_number='0412 345 678')  # Note: the format is wrong. We expect a format of xxxxxxxxxx
    dev_1.update_programming_language(programming_language='swift')

    # -- These commands should run without error to complete the task
    assert dev_1.full_name == f'{dev_1_first_name} {dev_1_last_name}'
    assert dev_1.mobile_number == '0412345678'
    assert dev_1.programming_language == 'swift'

    person_2 = Person(first_name='Adam', last_name='Rodgers')
    person_2.add_mobile_number('0499888777')
    assert person_2.mobile_number == '0499888777'

    try:
        person_2.programming_language
        complete = False
    except AttributeError:
        complete = True
    assert complete is True

    print('Completed!')
