# Title: DBMS
# Author: Ananya G M, K Nitesh Srivats
# Date: 01/06/2018

import Mail
import DBMS


def main():
    db = DBMS.DBMS()
    mail = Mail.Mail()
    
    while True:
        print("\n\n\n\n\n")
        multi = -1
        while multi < 0 or multi > 5:
            multi = eval(input(
                "0. Exit.\n"
                "1. Update from Database.\n"
                "2. Update from Form.\n"
                "3. Check Memberships.\n"
                "4. Display.\n"
                "5. Send Mails"))
        if multi == 1:
            db.update_from_db()
        elif multi == 2:
            db.update_from_form()
        elif multi == 3:
            db.membership()
        elif multi == 4:
            choice = -1
            while choice != 2 and choice != 1:
                choice = eval(input("\n1. Individual.\n2. Group."))
                db.membership(choice)
        elif multi == 5:
            mail.send_mail()
        else:
            return


if __name__ == '__main__':
    main()
