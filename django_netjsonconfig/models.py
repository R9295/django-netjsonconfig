from .base.config import AbstractConfig, TemplatesVpnMixin
from .base.template import AbstractTemplate
from .base.vpn import AbstractVpn, AbstractVpnClient


class Config(TemplatesVpnMixin, AbstractConfig):
    """
    Concrete Config model
    """
    class Meta(AbstractConfig.Meta):
        abstract = False


class Template(AbstractTemplate):
    """
    Concrete Template model
    """
    class Meta(AbstractTemplate.Meta):
        abstract = False


class VpnClient(AbstractVpnClient):
    """
    Concrete VpnClient model
    """
    class Meta(AbstractVpnClient.Meta):
        abstract = False


class Vpn(AbstractVpn):
    """
    Concrete VPN model
    """
    class Meta(AbstractVpn.Meta):
        abstract = False