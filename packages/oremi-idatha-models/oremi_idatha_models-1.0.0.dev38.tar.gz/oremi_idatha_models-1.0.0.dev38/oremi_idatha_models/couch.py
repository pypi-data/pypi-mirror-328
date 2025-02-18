# Copyright 2024-2025 Sébastien Demanou. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from typing import Any
from typing import Generic
from typing import TypeVar

from pydantic import BaseModel

DocumentViewValue = TypeVar('DocumentViewValue')
DocumentViewDoc = TypeVar('DocumentViewDoc', bound=dict)


class DocumentViewResponse(BaseModel, Generic[DocumentViewValue, DocumentViewDoc]):
  """
  View response.

  Docs: http://docs.couchdb.org/en/latest/api/ddoc/views.html#get--db-_design-ddoc-_view-view
  """

  rows: list[dict[str, Any]]  # List of view row objects
  offset: int | None = None
  total_rows: int | None = None
  update_seq: Any | None = None


class FindResponse(BaseModel):
  docs: list[dict]
  warning: str | None = None
  execution_stats: dict | None = None
  bookmark: str | None = None


class GenericResponse(BaseModel):
  ok: bool
  id: str
  rev: str


class OkResponse(BaseModel):
  ok: bool


class GetNodeVersionResponse(BaseModel):
  pass


class MaybeDocument(BaseModel):
  _id: str | None = None
  _rev: str | None = None


class IdentifiedDocument(BaseModel):
  _id: str


class RevisionedDocument(BaseModel):
  _rev: str


class Document(IdentifiedDocument, RevisionedDocument, BaseModel):
  pass


class FilterDocument(IdentifiedDocument, BaseModel):
  filters: dict[str, str]
  language: str | None = None


DesignDocumentView = dict[str, str]


class DesignDocument(IdentifiedDocument, BaseModel):
  views: dict[str, DesignDocumentView]
  language: str | None = None


class CreateSessionResponse(BaseModel):
  ok: bool
  name: str
  roles: list[str]


class SessionInfo(BaseModel):
  authenticated: str
  authentication_handlers: list[str]
  authentication_db: str | None = None


class UserCtx(BaseModel):
  name: str
  roles: list[str]


class GetSessionResponse(BaseModel):
  info: SessionInfo
  ok: bool
  userCtx: UserCtx
