-- Create table game
CREATE TABLE game 
  ( 
     game_id     SERIAL PRIMARY KEY NOT NULL, 
     game_name   VARCHAR(50) NOT NULL, 
     competitors INT NOT NULL, 
     game_round  INT NOT NULL, 
     rounds      INT NOT NULL 
  ); 
-- Create table game_players
CREATE TABLE game_players 
  ( 
     game_id INT REFERENCES game(game_id) NOT NULL, 
     player_id   SERIAL PRIMARY KEY NOT NULL, 
     player_name VARCHAR(50) NOT NULL 
  );
-- Create table game_matches
CREATE TABLE game_matches 
  ( 
     game_id        INT REFERENCES game(game_id) NOT NULL, 
     round_id       INT NOT NULL, 
     match_id       SERIAL PRIMARY KEY NOT NULL, 
     player1        INT REFERENCES game_players (player_id) NOT NULL, 
     player2        INT REFERENCES game_players (player_id) NOT NULL
  ); 
-- Create table game_results
CREATE TABLE game_results 
  ( 
     game_id   INT REFERENCES game(game_id) NOT NULL, 
     round_id  INT NOT NULL, 
     match_id  INT REFERENCES game_matches(match_id) NOT NULL, 
     player_id INT REFERENCES game_players (player_id) NOT NULL, 
     results    INT NOT NULL 
  );  



