path "database/creds/legacy_mysql_role" {
  capabilities = ["create", "read"]
}

path "/sys/leases/renew" {
  capabilities = ["update"]
}
