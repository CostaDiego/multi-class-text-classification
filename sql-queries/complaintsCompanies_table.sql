CREATE TABLE complaints_companies (
	complaint_id int NOT NULL UNIQUE PRIMARY KEY,
	company varchar NOT NULL,
	company_response_to_user varchar,
	company_response_to_public varchar,
	was_response_timely varchar(3),
	date_complaint DATE
);