#----------------------------------------------------------------------
# gameGuru.py
# Victor Stasek
# CS230 - MWF 9:00AM
# 12/6/13
#----------------------------------------------------------------------

import sys
import sqlite3
# prettytable is not my work. Copyright info located in 'prettytable.py'.
from prettytable import from_db_cursor

#----------------------------------------------------------------------

def findList(answer, curs):

    """One of the two primary functions in gameGuru. Finds a list of games that match
    criteria supplied by the user. 'answer' is a string containing either 1-5. This
    determines what type of criteria will be used. 'curs' is a database cursor object."""

    if answer == '1':
        print("i.e. Entering '10' will list only games appropriate for ages 10 and under")
        print("Appropriateness is based on the ESRB rating system.")
        cap = input('Enter age cap: ')
        print()

        curs.execute("SELECT * FROM Games NATURAL JOIN isFor WHERE ageCap < ?", (cap,))
        pt = from_db_cursor(curs)
        print(pt)

#------------
        
    elif answer == '2':
        year = input("Enter year: ")
        print("Enter whether you want all games made 'Before' or 'After' this year.")
        print("i.e. Entering 'Before' will list only games made before the year you entered.")
        beforeOrAfter = checkUserInput(["Before","After"])

        if beforeOrAfter == 'Before':
            curs.execute("SELECT * FROM Games NATURAL JOIN isFor WHERE year < ?", (year,))
            pt = from_db_cursor(curs)
            print(pt)
        else:
            curs.execute("SELECT * FROM Games NATURAL JOIN isFor WHERE year > ?", (year,))
            pt = from_db_cursor(curs)
            print(pt)

#------------

    elif answer == '3':
        developer = input('Enter developer name: ')
        developer = developer.title()
        curs.execute("SELECT * FROM Games NATURAL JOIN isFor WHERE developer = ?", (developer,))
        pt = from_db_cursor(curs)
        print(pt)

#------------

    elif answer == '4':
        console = input('Enter console name: ')
        console = console.title()
        curs.execute("SELECT * FROM Games NATURAL JOIN isFor WHERE isFor = ?", (console,))
        pt = from_db_cursor(curs)
        print(pt)

#------------

    elif answer == '5':
        print("Enter the game's genre")
        print("Genre choices include: 'Action-Adventure', 'Fighting', 'Platformer', 'Racing', 'Role-Playing', 'Shooter', and 'Sports'")
        genre = checkUserInput(["Action-Adventure","Fighting","Platformer","Racing","Role-Playing","Shooter","Sports"])
        genreSpecificList(genre, curs)

#----------------------------------------------------------------------

def genreSpecificList(genre, curs):

    """Used to find game list based on criteria related to genre. Part of the findList() function.
    'genre' is a string containing the genre the user wants to find games for. 'curs' is a database
    cursor object."""

    if genre == 'Action-Adventure':
        print("If you want all Action-Adventure games, type 'all'")
        print("If you want only the games in an Action-Adventure subgenre, type the subgenre.")
        print("Subgenre choices include: 'Standard', 'Stealth', and 'Survival Horror'")
        subGenre = checkUserInput(["All","Standard","Stealth","Survival Horror"])
        
        if subGenre == 'All':
            curs.execute("SELECT * FROM Games NATURAL JOIN isFor NATURAL JOIN Action_Adventure WHERE genre = 'Action-Adventure'")
            pt = from_db_cursor(curs)
            print(pt)
        else:
            curs.execute("SELECT * FROM Games NATURAL JOIN isFor NATURAL JOIN Action_Adventure WHERE genre = ? AND type = ?", (genre, subGenre))
            pt = from_db_cursor(curs)
            print(pt)

#------------
        
    elif genre == 'Fighting':
        curs.execute("SELECT * FROM Games NATURAL JOIN isFor WHERE genre = 'Fighting'")
        pt = from_db_cursor(curs)
        print(pt)

