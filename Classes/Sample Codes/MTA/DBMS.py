# Title: DBMS
# Author: Ananya G M, K Nitesh Srivats
# Date: 01/06/2018

import pandas as pd
import os


class DBMS:
    def __init__(self):
        logs_path = os.getcwd()
        self.database_path = os.path.join(logs_path, 'Database Main.xlsx')
        self.form_path = os.path.join(logs_path, 'Form.csv')
        self.new_database_path = os.path.join(logs_path, 'MTA-BMS.xlsx')
        self.ieee_path = os.path.join(logs_path, 'members.xlsx')

    def mail_counter(self, Choice):
        form = pd.read_csv(self.form_path)
        data = pd.read_excel(self.database_path)

        for i in range(len(data)):
            if data['Payment ID'].iloc[i] not in form['Payment ID'].tolist() and data['Mail Count'].iloc[i] < 2:
                if data['Amount'].iloc[i] != 15000 and Choice == 1:
                    data['Mail Count'].iloc[i] += 1
                elif data['Amount'].iloc[i] == 15000 and Choice == 2:
                    data['Mail Count'].iloc[i] += 1

        data.to_excel(self.database_path, index=False)

    def update_from_db(self):
        data = pd.read_excel(self.database_path)
        new = pd.read_excel(self.new_database_path)

        new = new.rename(columns={'Customer Email': "Username",
                                  'Customer Phone': "Phone number",
                                  'Payment Id': "Payment ID"})

        for i in range(len(new)):
            if new['Payment ID'].iloc[i] not in data['Payment ID'].tolist():
                data = data.append(new.iloc[i])

        data.fillna(0, inplace=True)
        data.to_excel(self.database_path, index=False)

    def update_from_form(self):
        form = pd.read_csv(self.form_path)
        data = pd.read_excel(self.database_path)

        data.fillna(0, inplace=True)
        form.fillna(0, inplace=True)
        form.drop(['Are you an IEEE member?'], axis=1, inplace=True)

        for i in range(len(form)):
            for j in range(len(data)):
                if form['Payment ID'].iloc[i] == data['Payment ID'].iloc[j] \
                        and data['Name'].iloc[j] == 0:
                    data['Name'].iloc[j] = form['Name'].iloc[i]
                    data['Date of birth'].iloc[j] = form['Date of birth'].iloc[i]
                    data['IEEE Membership ID'].iloc[j] = form['IEEE Membership ID'].iloc[i]
                    data['College'].iloc[j] = form['College'].iloc[i]
                    data['Branch'].iloc[j] = form['Branch'].iloc[i]
                    data['Year of study'].iloc[j] = form['Year of study'].iloc[i]
                    data['Timestamp'].iloc[j] = form['Timestamp'].iloc[i]
                    data['Username'].iloc[j] = form['Username'].iloc[i]
                    data['Phone number'].iloc[j] = form['Phone number'].iloc[i]
                    break
                elif form['Payment ID'].iloc[i] == data['Payment ID'].iloc[j] \
                        and data['Amount'].iloc[j] == 15000 \
                        or form['Payment ID'].iloc[i] == 0:
                    data = data.append(form.iloc[i])
                    break

        data.to_excel(self.database_path, index=False)

    def display(self, choice):
        data = pd.read_excel(self.database_path)
        display = pd.DataFrame(columns=['Name', 'Email', 'Phone Number', 'ID'])

        for i in range(len(data)):
            if data['Amount'].iloc[i] != 15000 and choice == 1:
                display = display.append(
                    pd.DataFrame([[data['Name'].iloc[i],
                                   data['Username'].iloc[i],
                                   data['Phone number'].iloc[i],
                                   data['IEEE Membership ID'].iloc[i]]],
                                 columns=['Name', 'Email',
                                          'Phone Number', 'ID']))
            elif data['Amount'].iloc[i] == 15000 and choice == 2:
                display = display.append(
                    pd.DataFrame([[data['Name'].iloc[i],
                                   data['Username'].iloc[i],
                                   data['Phone number'].iloc[i],
                                   data['Payment ID'].iloc[i]]],
                                 columns=['Name', 'Email',
                                          'Phone Number', 'ID']))

        display = display.sort_values(['ID'], ascending=False)
        print(display)

    def check_membership(self):
        data = pd.read_excel(self.database_path)
        ieee = pd.read_excel(self.ieee_path)
        check = pd.DataFrame(columns=['Name', 'ID', 'Name Given'])
        id = "IEEE Membership ID"
        for i in range(len(data)):
            if data[id].iloc[i] != 0:
                flag = 0
                for j in range(len(ieee)):
                    if ieee[id].iloc[j] == data[id].iloc[i]:
                        name = ieee['First Name'].iloc[j] + ' ' + \
                               ieee['Last Name'].iloc[j]
                        check = check.append(
                            pd.DataFrame([[name,
                                           data['IEEE Membership ID'].iloc[i],
                                           data['Name'].iloc[i]]],
                                         columns=['Name', 'ID', 'Name Given']))
                        flag = 1
                        break
                if flag == 0:
                    check = check.append(
                        pd.DataFrame([[0,
                                       data['IEEE Membership ID'].iloc[i],
                                       data['Name'].iloc[i]]],
                                     columns=['Name', 'ID', 'Name Given']))

        write_path = os.path.join(os.getcwd(), 'Check Membership.xlsx')

        check.to_excel(write_path, index=False)
