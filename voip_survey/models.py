from datetime import date
from voip_survey import db


class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_name = db.Column(db.String())
    site_code = db.Column(db.String())
    street_address = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    zip_code = db.Column(db.String())
    primary_full_name = db.Column(db.String())
    primary_email = db.Column(db.String())
    primary_phone = db.Column(db.String())
    timezone = db.Column(db.String())
    primary_retail_number = db.Column(db.String())
    alternate_retail_number = db.Column(db.String())
    primary_priority_number = db.Column(db.String())
    alternate_priority_number = db.Column(db.String())
    op_number = db.Column(db.String())
    billing_number = db.Column(db.String())
    fax_number = db.Column(db.String())
    fire_number = db.Column(db.String())
    credit_number = db.Column(db.String())
    maximum_calls = db.Column(db.String())
    wired_desk_qty = db.Column(db.String())
    cordless_qty = db.Column(db.String())
    overhead_paging = db.Column(db.String())
    carrier = db.Column(db.String())
    isp = db.Column(db.String())
    outbound_cid = db.Column(db.String())
    modem_config = db.Column(db.String())
    form_payload = db.Column(db.JSON)
    qb_response = db.Column(db.JSON)
    submission_date = db.Column(db.Date, nullable=False, default=date.today())

    def __repr__(self):
        return f"Post('{self.site_name}', '{self.site_code}', '{self.street_address}', '{self.city}', '{self.state}'," \
               f" '{self.zip_code}', '{self.primary_full_name}', '{self.primary_phone}', '{self.primary_email}'," \
               f" '{self.timezone}', '{self.primary_retail_number}', '{self.alternate_retail_number}', " \
               f"'{self.primary_priority_number}', '{self.alternate_priority_number}', '{self.billing_number}', " \
               f"'{self.fax_number}', '{self.fire_number}', '{self.credit_number}', '{self.maximum_calls}', " \
               f"'{self.wired_desk_qty}', '{self.cordless_qty}', '{self.overhead_paging}')"