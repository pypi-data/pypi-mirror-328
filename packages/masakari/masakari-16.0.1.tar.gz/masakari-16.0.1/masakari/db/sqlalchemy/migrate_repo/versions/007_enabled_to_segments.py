# Copyright 2020 Inspur.
# All Rights Reserved.
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

from sqlalchemy import Column, MetaData, Table
from sqlalchemy import Boolean


def upgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine
    segments_table = Table('failover_segments', meta, autoload=True)

    enable_column = Column('enabled', Boolean, default=True)
    segments_table.create_column(enable_column)
