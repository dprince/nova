# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012, Red Hat, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Client side of the consoleauth RPC API.
"""

from nova.openstack.common import cfg
import nova.openstack.common.rpc.proxy

CONF = cfg.CONF


class ConsoleAuthAPI(nova.openstack.common.rpc.proxy.RpcProxy):
    '''Client side of the consoleauth rpc API.

    API version history:

        1.0 - Initial version.
    '''

    #
    # NOTE(russellb): This is the default minimum version that the server
    # (manager) side must implement unless otherwise specified using a version
    # argument to self.call()/cast()/etc. here.  It should be left as X.0 where
    # X is the current major API version (1.0, 2.0, ...).  For more information
    # about rpc API versioning, see the docs in
    # openstack/common/rpc/dispatcher.py.
    #
    BASE_RPC_API_VERSION = '1.0'

    def __init__(self):
        super(ConsoleAuthAPI, self).__init__(
                topic=CONF.consoleauth_topic,
                default_version=self.BASE_RPC_API_VERSION)

    def authorize_console(self, ctxt, token, console_type, host, port,
                          internal_access_path):
        # The remote side doesn't return anything, but we want to block
        # until it completes.
        return self.call(ctxt,
                self.make_msg('authorize_console',
                              token=token, console_type=console_type,
                              host=host, port=port,
                              internal_access_path=internal_access_path))

    def check_token(self, ctxt, token):
        return self.call(ctxt, self.make_msg('check_token', token=token))
