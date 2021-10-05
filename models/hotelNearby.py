from odoo import models, fields, api


class HotelsNearby(models.Model):
    _name = 'hotels.nearby'
    _description = 'Near By Hotel'

    name = fields.Char(string="Hotel Name")
    description = fields.Text(string="Details")
    address = fields.Char(string="Address")
    location = fields.Char(string="Location")
    number = fields.Char(string="Number")
    available_rooms = fields.Integer(string="Available Rooms")
    book_hotel_ids = fields.One2many('book.hotel', 'hotel_name_id', string='Book Hotel', index=True)
    # price = fields.One2many('book.hotel', 'total_price', string="Price")
    image = fields.Binary(string='Image', attachment=True)

    def book_now(self):
        return {
            'res_model': 'book.hotel',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref('hotel_booking.hotel_booking_form').id,
            'target': 'new',
            'context': {'default_hotel_name_id': self.id}
        }
