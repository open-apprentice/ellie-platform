# Prior to running you must export the variables from the command line. 
# $ export DB_DATABASE=your-database-name
# $ export DB_PASSWORD=your-super-password
# you can test them by:
# echo $DB_DATABASE
# echo $DB_PASSWORD
#
# then you can run `$ make run-db`

run-db:
	docker run --name ellie_pg -p 5432:5432 -e POSTGRES_PASSWORD=${DB_PASSWORD} -e POSTGRES_DB=${DB_DATABASE} -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres
# To use a Docker Container for the Postgres DB - 'postgres' is the user. 
	