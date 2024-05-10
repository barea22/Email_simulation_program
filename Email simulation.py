#Email simulator

class Email:
    """Class for representing an email"""

    def __init__(self, email_address, subject_line, email_content):
        """Constructor method for the Email class"""
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False


    def mark_as_read(self):
        """
        Method to Mark an email as read
        """
        self.has_been_read = True


    # Class variable used to store and access the emails
    inbox = []


def populate_inbox():
    """
    Populates the inbox with emails
    """
    emails = [Email("Swansea_florist",  "Delivery notice", "Your flowers will be delivered by the Post man on sunday 6pm!"),
             Email("Skynet",  "Maintenance Update!",  "This is to inform you about the scheduled maintenance on Tuesday 12am- 4am"),
             Email("donot_reply", "EE Mobile", "Your one-time password is  FWSR44223EED. Paasword expires in 15minutes.")]
    Email.inbox.extend(emails)



def list_emails():
    """
    Displays all the email subject lines with their corresponding email number
    """
    print("\nInbox:")
    for index, email in enumerate(Email.inbox):
        print(f"{index}. {email.subject_line}")


def read_email(index):
    """
    Displays the details of the selected email

    """
    # Checking if the selected email number corresponds to an email in the inbox
    if 0 <= index < len(Email.inbox):
        email = Email.inbox[index]
        print(f"\nFrom: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")

        # Mark the email as read if it hasn't already been read
        if not email.has_been_read:
            email.mark_as_read()
            print(f"\nEmail from {email.email_address} marked as read.\n")

    else:
        print("Invalid email number.")


def view_unread_emails():
    """
    Displays all the unread email subject lines with their corresponding email number
    """
    print("\nUnread Emails:")
    for index, email in enumerate(Email.inbox):
        if not email.has_been_read:
            print(f"{index}. {email.subject_line}")


populate_inbox()

# Main simulator Program
while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

Enter selection: '''))

    if user_choice == 1:
        list_emails()
        index = int(input("Enter the number of the email you want to read: "))
        read_email(index)
    elif user_choice == 2:
        view_unread_emails()
    elif user_choice == 3:
        print("Quitting application. \n poweredby@David_EnenduCoding")
        break
    else:
        print("Invalid choice. Please select again.")
