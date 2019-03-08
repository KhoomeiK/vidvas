# vidvas
Sanskrit text database and navigator

# Structure
backend: Flask (routing), Graphene (GraphQL interface with database), sqlAlchemy (interface with SQL), Postgres (database) 
frontend: React

# Broad Todo:
- DONE (TODO manual few) scrape sacred-texts rigveda
- DONE model and implement database
- DONE (TODO parameters for sect, page, verse) set up flask server and graphql
- build react frontend consumes gql api
- https support, serve from server IP to veda.dev

# Links
https://medium.com/@marvinkome/creating-a-graphql-server-with-flask-ae767c7e2525
https://medium.com/@fasterpancakes/graphql-server-up-and-running-with-50-lines-of-python-85e8ada9f637
https://graphql.org/graphql-js/passing-arguments/

# Start postgres server
/var/lib/postgresql/9.6
pg_ctlcluster 9.6 main start

