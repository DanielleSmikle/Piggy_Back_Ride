-- settings.sql
CREATE DATABASE piggy;
CREATE USER piggyuser WITH PASSWORD 'piggy';
GRANT ALL PRIVILEGES ON DATABASE piggy TO piggyuser;