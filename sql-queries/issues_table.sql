CREATE TABLE issues (
	issue_id int NOT NULL UNIQUE PRIMARY KEY,
	main_issue varchar NOT NULL,
	sub_issue varchar
);