from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break

class AddressBook(UserDict):
    def add_record(self, name, phones=None):
        record = Record(name)
        if phones:
            for phone in phones:
                record.add_phone(phone)
        self.data[name] = record

    def delete_record(self, name):
        del self.data[name]

    def edit_record(self, name, new_name=None, new_phones=None):
        if name not in self.data:
            print(f"{name} not found in the address book.")
            return

        record = self.data[name]
        if new_name:
            record.name.value = new_name

        if new_phones:
            record.phones = []
            for phone in new_phones:
                record.add_phone(phone)

    def find_records_by_name(self, name):
        results = []
        for record in self.data.values():
            if record.name.value == name:
                results.append(record)
        return results

    def find_records_by_phone(self, phone):
        results = []
        for record in self.data.values():
            for record_phone in record.phones:
                if record_phone.value == phone:
                    results.append(record)
                    break
        return results


if __name__ == "__main__":

    address_book = AddressBook()