#------------

    elif genre == 'Platformer':
        print("If you want ALL Platformer games, type 'all'")
        print("If you want only the games in a Platformer subgenre, type the subgenre.")
        print("Subgenre choices include: '2D' and '3D'")
        subGenre = checkUserInput(["All","2D","3D"])

        if subGenre == 'All':
            curs.execute("SELECT * FROM Games NATURAL JOIN isFor NATURAL JOIN Platformer WHERE genre = 'Platformer'")
            pt = from_db_cursor(curs)
            print(pt)

        else:
            curs.execute("SELECT * FROM Games NATURAL JOIN isFor NATURAL JOIN Platformer WHERE genre = 'Platformer' and type = ?", (subGenre,))
            pt = from_db_cursor(curs)
            print(pt)

#------------

    elif genre == 'Racing':
        curs.execute("SELECT * FROM Games NATURAL JOIN isFor WHERE genre = 'Racing'")
        pt = from_db_cursor(curs)
        print(pt)

#------------

    elif genre == 'Role-Playing':
        print("If you want ALL RPGs, type 'all'")
        print("If you want only the games in an RPG subgenre, type the subgenre.")
        print("Subgenre choices include: 'Action', 'Sandbox', and 'Standard'")
        subGenre = checkUserInput(["All","Action","Sandbox","Standard"])
        
        if subGenre == 'All':
            curs.execute("SELECT * FROM Games NATURAL JOIN isFor NATURAL JOIN RPG WHERE genre = 'RPG'")
            pt = from_db_cursor(curs)
            print(pt)

        else:
            curs.execute("SELECT * FROM Games NATURAL JOIN isFor NATURAL JOIN RPG WHERE genre = 'RPG' and type = ?", (subGenre,))
            pt = from_db_cursor(curs)
            print(pt)

#------------

    elif genre == 'Shooter':
        print("If you want ALL Shooter games, type 'all'")
        print("If you want only the games in a Shooter subgenre, type the subgenre.")
        print("Subgenre choices include: 'Aerial', 'First-Person', 'Light Gun', 'Side-Scroller', and 'Third-Person'")
        subGenre = checkUserInput(["All","Aerial","First-Person","Light Gun","Side-Scroller","Third-Person"])
        
        if subGenre == 'All':
            curs.execute("SELECT * FROM Games NATURAL JOIN isFor NATURAL JOIN Shooter WHERE genre = 'Shooter'")
            pt = from_db_cursor(curs)
            print(pt)

        else:
            curs.execute("SELECT * FROM Games NATURAL JOIN isFor NATURAL JOIN Shooter WHERE genre = 'Shooter' and type = ?", (subGenre,))
            pt = from_db_cursor(curs)
            print(pt)
            
#------------

    elif genre == 'Sports':
        print("If you want ALL Sport games, type 'all'")
        print("If you want only the games in a Sports subgenre, type the subgenre.")
        print("Subgenre choices include: 'Baseball', 'Basketball', 'Collection', 'Fishing', 'Football', 'Hunting', 'Soccer', and 'Skateboarding'")
        subGenre = checkUserInput(["All","Baseball","Basketball","Collection","Fishing","Football","Hunting","Soccer","Skateboarding"])

        if subGenre == 'All':
            curs.execute("SELECT * FROM Games NATURAL JOIN isFor NATURAL JOIN Sports WHERE genre = 'Sports'")
            pt = from_db_cursor(curs)
            print(pt)

        else:
            curs.execute("SELECT * FROM Games NATURAL JOIN isFor NATURAL JOIN Sports WHERE genre = 'Sports' and type = ?", (subGenre,))
            pt = from_db_cursor(curs)
            print(pt)

#----------------------------------------------------------------------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

