# docker-compose-library

A collection of ready-to-use and hopefully updated open-source applications with
the help of Docker-Compose.

## Setup

Copy [.env.template](.env.template) as `.env` and customize the variables.

Run an application with:

```
docker-compose -f apps/<category>/<app-name>.yml up
```

or

```
docker stack deploy -c apps/<category>/<app-name>.yml <id>
```

## Applications list

| Name                                        | Category              |
| ------------------------------------------- | --------------------- |
| [Ghost](blog/ghost.yml)                     | blog                  |
| [Bonita](business-intelligence/bonita.yml)  | business-intelligence |
| [Shout](chat/shout.yml)                     | chat                  |
| [drupal](cms/drupal.yml)                    | cms                   |
| [joomla](cms/joomla.yml)                    | cms                   |
| [wordpress](cms/wordpress.yml)              | cms                   |
| [eXo](collaboration/eXo.yml)                | collaboration         |
| [gitlab](collaboration/gitlab.yml)          | collaboration         |
| [hastebin](collaboration/hastebin.yml)      | collaboration         |
| [hublin](collaboration/hublin.yml)          | collaboration         |
| [mattermost](collaboration/mattermost.yml)  | collaboration         |
| [openfire](collaboration/openfire.yml)      | collaboration         |
| [rocket.chat](collaboration/rocketchat.yml) | collaboration         |
| [suitecrm](crm/suitecrm.yml)                | crm                   |
| [mongo](database/suitecrm.yml)              | database              |
| [mysql](database/mysql.yml)                 | database              |
| [postgres](database/postgres.yml)           | database              |
| [redis](database/redis.yml)                 | database              |
| [kong](development/kong.yml)                | development           |
| [sonarqube](development/sonarqube.yml)      | development           |
| [alfresco](document/alfresco.yml)           | document              |
| [ckan](document/ckan.yml)                   | document              |
| [logicaldoc](document/logicaldoc.yml)       | document              |
| [nuxeo](document/nuxeo.yml)                 | document              |
| [xibo](document/xibo.yml)                   | document              |
| [prestashop](document/prestashop.yml)       | ecommerce             |
| [odoo](erp/odoo.yml)                        | erp                   |
| [tuleap](project-management/tuleap.yml)     | project-management    |
| [owncloud](storage/owncloud.yml)            | storage               |
| [mistserver](streaming/mistserver.yml)      | streaming             |
| [red5](streaming/red5.yml)                  | streaming             |
| [osticket](trouble-ticketing/osticket.yml)  | trouble-ticketing     |
| [redmine](trouble-ticketing/redmine.yml)    | trouble-ticketing     |
| [dokuwiki](wiki/dokuwiki.yml)               | wiki                  |
| [mediawiki](wiki/mediawiki.yml)             | wiki                  |

## scripts

### unify_yamls.py

undocumented and probably going to be deprecated

### v1_to_v2.py

deprecated: bulk update from v1 to v2 composer:
`find . -name "*.yml" -exec python v1_to_v2.py --source {} --destination {} \;`
