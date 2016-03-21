# docker-compose-library

run with:
`[optional_env_vars] docker-compose -f ***.yml up --force-recreate`

bulk from v1 to v2 composer:
`find . -name "*.yml" -exec python v1_to_v2.py --source {} --destination {} \;`