def addGame(curs, conn):

    """One of the two primary functions in gameGuru. Allows user to add games to
    the database file."""

    
    title = input("Enter name of game: ")
    year = input("Enter year game was released: ")
    genre = inputGenreData(title, year, curs, conn)
    developer = input("Enter developer: ")
    maxPlayers = input("Enter max number of players: ")
    ageCap = determineAgeCap()
    inputIsForData(title, year, curs, conn)

    # inserts data into the Games table
    curs.execute("INSERT INTO Games VALUES(?, ?, ?, ?, ?, ?);", (title, year, genre, developer, maxPlayers, ageCap))
    conn.commit()

    # converts 'query' into correct database table name when they differ
    if genre == 'Action-Adventure':
        queryGenre = 'Action_Adventure'
    elif genre == 'Role-Playing':
        queryGenre = 'RPG'
    else: queryGenre = genre

    print(queryGenre, title)

    # show user the game that they added
    curs.execute("SELECT * FROM Games NATURAL JOIN isFor NATURAL JOIN " + queryGenre + " WHERE title = ? AND year = ?", (title, year))
    pt = from_db_cursor(curs)
    print(pt)

#----------------------------------------------------------------------

def inputGenreData(title, year, curs, conn):

    """Used with addGame(). Used to input data into the correct genre subclass table in the db file.
    Also returns 'genre' for the purpose of inputing data into Games table."""

    print()
    print("Enter the game's genre")
    print("Genre choices include: 'Action-Adventure', 'Fighting', 'Platformer', 'Racing', 'Role-Playing', 'Shooter', and 'Sports'")    
    genre = checkUserInput(["Action-Adventure","Fighting","Platformer","Racing","Role-Playing","Shooter","Sports"])

#------------

    if genre in ["Fighting","Racing"]:
        curs.execute("INSERT INTO Fighting VALUES (?, ?);", (title, year))
        conn.commit()
        return genre

#------------
    
    elif genre == "Action-Adventure":
        print("Enter game's sub-genre")
        print("Subgenre choices include: 'Standard', 'Stealth', and 'Survival Horror'")
        subGenre = checkUserInput(["Standard","Stealth","Survival Horror"])

        print("Enter game's perspective")
        print("Choices include: 'First' or 'Third'")
        perspective = checkUserInput(["First","Third"])

        curs.execute("INSERT INTO Action_Adventure VALUES(?, ?, ?, ?);", (title, year, subGenre, perspective))
        conn.commit()
        return genre

#------------

    elif genre == "Platformer":
        print("Enter game's sub-genre")
        print("Subgenre choices include: '2D' and '3D'")
        subGenre = checkUserInput(["2D","3D"])

        print("Enter game's perspective")
        print("Choices include: 'First' or 'Third'")
        perspective = checkUserInput(["First","Third"])

        curs.execute("INSERT INTO Platformer VALUES(?, ?, ?, ?);", (title, year, subGenre, perspective))
        conn.commit()
        return genre

#------------

    elif genre == "Role-Playing":
        print("Enter game's sub-genre")
        print("Subgenre choices include: 'Action', 'Sandbox', and 'Standard'")
        subGenre = checkUserInput(["Action","Sandbox","Standard"])

        curs.execute("INSERT INTO Platformer VALUES(?, ?, ?);", (title, year, subGenre))
        conn.commit()
        return genre

#------------

    elif genre == "Shooter":
        print("Enter game's sub-genre")
        print("Subgenre choices include: 'Aerial', 'First-Person', 'Light Gun', 'Side-Scroller', and 'Third-Person'")
        subGenre = checkUserInput(["Aerial","First-Person","Light Gun","Side-Scroller","Third-Person"])

        curs.execute("INSERT INTO Platformer VALUES(?, ?, ?);", (title, year, subGenre))
        conn.commit()
        return genre

#------------

    elif genre == "Sports":
        print("Enter game's sub-genre")
        print("Subgenre choices include: 'Baseball', 'Basketball', 'Collection', 'Fishing', 'Football', 'Hunting', 'Soccer', and 'Skateboarding'")
        subGenre = checkUserInput(["Baseball","Basketball","Collection","Fishing","Football","Hunting","Soccer","Skateboarding"])

        curs.execute("INSERT INTO Platformer VALUES(?, ?, ?);", (title, year, subGenre))
        conn.commit()
        return genre

