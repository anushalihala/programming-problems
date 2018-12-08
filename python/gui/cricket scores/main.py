import sys
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
import fantasycricket
import newteam
import openteam
import evaluateteams

class Team():
    def __init__(self):
        self.conn = sqlite3.connect('fantasycricketdb.db')
        self.cur = self.conn.cursor()
        self.teamID = 0
        self.initialPoints = 1000
        self.maxCtg = {'BAT':4,'BOW':3, 'AR':3, 'WK':1}
        
        try:
            n = len( self.cur.execute("SELECT * FROM sqlite_master WHERE type='table'").fetchall() )
        except:
            print('Run Time Error')
        
        if(n==0):
            print('Creating database..')
            self.setupDatabase()                 
        elif(n!=6):
            print("Database is corrupted.")
            ans = input("Reset database? [y/n]: ")
            while(ans!='y' and ans!='n'):
                ans = input("Reset database? [y/n]: ") 
                
            if(ans=='y'):
                print('Resetting..')
                self.setupDatabase()
            else:
                exit()
        
        
    def setupDatabase(self):
        #dropping all tables
        self.cur.execute('DROP TABLE IF EXISTS Teams')
        self.cur.execute('DROP TABLE IF EXISTS Players')
        self.cur.execute('DROP TABLE IF EXISTS Matches')
        self.cur.execute('DROP TABLE IF EXISTS PlayerMatch')
        self.cur.execute('DROP TABLE IF EXISTS TeamPlayer')
        
        #creating tables
        self.cur.execute('''CREATE TABLE `Matches` (
                            `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,  
                            `match`	TEXT
                            )''')
        self.cur.execute('''CREATE TABLE `Players` (
                            `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                            `player`	TEXT,
                            `ctg`	VARCHAR ( 3 ),
                            `value`	INTEGER
                            )''')
        self.cur.execute('''CREATE TABLE `Teams` (
                            `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                            `team`	TEXT,
                            `points`	INTEGER
                            )''')
        self.cur.execute('''CREATE TABLE `PlayerMatch` (
                            `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                            `match_id`	INTEGER,
                            `player_id`	INTEGER,
                            `scored`	INTEGER,
                            `faced`	INTEGER,
                            `fours`	INTEGER,
                            `sixes`	INTEGER,
                            `bowled`	INTEGER,
                            `maiden`	INTEGER,
                            `given`	INTEGER,
                            `wkts`	INTEGER,
                            `catches`	INTEGER,
                            `stumping`	INTEGER,
                            `ro`	INTEGER,
                            `points`	INTEGER DEFAULT -1,
                            UNIQUE(`match_id`,`player_id`),
                            FOREIGN KEY(`player_id`) REFERENCES `Players`(`id`),
                            FOREIGN KEY(`match_id`) REFERENCES `Matches`(`id`)
                            )''')
        self.cur.execute('''CREATE TABLE `TeamPlayer` (
                            `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                            `team_id`	INTEGER,
                            `player_id`	INTEGER,
                            FOREIGN KEY(`player_id`) REFERENCES `Players`(`id`),
                            FOREIGN KEY(`team_id`) REFERENCES `Teams`(`id`),
                            UNIQUE(`team_id`,`player_id`)
                            )''')
                            
        matches = [('Match1',)]
        
        players = [('Kohli', 'BAT', 120), 
                    ('Yuvraj', 'BAT', 100), 
                    ('Rahane', 'BAT', 100), 
                    ('Dhawan', 'AR', 85), 
                    ('Dhoni', 'BAT', 75), 
                    ('Axar', 'BOW', 100), 
                    ('Pandya', 'BOW', 75), 
                    ('Jadeja', 'BOW', 85), 
                    ('Kedar', 'BOW', 90), 
                    ('Ashwin', 'AR', 100), 
                    ('Umesh', 'WK', 110), 
                    ('Bumrah', 'WK', 60), 
                    ('Bhuwaneshwar', 'AR', 75), 
                    ('Rohit', 'BAT', 85), 
                    ('Kartick', 'AR', 75)]
        
        playermatches =[(1, 1, 102, 98, 8, 2, 0, 0, 0, 0, 0, 0, 1, 88), 
                        (1, 2, 12, 20, 1, 0, 48, 0, 36, 1, 0, 0, 0, 21), 
                        (1, 3, 49, 75, 3, 0, 0, 0, 0, 0, 1, 0, 0, 37), 
                        (1, 4, 32, 35, 4, 0, 0, 0, 0, 0, 0, 0, 0, 20), 
                        (1, 5, 56, 45, 3, 1, 0, 0, 0, 0, 3, 2, 0, 88), 
                        (1, 6, 8, 4, 2, 0, 48, 2, 35, 1, 0, 0, 0, 20), 
                        (1, 7, 42, 36, 3, 3, 30, 0, 25, 0, 1, 0, 0, 40), 
                        (1, 8, 18, 10, 1, 1, 60, 3, 50, 2, 1, 0, 1, 52), 
                        (1, 9, 65, 60, 7, 0, 24, 0, 24, 0, 0, 0, 0, 44), 
                        (1, 10, 23, 42, 3, 0, 60, 2, 45, 6, 0, 0, 0, 88), 
                        (1, 11, 0, 0, 0, 0, 54, 0, 50, 4, 1, 0, 0, 60), 
                        (1, 12, 0, 0, 0, 0, 60, 2, 49, 1, 0, 0, 0, 10), 
                        (1, 13, 15, 12, 2, 0, 60, 1, 46, 2, 0, 0, 0, 29), 
                        (1, 14, 46, 65, 5, 1, 0, 0, 0, 0, 1, 0, 0, 40), 
                        (1, 15, 29, 42, 3, 0, 0, 0, 0, 0, 2, 0, 1, 47)] 
                        
        for row in matches:
            self.cur.execute('INSERT INTO Matches(match) VALUES(?)',row)
            
        for row in players:
            self.cur.execute('INSERT INTO Players(player, ctg, value) VALUES(?, ?, ?)',row)   
            
        for row in playermatches:
            self.cur.execute('INSERT INTO PlayerMatch(match_id, player_id, scored, faced, fours, sixes, bowled, maiden, given, wkts, catches, stumping, ro) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',row[:-1])
            
        self.conn.commit()
    
    def getID(self):
        return self.teamID
        
    def changeTeam(self, id):
        self.teamID = id
        
    def getInitialPoints(self):
        return self.initialPoints
        
    def setInitialPoints(self, points):
        self.initialPoints = points
        
    def getMaxCtg(self):
        return self.maxCtg
        
    def setMaxCtg(self, maxCtgs):
        self.maxCtg = maxCtgs
    
    def getTeamName(self):
        self.cur.execute('SELECT team FROM Teams WHERE id=?',(self.teamID,))
        return self.cur.fetchone()[0]
        
    def getTeamPoints(self):
        self.cur.execute('SELECT points FROM Teams WHERE id=?',(self.teamID,))
        return self.cur.fetchone()[0]
        
    def createTeam(self, teamName):
        self.cur.execute('INSERT INTO Teams(team,points) VALUES(?,?)', (teamName, self.initialPoints))
        self.teamID = self.cur.lastrowid
        self.conn.commit()
    
    def getTeamPlayers(self):
        sql = '''SELECT Players.*
                 FROM TeamPlayer JOIN Players on TeamPlayer.player_id = Players.id
                 WHERE TeamPlayer.team_id = ?'''
        self.cur.execute(sql,(self.teamID,))
        rows = self.cur.fetchall()
        return rows
                      
    def getOtherPlayers(self, ctg):
        sql = '''SELECT * 
                FROM Players 
                WHERE ctg = ?
                EXCEPT 
                SELECT Players.* 
                FROM Players 
                JOIN TeamPlayer 
                ON TeamPlayer.player_id = Players.id
                WHERE TeamPlayer.team_id = ?'''
        self.cur.execute(sql,(ctg, self.teamID))
        rows = self.cur.fetchall()
        return rows
        
    def getTeamCtgs(self):
        sql = '''SELECT Players.ctg,COUNT(Players.id) 
                FROM TeamPlayer JOIN Players on TeamPlayer.player_id = Players.id
                WHERE TeamPlayer.team_id = ?
                GROUP BY Players.ctg'''

        self.cur.execute(sql,(self.teamID,))
        rows = self.cur.fetchall()
        
        d = dict()
        for row in rows:
            d[row[0]]=row[1]
            
        return d
            
    def addTeamMember(self,playerID):
        sql = '''INSERT INTO TeamPlayer(team_id, player_id) VALUES(?, ?)'''
        self.cur.execute(sql,(self.teamID, playerID))
        
        self.cur.execute('SELECT value FROM Players WHERE id = ?',(playerID,))
        playerValue = self.cur.fetchone()[0]

        self.cur.execute('SELECT points FROM Teams WHERE id = ?',(self.teamID,))
        prevTeamPoints = self.cur.fetchone()[0]
        
        newTeamValue = prevTeamPoints - playerValue
        self.cur.execute('UPDATE Teams SET points = ? WHERE id = ?',(newTeamValue,self.teamID))
        
        self.conn.commit()
    
    def removeTeamMember(self,playerID):
        sql = '''DELETE FROM TeamPlayer WHERE team_id = ? and player_id = ?'''
        self.cur.execute(sql,(self.teamID, playerID))
        
        self.cur.execute('SELECT value FROM Players WHERE id = ?',(playerID,))
        playerValue = self.cur.fetchone()[0]

        self.cur.execute('SELECT points FROM Teams WHERE id = ?',(self.teamID,))
        prevTeamPoints = self.cur.fetchone()[0]
        
        newTeamValue = prevTeamPoints + playerValue
        self.cur.execute('UPDATE Teams SET points = ? WHERE id = ?',(newTeamValue,self.teamID))
        
        self.conn.commit()
        
    def getAllTeams(self):
        self.cur.execute('SELECT id,team FROM Teams')
        return self.cur.fetchall()
    
    def getAllMatches(self):
        self.cur.execute('SELECT id,match FROM Matches')
        return self.cur.fetchall()
    
    def evaluate(self, selectedTeamID, matchID):
        self.calcPoints(matchID)
        
        sql = '''SELECT Players.player, PlayerMatch.points
                 FROM (TeamPlayer JOIN Players on TeamPlayer.player_id = Players.id) JOIN PlayerMatch ON PlayerMatch.player_id = TeamPlayer.player_id
                 WHERE TeamPlayer.team_id = ? and PlayerMatch.match_id = ?'''
        self.cur.execute(sql,(selectedTeamID, matchID))
        return self.cur.fetchall()

    def calcPoints(self, matchID):
        sql = '''SELECT PlayerMatch.*
                 FROM TeamPlayer JOIN PlayerMatch ON PlayerMatch.player_id = TeamPlayer.player_id
                 WHERE TeamPlayer.team_id = ? and PlayerMatch.match_id = ?'''
        rows = self.cur.execute(sql,(self.teamID, matchID))

        update = []
        for row in rows:
            if row[-1] < 0:
                p = self.calcPoint(row[3:-1])
                update.append([row[0],p])
        
        for row in update:
            self.cur.execute('UPDATE PlayerMatch SET points = ? WHERE id = ?', (row[1],row[0]))
        self.conn.commit()
            
    def calcPoint(self, playerMatchTuple):
        points = 0
        points += playerMatchTuple[0]//2
        points += 5 if playerMatchTuple[0]>=50 else 0
        points += 10 if playerMatchTuple[0]>=100 else 0
        
        if playerMatchTuple[1]>0:
            points += 2 if playerMatchTuple[0]/playerMatchTuple[1]>=80 and playerMatchTuple[0]/playerMatchTuple[1]<=100 else 0
            points += 4 if playerMatchTuple[0]/playerMatchTuple[1]>=100 else 0
       
        points +=  playerMatchTuple[2]
        points +=  2*playerMatchTuple[3]
        points +=  10*playerMatchTuple[7]
        points +=  5 if playerMatchTuple[7]>=3 else 0
        points +=  5 if playerMatchTuple[7]>=3 else 0
        
        if playerMatchTuple[4]>0:
            economy_rate = playerMatchTuple[6]/(playerMatchTuple[4]/6)
            if economy_rate>=3.5 and economy_rate<=4.5:
                points += 4
            elif economy_rate>=2 and economy_rate<=3.5:
                points += 7
            elif economy_rate<2:
                points += 10
                
        points +=  10*(playerMatchTuple[-1]+playerMatchTuple[-2]+playerMatchTuple[-3]) 
        
        return points
        
    def __del__(self):
        self.cur.close()

