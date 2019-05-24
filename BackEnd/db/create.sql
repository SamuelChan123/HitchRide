
CREATE TABLE Person
(id SERIAL PRIMARY KEY,
name VARCHAR(64) NOT NULL,
 email VARCHAR(64) NOT NULL,
 phone VARCHAR(32), rating FLOAT(32));

CREATE TABLE Entry
(id SERIAL PRIMARY KEY, personid INTEGER UNIQUE NOT NULL, originlatitude FLOAT(48) NOT NULL, originlongitude FLOAT(48) NOT NULL, destlatitude FLOAT(48) NOT NULL, destlongitude FLOAT(48) NOT NULL, starttime TIMESTAMP NOT NULL, radiusmiles FLOAT(48) NOT NULL, type VARCHAR(32), comment VARCHAR(64));
CREATE TABLE Groups
(id SERIAL PRIMARY KEY,
  group_members VARCHAR(128) NOT NULL, originlatitude FLOAT(48) NOT NULL, originlongitude FLOAT(48) NOT NULL, destlatitude FLOAT(48) NOT NULL, destlongitude FLOAT(48) NOT NULL,  starttime TIMESTAMP NOT NULL);

 CREATE FUNCTION FuncEntryCheck() RETURNS TRIGGER AS $$
 BEGIN
   -- IF NEW.id IN(SELECT entry FROM table)
   --   THEN RAISE EXCEPTION '';
   -- END IF;
   RETURN NEW;
 END;
 $$ LANGUAGE plpgsql;

 CREATE TRIGGER EntryCheck
   BEFORE INSERT OR UPDATE ON Entry
   FOR EACH ROW
   EXECUTE PROCEDURE FuncEntryCheck();
