-- Database: productcomplaintdb

-- DROP DATABASE productcomplaintdb;

CREATE DATABASE productcomplaintdb
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'en_US.UTF-8'
       LC_CTYPE = 'en_US.UTF-8'
       CONNECTION LIMIT = -1;
--GRANT CONNECT, TEMPORARY ON DATABASE productcomplaintdb TO public;
GRANT ALL ON DATABASE productcomplaintdb TO postgres;
GRANT ALL ON DATABASE productcomplaintdb TO costadiego;

