from odoo.tests import common

class TestMaterialRegistration(common.TransactionCase):

    def setUp(self):
        super(TestMaterialRegistration, self).setUp()
        self.supplier = self.env["res.partner"].create({
            "name" : "Supplier 1",
        })
        self.buy_price_1 = 1000
        self.buy_price_2 = 50
        self.material_type = "fabric"
        self.code_1 = "FAB-001"
        self.code_2 = "FAB-002"
        self.material_registration_1 = self.env["material.registration"].create({
            "name" : "Material 1",
            "material_type" : self.material_type,
            "buy_price" : self.buy_price_1,
            "supplier_id" : self.supplier.id,
            "code" : self.code_1,
        })

    def test_01_create_material_registration(self):
        material_registration = self.env["material.registration"].create({
            "name" : "Material 1",
            "material_type" : self.material_type,
            "buy_price" : self.buy_price_1,
            "supplier_id" : self.supplier.id,
            "code" : self.code_2,
        })
        self.assertEqual(material_registration.name, "Material 1")
        self.assertEqual(material_registration.material_type, self.material_type)
        self.assertEqual(material_registration.buy_price, self.buy_price_1)
        self.assertEqual(material_registration.supplier_id, self.supplier)
        self.assertEqual(material_registration.code, self.code_2)

    def test_02_create_material_registration_duplicate_code(self):
        with self.assertRaises(Exception):
            material_registration = self.env["material.registration"].create({
                "name" : "Material 1",
                "material_type" : self.material_type,
                "buy_price" : self.buy_price_1,
                "supplier_id" : self.supplier.id,
                "code" : self.code_1,
            })

    def test_03_create_material_registration_less_100_buy_price(self):
        with self.assertRaises(Exception):
            material_registration = self.env["material.registration"].create({
                "name" : "Material 1",
                "material_type" : self.material_type,
                "buy_price" : self.buy_price_2,
                "supplier_id" : self.supplier.id,
                "code" : self.code_2,
            })

    def test_04_write_material_registration(self):
        material_registration = self.material_registration_1
        material_registration.write({
            "name" : "Material 2",
            "material_type" : "jeans",
            "buy_price" : 2000,
            "supplier_id" : self.supplier.id,
            "code" : "JEANS-001",
        })


        self.assertEqual(material_registration.name, "Material 2")
        self.assertEqual(material_registration.material_type, "jeans")
        self.assertEqual(material_registration.buy_price, 2000)
        self.assertEqual(material_registration.supplier_id, self.supplier)
        self.assertEqual(material_registration.code, "JEANS-001")

    def test_05_write_material_registration_duplicate_code(self):
        material_registration = self.env["material.registration"].create({
            "name" : "Material 1",
            "material_type" : self.material_type,
            "buy_price" : self.buy_price_1,
            "supplier_id" : self.supplier.id,
            "code" : self.code_2,
        })

        with self.assertRaises(Exception):
            material_registration.write({
                "code" : self.code_1,
            })

    def test_06_write_material_registration_less_100_buy_price(self):
        material_registration = self.material_registration_1
        with self.assertRaises(Exception):
            material_registration.write({
                "buy_price" : self.buy_price_2,
            })

    def test_07_unlink_material_registration(self):
        material_registration = self.material_registration_1
        material_registration.unlink()
        self.assertFalse(material_registration.exists())
        
        

    