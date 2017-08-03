# Leviton Cloud Services API model ApiPartner.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from decora_wifi.base_model import BaseModel


class ApiPartner(BaseModel):
    def __init__(self, session, model_id=None):
        super(ApiPartner, self).__init__(session, model_id)

    def count(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def count_oauth_tokens(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/:id/oauthTokens/count"
        return session.call_api(api, attribs, 'get')

    def create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def create_oauth_tokens(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/:id/oauthTokens"
        return session.call_api(api, attribs, 'post')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_oauth_tokens(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/:id/oauthTokens"
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_oauth_tokens(cls, session, oauth_token, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/:id/oauthTokens/{0}".format(oauth_token)
        return session.call_api(api, attribs, 'delete')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_oauth_tokens(cls, session, oauth_token, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/:id/oauthTokens/{0}".format(oauth_token)
        return session.call_api(api, attribs, 'get')

    def find_one(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/findOne".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.set_model_data(data)
        return self

        return self._session.call_api(api, attribs, 'get')

    def get_oauth_token_api_partner(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/OauthTokens/{0}/apiPartner".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_oauth_tokens(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/:id/oauthTokens"
        return session.call_api(api, attribs, 'get')

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def replace_or_create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/replaceOrCreate".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def update_attributes(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/:id"
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_oauth_tokens(cls, session, oauth_token, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/:id/oauthTokens/{0}".format(oauth_token)
        return session.call_api(api, attribs, 'put')

    def upsert(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners".format(self._id)
        return self._session.call_api(api, attribs, 'put')

    def upsert_with_where(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/upsertWithWhere".format(self._id)
        return self._session.call_api(api, attribs, 'post')
