# vidvas
Sanskrit text database and navigator

# Structure
backend: Flask (routing), Graphene (GraphQL interface with database), sqlAlchemy (interface with SQL), Postgres (database) 
frontend: React

# Broad Todo:
- DONE (TODO manual few) scrape sacred-texts rigveda
- DONE model and implement database
- DONE (TODO parameters for sect, page, verse) set up flask server and graphql
- serve requested documents from Postgres, through GraphQL, out of Flask as JSON
- frontend consumes gql api

# Links
https://medium.com/@marvinkome/creating-a-graphql-server-with-flask-ae767c7e2525
https://medium.com/@fasterpancakes/graphql-server-up-and-running-with-50-lines-of-python-85e8ada9f637