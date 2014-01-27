from splunkdj.setup import forms

import datetime


def load_extraction_date(request, form_cls, field):
    service = request.service
    date_extraction = service.confs['mysetup']['date_extraction']
    try:
        return datetime.date(
            int(date_extraction['year']),
            int(date_extraction['month']),
            int(date_extraction['day']))
    except ValueError:
        # Return an empty field value for the default non-integer placeholders
        return None


def save_extraction_date(request, form, field, value):
    service = request.service
    service.confs['mysetup']['date_extraction'].update(
        year=value.year,
        month=value.month,
        day=value.day)


def what_is_today():
    now = datetime.datetime.now()
    today = now.strftime("%m/%d/%Y")
    return today


class SetupForm(forms.Form):
    # The cust fields are saved in a custom myconf.conf file
    custname = forms.CharField(
        label="Customer name",
        endpoint="configs/conf-mysetup", entity="customerinfo", field="custname",
        max_length=100)
    custdate = forms.DateField(
        label="Date of birth",
        endpoint="configs/conf-mysetup", entity="customerinfo", field="custdate",
        initial="mm/dd/yyyy")
    custemail = forms.EmailField(
        label="Email address",
        endpoint="configs/conf-mysetup", entity="customerinfo", field="custemail",
        max_length=100)
    custpassword = forms.CharField(
        label="Password",
        endpoint="configs/conf-mysetup", entity="customerinfo", field="custpassword",
        max_length=100,
        widget=forms.PasswordInput(render_value=True))

    # This field changes the size of an index called "mytestindex"
    indexsize = forms.IntegerField(
        label="Max size (MB) for the 'mytestindex' index",
        endpoint="data/indexes/", entity="mytestindex", field="maxTotalDataSizeMB")

    # This field shows how to use the load and save functions to extract parts of a date
    extraction_date = forms.DateField(
        label="Today's date",
        load=load_extraction_date, save=save_extraction_date,
        initial=what_is_today)