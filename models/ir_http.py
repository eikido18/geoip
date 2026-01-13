from odoo import models

class Website(models.Model):
    _inherit = 'website'

    def _get_geoip_country_code(self):
        """Disable automatic country detection"""
        return False