# rest-api web skeleton

## developer

### default tests
1. neosapience/appname-api -> your docker image name as quay.io/neos/...
1. build base docker image
    ```bash
    $ make build-base
    ```

1. build image
    ```bash
    $ make build
    ```

1. test
    ```
    & make test && make logs
    ```

### developer service up
```
& make up
```


## monitoring
* flower for celery
* mongo-express for mongo

