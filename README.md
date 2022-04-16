# mikrotik_traffic_counter_en

- [mikrotik_traffic_counter_en](#mikrotik_traffic_counter_en)
  - [Running with docker-compose](#running-with-docker-compose)
    - [Install latest docker-compose](#install-latest-docker-compose)
    - [Change variables](#change-variables)
    - [Running](#running)
  - [Local installation](#local-installation)


## Running with docker-compose
The simplest way to run from docker-compose

### Install latest docker-compose

First remove old version acording to your distro, i.e. `sudo apt-get remove docker-compose`

Then find the latest version from [the release page at GitHub](https://github.com/docker/compose/releases) or by curling
```
# curl + grep
VERSION=$(curl --silent https://api.github.com/repos/docker/compose/releases/latest | grep -Po '"tag_name": "\K.*\d')
```

And download to your $PATH-location 

```
DESTINATION=/usr/local/bin/docker-compose
sudo curl -L https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-$(uname -s)-$(uname -m) -o $DESTINATION
sudo chmod 755 $DESTINATION
```

### Change variables 

Edit `docker-compose.yml` and set database credentials `SQLUSER` = `MYSQL_USER` and `SQLPASSWD` = `MYSQL_PASSWORD`. 

Also set your `MYSQL_ROOT_USER`, `MYSQL_ROOT_PASSWORD`.

### Running

Finally, run with docker-compose

```
docker-compose up --build -d
``` 

## Local installation

Please refer to [installation](https://github.com/h-haghpanah/mikrotik_traffic_counter_en/tree/main/installation)
