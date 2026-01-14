class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact_obj):
        self.contacts.append(contact_obj)

    def show(self):
        return "\n".join([f"{c.name} {c.email} {c.phone}" for c in self.contacts])

if __name__ == "__main__":
    cl = ContactList()
    cl.add_contact(Contact("John Brown", "brown@onet.pl", "555234000"))
    print(cl.show())