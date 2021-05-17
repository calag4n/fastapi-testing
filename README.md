# Start server

### Pre-requirements:
- make
- docker
- docker-compose

### Shell commanhs:
- Run app `make run `
- Run tests `make run-tests`
- Run app within docker (with mongo) `make run-docker`
- Run tests within docker (with mongo) `make run-docker-tests`

# Flow
DB is initialized in `api/controllers/db.py`
Request is send to `/users/`
-> `POST`, `GET`, `PUT` and `DELETE` are accepted with handlers
in `api/routers/users.py`

-> request is send to the controller in `api/controllers/users.py`
-> data is _compute_ with model's help and a response is returned
