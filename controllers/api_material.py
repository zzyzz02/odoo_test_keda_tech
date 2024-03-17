# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
import json

class MaterialRegistrationAPI(http.Controller):
    
    @http.route("/api/material", auth="public", methods=["GET"], type="http", csrf=False)
    def get_material_registration(self, **params):
        acceptable_params = {
            "id" : "id",
            "name" : "name",
            "code" : "code",
            "type" : "material_type",
            "buy_price" : "buy_price",
            "supplier" : "supplier_id.name",
        }

        limit = int(params.get("limit", 100)) 
        page = int(params.get("page", 1))
        offset = (page - 1) * limit
        order = params.get("order", "id")
        domain = []

        for key,value in params.items():
            if key in acceptable_params:
                domain.append((acceptable_params[key], "=", value))
        
        material = request.env["material.registration"].sudo().search(domain, limit=limit, offset=offset, order=order)
        return json.dumps({
            "status" : "success",
            "total" : len(material),
            "page" : page,
            "limit" : limit,
            "data" : [
                {
                    "id" : m.id,
                    "name" : m.name,
                    "code" : m.code,
                    "material_type" : m.material_type,
                    "buy_price" : m.buy_price,
                    "currency" : m.currency_id.name,
                    "supplier" : {
                        "id" : m.supplier_id.id,
                        "name" : m.supplier_id.name,
                    }
                } for m in material
            ]
        
        })
    
    @http.route("/api/material", auth="public", methods=["POST"], csrf=False, type="json")
    def create_material_registration(self, **params):
        
        required_params = ["name", "material_type", "buy_price", "supplier", "code"]
        for param in required_params:  
            if param not in params:
                return {
                    "status" : "error",
                    "message" : "Parameter %s is required" % param,
                }

        acceptable_params = {
            "name" : "name",
            "code" : "code",
            "material_type" : "material_type",
            "buy_price" : "buy_price",
            "supplier" : "supplier_id",
        }
        suplier_id = False

        data = {}
        for param in params:
            if param not in acceptable_params:
                return {
                    "status" : "error",
                    "message" : "Invalid parameter %s" % param,
                }
            if param == "supplier":
                supplier_id = request.env["res.partner"].sudo().search([("name", "=", params[param])], limit=1)
                if not supplier_id:
                    return {
                        "status" : "error",
                        "message" : "Supplier not found",
                    }
                params[param] = supplier_id.id


            
            data[acceptable_params[param]] = params[param]
        try:    
            material = request.env["material.registration"].create(data)
        except Exception as e:
            return {
                "status" : "error",
                "message" : str(e),
            }
        

        return {
            "status" : "success",
            "data" : {
                "id" : material.id,
                "name" : material.name,
                "code" : material.code,
                "material_type" : material.material_type,
                "buy_price" : material.buy_price,
                "currency" : material.currency_id.name,
                "supplier" : {
                    "id" : material.supplier_id.id,
                    "name" : material.supplier_id.name,
                }
            }
        }
    
    @http.route("/api/material/<int:id>", auth="public", methods=["PUT"], csrf=False, type="json")
    def update_material_registration(self, id, **params):
        material = request.env["material.registration"].sudo().search([("id", "=", id)], limit=1)
        if not material:
            return {
                "status" : "error",
                "message" : "Material not found",
            }
        acceptable_params = {
            "name" : "name",
            "code" : "code",
            "material_type" : "material_type",
            "buy_price" : "buy_price",
            "supplier" : "supplier_id",
        }
        suplier_id = False

        data = {}
        for param in params:
            if param not in acceptable_params:
                return {
                    "status" : "error",
                    "message" : "Invalid parameter %s" % param,
                }
            if param == "supplier":
                supplier_id = request.env["res.partner"].sudo().search([("name", "=", params[param])], limit=1)
                if not supplier_id:
                    return {
                        "status" : "error",
                        "message" : "Supplier not found",
                    }
                params[param] = supplier_id.id

            if not params[param]:
                return {
                    "status" : "error",
                    "message" : "Parameter %s is required" % param,
                }

            data[acceptable_params[param]] = params[param]
        try:    
            material.write(data)
        except Exception as e:
            return {
                "status" : "error",
                "message" : str(e),
            }
        return {
            "status" : "success",
            "data" : {
                "id" : material.id,
                "name" : material.name,
                "code" : material.code,
                "material_type" : material.material_type,
                "buy_price" : material.buy_price,
                "currency" : material.currency_id.name,
                "supplier" : {
                    "id" : material.supplier_id.id,
                    "name" : material.supplier_id.name,
                }
            }
        }
    
    @http.route("/api/material/<int:id>", auth="public", methods=["DELETE"], csrf=False, type="http")
    def delete_material_registration(self, id):
        material = request.env["material.registration"].sudo().search([("id", "=", id)], limit=1)
        if not material:
            return json.dumps({
                "status" : "error",
                "message" : "Material not found",
            })
        material.unlink()
        return json.dumps({
            "status" : "success",
            "message" : "Material has been deleted",
        })