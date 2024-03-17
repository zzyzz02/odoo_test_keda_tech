from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class MaterialRegistration(models.Model):
    _name = "material.registration"
    _description = "Material Registration"

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    code = fields.Char(string="Code", required=True)
    material_type = fields.Selection([("fabric", "Fabric"), 
                                      ("jeans", "Jeans"), ("cotton", "Cotton")], string="Material Type", required=True)
    buy_price = fields.Float(string="Buy Price")
    currency_id = fields.Many2one("res.currency", string="Currency", default=lambda self: self.env.company.currency_id, required=True)
    supplier_id = fields.Many2one("res.partner", string="Supplier", required=True)

    @api.model
    def create(self, vals):
        if vals.get("code"):
            duplicate_record = self.search([("code", "=", vals.get("code"))], limit=1)

            if duplicate_record:
                raise ValidationError(_("Code had been use by %s") % duplicate_record.name)
        if vals.get("buy_price") < 100:
            raise ValidationError(_("Buy price can't be less than 100"))

        return super(MaterialRegistration, self).create(vals)        


    def write(self, vals):
        if vals.get("code"):
            duplicate_record = self.search([("code", "=", vals.get("code")), ("id", "!=", self.id)], limit=1)

            if duplicate_record:
                raise ValidationError(_("Code had been use by %s") % duplicate_record.name)
        if vals.get("buy_price") < 100:
            raise ValidationError(_("Buy price can't be less than 100"))

        return super(MaterialRegistration, self).write(vals)

            
   


    