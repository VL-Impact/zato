# -*- coding: utf-8 -*-

"""
Copyright (C) 2019, Zato Source s.r.o. https://zato.io

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals


# Zato
from zato.common.broker_message import OUTGOING
from zato.server.service.internal import AdminService, AdminSIO

# ################################################################################################################################
# ################################################################################################################################

class Execute(AdminService):
    """ Executes SFTP command(s) using a relevant connector.
    """
    class SimpleIO(AdminSIO):
        input_required = 'id', 'data', 'log_level'
        output_optional = 'response_time', 'stdout', 'stderr'

    def handle(self):
        msg = self.request.input.deepcopy()
        msg['action'] = OUTGOING.SFTP_EXECUTE.value
        msg['cid'] = self.cid

        out = self.server.connector_sftp.invoke_sftp_connector(msg)
        self.response.payload = out.text

# ################################################################################################################################
# ################################################################################################################################
