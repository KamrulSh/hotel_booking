from odoo import models, fields


class HotelBook(models.Model):
    _name = 'book.hotel'
    _description = 'Book a Hotel'
    _rec_name = 'user'

    def _default_user(self):
        return self.env.user.id

    user = fields.Many2one('res.users', string="User", default=_default_user, required=True, ondelete='cascade',
                           index=True, readonly=True)

    hotel_name_id = fields.Many2one('hotels.nearby', string="Hotels", readonly=True)
    customer_name = fields.Char(string="Customer Name")
    customer_address = fields.Char(string="Customer Address")
    customer_number = fields.Char(string="Customer Number")
    expected_room = fields.Integer(string="Expected Room")
    statusID = fields.Selection([
        ('request', 'Pending'),
        ('approve', 'Approved'),
        ('reject', 'Rejected')
    ], string='Booking Status', default='request', required=True,
        index=True, readonly=True)
    room_type = fields.Selection([
        ('exe_king_room', 'Executive King Room'),
        ('dlx_king_room', ' Deluxe King Room')
    ], required=True, default='exe_king_room')

    def approve_booking(self):
        for record in self:
            record.statusID = 'approve'

    def reject_booking(self):
        for record in self:
            record.statusID = 'reject'
