# -*- coding: utf-8 -*-
# TencentBlueKing is pleased to support the open source community by making
# 蓝鲸智云 - PaaS 平台 (BlueKing - PaaS System) available.
# Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
# Licensed under the MIT License (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
#     http://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.
#
# We undertake not to change the open source license (MIT license) applicable
# to the current version of the project delivered to anyone in the future.

from paasng.utils.basic import make_app_pattern, re_path

from .views import DevSandboxViewSet, DevSandboxWithCodeEditorViewSet

urlpatterns = [
    re_path(
        make_app_pattern(r"/dev_sandbox/$", include_envs=False),
        DevSandboxViewSet.as_view({"post": "deploy", "delete": "delete", "get": "get_detail"}),
    ),
    re_path(
        make_app_pattern(r"/user/dev_sandbox_with_code_editor/$", include_envs=False),
        DevSandboxWithCodeEditorViewSet.as_view({"post": "deploy", "delete": "delete", "get": "get_detail"}),
    ),
    re_path(
        make_app_pattern(r"/user/dev_sandbox_with_code_editor/commit/$", include_envs=False),
        DevSandboxWithCodeEditorViewSet.as_view({"post": "commit"}),
    ),
    re_path(
        r"api/bkapps/applications/(?P<code>[^/]+)/user/dev_sandbox_with_code_editors/pre_deploy_check/$",
        DevSandboxWithCodeEditorViewSet.as_view({"get": "pre_deploy_check"}),
    ),
    re_path(
        r"api/bkapps/applications/(?P<code>[^/]+)/user/dev_sandbox_with_code_editors/lists/$",
        DevSandboxWithCodeEditorViewSet.as_view({"get": "list_app_dev_sandbox"}),
    ),
    re_path(
        make_app_pattern(r"/user/dev_sandbox_password/$", include_envs=False),
        DevSandboxWithCodeEditorViewSet.as_view({"get": "get_password"}),
    ),
]
