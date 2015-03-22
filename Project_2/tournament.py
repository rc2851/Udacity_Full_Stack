#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import math

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""

    #connect to the database
    db = connect()
    cursor = db.cursor()

    #Delete game results from table game_results
    sql = "DELETE FROM game_results"
    cursor.execute(sql)
    db.commit()

    #Delete game matches from table game_matches
    sql = "DELETE FROM game_matches"
    cursor.execute(sql)
    db.commit()
    
    cursor.close()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""

    #Delete game matches and results
    deleteMatches()
    
    #connect to the database
    db = connect()
    cursor = db.cursor()
       
    #Delete players from table game_players
    sql = "DELETE FROM game_players"
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""

    #connect to the database
    db = connect()
    cursor = db.cursor()

    #Query to count players
    sql =       "SELECT Count(player_id) " 
    sql = sql + "FROM   game_players "

    cursor.execute(sql)
    players = cursor.fetchone()
    cursor.close()
    db.close()
    return players[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    
    #Get the active tournament game id if it exists
    game = getGameId()

    #Start a new tournament if one does not already exist
    if game is None:
        setNewGame()
        game = getGameId()
    
    gameId = game[0]

    #connect to the database
    db = connect()
    cursor = db.cursor()

    #Insert new player into game_players table
    sql =       "INSERT INTO game_players "
    sql = sql + "            (game_id, "
    sql = sql + "             player_name) "
    sql = sql + "VALUES      (%s, "
    sql = sql + "             %s) "

    cursor.execute((sql), (gameId, name,))
    db.commit()

    #Get count of tournament players
    players = countPlayers()

    #Calculate the number of tournament rounds based on the number of players, and 2 players per match
    rounds = int(math.ceil(math.log(players,2)))

    #Update tournament with number of players and number of rounds
    sql =       "UPDATE game "
    sql = sql + " SET competitors = " + str(players)
    sql = sql + " , rounds = "        + str(rounds)
    sql = sql + " WHERE game_id = "   + str(gameId)

    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    #connect to the database
    db = connect()
    cursor = db.cursor()

    #Player standings query
    sql =       "SELECT p.player_id, "
    sql = sql + "       p.player_name, "
    sql = sql + "       COALESCE(Sum(r.results), 0) wins, "
    sql = sql + "       COALESCE(Count(r.results), 0) matches "
    sql = sql + "FROM   game_players p "
    sql = sql + "       LEFT JOIN game_results r "
    sql = sql + "              ON r.player_id = p.player_id "
    sql = sql + "GROUP  BY p.player_id, "
    sql = sql + "          p.player_name "
    sql = sql + "ORDER BY wins DESC, matches DESC, player_id ASC "

    cursor.execute(sql);
    playerStandings = cursor.fetchall()
    cursor.close()
    db.close()
    #print playerStandings
    return playerStandings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    #Get the game_id, and round of the active tournament
    game = getGameId()
    gameId = game[0]
    roundId = game[1]

    #set game match
    setMatch(gameId, roundId, winner, loser)

    #Get match id
    matchId = getMatch(str(gameId), str(winner), str(loser))

    #Set winner results into table game_results
    setResults(gameId, roundId, matchId, winner, 1)
    
    #Set loser results into table game_results
    setResults(gameId, roundId, matchId, loser, 0)

    return reportMatch

 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    #connect to the database
    db = connect()
    cursor = db.cursor()

    #Query to match players for next round based on game results
    sql =       "SELECT m.player_id, "
    sql = sql + "       m.player_name, " 
    sql = sql + "       m.o_id, "
    sql = sql + "       m.o_name "
    sql = sql + "FROM   (SELECT o.*, " 
    sql = sql + "               Lead(o.player_id) "
    sql = sql + "                 OVER () o_id, "
    sql = sql + "               Lead(o.player_name) "
    sql = sql + "                 OVER () o_name "
    sql = sql + "        FROM   (SELECT r.player_id, "
    sql = sql + "                       p.player_name, "
    sql = sql + "                       Rank() "
    sql = sql + "                         OVER ( "
    sql = sql + "                           partition BY r.game_id "
    sql = sql + "                           ORDER BY r.results DESC, r.player_id) player_rank "
    sql = sql + "                FROM   game_results r "
    sql = sql + "                       LEFT JOIN game_players p "
    sql = sql + "                              ON p.player_id = r.player_id) o)m "
    sql = sql + "WHERE  Mod(m.player_rank, 2) = 1 "
    
    cursor.execute(sql);
    matches = cursor.fetchall()

    #Get the present game id and round
    game = getGameId()

    #Register new matches in table game_matches
    for row in matches:
        #print (row[0], row[1], row[2], row[3])
        setMatch(game[0], game[1]+1, row[0], row[2])
        
    cursor.close()
    db.close()

    return matches


def getGameId():

    '''Return the present tournament game id, and round '''
    
    #connect to the database
    db = connect()
    cursor = db.cursor()

    sql =       "SELECT game_id, "
    sql = sql + "       game_round "
    sql = sql + "FROM   game "
    sql = sql + "ORDER  BY game_id DESC " 
    sql = sql + "LIMIT  1 "

    cursor.execute(sql);
    gameId = cursor.fetchone()
    cursor.close()
    db.close()
    
    return gameId

def setNewGame():

    '''Start a new Chess tournament '''
    
    #connect to the database
    db = connect()
    cursor = db.cursor()

    sql =       "INSERT INTO game "
    sql = sql + "            (game_name, "
    sql = sql + "             competitors, "
    sql = sql + "             game_round, "
    sql = sql + "             rounds) "
    sql = sql + "VALUES      (%s, "
    sql = sql + "             %s, "
    sql = sql + "             %s, "
    sql = sql + "             %s) "

    cursor.execute((sql), ('Chess', 0, 1, 1,))
    db.commit()
    cursor.close()
    db.close()


def getMatch(gameId, player1, player2):
    
    #Get game match id

    #connect to the database
    db = connect()
    cursor = db.cursor()

    #Query match_id of opponents
    sql =       "SELECT match_id "
    sql = sql + "FROM   game_matches "
    sql = sql + "WHERE  game_id = " + gameId  
    sql = sql + " AND    player1 = " + player1  
    sql = sql + " AND    player2 = " + player2

    cursor.execute(sql)
    matchId = cursor.fetchone()    
    cursor.close()
    db.close()
    return matchId

    
def setMatch(gameId, roundId, player1, player2):

    #Insert game match into table game_matches

    #connect to the database
    db = connect()
    cursor = db.cursor()

    sql =       "INSERT INTO game_matches "
    sql = sql + "            (game_id, "
    sql = sql + "             round_id, "
    sql = sql + "             player1, "
    sql = sql + "             player2) "
    sql = sql + "VALUES      (%s, "
    sql = sql + "             %s, "
    sql = sql + "             %s, "
    sql = sql + "             %s) "
    
    cursor.execute((sql), (gameId, roundId, player1, player2,))
    db.commit()
    cursor.close()
    db.close()

    
def setResults(gameId, roundId, matchId, playerId, result):

    #Insert match results into table game_results

    #connect to the database
    db = connect()
    cursor = db.cursor()

    sql =         "INSERT INTO game_results " 
    sql = sql + "            ( "
    sql = sql + "                        game_id, "
    sql = sql + "                        round_id, "
    sql = sql + "                        match_id, "
    sql = sql + "                        player_id, "
    sql = sql + "                        results "
    sql = sql + "            ) "
    sql = sql + "            VALUES "
    sql = sql + "            ( "
    sql = sql + "                        %s, " 
    sql = sql + "                        %s, "
    sql = sql + "                        %s, "
    sql = sql + "                        %s, "
    sql = sql + "                        %s) "

    cursor.execute((sql), (gameId, roundId, matchId, playerId, result,))
    db.commit()
    cursor.close()
    db.close()
