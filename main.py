import sqlite3
conn = sqlite3.connect('store')
cursor = conn.cursor()
# print ("Database has been created")

# conn.execute("DROP TABLE IF EXISTS pet")

# conn.execute("CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), checkups SMALLINT UNSIGNED, birth DATE, death DATE)")
# conn.execute("INSERT INTO pet (name,owner,species,sex,checkups,birth,death)VALUES \
#   ('Fluffy','Harold','cat','f',5,'2001-02-04','')")

# conn.execute("INSERT INTO pet (name,owner,species,sex,checkups,birth,death)VALUES \
#   ('Claws','Gwen','cat','m',2,'2000-03-17','')")

# conn.commit()

# cursor = conn.execute("SELECT name,owner,species,sex,checkups,birth,death from pet")

# for row in cursor:
#    print("name = ", row[0])
#    print("owner = ", row[1])
#    print("species = ", row[2])
#    print("sex = ", row[3])
#    print("checkups = ", row[4])
#    print("birth = ", row[5])
#    print("death = ", row[6], "\n")

# Ask the user for the name, owner, and new death date
name = input("Enter the animal's name: ")
owner = input("Enter the owner's name: ")
death_date = input("Enter the death date (YYYY-MM-DD): ")

# Update the death date for the specified pet
cursor.execute("""
    UPDATE pet
    SET death = ?
    WHERE name = ? AND owner = ?
""", (death_date, name, owner))

# Commit the update and confirm
conn.commit()
print("Death date updated successfully.")

# Optional: display the updated record
cursor.execute("""
    SELECT name, owner, species, sex, checkups, birth, death
    FROM pet
    WHERE name = ? AND owner = ?
""", (name, owner))

row = cursor.fetchone()
if row:
    print("\nUpdated Record:")
    print("Name:", row[0])
    print("Owner:", row[1])
    print("Species:", row[2])
    print("Sex:", row[3])
    print("Checkups:", row[4])
    print("Birth:", row[5])
    print("Death:", row[6])
else:
    print("No matching pet found.")

conn.close()



print ("Table created successfully")

