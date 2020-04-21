CREATE TABLE complaints_users (
	complaint_id int NOT NULL UNIQUE PRIMARY KEY,
	product_id int NOT NULL,
	issue_id int NOT NULL,
	complaint_text varchar,
	date_complaint DATE,
	was_user_disputed varchar(3),
	FOREIGN KEY (product_id) REFERENCES products(product_id),
	FOREIGN KEY (issue_id) REFERENCES issues(issue_id)
);