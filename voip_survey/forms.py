from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp

us_states = [('State', 'State'), ('AK', 'Alaska'), ('AL', 'Alabama'), ('AZ', 'Arizona'), ('AR', 'Arkansas'),
             ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'),
             ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'),
             ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'),
             ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'),
             ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'),
             ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'),
             ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'),
             ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'),
             ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'),
             ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')]

time_zones = ['Timezone', 'Hawaii', 'Alaska', 'Pacific', 'Mountain', 'Central', 'Eastern']

max_calls = ['Maximum Simultaneous Calls?', '4', '8']

paging = ['Overhead Paging?', 'Yes', 'No']

modem = ['Modem Configuration?', 'Static', 'Dynamic']

class PhoneField(StringField):
    def process_formdata(self, valuelist):
        self.data = [v.replace('-', '') for v in valuelist]
        super().process_formdata(self.data)


class QuestionnaireForm(FlaskForm):
    site_name = StringField('Site Name', validators=[DataRequired()])
    site_code = StringField('Site Code', validators=[Length(min=7, max=7, message='must be 6 numeric digits'),
                                        Regexp('^\d+$', message='Must be 6 numeric digits')])
    street_address = StringField('Street Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = SelectField('State', choices=us_states, validators=[DataRequired()], default='State')
    zip_code = StringField('Zip Code', validators=[DataRequired(), Length(min=5, max=5, message='Invalid Zip Code')])
    primary_full_name = StringField('Contact Name', validators=[DataRequired()])
    primary_email = StringField('Contact Email', validators=[DataRequired(), Email()])
    primary_phone = PhoneField('Primary Phone', validators=[DataRequired()])
    timezone = SelectField('Timezone', choices=[(time_zones, time_zones) for time_zones in time_zones],
                           validators=[DataRequired()], default='Timezone')
    primary_retail_number = PhoneField('Primary Retail Number', validators=[DataRequired()])
    alternate_retail_number = PhoneField('Alternate Retail Number')
    primary_priority_number = PhoneField('Primary Priority Number', validators=[DataRequired()])
    alternate_priority_number = PhoneField('Alternate Priority Number')
    op_number = StringField('Operating Unit Number',
                            validators=[Length(min=6, max=6, message='must be 7 numeric digits'),
                                        Regexp('^\d+$', message='Must be 7 numeric digits')])
    billing_number = PhoneField('Billing Phone Number')
    fax_number = PhoneField('Fax Phone Number')
    fire_number = PhoneField('Fire Alarm Phone Number')
    credit_number = PhoneField('Credit Card Phone Number')
    maximum_calls = SelectField('Maximum Simultaneous Calls?', choices=[(max_calls, max_calls) for max_calls in
                                                                        max_calls], validators=[DataRequired()],
                                default='Maximum Simultaneous Calls')
    wired_desk_qty = StringField('Wired Desk Phone QTY', validators=[DataRequired()])
    cordless_qty = StringField('Cordless Handset QTY', validators=[DataRequired()])
    overhead_paging = SelectField('Overhead Paging Required?', choices=[(paging, paging) for paging in
                                                                        paging], validators=[DataRequired()],
                                  default='Overhead Paging Required?')
    carrier = StringField('Phone Carrier', validators=[DataRequired()])
    isp = StringField('Internet Service Provider', validators=[DataRequired()])
    outbound_cid = StringField('Outbound Caller ID', validators=[DataRequired()])
    modem_config = SelectField('Modem Configuration', choices=[(modem, modem) for modem in
                                                               modem], validators=[DataRequired()],
                               default='Modem Configuration?')
    submit = SubmitField('Submit')


class AuthForm(FlaskForm):
    password = PasswordField('Password',
                             validators=[DataRequired()])
    submit = SubmitField('Login')
