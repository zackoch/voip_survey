from flask import render_template, url_for, flash, redirect
from voip_survey import app, db
from voip_survey.forms import AuthForm, QuestionnaireForm
from voip_survey.models import Submission
from voip_survey import os
import requests
from datetime import date
from voip_survey import path


headers = {
    'Content-Type': "application/json",
    'QB-Realm-Hostname': os.getenv("QB_REALM_VOIP"),
    'User-Agent': "api_chrome_test",
    'Authorization': os.getenv("QB_AUTH_VOIP")
}


@app.route("/voip/", methods=['GET', 'POST'])
def auth():
    password = os.getenv('VOIP_FORM_USER')
    form = AuthForm()
    if form.validate_on_submit():
        if form.password.data.lower() == password:
            return redirect(url_for('home'))
        else:
            flash('Invalid Password - please try again, or click the help link below for assistance.', 'danger')
    return render_template('auth.html', title='Authenticate', form=form)


@app.route("/voip/" + path, methods=['GET', 'POST'])
def home():
    form = QuestionnaireForm()
    if form.validate_on_submit():

        if form.state.data == 'State':
            form.state.data = ''

        if form.timezone.data == 'Timezone':
            form.timezone.data = ''

        if form.maximum_calls.data == 'Maximum Simultaneous Calls?':
            form.maximum_calls.data = ''

        if form.overhead_paging.data == 'Overhead Paging?':
            form.overhead_paging.data = ''

        if form.modem_config.data == 'Modem Configuration?':
            form.modem_config.data = ''

        form_data = {
            '6': {'value': str(form.site_name.data)},
            '7': {'value': str(form.site_code.data)},
            '8': {'value': str(form.street_address.data)},
            '9': {'value': str(form.city.data)},
            '10': {'value': str(form.state.data)},
            '11': {'value': str(form.zip_code.data)},
            '12': {'value': str(form.primary_full_name.data)},
            '13': {'value': str(form.primary_email.data)},
            '14': {'value': str(form.primary_phone.data)},
            '15': {'value': str(form.timezone.data)},
            '16': {'value': str(form.primary_phone.data)},
            '17': {'value': str(form.primary_priority_number.data)},
            '18': {'value': str(form.primary_retail_number.data)},
            '19': {'value': str(form.alternate_retail_number.data)},
            '20': {'value': str(form.alternate_priority_number.data)},
            '21': {'value': str(form.op_number.data)},
            '34': {'value': str(form.billing_number.data)},
            '22': {'value': str(form.fax_number.data)},
            '23': {'value': str(form.fire_number.data)},
            '24': {'value': str(form.credit_number.data)},
            '25': {'value': str(form.maximum_calls.data)},
            '26': {'value': str(form.wired_desk_qty.data)},
            '27': {'value': str(form.cordless_qty.data)},
            '28': {'value': str(form.overhead_paging.data)},
            '29': {'value': str(form.carrier.data)},
            '30': {'value': str(form.isp.data)},
            '31': {'value': str(form.outbound_cid.data)},
            '32': {'value': str(form.modem_config.data)},
            '33': {'value': str(date.today())}
        }

        json_payload = {
            'to': os.getenv('QB_TABLE_VOIP'),
            'data': [form_data]
        }

        r = requests.post(os.getenv('QB_API'), headers=headers, json=json_payload)
        response = r.json()

        submission = Submission(site_name=form.site_name.data,
                                site_code=form.site_code.data,
                                street_address=form.street_address.data,
                                city=form.city.data,
                                state=form.state.data,
                                zip_code=form.zip_code.data,
                                primary_full_name=form.primary_full_name.data,
                                primary_email=form.primary_email.data,
                                primary_phone=form.primary_phone.data,
                                timezone=form.timezone.data,
                                primary_retail_number=form.primary_retail_number.data,
                                alternate_retail_number=form.alternate_retail_number.data,
                                primary_priority_number=form.primary_priority_number.data,
                                alternate_priority_number=form.alternate_priority_number.data,
                                billing_number=form.billing_number.data,
                                fax_number=form.fax_number.data,
                                fire_number=form.fire_number.data,
                                credit_number=form.credit_number.data,
                                maximum_calls=form.maximum_calls.data,
                                wired_desk_qty=form.wired_desk_qty.data,
                                cordless_qty=form.cordless_qty.data,
                                overhead_paging=form.overhead_paging.data,
                                carrier=form.carrier.data,
                                isp=form.isp.data,
                                outbound_cid=form.outbound_cid.data,
                                modem_config=form.modem_config.data,
                                form_payload=json_payload,
                                qb_response=response
                                )
        db.session.add(submission)
        db.session.commit()

        flash(f'Thank you, your submission was successful. You may now close this page.', 'success')
        return redirect(url_for('home'))
    return render_template('home.html', title='Questionnaire', form=form)
