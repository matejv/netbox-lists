__version__ = "0.1.0"

from extras.plugins import PluginConfig


class ListsPluginConfig(PluginConfig):
    name = "netbox_lists"
    verbose_name = "NetBox Lists"
    version = "0.1.0"
    author = "Devon Mar"
    base_url = "lists"
    required_settings = []
    default_settings = {
        "as_cidr": True,
        "service_primary_ips": True,
        "summarize": True,
        "oxidized_attrs": [
            "id",
            "name",
            "role__slug",
            "platform__slug",
            "primary_ip__address",
            "tags"
        ],
    }


config = ListsPluginConfig
