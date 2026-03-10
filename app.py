from waitress import serve
import api

# host: defines the ip addresses where traffic is allowed from
# all zeros means we allow all traffic?
serve(api.app, host="0.0.0.0", port=8080)