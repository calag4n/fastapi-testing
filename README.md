# FastAPI Testing
## Pre-requirements:
- make
- docker
- docker-compose

## Start server
### Modify environtment variables within docker containers
To change environtment variables within app container, change **.env** and
**.env.tests** for tests respectively

### Shell commanhs:
#### Without docker (all deps should be alread properly installed)
- Run app
```bashsh
make run
```
- Run tests
```
make run-tests
```

#### Docker commands
- Build an image and run {app|tests}
```
make run-docker[-tests]
```
- Gracefully stop all containers
```
make stop-docker[-tests]
```
- Force remove all containers
```
make rm-docker[-tests]
```
- Hint
```
make stop-docker[-tests] \
make rm-docker[-tests] \
make run-docker[-tests]
```

# Flow
## Routes:
### Users
- Create user `POST /users/`
- Get all users `GET /users/`
- Get specific user `GET /users/{user_uid}`
- Update specific user `PUT /users/{user_uid}`
- Delete specific user `DELETE /users/{user_uid}`

# Unchaged :)
DB is initialized in `api/controllers/db.py`

-> request is send to the controller in `api/controllers/users.py`
-> data is _compute_ with model's help and a response is returned
