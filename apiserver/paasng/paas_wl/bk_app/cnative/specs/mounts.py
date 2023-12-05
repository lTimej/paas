# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making
蓝鲸智云 - PaaS 平台 (BlueKing - PaaS System) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except
in compliance with the License. You may obtain a copy of the License at

    http://opensource.org/licenses/MIT

Unless required by applicable law or agreed to in writing, software distributed under
the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the specific language governing permissions and
limitations under the License.

We undertake not to change the open source license (MIT license) applicable
to the current version of the project delivered to anyone in the future.
"""
from paas_wl.bk_app.cnative.specs.constants import MountEnvName, VolumeSourceType
from paas_wl.bk_app.cnative.specs.models import Mount
from paas_wl.workloads.configuration.configmap.kres_entities import ConfigMap, configmap_kmodel
from paasng.platform.applications.models import ModuleEnvironment


class VolumeSourceManager:
    def __init__(self, env: ModuleEnvironment):
        self.env = env
        self.wl_app = env.wl_app

    def deploy(self):
        mount_queryset = Mount.objects.filter(
            module_id=self.env.module.id, environment_name__in=[self.env.environment, MountEnvName.GLOBAL.value]
        )
        for m in mount_queryset:
            self._upsert(m)

    def _upsert(self, mount: Mount):
        if mount.source_type == VolumeSourceType.ConfigMap:
            configmap_kmodel.upsert(ConfigMap(app=self.wl_app, name=mount.source.name, data=mount.source.data))

    def delete_source_config(self, mount: Mount):
        if mount.source_type == VolumeSourceType.ConfigMap:
            configmap_kmodel.delete(ConfigMap(app=self.wl_app, name=mount.source.name, data=mount.source.data))