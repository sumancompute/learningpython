# press 1 to add a contact (name, email).. press 2 to list contacts
# other than 1 & 2, program exit
# if there is no any contact list, but user enters 2, then show , no list in the contact
contact_list = []
def add_contact(cname, cemail):
    new_contact = {"name":cname, "email":cemail}
    contact_list.append(new_contact)
    return

def list_contacts():
    if len(contact_list) == 0:
        print(" No contact added yet .")
        return
    
    for contact in contact_list:
        print(f"{contact["name"]} -- {contact["email"]}")
    return
    
def main():
    while True:
        num = input("Press 1 to add a contact, press 2 to list the contact details, press other to exit")

        match num:
            case "1":
                cname = input("Enter the name of the contact : ")
                cemail = input("Enter the email of the contact : ")
                add_contact(cname, cemail)
                continue

            case "2":
                list_contacts()
                continue
            
            case _:
                print("Program exit")
                return

if __name__ == "__main__":
    main()
