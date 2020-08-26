<b> DESCRIPTION </b> <br>
 This is a basic project I did for a startup company that had an existing client list in a static Excel. 
 These scripts transformed the existing client list into an SQLite database, allow manual client entry to write into the SQLite
 as well as batch additions to this SQLite.
 It then sends personalised e-mails with possible attached reports to the client list in HTML and plain text format.
<br><br>
<b> mail_sender_main.py </b><br>
  Uses SQL database to send HTML and plain text e-mail.
    - lines 9-47: contain plain text and HTM e-mail to send.
    - lines 79, 81: sender server and e-mail.
    - line 91: e-mail subject and datetime.now() timestamp 
<br><br>
<b> manual_client_input.py </b><br>
  Manually adds clients via prompt (first name, last name, title, email, company).
    - line 5: specify working directory for SQLdb.
<br><br>
<b> csv_batch_client_inpit.py </b><br>
  Adds CSV from working directory of client data to SQLdb in column format (first_name, last_name, title, e_mail, company).
    - line 6: specify working directory for SQLdb and CSV.
<br><br>
<b> MTM_email.htm </b><br>
 Sample e-mail as per initial commit.
<br><br>
<b> client_csv.csv </b><br>
  Sample client list as per initial commit.
