# Leviton Cloud Services API model OmniNotifier.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from decora_wifi.base_model import BaseModel


class OmniNotifier(BaseModel):
    def __init__(self, session, model_id=None):
        super(OmniNotifier, self).__init__(session, model_id)

    def count(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def count_omni_notifier_emails(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/:id/omniNotifierEmails/count"
        return session.call_api(api, attribs, 'get')

    def count_residence_omni_notifiers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/omniNotifiers/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many_residence_omni_notifiers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/omniNotifiers".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def create_omni_notifier_emails(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/:id/omniNotifierEmails"
        return session.call_api(api, attribs, 'post')

    def create_residence_omni_notifiers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/omniNotifiers".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_omni_notifier_emails(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/:id/omniNotifierEmails"
        return session.call_api(api, attribs, 'delete')

    def delete_residence_omni_notifiers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/omniNotifiers".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_omni_notifier_emails(cls, session, omni_notifier_email, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/:id/omniNotifierEmails/{0}".format(omni_notifier_email)
        return session.call_api(api, attribs, 'delete')

    def destroy_by_id_residence_omni_notifiers(self, omni_notifier, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/omniNotifiers/{1}".format(self._id, omni_notifier)
        return self._session.call_api(api, attribs, 'delete')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_omni_notifier_emails(cls, session, omni_notifier_email, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/:id/omniNotifierEmails/{0}".format(omni_notifier_email)
        return session.call_api(api, attribs, 'get')

    def find_by_id_residence_omni_notifiers(self, omni_notifier, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/omniNotifiers/{1}".format(self._id, omni_notifier)
        return self._session.call_api(api, attribs, 'get')

    def find_one(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/findOne".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.set_model_data(data)
        return self

        return self._session.call_api(api, attribs, 'get')

    def get_omni_notifier_email_omni_notifier(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifierEmails/{0}/omniNotifier".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_omni_notifier_emails(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/:id/omniNotifierEmails"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def get_residence(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/:id/residence"
        return session.call_api(api, attribs, 'get')

    def get_residence_omni_notifiers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/omniNotifiers".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get_session_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/getSessionId".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def replace_or_create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/replaceOrCreate".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def send_email(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/sendEmail".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def update_attributes(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/:id"
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_omni_notifier_emails(cls, session, omni_notifier_email, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/:id/omniNotifierEmails/{0}".format(omni_notifier_email)
        return session.call_api(api, attribs, 'put')

    def update_by_id_residence_omni_notifiers(self, omni_notifier, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/omniNotifiers/{1}".format(self._id, omni_notifier)
        return self._session.call_api(api, attribs, 'put')

    def upsert(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers".format(self._id)
        return self._session.call_api(api, attribs, 'put')

    def upsert_with_where(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OmniNotifiers/upsertWithWhere".format(self._id)
        return self._session.call_api(api, attribs, 'post')