#----------------------------------------------------------------------

def determineAgeCap():

    """Used when user is adding a game to the database
    Asks user to enter an ESRB rating and converts it to its corrresponding
    age rating."""

    print()
    print("Enter ESRB Rating")
    print("Choices include: 'KA', 'EC', 'E', 'E10', 'T', 'M', 'AO', 'RP'")
    ageCap = input(">>> ")
    ageCap = ageCap.upper()
    print()

    while ageCap not in ["KA","EC","E","E10","T","M","AO","RP"]:
        print("You did not enter a valid ESRB rating.")
        print("Make sure you chose one of the aforementioned ESRB ratings.")
        ageCap = input(">>> ")
        ageCap = ageCap.upper()
        print()

    # convert ESRB Rating into corresponding age cap
    if ageCap in ["KA","EC","E"]:
        return 0
    elif ageCap == "E10":
        return 10
    elif ageCap == "T":
        return 13
    elif ageCap == "M":
        return 17
    elif ageCap == "AO":
        return 18
    elif ageCap == "RP":
        return 'NULL'

#----------------------------------------------------------------------

def inputIsForData(title, year, curs, conn):

    """Used when user is adding a game to the database.
    Takes care of adding data to the 'isFor' table in the database"""

    console = input("Enter console: ")
    curs.execute("INSERT INTO isFor VALUES(?, ?, ?);", (title, year, console))
    conn.commit()
    
    consoleDecision = input("Is the game on another console? (Y/N) ")
    while consoleDecision[0] in ["Y","y"]:
        console = input("Enter console: ")
        curs.execute("INSERT INTO isFor VALUES(?, ?, ?);", (title, year, console))
        conn.commit()
        consoleDecision = input("Is the game on another console? (Y/N) ")

#----------------------------------------------------------------------


def checkUserInput(seq):

    """Used to make sure that user input x is in a set of choices contained in 'seq.'
    (e.g. Make sure user inputs one of the limited number of game genres modeled.)
    If user input is not in 'seq', asks user to re-enter input until a valid choice is made.
    returns user input 'x'."""

    x = input(">>> ")
    x = x.title()
    print()
    
    # while loop makes sure x is one of the items in seq
    while x not in seq:
        print("Your choice was not valid.")
        print("Make sure you chose one of aforementioned choices and that it is in the correct format")
        x = input(">>> ")
        x = x.title()
        print()

    return x

#----------------------------------------------------------------------

def main(argv):

    conn = sqlite3.connect('gameGuru.db')
    curs = conn.cursor()

    print("Welcome to Game Guru!")

    repeat = 'Y'
    while repeat[0] in ['Y','y']:
        print("Enter '1' if you would like to obtain a list of games.")
        print("Enter '2' if you would like to add a game to the database.")
        x = input(">>> ")
        print()

        # user wants to obtain a list of games
        if x == '1':
            listRepeat = 'Y'
            while listRepeat[0] in ['Y','y']:
                print("Enter '1' to search for age appropriate games.")
                print("Enter '2' to search for games before or after a certain year.")
                print("Enter '3' to search for games made by a specific developer.")
                print("Enter '4' to search for games on a specific console.")
                print("Enter '5' to search for games of a particular genre.")
                answer = input('>>> ')
                print()
                findList(answer, curs)

                listRepeat = input("Would you like to obtain another list? (Y/N) ")
                print()

        # user wants to add a game
        elif x == '2':
            addRepeat = 'Y'
            while addRepeat[0] in ['Y','y']:
                addGame(curs, conn)
                addRepeat = input("Would you like to add another game? (Y/N) ")
                print()

        repeat = input("Would you like to do anything else? (Y/N) ")
        print()

    print("Thank you for using Game Guru!")
    conn.close()

#----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
