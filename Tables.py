tables = ['dhcp', "smtp", "irc", "weird", "ssh", "conn", 'ftp',
          "http", "dns", "signature", "ssl", "ids", "files", 'ssh',
          'main']  # this list declares every table in the database

# the following dictionary denotes normalized FIELDS
normalized_fields = {'fuids': 'fuid', 'path': 'path', 'to': 'to', 'rcptto': 'receipent', 'analyzers': 'analyzer',
                     'conn_uids': 'conn_uid', 'rx_hosts': 'rx_host', 'tx_hosts': 'tx_host', "tunnel_parents": 'parent'
    , "ttls": 'ttl', 'answers': 'answer'
    , 'resp_meme_types': 'resp_meme_type', 'resp_fuids': 'resp_fuid', 'orig_meme_types': 'orig_meme_types'
    , 'orig_fuids': 'orig_fuid', 'proxied_headers': 'header', 'tags': 'tag',
                     'validation_status': 'validation_status'}

normalized_tables = ['http_proxied_headers', 'http_resp_meme_types', 'http_tags', 'http_orig_meme_types',
                     'http_orig_fuids', 'http_resp_fuids',
                     'files_tx_hosts', 'files_conn_uids', 'files_analyzers', 'files_rx_hosts', 'ftp_data_channel',
                     'conn_tunnel_parents', 'dns_ttls', 'dns_answers', 'smtp_analyzers', 'smtp_rcptto', 'smtp_to',
                     'smtp_fuids', 'smtp_path', 'ssl_validation_status']
valid = ['conn.log', 'dhcp.log', 'dns.log', 'ftp.log', 'http.log', 'irc.log',
         'smtp.log', 'ssl.log', 'files.log', 'signatures.log', 'weird.log',
         'ssh.log']  # this list stores the valid log files bila can deal with

UnsupportedFiles = ['x509.log', 'packet_filter.log', 'app_stats.log', 'capture_loss.log', 'dnp3.log', 'intel.log',
                    'known_certs.log', 'radius.log', 'modbus.log', 'notice.log', 'reporter.log',
                    'notice.log', 'software.log', 'snmp.log', 'socks.log',
                    'syslog.log', 'traceroute.log',
                    'known_hosts.log']