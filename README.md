# Start server

```sh
python main.py
```

# Flow

DB is initialized in `api/controllers/connect.py`

Request is send to `/users`

-> `POST` or `GET` function in `api/routers/users.py`

-> request is send to the controller in `api/controllers/users.py`

-> data is _compute_ with model's help and a response is returned
