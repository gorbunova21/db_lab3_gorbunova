SELECT * FROM authors;
CREATE TABLE authorscopy AS SELECT * FROM authors; 
DELETE FROM authorscopy;
SELECT * FROM authorscopy;

DO $$
 DECLARE
 	 authorcopy_id authorscopy.author_id%TYPE;
	 authorcopy_name authorscopy.author_name%TYPE;

 BEGIN
     authorcopy_id := 'A_';
     authorcopy_name := 'Author_';
     FOR counter IN 1..10
         LOOP
            INSERT INTO authorscopy (author_id, author_name)
             VALUES (authorcopy_id || counter, authorcopy_name || counter);
         END LOOP;
 END;
 $$