class Window(QtWidgets.QMainWindow):
        
    def __init__(self):
        super(Window,self).__init__()

        self.ui = fantasycricket.Ui_MainWindow()
        self.ui.setupUi(self)   
        self.ui.actionNEW_Team.triggered.connect(self.openNewTeam)
        self.ui.actionOPEN_Team.triggered.connect(self.openTeam)
        self.ui.actionEVALUATE_Team.triggered.connect(self.evaluateTeams)
        
        self.ui.radBat.toggled.connect(lambda:self.setOtherPlayers( 'BAT' ))
        self.ui.radBow.toggled.connect(lambda:self.setOtherPlayers( 'BOW' ))
        self.ui.radAr.toggled.connect(lambda:self.setOtherPlayers( 'AR' ))
        self.ui.radWk.toggled.connect(lambda:self.setOtherPlayers( 'WK' ))
        
        self.ui.lstTeamPlayers.doubleClicked.connect( lambda:self.removeTeamMember( self.ui.lstTeamPlayers.currentIndex().row() ) )
        self.ui.lstOtherPlayers.doubleClicked.connect( lambda:self.addTeamMember( self.ui.lstOtherPlayers.currentIndex().row() ) )
        
        self.t = Team()
        self.teamPlayersModel = QtCore.QStringListModel()
        self.teamPlayers = []
        self.otherPlayersModel = QtCore.QStringListModel()
        self.otherPlayers = []
        self.otherPlayersCtg = 'BAT'
        self.ctgToBtn = {'BAT':self.ui.radBat, 'BOW':self.ui.radBow, 'AR':self.ui.radAr, 'WK':self.ui.radWk}
        self.show()
        
    def teamCreated(self, tName):
        self.t.createTeam(tName)
        self.setTeam()
        
    def teamChanged(self, tID):
        self.t.changeTeam(tID)
        self.setTeam()

    def setTeam(self):
        if self.ui.centralwidget.isEnabled() == False:
            self.ui.centralwidget.setEnabled(True)   
        self.ui.lblTeamName.setText(self.t.getTeamName())
        self.ui.lblPoints.setText(str(self.t.getTeamPoints()))
        self.ui.lblPointsUsed.setText(str(self.t.getInitialPoints() - self.t.getTeamPoints()))
        self.setCtgs()
        self.setTeamPlayers()
        self.ctgToBtn[self.otherPlayersCtg].toggle()
        self.setOtherPlayers( self.otherPlayersCtg )
        
    def setCtgs(self):
        d = self.t.getTeamCtgs()
        self.ui.lblBatCount.setText( str(d.get('BAT',0)) )
        self.ui.lblBowCount.setText( str(d.get('BOW',0)) )
        self.ui.lblArCount.setText( str(d.get('AR',0)) )
        self.ui.lblWkCount.setText( str(d.get('WK',0)) )
        
    def setTeamPlayers(self):
        self.teamPlayers = self.t.getTeamPlayers()
        self.teamPlayersModel.setStringList([row[1] for row in self.teamPlayers])
        self.ui.lstTeamPlayers.setModel(self.teamPlayersModel)
        
    def setOtherPlayers(self, ctg):
        self.otherPlayersCtg = ctg
        self.otherPlayers = self.t.getOtherPlayers( ctg )
        self.otherPlayersModel.setStringList([row[1] for row in self.otherPlayers])
        self.ui.lstOtherPlayers.setModel(self.otherPlayersModel)

    def addTeamMember(self, idx):
        tCtg = self.otherPlayers[idx][2]
        current = self.t.getTeamCtgs().get(tCtg,0)
        max = self.t.getMaxCtg()[tCtg]
        
        if current < max:
            tVal = self.otherPlayers[idx][3]
            capacity = self.t.getTeamPoints()
            if capacity >= tVal:
                tID = self.otherPlayers[idx][0]
                self.t.addTeamMember(tID)
                self.setTeam()
            else:
                msgbox = QtWidgets.QMessageBox(text="You do not have enough points to add this player")
                msgbox.setWindowTitle("Error")
                msgbox.exec()
        else:
            msgbox = QtWidgets.QMessageBox(text="Can not have more than " + str(max) + " " + tCtg + "s")
            msgbox.setWindowTitle("Error")
            msgbox.exec()
                
    def removeTeamMember(self, idx):
        tID = self.teamPlayers[idx][0]
        self.t.removeTeamMember(tID)
        self.setTeam()
        
    def openNewTeam(self):
        d = QtWidgets.QDialog()
        dui = newteam.Ui_NewDialog()
        dui.setupUi(d)
        
        def myslot():
            newteam = dui.tbNewTeam.toPlainText()
            if len(newteam)>0:
                self.teamCreated(newteam)
            else:
                msgbox = QtWidgets.QMessageBox(text="Invalid Name")
                msgbox.setWindowTitle("Error")
                msgbox.exec()
             
        dui.buttonBox.accepted.connect(myslot)
        d.exec_()
        
    def openTeam(self):
        d = QtWidgets.QDialog()
        dui = openteam.Ui_OpenDialog()
        dui.setupUi(d)
        
        data = self.t.getAllTeams()
        
        model = QtCore.QStringListModel([row[1] for row in data])        
        dui.cmbOpenTeam.setModel(model)
        
        def myslot():
            try:
                selectedID = data[dui.cmbOpenTeam.currentIndex()][0]
                if selectedID != self.t.getID():
                    self.teamChanged(selectedID)
            except:
                pass
        
        dui.buttonBox.accepted.connect(myslot)
        d.exec_()
        
    def evaluateTeams(self):
        d = QtWidgets.QDialog()
        dui = evaluateteams.Ui_EvaluateTeams()
        dui.setupUi(d)
        
        teamData = self.t.getAllTeams()
        teamModel = QtCore.QStringListModel([row[1] for row in teamData])           
        dui.cmbTeam.setModel(teamModel)
        
        matchData = self.t.getAllMatches()
        matchModel = QtCore.QStringListModel([row[1] for row in matchData])           
        dui.cmbMatch.setModel(matchModel)
        
        def myslot(idxT, idxM):
            tID = teamData[idxT][0]
            mID = matchData[idxM][0]
            data = self.t.evaluate(tID, mID)
            
            dui.lstPlayers.clear()
            dui.lstPlayers.addItems([row[0] for row in data])
            
            pointList = [row[1] for row in data]
            dui.lstPoints.clear()
            dui.lstPoints.addItems( [str(p) for p in pointList] )
            
            tot = sum(pointList)
            dui.lblTotPoints.setText( str(tot) )
            
        dui.btnCalc.clicked.connect( lambda: myslot(dui.cmbTeam.currentIndex(), dui.cmbMatch.currentIndex()) )
        
        d.exec_()     
        
    def __del__(self):
        try:
            del self.t
        except:
            pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


