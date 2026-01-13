from odoo import models

class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _get_geoip_response(cls, ip_address):
        """
        Overriding the GeoIP lookup to return None.
        This prevents Odoo from assigning a country code based on IP.
        """
        return None